# -*- coding: utf-8 -*-

'''In this script we define default data of load cases to be used (or changed)
while displaying loads or results associated to single load cases 
'''
from postprocess.xcVtk import vtk_graphic_base
from postprocess.reports import graphical_reports
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
                  forces (defaults to (1.0,1.0,1.0))
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
if Lvoladzd >0:
    setsForc=[zap,murestr,aletd]
else:
    setsForc=[zap,murestr,aleti]

    
G1=graphical_reports.RecordLoadCaseDisp(loadCaseName='G1',loadCaseDescr='G1: peso propio',loadCaseExpr='1.0*G1',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=setsForc)
G1.unitsScaleLoads=1e-3
G1.unitsScaleDispl=1e3
G1.unitsDispl='[mm]'
G1.unitsScaleMom=1e-3
G1.unitsMom='[m.kN]'
G1.unitsScaleForc=1e-3
G1.unitsForc='[kN]'
G1.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')
#G1.cameraParameters.hCamFct=1.5
G1.setsToDispBeamLoads=[]
#G1.compElLoad='transYComponent'

G2=graphical_reports.RecordLoadCaseDisp(loadCaseName='G2',loadCaseDescr='G2: carga muerta',loadCaseExpr='1.0*G2',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=setsForc)
G2.unitsScaleLoads=1e-3
G2.unitsScaleDispl=1e3
G2.unitsDispl='[mm]'
G2.unitsScaleMom=1e-3
G2.unitsMom='[m.kN]'
G2.unitsScaleForc=1e-3
G2.unitsForc='[kN]'
G2.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')


G3=graphical_reports.RecordLoadCaseDisp(loadCaseName='G3',loadCaseDescr='G3: retracción',loadCaseExpr='1.0*G3',setsToDispLoads=[],setsToDispDspRot=[overallSet],setsToDispIntForc=setsForc)
G3.unitsScaleLoads=1e-3
G3.unitsScaleDispl=1e3
G3.unitsDispl='[mm]'
G3.unitsScaleMom=1e-3
G3.unitsMom='[m.kN]'
G3.unitsScaleForc=1e-3
G3.unitsForc='[kN]'
G3.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')


G4=graphical_reports.RecordLoadCaseDisp(loadCaseName='G4',loadCaseDescr='G4: empuje del terreno',loadCaseExpr='1.0*G4',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=setsForc)
G4.unitsScaleLoads=1e-3
G4.unitsScaleDispl=1e3
G4.unitsDispl='[mm]'
G4.unitsScaleMom=1e-3
G4.unitsMom='[m.kN]'
G4.unitsScaleForc=1e-3
G4.unitsForc='[kN]'
G4.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')



Q1a_1=graphical_reports.RecordLoadCaseDisp(loadCaseName='Q1a_1',loadCaseDescr='Q1a_1: tren de cargas, posición A1',loadCaseExpr='1.0*Q1a_1',setsToDispLoads=[overallSet],setsToDispDspRot=[],setsToDispIntForc=setsForc)
Q1a_1.unitsScaleLoads=1e-3
Q1a_1.unitsScaleDispl=1e3
Q1a_1.unitsDispl='[mm]'
Q1a_1.unitsScaleMom=1e-3
Q1a_1.unitsMom='[m.kN]'
Q1a_1.unitsScaleForc=1e-3
Q1a_1.unitsForc='[kN]'
Q1a_1.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')


Q1a_2=graphical_reports.RecordLoadCaseDisp(loadCaseName='Q1a_2',loadCaseDescr='Q1a_2: tren de cargas, posición A2',loadCaseExpr='1.0*Q1a_2',setsToDispLoads=[overallSet],setsToDispDspRot=[],setsToDispIntForc=setsForc)
Q1a_2.unitsScaleLoads=1e-3
Q1a_2.unitsScaleDispl=1e3
Q1a_2.unitsDispl='[mm]'
Q1a_2.unitsScaleMom=1e-3
Q1a_2.unitsMom='[m.kN]'
Q1a_2.unitsScaleForc=1e-3
Q1a_2.unitsForc='[kN]'
Q1a_2.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')


