# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function

import xc_base
import geom
import xc
from model import predefined_spaces
from solution import predefined_solutions
from materials.awc_nds import AWCNDS_materials
from materials import typical_materials

# Loads
from actions import load_cases as lcm
from actions import combinations as combs

# Problem type
sheathingBeam= xc.FEProblem()
sheathingBeam.title= 'Sheating design'
preprocessor= sheathingBeam.getPreprocessor   
nodes= preprocessor.getNodeHandler
modelSpace= predefined_spaces.StructuralMechanics2D(nodes)

# Materials
# Mechanical properties taken from:
# http://www.pfsteco.com/techtips/pdf/tt_plywooddesigncapacities
structuralPanelGeom= AWCNDS_materials.PlywoodPanels['19/32']
plywood= typical_materials.MaterialData(name='Douglas-Fri Plywood',E=4.2e9,nu=0.2,rho=500)
section= structuralPanelGeom.defElasticShearSection2d(preprocessor,plywood)

thickness= structuralPanelGeom.h

spanBendingStiffness= (32-1.5+0.25)*0.0254
spanInternalForces= 32*0.0254
span= spanInternalForces
pointHandler= preprocessor.getMultiBlockTopology.getPoints
pt1= pointHandler.newPntFromPos3d(geom.Pos3d(0.0,0.0,0.0))
pt2= pointHandler.newPntFromPos3d(geom.Pos3d(span,0.0,0.0))
pt3= pointHandler.newPntFromPos3d(geom.Pos3d(2.0*span,0.0,0.0))
pt4= pointHandler.newPntFromPos3d(geom.Pos3d(3.0*span,0.0,0.0))
pt11= pointHandler.newPntFromPos3d(geom.Pos3d(0.0,thickness,0.0))
pt12= pointHandler.newPntFromPos3d(geom.Pos3d(span,thickness,0.0))
pt13= pointHandler.newPntFromPos3d(geom.Pos3d(2.0*span,thickness,0.0))
pt14= pointHandler.newPntFromPos3d(geom.Pos3d(3.0*span,thickness,0.0))

lines= preprocessor.getMultiBlockTopology.getLines
l1= lines.newLine(pt1.tag,pt2.tag)
l2= lines.newLine(pt2.tag,pt3.tag)
l3= lines.newLine(pt3.tag,pt4.tag)
l11= lines.newLine(pt11.tag,pt12.tag)
l12= lines.newLine(pt12.tag,pt13.tag)
l13= lines.newLine(pt13.tag,pt14.tag)

infSet= preprocessor.getSets.defSet("inf")
infSet.getLines.append(l1)
infSet.getLines.append(l2)
infSet.getLines.append(l3)

supSet= preprocessor.getSets.defSet("sup")
supSet.getLines.append(l11)
supSet.getLines.append(l12)
supSet.getLines.append(l13)


# Mesh
modelSpace= predefined_spaces.StructuralMechanics2D(nodes)
nodes.newSeedNode()
trfs= preprocessor.getTransfCooHandler
lin= trfs.newLinearCrdTransf2d("lin")
seedElemHandler= preprocessor.getElementHandler.seedElemHandler
seedElemHandler.defaultMaterial= section.name
seedElemHandler.defaultTransformation= "lin"
elem= seedElemHandler.newElement("ElasticBeam2d",xc.ID([0,0]))

xcTotalSet= preprocessor.getSets.getSet("total")
mesh= infSet.genMesh(xc.meshDir.I)
infSet.fillDownwards()
mesh= supSet.genMesh(xc.meshDir.I)
supSet.fillDownwards()

# Constraints
for p in [pt1,pt2,pt3,pt4]:
    n= p.getNode()
    modelSpace.fixNode00F(n.tag)

for n in supSet.getNodes:
    pos= n.getInitialPos3d
    nInf= infSet.getNearestNode(pos)
    modelSpace.constraints.newEqualDOF(nInf.tag,n.tag,xc.ID([1]))

for p in [pt12,pt13]:
    n= p.getNode()
    pos= n.getInitialPos3d
    nInf= infSet.getNearestNode(pos)
    modelSpace.constraints.newEqualDOF(nInf.tag,n.tag,xc.ID([0]))


# Actions
L= 40*47.88026 # Live load N/m2
D= 15*47.88026 # Dead load N/m2
W= D+L
loadCaseManager= lcm.LoadCaseManager(preprocessor)
loadCaseNames= ['deadLoad','liveLoad','totalLoad']
loadCaseManager.defineSimpleLoadCases(loadCaseNames)

# Dead load.
cLC= loadCaseManager.setCurrentLoadCase('deadLoad')
for e in supSet.getElements:
    e.vector2dUniformLoadGlobal(xc.Vector([0.0,-D]))

# Live load.
cLC= loadCaseManager.setCurrentLoadCase('liveLoad')
for e in supSet.getElements:
    e.vector2dUniformLoadGlobal(xc.Vector([0.0,-L]))

# Total load.
cLC= loadCaseManager.setCurrentLoadCase('totalLoad')
for e in supSet.getElements:
    e.vector2dUniformLoadGlobal(xc.Vector([0.0,-W]))

#We add the load case to domain.
preprocessor.getLoadHandler.getLoadPatterns.addToDomain("liveLoad")

# Solution
# Linear static analysis.
analisis= predefined_solutions.simple_static_linear(sheathingBeam)
result= analisis.analyze(1)

uYMax= -1e6
for n in infSet.getNodes:
    uY= -n.getDisp[1]
    uYMax= max(uY,uYMax)

r= span/uYMax
print('uYMax= ', uYMax*1e3, ' mm (L/'+str(r)+')')

DeltaLL= 12*L*span**4/1743.0/section.sectionProperties.EI()/2 #Two layers
r= span/DeltaLL
print('DeltaLL= ', DeltaLL*1e3, ' mm (L/'+str(r)+')')

