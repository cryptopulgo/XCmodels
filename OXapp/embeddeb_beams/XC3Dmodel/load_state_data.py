# -*- coding: utf-8 -*-

'''In this script we define default data of load cases to be used (or changed)
while displaying loads or results associated to single load cases 
'''
from postprocess.xcVtk import vtk_graphic_base
from postprocess.reports import graphical_reports
from postprocess.xcVtk import vtk_graphic_base
'''
Definition of record objects with these attributes:
  loadCaseName:  name of the load case to be depicted
  loadCaseDescr: description text of the load case
  loadCaseExpr:  mathematical expression to define the load case (ex:
                 '1.0*GselfWeight+1.0*DeadLoad')
  setsToDispLoads: ordered list of sets of elements to display loads
  setsToDispBeamLoads: ordered list of sets of beam elements to display loads
                 (defaults to [])
  compElLoad: component of load on beam elements to be represented
              available components: 'axialComponent', 'transComponent',
              'transYComponent','transZComponent'
  unitsScaleLoads: factor to apply to loads if we want to change
                 the units (defaults to 1).
  unitsLoads: text to especify the units in which loads are 
                 represented (defaults to 'units:[m,kN]')
  vectorScaleLoads: factor to apply to the vectors length in the 
                 representation of loads (defaults to 1 -> auto-scale).
  vectorScalePointLoads: factor to apply to the vectors length in the 
                 representation of nodal loads (defaults to 1).
  multByElemAreaLoads: boolean value that must be True if we want to 
                 represent the total load on each element 
                 (=load multiplied by element area) and False if we 
                 are going to depict the value of the uniform load 
                 per unit area (defaults to False)
  listDspRot: ordered list of displacement or rotations to be displayed
                 available components: 'uX', 'uY', 'uZ', 'rotX', rotY', 'rotZ'
                 (defaults to ['uX', 'uY', 'uZ'])
  setsToDispDspRot: ordered list of sets of elements to display displacements 
                 or rotations
  unitsScaleDispl: factor to apply to displacements if we want to change
                 the units (defaults to 1).
  unitsDispl: text to especify the units in which displacements are 
                 represented (defaults to '[m]'
  listIntForc:   ordered list of internal forces to be displayed as scalar field 
                 over «shell» elements
                 available components: 'N1', 'N2', 'M1', 'M2', 'Q1', 'Q2'
                 (defaults to ['N1', 'N2', 'M1', 'M2', 'Q1', 'Q2'])
  setsToDispIntForc: ordered list of sets of elements (of type «shell»)to 
                    display internal forces
  listBeamIntForc: ordered list of internal forces to be displayed 
                 as diagrams on lines for «beam» elements
                 available components: 'N', 'My', 'Mz', 'Qy', 'Qz','T'
                 (defaults to ['N', 'My', 'Mz', 'Qy', 'Qz','T'])
  setsToDispBeamIntForc: ordered list of sets of elements (of type «beam»)to 
                    display internal forces (defaults to [])
  scaleDispBeamIntForc: tuple (escN,escQ,escM) correponding to the scales to 
                  apply to displays of, respectively, N Q and M beam internal 
                  forces (defaults to (1.0,1.0,1.0) -> auto-scale)
  unitsScaleForc: factor to apply to internal forces if we want to change
                 the units (defaults to 1).
  unitsForc: text to especify the units in which forces are 
                 represented (defaults to '[kN/m]')
  unitsScaleMom: factor to apply to internal moments if we want to change
                 the units (defaults to 1).
  unitsMom:  text to especify the units in which bending moments are 
                 represented (defaults to '[kN.m/m]')
  cameraParameters: parameters that define the position and orientation of the
                 camera (defaults to "XYZPos")
  
  cameraParametersBeams: parameters that define the position and orientation of the
                 camera for beam elements displays (defaults to "XYZPos")
  
'''




'''
G1=graphical_reports.RecordLoadCaseDisp(loadCaseName='GselfWeight',loadCaseDescr='G1: self weight',loadCaseExpr='1.0*GselfWeight',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[slabs])
G1.unitsScaleLoads=1e-3
G1.unitsScaleDispl=1e3
G1.unitsDispl='[mm]'
G1.unitsScaleMom=1e-3
G1.unitsMom='[m.kN]'
G1.unitsScaleForc=1e-3
G1.unitsForc='[kN]'
G1.setsToDispBeamIntForc=[beams,columns]
G1.listBeamIntForc=['My','Mz','Qy','Qz','N']
G1.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')
G1.setsToDispBeamLoads=[]
G1.vectorScalePointLoads=0.005
G1.compElLoad='transComponent'

'''
D=graphical_reports.RecordLoadCaseDisp(loadCaseName='DeadL',loadCaseDescr='D: dead load',loadCaseExpr='1.0*DeadL',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[slabs])


