# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function

import math
import vtk
import xc_base
import geom
import xc
from solution import predefined_solutions
from model import predefined_spaces
from materials import typical_materials
from materials.astm import ASTM_materials

from materials.sections import structural_steel as steel
from actions import load_cases as lcm
from actions import combinations as combs
from datetime import date

#Units
foot2m= 0.3048
inch2m= 0.0254

# Problem type
steelBeam= xc.FEProblem()
steelBeam.title= 'Steel beams at 2dn floor. Courtyard facade.'
preprocessor= steelBeam.getPreprocessor   
nodes= preprocessor.getNodeHandler

# Materials
## Steel material
steel= ASTM_materials.A572
steel.gammaM= 1.00
## Profile geometry
# profile= ASTM_materials.CShape(steel,'C380X50.4')
# numberOfProfiles= 2 # 2 channel shaped profiles!!
profile= ASTM_materials.WShape(steel,'W16X57')
numberOfProfiles= 1 # 1 w profile
xcSection= profile.defElasticShearSection2d(preprocessor,steel)

# Model geometry

## Points.
span= 27*foot2m+3*inch2m
pointHandler= preprocessor.getMultiBlockTopology.getPoints
p0= pointHandler.newPntFromPos3d(geom.Pos3d(0.0,0.0,0.0))
p1= pointHandler.newPntFromPos3d(geom.Pos3d(span,0.0,0.0))
p2= pointHandler.newPntFromPos3d(geom.Pos3d(2*span,0.0,0.0))

## Lines
lineHandler= preprocessor.getMultiBlockTopology.getLines
l1= lineHandler.newLine(p0.tag,p1.tag)
l1.nDiv= 10
l2= lineHandler.newLine(p1.tag,p2.tag)
l2.nDiv= 10

# Mesh
modelSpace= predefined_spaces.StructuralMechanics2D(nodes)
trfs= preprocessor.getTransfCooHandler
lin= trfs.newLinearCrdTransf2d("lin")
seedElemHandler= preprocessor.getElementHandler.seedElemHandler
seedElemHandler.defaultMaterial= xcSection.name
seedElemHandler.defaultTransformation= "lin"
elem= seedElemHandler.newElement("ElasticBeam2d",xc.ID([0,0]))

xcTotalSet= preprocessor.getSets.getSet('total')
mesh= xcTotalSet.genMesh(xc.meshDir.I)

# Constraints
modelSpace.fixNode00F(p0.getNode().tag)
modelSpace.fixNodeF0F(p1.getNode().tag)
modelSpace.fixNodeF0F(p2.getNode().tag)

# Actions

## Load cases
loadCaseManager= lcm.LoadCaseManager(preprocessor)
loadCaseNames= ['deadLoad','liveLoad','snowLoad','windLoad']
loadCaseManager.defineSimpleLoadCases(loadCaseNames)

def defineLoad(loadCaseName, loadValue):
    cLC= loadCaseManager.setCurrentLoadCase(loadCaseName)
    loadVector= xc.Vector([0.0,-loadValue])
    for e in xcTotalSet.elements:
        e.vector2dUniformLoadGlobal(loadVector)

### Load values from "CD_reactions.ods"    
### Dead load
defineLoad('deadLoad',14.88e3/numberOfProfiles)
### Live load
defineLoad('liveLoad',22.86e3/numberOfProfiles)
### Snow load
defineLoad('snowLoad',10.05e3/numberOfProfiles)
### Wind load
defineLoad('windLoad',-6.35e3/numberOfProfiles)

## Load combinations
combContainer= combs.CombContainer()
### Serviceability limit states.
combContainer.SLS.qp.add('SLS01', '1.0*liveLoad')
combContainer.SLS.qp.add('SLS02', '1.0*deadLoad+1.0*liveLoad')
combContainer.SLS.qp.add('SLS03', '1.0*deadLoad+1.0*snowLoad')
### Ultimate limit state.
combContainer.ULS.perm.add('ULS01', '1.4*deadLoad')
combContainer.ULS.perm.add('ULS02', '1.2*deadLoad + 1.6*liveLoad + 0.5*snowLoad')
combContainer.ULS.perm.add('ULS03', '1.2*deadLoad + 1.6*snowLoad + 0.5*liveLoad ')
combContainer.ULS.perm.add('ULS04', '1.2*deadLoad + 1.6*snowLoad + 0.5*windLoad')
combContainer.ULS.perm.add('ULS05', '1.2*deadLoad + 1.0*windLoad + 0.5*liveLoad ')
combContainer.ULS.perm.add('ULS06', '1.2*deadLoad + 0.5*liveLoad + 0.2*snowLoad')
combContainer.ULS.perm.add('ULS07', '0.9*deadLoad + 1.0*windLoad')
### Dump combination definition into XC.
combContainer.dumpCombinations(preprocessor)

# Solution
## Linear static analysis.
analysis= predefined_solutions.simple_static_linear(steelBeam)

