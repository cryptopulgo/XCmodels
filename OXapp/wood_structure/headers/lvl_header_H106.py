# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
import xc_base
import geom
import xc
from model import predefined_spaces
from solution import predefined_solutions
from materials.sections import section_properties
from materials.awc_nds import AWCNDS_materials

# Loads
from actions import load_cases as lcm

# Units
inchToMeter= 2.54/100.0
footToMeter= 0.3048
poundToN= 4.44822
psiToPa= 6894.76

# Problem type
prb= xc.FEProblem()
prb.title= 'Floor header H1.6'
preprocessor= prb.getPreprocessor
nodes= preprocessor.getNodeHandler
modelSpace= predefined_spaces.StructuralMechanics2D(nodes)

# Materials LVL 1.55E (page 10 of the PDF document from "SolidStart")
header= AWCNDS_materials.LVLHeaderSections['3.5x9-1/4']
section= header.defElasticShearSection2d(preprocessor)

Cr= 1.0#1.15 # Repetitive member factor (AWC-NDS2018 supplement table 4F)
CD= AWCNDS_materials.getLoadDurationFactor(10)
CM= AWCNDS_materials.getWetServiceFactor('Fb',5)
Ct= AWCNDS_materials.getTemperatureFactor('Fb','dry',AWCNDS_materials.convertToFahrenheit(25))


# Beam geometry
beamSpan= 5.0*footToMeter
centerSpacing= 24.0*inchToMeter # Distance between trusses
## Key points
pointHandler= preprocessor.getMultiBlockTopology.getPoints
p0= pointHandler.newPntFromPos3d(geom.Pos3d(0.0,0.0,0.0))
p1= pointHandler.newPntFromPos3d(geom.Pos3d(beamSpan,0.0,0.0))

## Lines
lineHandler= preprocessor.getMultiBlockTopology.getLines
l1= lineHandler.newLine(p0.tag,p1.tag)
l1.setElemSize(centerSpacing)

# Mesh
modelSpace= predefined_spaces.StructuralMechanics2D(nodes)
trfs= preprocessor.getTransfCooHandler
lin= trfs.newLinearCrdTransf2d("lin")
seedElemHandler= preprocessor.getElementHandler.seedElemHandler
seedElemHandler.defaultMaterial= section.name
seedElemHandler.defaultTransformation= "lin"
elem= seedElemHandler.newElement("ElasticBeam2d",xc.ID([0,0]))

xcTotalSet= preprocessor.getSets.getSet('total')

mesh= xcTotalSet.genMesh(xc.meshDir.I)

# Constraints
modelSpace.fixNode00F(p0.getNode().tag)
modelSpace.fixNode00F(p1.getNode().tag)

# Actions
loadCaseManager= lcm.LoadCaseManager(preprocessor)
loadCaseNames= ['load']
loadCaseManager.defineSimpleLoadCases(loadCaseNames)

## Loads on nodes.
uniformLoad= 11.042e3
cLC= loadCaseManager.setCurrentLoadCase('load')
L= 40*47.88026 # Live load N/m2
D= 15*47.88026 # Dead load N/m2
uniformLoad= (D+L)*(9+7.25)*footToMeter#N/m
for e in xcTotalSet.elements:
  e.vector2dUniformLoadGlobal(xc.Vector([0.0,-uniformLoad,0.0]))



#We add the load case to domain.
preprocessor.getLoadHandler.getLoadPatterns.addToDomain('load')

# Solution
# Linear static analysis.
analysis= predefined_solutions.simple_static_linear(prb)
result= analysis.analyze(1)

# Checking
print('*****',prb.title,'******')
print('Uniform load: ', uniformLoad/1e3, ' kN/m')
print('Header: ', header.sectionName)

nodes.calculateNodalReactions(True,1e-7)
Vmax= max(p0.getNode().getReaction[1],p1.getNode().getReaction[1])
eMidSpan= xcTotalSet.getNearestElement(geom.Pos3d(beamSpan/2.0,0.0,0.0))
Mmax= max(abs(eMidSpan.getM1),abs(eMidSpan.getM2))

## Shear
Vu= header.Vs

## Bending
Mu= header.Ms

print('Mmax= ', Mmax/1e3, ' kN.m Mu= ', Mu/1e3, ' kN.m; F= ',Mmax/Mu)
print('Vmax= ', Vmax/1e3, ' kN Vu= ', Vu/1e3, ' kN; F= ',Vmax/Vu)

## Deflection
ratioI= header.Iz()/(2252*(0.0254)**4)
nMidSpan= l1.getNearestNode(geom.Pos3d(beamSpan/2.0,0.0,0.0))
dMidSpan= ratioI*nMidSpan.getDisp[1]
ratio1= abs(dMidSpan)/beamSpan
print('dY= ',dMidSpan*1e3,' mm; ratio= L/', 1.0/ratio1, 'L= ', beamSpan, ' m')

# Fire design
## Bending
a_eff= 0.7e-3*30+7e-3
burnedSection= section_properties.RectangularSection('s',header.b-2*a_eff,header.h-a_eff)
Ss= burnedSection.getElasticSectionModulusZ()

Cfire= AWCNDS_materials.getFireDesignAdjustementFactor('Fb')
print('Cfire= ', Cfire)
Fb_adj= Cfire*header.getFb()*CD*CM*Ct
Mu= Fb_adj*Ss

## Shear
As= burnedSection.A()
Av= 2/3.0*As
Cfire= AWCNDS_materials.getFireDesignAdjustementFactor('Fv')
Fv_adj= Cfire*header.Fv*CD*CM*Ct
Vu= Fv_adj*Av

print('Mmax= ', Mmax/1e3, ' kN.m Mu= ', Mu/1e3, ' kN.m; F= ',Mmax/Mu)
print('Vmax= ', Vmax/1e3, ' kN Vu= ', Vu/1e3, ' kN; F= ',Vmax/Vu)