Lru=graphical_reports.RecordLoadCaseDisp(loadCaseName='LiveL_ru',loadCaseDescr='L_ru: live load (uniform on rooms)',loadCaseExpr='1.0*LiveL_ru',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[slabs])

Lrs=graphical_reports.RecordLoadCaseDisp(loadCaseName='LiveL_rs',loadCaseDescr='L_rs: live load (staggered pattern on rooms)',loadCaseExpr='1.0*LiveL_rs',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[slabs])

Lpu=graphical_reports.RecordLoadCaseDisp(loadCaseName='LiveL_pu',loadCaseDescr='L_pu: live load (uniform on terraces)',loadCaseExpr='1.0*LiveL_pu',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[slabs])

Lps=graphical_reports.RecordLoadCaseDisp(loadCaseName='LiveL_ps',loadCaseDescr='L_ps: live load (staggered pattern on terraces)',loadCaseExpr='1.0*LiveL_ps',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[slabs])

S=graphical_reports.RecordLoadCaseDisp(loadCaseName='SnowL',loadCaseDescr='S: snow load',loadCaseExpr='1.0*SnowL',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[slabs])


W_WE=graphical_reports.RecordLoadCaseDisp(loadCaseName='Wind_WE',loadCaseDescr='W_WE: Wind West-East',loadCaseExpr='1.0*Wind_WE',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[slabs])

W_NS=graphical_reports.RecordLoadCaseDisp(loadCaseName='Wind_NS',loadCaseDescr='W_NS: Wind North-South',loadCaseExpr='1.0*Wind_NS',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[slabs])


#Ultimate limit states
ULS01=graphical_reports.RecordLoadCaseDisp(loadCaseName='ULS01',loadCaseDescr='ULS01: 1.4*D',loadCaseExpr='1.4*DeadL',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[slabs])

ULS02_a=graphical_reports.RecordLoadCaseDisp(loadCaseName='ULS02_a',loadCaseDescr='ULS02_a: 1.2*D + 1.6*Lru + Lpu + 0.5*S',loadCaseExpr='1.2*DeadL+1.6*LiveL_ru+1.0*LiveL_pu+0.5*SnowL',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[slabs])

ULS02_b=graphical_reports.RecordLoadCaseDisp(loadCaseName='ULS02_b',loadCaseDescr='ULS02_b: 1.2*D + 1.6*Lrs + Lps + 0.5*S',loadCaseExpr='1.2*DeadL+1.6*LiveL_rs+1.0*LiveL_ps+0.5*SnowL',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[slabs])

ULS03_a=graphical_reports.RecordLoadCaseDisp(loadCaseName='ULS03_a',loadCaseDescr='ULS03_a: 1.2*D + 1.6*S + 0.5*Lru + Lpu',loadCaseExpr='1.2*DeadL+0.5*LiveL_ru+1.0*LiveL_pu+1.6*SnowL',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[slabs])

ULS03_b=graphical_reports.RecordLoadCaseDisp(loadCaseName='ULS03_b',loadCaseDescr='ULS03_b: 1.2*D + 1.6*S + 0.5*Lrs + Lps',loadCaseExpr='1.2*DeadL+0.5*LiveL_rs+1.0*LiveL_ps+1.6*SnowL',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[slabs])

ULS04_a=graphical_reports.RecordLoadCaseDisp(loadCaseName='ULS04_a',loadCaseDescr='ULS04_a: 1.2*D + 1.6*S + 0.5*W_WE',loadCaseExpr='1.2*DeadL+1.6*SnowL+0.5*Wind_WE',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[slabs])

ULS04_b=graphical_reports.RecordLoadCaseDisp(loadCaseName='ULS04_b',loadCaseDescr='ULS04_b: 1.2*D + 1.6*S + 0.5*W_NS',loadCaseExpr='1.2*DeadL+1.6*SnowL+0.5*Wind_NS',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[slabs])