# Checking
## Check deflection limit
### Deflection limit values.
deflectionLimits= dict()
deflectionLimits['SLS01']= span/540.0
deflectionLimits['SLS02']= span/240.0
deflectionLimits['SLS03']= span/240.0
### Nodes with maximum deflection (or almost).
midSpan1= span/2
midPos1= geom.Pos3d(midSpan1,0.0,0.0)
n1= l1.getNearestNode(geom.Pos3d(midSpan1,0.0,0.0))
midSpan2= 3*midSpan1
midPos2= geom.Pos3d(midSpan2,0.0,0.0)
n2= l2.getNearestNode(geom.Pos3d(midSpan2,0.0,0.0))

print(date.today(), steelBeam.title)
print('  cheking profile: ', profile.name)
print('  L= ', span, 'm')

print('  Serviceability limit states.')
for comb in combContainer.SLS.qp:
    preprocessor.resetLoadCase()
    preprocessor.getLoadHandler.addToDomain(comb)
    result= analysis.analyze(1)
    uy= max(abs(n1.getDisp[1]), abs(n2.getDisp[1]))
    lim= deflectionLimits[comb]
    if(uy<lim):
        print('    '+comb, 'uy= ', uy*1e3, 'mm < ', lim*1e3, 'mm => OK')
    else:
        print('    '+comb, 'uy= ', uy*1e3, 'mm > ', lim*1e3, 'mm => KO')

## Check flexural and shear strength.
print('  Ultimate limit states.')
for comb in combContainer.ULS.perm:
    preprocessor.resetLoadCase()
    preprocessor.getLoadHandler.addToDomain(comb)
    result= analysis.analyze(1)
    nodes.calculateNodalReactions(True,1e-7)
    VMax= -1e23
    VMin= -VMax
    MMax= -1e23
    MMin= -MMax
    for e in xcTotalSet.elements:
      VMax= max(VMax,max(e.getV1, e.getV2))
      VMin= min(VMin,min(e.getV1, e.getV2))
      MMax= max(MMax,max(e.getM1, e.getM2))
      MMin= min(MMin,min(e.getM1, e.getM2))
    Vmax= max(VMax,abs(VMin))
    Mmax= max(MMax,abs(MMin))
    Phi_b= 0.90 # LRFD
    Mu= Phi_b*profile.getWz()*profile.steelType.fy
    if(Mmax<Mu):
        print('    '+comb, 'Mmax= ', Mmax/1e3, 'kN m < ',  Mu/1e3, 'kN m => OK')
    else:
        print('    '+comb, 'Mmax= ', Mmax/1e3, 'kN m > ',  Mu/1e3, 'kN m => KO')
    Phi_v= 1.0 # LRFD AISC Specification section G2.1a
    Vu= Phi_v*profile.getNominalShearStrengthWithoutTensionFieldAction()
    if(Vmax<Vu):
        print('    '+comb, 'Vmax= ', Vmax/1e3, 'kN < ',  Vu/1e3, 'kN => OK')
    else:
        print('    '+comb, 'Vmax= ', Vmax/1e3, 'kN > ',  Vu/1e3, 'kN => KO')

quit()
# Checking
VMax= -1e23
VMin= -VMax
MMax= -1e23
MMin= -MMax
for e in xcTotalSet.elements:
  VMax= max(VMax,max(e.getV1, e.getV2))
  VMin= min(VMin,min(e.getV1, e.getV2))
  MMax= max(MMax,max(e.getM1, e.getM2))
  MMin= min(MMin,min(e.getM1, e.getM2))
Vmax= max(VMax,abs(VMin))
Mmax= max(MMax,abs(MMin))
eMidSpan1= xcTotalSet.getNearestElement(midPos1)
eMidSpan2= xcTotalSet.getNearestElement(midPos2)

print('Uniform load: ', 2*uniformLoad/1e3, ' kN/m')
print('Uniform load on each : ', uniformLoad/1e3, ' kN/m')
## Deflection
ratio1= d1/span
print('dY= ',d1*1e3,' mm; ratio= L/', 1/ratio1, 'L= ', span, ' m')
ratio2= d2/span
print('dY= ',d2*1e3,' mm; ratio= L/', 1/ratio2)

## Shear
Vu= profile.steelType.fy/math.sqrt(3.0)*profile.get('Avy')/1.67
print('Vmax= ', Vmax/1e3, ' kN Vu= ', Vu/1e3, ' kN; F= ',Vmax/Vu)

## Bending
Mu= profile.getWz()*profile.steelType.fy/1.67#250e6
print('Mmax= ', Mmax/1e3, ' kN m Mu= ', Mu/1e3, ' kN m; F= ',Mmax/Mu)


## Reactions.
R0= p0.getNode().getReaction[1]
R1= p1.getNode().getReaction[1]
R2= p2.getNode().getReaction[1]

print('R0= ', R0/1e3,' kN')
print('R1= ', R1/1e3,' kN')
print('R2= ', R2/1e3,' kN')