Q1b_1=graphical_reports.RecordLoadCaseDisp(loadCaseName='Q1b_1',loadCaseDescr='Q1b_1: tren de cargas, posición B1',loadCaseExpr='1.0*Q1b_1',setsToDispLoads=[overallSet],setsToDispDspRot=[],setsToDispIntForc=setsForc)
Q1b_1.unitsScaleLoads=1e-3
Q1b_1.unitsScaleDispl=1e3
Q1b_1.unitsDispl='[mm]'
Q1b_1.unitsScaleMom=1e-3
Q1b_1.unitsMom='[m.kN]'
Q1b_1.unitsScaleForc=1e-3
Q1b_1.unitsForc='[kN]'
Q1b_1.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')


Q1b_2=graphical_reports.RecordLoadCaseDisp(loadCaseName='Q1b_2',loadCaseDescr='Q1b_2: tren de cargas, posición B2',loadCaseExpr='1.0*Q1b_2',setsToDispLoads=[overallSet],setsToDispDspRot=[],setsToDispIntForc=setsForc)
Q1b_2.unitsScaleLoads=1e-3
Q1b_2.unitsScaleDispl=1e3
Q1b_2.unitsDispl='[mm]'
Q1b_2.unitsScaleMom=1e-3
Q1b_2.unitsMom='[m.kN]'
Q1b_2.unitsScaleForc=1e-3
Q1b_2.unitsForc='[kN]'
Q1b_2.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')


Q1c=graphical_reports.RecordLoadCaseDisp(loadCaseName='Q1c',loadCaseDescr='Q1c: tren de cargas, posición C',loadCaseExpr='1.0*Q1c',setsToDispLoads=[overallSet],setsToDispDspRot=[],setsToDispIntForc=setsForc)
Q1c.unitsScaleLoads=1e-3
Q1c.unitsScaleDispl=1e3
Q1c.unitsDispl='[mm]'
Q1c.unitsScaleMom=1e-3
Q1c.unitsMom='[m.kN]'
Q1c.unitsScaleForc=1e-3
Q1c.unitsForc='[kN]'
Q1c.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')


Q1d=graphical_reports.RecordLoadCaseDisp(loadCaseName='Q1d',loadCaseDescr='Q1d: tren de cargas, posición D',loadCaseExpr='1.0*Q1d',setsToDispLoads=[overallSet],setsToDispDspRot=[],setsToDispIntForc=setsForc)
Q1d.unitsScaleLoads=1e-3
Q1d.unitsScaleDispl=1e3
Q1d.unitsDispl='[mm]'
Q1d.unitsScaleMom=1e-3
Q1d.unitsMom='[m.kN]'
Q1d.unitsScaleForc=1e-3
Q1d.unitsForc='[kN]'
Q1d.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')


Q1e=graphical_reports.RecordLoadCaseDisp(loadCaseName='Q1e',loadCaseDescr='Q1e: tren de cargas, posición E',loadCaseExpr='1.0*Q1e',setsToDispLoads=[overallSet],setsToDispDspRot=[],setsToDispIntForc=setsForc)
Q1e.unitsScaleLoads=1e-3
Q1e.unitsScaleDispl=1e3
Q1e.unitsDispl='[mm]'
Q1e.unitsScaleMom=1e-3
Q1e.unitsMom='[m.kN]'
Q1e.unitsScaleForc=1e-3
Q1e.unitsForc='[kN]'
Q1e.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')


Q1f=graphical_reports.RecordLoadCaseDisp(loadCaseName='Q1f',loadCaseDescr='Q1f: tren de cargas, posición F',loadCaseExpr='1.0*Q1f',setsToDispLoads=[overallSet],setsToDispDspRot=[],setsToDispIntForc=setsForc)
Q1f.unitsScaleLoads=1e-3
Q1f.unitsScaleDispl=1e3
Q1f.unitsDispl='[mm]'
Q1f.unitsScaleMom=1e-3
Q1f.unitsMom='[m.kN]'
Q1f.unitsScaleForc=1e-3
Q1f.unitsForc='[kN]'
Q1f.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')