ULS05_a=graphical_reports.RecordLoadCaseDisp(loadCaseName='ULS05_a',loadCaseDescr='ULS05_a: 1.2*D + W_WE + 0.5*Lru + Lpu',loadCaseExpr='1.2*DeadL+1.0*Wind_WE+0.5*LiveL_ru+1*LiveL_pu',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[slabs])

ULS05_b=graphical_reports.RecordLoadCaseDisp(loadCaseName='ULS05_b',loadCaseDescr='ULS05_b: 1.2*D + W_NS + 0.5*Lru + Lpu',loadCaseExpr='1.2*DeadL+1.0*Wind_NS+0.5*LiveL_ru+1*LiveL_pu',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[slabs])

ULS05_c=graphical_reports.RecordLoadCaseDisp(loadCaseName='ULS05_c',loadCaseDescr='ULS05_c: 1.2*D + W_WE + 0.5*Lrs + Lps',loadCaseExpr='1.2*DeadL+1.0*Wind_WE+0.5*LiveL_rs+1*LiveL_ps',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[slabs])

ULS05_d=graphical_reports.RecordLoadCaseDisp(loadCaseName='ULS05_d',loadCaseDescr='ULS05_d: 1.2*D + W_NS + 0.5*Lrs + Lps',loadCaseExpr='1.2*DeadL+1.0*Wind_NS+0.5*LiveL_rs+1*LiveL_ps',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[slabs])

ULS06_a=graphical_reports.RecordLoadCaseDisp(loadCaseName='ULS06_a',loadCaseDescr='ULS06_a: 1.2*D + 0.5*Lru + Lpu + 0.2*S',loadCaseExpr='1.2*DeadL+0.5*LiveL_ru+1*LiveL_pu+0.2*SnowL',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[slabs])

ULS06_b=graphical_reports.RecordLoadCaseDisp(loadCaseName='ULS06_b',loadCaseDescr='ULS06_b: 1.2*D + 0.5*Lrs + Lps + 0.2*S',loadCaseExpr='1.2*DeadL+0.5*LiveL_rs+1*LiveL_ps+0.2*SnowL',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[slabs])

ULS07_a=graphical_reports.RecordLoadCaseDisp(loadCaseName='ULS07_a',loadCaseDescr='ULS07_a: 0.9*D + W_WE',loadCaseExpr='0.9*DeadL+1.0*Wind_WE',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[slabs])

ULS07_b=graphical_reports.RecordLoadCaseDisp(loadCaseName='ULS07_b',loadCaseDescr='ULS07_b: 0.9*D + W_NS',loadCaseExpr='0.9*DeadL+1.0*Wind_NS',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[slabs])

LC=[D,Lru,Lrs,Lpu,Lps,S,W_WE,W_NS]
for lc in LC:
    lc.unitsScaleLoads=1e-3
    lc.unitsScaleDispl=1e3
    lc.unitsDispl='[mm]'
    lc.unitsScaleMom=1e-3
    lc.unitsMom='[m.kN]'
    lc.unitsScaleForc=1e-3
    lc.unitsForc='[kN]'
    lc.setsToDispBeamIntForc=[beams,columns]
    lc.listBeamIntForc=['My','Mz','Qy','Qz','N']
    lc.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')
    lc.setsToDispBeamLoads=[]
    lc.vectorScalePointLoads=0.005
    lc.compElLoad='transComponent'

#D.vectorScalePointLoads=1
    
ULS=[ULS01,ULS02_a,ULS02_b,ULS03_a,ULS03_b,ULS04_a,ULS04_b,ULS05_a,ULS05_b,ULS05_c,ULS05_d,ULS06_a,ULS06_b,ULS07_a,ULS07_b]
for lc in ULS:
    lc.setsToDispDspRot=[]#[overallSet]
    lc.setsToDispIntForc=[]
    lc.unitsScaleLoads=1e-3
    lc.unitsScaleDispl=1e3
    lc.unitsDispl='[mm]'
    lc.unitsScaleMom=1e-3
    lc.unitsMom='[m.kN]'
    lc.unitsScaleForc=1e-3
    lc.unitsForc='[kN]'
    lc.setsToDispBeamIntForc=[steel_beam]
    lc.listBeamIntForc=['My']#,'Qz']
    lc.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')
    lc.setsToDispBeamLoads=[]
    lc.vectorScalePointLoads=0.005
    lc.compElLoad='transYComponent'
    lc.compElLoad='axialComponent'
