# -*- coding: utf-8 -*-
from postprocess.control_vars import *
from postprocess import limit_state_data as lsd
from postprocess.xcVtk.FE_model import vtk_FE_graphic
from postprocess.xcVtk import control_var_diagram as cvd

model_path="../"
#Project directory structure
execfile(model_path+'project_directories.py')

modelDataInputFile=model_path+"model_data.py" #data for FE model generation
execfile(modelDataInputFile)


#Load properties to display:
fName= model_path+check_results_directory+'verifRsl_shearULS.py'
execfile(fName)
execfile('../captionTexts.py')


limitStateLabel= lsd.shearResistance.label


#Available arguments: 'CF', 'N', 'My', 'Mz', 'Mu', 'Vy', 'Vz', 'theta', 'Vcu', 'Vsu', 'CF'
argument= 'Vcu'

setDispRes=beamX   #set of linear elements to which display results 

#setDisp=overallSet    #set of elements (any type) to be displayed
setDisp=beamX

diagram= cvd.ControlVarDiagram(scaleFactor= 1,fUnitConv= 1,sets=[setDispRes],attributeName= limitStateLabel,component= argument)
diagram.addDiagram()


defDisplay= vtk_FE_graphic.RecordDefDisplayEF()
 #predefined view names: 'XYZPos','XNeg','XPos','YNeg','YPos',
 #                        'ZNeg','ZPos'  (defaults to 'XYZPos')
defDisplay.viewName= "YPos" #Point of view.
defDisplay.setupGrid(setDisp)
defDisplay.defineMeshScene(None,defFScale=0.0)
defDisplay.appendDiagram(diagram) #Append diagram to the scene.

caption= capTexts[limitStateLabel] + ', ' + capTexts[argument] + '. '+ setDispRes.description.capitalize() + ', ' + 'Dir. 1'
defDisplay.displayScene(caption)