Q1b_fren=graphical_reports.RecordLoadCaseDisp(loadCaseName='Q1b_fren',loadCaseDescr='Q1b_fren: tren de cargas, posición B1+frenado',loadCaseExpr='1.0*Q1b_fren',setsToDispLoads=[overallSet],setsToDispDspRot=[],setsToDispIntForc=setsForc)
Q1b_fren.unitsScaleLoads=1e-3
Q1b_fren.unitsScaleDispl=1e3
Q1b_fren.unitsDispl='[mm]'
Q1b_fren.unitsScaleMom=1e-3
Q1b_fren.unitsMom='[m.kN]'
Q1b_fren.unitsScaleForc=1e-3
Q1b_fren.unitsForc='[kN]'
Q1b_fren.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')
#Q1b_fren.cameraParameters.hCamFct=1.5

Q1d_fren=graphical_reports.RecordLoadCaseDisp(loadCaseName='Q1d_fren',loadCaseDescr='Q1d_fren: tren de cargas, posición D+frenado',loadCaseExpr='1.0*Q1d_fren',setsToDispLoads=[overallSet],setsToDispDspRot=[],setsToDispIntForc=setsForc)
Q1d_fren.unitsScaleLoads=1e-3
Q1d_fren.unitsScaleDispl=1e3
Q1d_fren.unitsDispl='[mm]'
Q1d_fren.unitsScaleMom=1e-3
Q1d_fren.unitsMom='[m.kN]'
Q1d_fren.unitsScaleForc=1e-3
Q1d_fren.unitsForc='[kN]'
Q1d_fren.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')
#Q1d_fren.cameraParameters.hCamFct=1.5

Q1e_fren=graphical_reports.RecordLoadCaseDisp(loadCaseName='Q1e_fren',loadCaseDescr='Q1e_fren: tren de cargas, posición E+frenado',loadCaseExpr='1.0*Q1e_fren',setsToDispLoads=[overallSet],setsToDispDspRot=[],setsToDispIntForc=setsForc)
Q1e_fren.unitsScaleLoads=1e-3
Q1e_fren.unitsScaleDispl=1e3
Q1e_fren.unitsDispl='[mm]'
Q1e_fren.unitsScaleMom=1e-3
Q1e_fren.unitsMom='[m.kN]'
Q1e_fren.unitsScaleForc=1e-3
Q1e_fren.unitsForc='[kN]'
Q1e_fren.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')
#Q1e_fren.cameraParameters.hCamFct=1.5

Q2_1=graphical_reports.RecordLoadCaseDisp(loadCaseName='Q2_1',loadCaseDescr='Q2_1: viento aislado',loadCaseExpr='1.0*Q2_1',setsToDispLoads=[overallSet],setsToDispDspRot=[],setsToDispIntForc=setsForc)
Q2_1.unitsScaleLoads=1e-3
Q2_1.unitsScaleDispl=1e3
Q2_1.unitsDispl='[mm]'
Q2_1.unitsScaleMom=1e-3
Q2_1.unitsMom='[m.kN]'
Q2_1.unitsScaleForc=1e-3
Q2_1.unitsForc='[kN]'
Q2_1.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')
#Q2_1.cameraParameters.hCamFct=1.9
Q2_1.setsToDispBeamLoads=[]

Q2_2=graphical_reports.RecordLoadCaseDisp(loadCaseName='Q2_2',loadCaseDescr='Q2_2: viento con SC uso',loadCaseExpr='1.0*Q2_2',setsToDispLoads=[overallSet],setsToDispDspRot=[],setsToDispIntForc=setsForc)
Q2_2.unitsScaleLoads=1e-3
Q2_2.unitsScaleDispl=1e3
Q2_2.unitsDispl='[mm]'
Q2_2.unitsScaleMom=1e-3
Q2_2.unitsMom='[m.kN]'
Q2_2.unitsScaleForc=1e-3
Q2_2.unitsForc='[kN]'
Q2_2.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')
#Q2_2.cameraParameters.hCamFct=1.9


