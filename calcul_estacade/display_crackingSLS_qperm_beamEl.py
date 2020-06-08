# -*- coding: utf-8 -*-
from postprocess.control_vars import *
from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import vtk_FE_graphic
from postprocess.xcVtk.diagrams import control_var_diagram as cvd
from postprocess import limit_state_data as lsd

model_path="./"
#Project directory structure
execfile(model_path+'env_config.py')

modelDataInputFile=model_path+"model_data.py" #data for FE model generation
execfile(modelDataInputFile)


#Load properties to display:
fName=  cfg.projectDirTree.getVerifCrackQpermFile()
execfile(fName)
execfile(model_path+'/captionTexts.py')

limitStateLabel= lsd.quasiPermanentLoadsCrackControl.label

#Possible arguments: 'getCF', 'getMaxSteelStress'
argument= 'getMaxSteelStress'

setDispRes= setColumns #set of linear elements to which display results 

diagram= cvd.ControlVarDiagram(scaleFactor= 0.02,fUnitConv= 1,sets=[setDispRes],attributeName= limitStateLabel,component= argument)
diagram.addDiagram()

displaySettings= vtk_FE_graphic.DisplaySettingsFE()
 #predefined view names: 'XYZPos','XNeg','XPos','YNeg','YPos',
 #                        'ZNeg','ZPos'  (defaults to 'XYZPos')
#displaySettings.cameraParameters= vtk_graphic_base.CameraParameters('YPos') #Point of view.
displaySettings.setupGrid(setDispRes)
displaySettings.defineMeshScene(None)
displaySettings.appendDiagram(diagram) #Append diagram to the scene.

caption= capTexts[limitStateLabel] + ', ' + capTexts[argument] + '. '+ setDispRes.genDescr.capitalize() + ', ' + setDispRes.sectDescr[0]
displaySettings.displayScene(caption)



