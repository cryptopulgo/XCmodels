# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
import xc_base
import geom
import xc
from model import predefined_spaces
from solution import predefined_solutions
from materials.sections import section_properties
from materials import typical_materials

# Loads
from actions import load_cases as lcm

# Units
inchToMeter= 2.54/100.0
footToMeter= 0.3048
poundToN= 4.44822
psiToPa= 6894.76

# Problem type
cantilever= xc.FEProblem()
cantilever.title= 'Cantilevers C2 and C5'
preprocessor= cantilever.getPreprocessor   
nodes= preprocessor.getNodeHandler
modelSpace= predefined_spaces.StructuralMechanics2D(nodes)

# Materials LSL 1.55E (page 10 of the PDF document from "SolidStart")
sectionGeometry= section_properties.RectangularSection("header",b=2*5.25*inchToMeter,h=14.0*inchToMeter)
LSL= typical_materials.MaterialData(name='LSL',E=1.55e6*psiToPa,nu=0.2,rho=500)
section= sectionGeometry.defElasticShearSection2d(preprocessor,LSL)

# Cantilever geometry
cantileverLength= 0.86
centerSpacing= 12.0*inchToMeter # Distance between trusses
## Key points
pos4= geom.Pos3d(cantileverLength,0.0,0.0)
pos3= pos4+geom.Vector3d(-centerSpacing,0.0,0.0)
pos2= pos3+geom.Vector3d(-centerSpacing,0.0,0.0)
pos1= pos2+geom.Vector3d(-centerSpacing,0.0,0.0)
pos0= geom.Pos3d(0.0,0.0,0.0)
positions= [pos0,pos1,pos2,pos3,pos4]
pointHandler= preprocessor.getMultiBlockTopology.getPoints
points= list()
for p in positions:
    points.append(pointHandler.newPntFromPos3d(p))

## Lines
lines= list()
lineHandler= preprocessor.getMultiBlockTopology.getLines
p0= points[0]
for p1 in points[1:]:
    l= lineHandler.newLine(p0.tag,p1.tag)
    l.setElemSize(centerSpacing/2.0)
    lines.append(l)
    p0= p1

# Mesh
modelSpace= predefined_spaces.StructuralMechanics2D(nodes)
nodes.newSeedNode()
trfs= preprocessor.getTransfCooHandler
lin= trfs.newLinearCrdTransf2d("lin")
seedElemHandler= preprocessor.getElementHandler.seedElemHandler
seedElemHandler.defaultMaterial= section.name
seedElemHandler.defaultTransformation= "lin"
elem= seedElemHandler.newElement("ElasticBeam2d",xc.ID([0,0]))

xcTotalSet= preprocessor.getSets.getSet('total')

mesh= xcTotalSet.genMesh(xc.meshDir.I)

# Constraints
n0= points[0].getNode()
modelSpace.fixNode000(n0.tag)

# Actions
loadCaseManager= lcm.LoadCaseManager(preprocessor)
loadCaseNames= ['load']
loadCaseManager.defineSimpleLoadCases(loadCaseNames)

## Loads on nodes.
cLC= loadCaseManager.setCurrentLoadCase('load')
trussLoad= xc.Vector([0.0,-(13.22+12.68)*1e3,0.0])
facadeLoad= xc.Vector([0.0,-51.55e3,0.0])
totalLoad= 0.0
for p in points[1:-1]:
    n= p.getNode()
    n.newLoad(trussLoad)
    totalLoad+= trussLoad[1]
points[-1].getNode().newLoad(facadeLoad)
totalLoad+= facadeLoad[1]

#We add the load case to domain.
preprocessor.getLoadHandler.getLoadPatterns.addToDomain('load')

# Solution
# Linear static analysis.
analisis= predefined_solutions.simple_static_linear(cantilever)
result= analisis.analyze(1)

# Checking

nodes.calculateNodalReactions(True,1e-7)
Vmax= n0.getReaction[1]
Mmax= n0.getReaction[2]
print('*****',cantilever.title,'******')
print('Load from trusses: ', trussLoad[1]/1e3, ' kN/truss')
print('Facade load: ', facadeLoad[1]/1e3, ' kN')
print('Total load: ', totalLoad/1e3, ' kN')
print('Header: (2) 5.25x14')


Fb= 1730*psiToPa

## Shear
Vu= 2*17041.0*poundToN
print('Vmax= ', Vmax/1e3, ' kN Vu= ', Vu/1e3, ' kN; F= ',Vmax/Vu)

## Bending
Mu= 2*24297.0*poundToN*footToMeter
print('Mmax= ', Mmax/1e3, ' kN Mu= ', Mu/1e3, ' kN; F= ',Mmax/Mu)

## Deflection
dY= points[-1].getNode().getDisp[1]
ratio1= abs(dY)/cantileverLength
print('dY= ',dY*1e3,' mm; ratio= L/', 1.0/ratio1)