Q3_1=graphical_reports.RecordLoadCaseDisp(loadCaseName='Q3_1',loadCaseDescr='Q3_1: temperatura uniforme, contracción',loadCaseExpr='1.0*Q3_1',setsToDispLoads=[],setsToDispDspRot=[overallSet],setsToDispIntForc=setsForc)
Q3_1.unitsScaleLoads=1e-3
Q3_1.unitsScaleDispl=1e3
Q3_1.unitsDispl='[mm]'
Q3_1.unitsScaleMom=1e-3
Q3_1.unitsMom='[m.kN]'
Q3_1.unitsScaleForc=1e-3
Q3_1.unitsForc='[kN]'
Q3_1.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')


Q3_2=graphical_reports.RecordLoadCaseDisp(loadCaseName='Q3_2',loadCaseDescr='Q3_2: temperatura uniforme, dilatación',loadCaseExpr='1.0*Q3_2',setsToDispLoads=[],setsToDispDspRot=[overallSet],setsToDispIntForc=setsForc)
Q3_2.unitsScaleLoads=1e-3
Q3_2.unitsScaleDispl=1e3
Q3_2.unitsDispl='[mm]'
Q3_2.unitsScaleMom=1e-3
Q3_2.unitsMom='[m.kN]'
Q3_2.unitsScaleForc=1e-3
Q3_2.unitsForc='[kN]'
Q3_2.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')


Q3_3=graphical_reports.RecordLoadCaseDisp(loadCaseName='Q3_3',loadCaseDescr='Q3_3: diferencia temperatura, fibra sup. más caliente',loadCaseExpr='1.0*Q3_3',setsToDispLoads=[],setsToDispDspRot=[overallSet],setsToDispIntForc=setsForc)
Q3_3.unitsScaleLoads=1e-3
Q3_3.unitsScaleDispl=1e3
Q3_3.unitsDispl='[mm]'
Q3_3.unitsScaleMom=1e-3
Q3_3.unitsMom='[m.kN]'
Q3_3.unitsScaleForc=1e-3
Q3_3.unitsForc='[kN]'
Q3_3.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')


Q3_4=graphical_reports.RecordLoadCaseDisp(loadCaseName='Q3_4',loadCaseDescr='Q3_4: diferencia temperatura, fibra sup. más fría',loadCaseExpr='1.0*Q3_4',setsToDispLoads=[],setsToDispDspRot=[overallSet],setsToDispIntForc=setsForc)
Q3_4.unitsScaleLoads=1e-3
Q3_4.unitsScaleDispl=1e3
Q3_4.unitsDispl='[mm]'
Q3_4.unitsScaleMom=1e-3
Q3_4.unitsMom='[m.kN]'
Q3_4.unitsScaleForc=1e-3
Q3_4.unitsForc='[kN]'
Q3_4.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')


Q4=graphical_reports.RecordLoadCaseDisp(loadCaseName='Q4',loadCaseDescr='Q4: sobrecarga sobre relleno trasdós',loadCaseExpr='1.0*Q4',setsToDispLoads=[overallSet],setsToDispDspRot=[overallSet],setsToDispIntForc=[zap])
Q4.unitsScaleLoads=1e-3
Q4.unitsScaleDispl=1e3
Q4.unitsDispl='[mm]'
Q4.unitsScaleMom=1e-3
Q4.unitsMom='[m.kN]'
Q4.unitsScaleForc=1e-3
Q4.unitsForc='[kN]'
Q4.cameraParameters= vtk_graphic_base.CameraParameters('XYZPos',1.5)
Q4.setsToDispBeamLoads=[]
#
resLoadCases=[G1,G2,G3,G4,Q1a_1,Q1a_2,Q1b_1,Q1b_2,Q1c,Q1d,Q1e,Q1f,Q1b_fren,Q1e_fren,Q1d_fren,Q2_1,Q2_2,Q3_1,Q3_2,Q3_3,Q3_4,Q4]
