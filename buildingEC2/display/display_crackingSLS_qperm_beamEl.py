# -*- coding: utf-8 -*-
from postprocess.control_vars import *
from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import vtk_FE_graphic
from postprocess.xcVtk.diagrams import control_var_diagram as cvd

model_path="../"
#Project directory structure
execfile(model_path+'env_config.py')

modelDataInputFile=model_path+"model_data.py" #data for FE model generation
execfile(modelDataInputFile)


#Load properties to display:
preprocessor= model.getPreprocessor()
fName=  cfg.projectDirTree.getVerifCrackQpermFile()
execfile(fName)
execfile('../captionTexts.py')

limitStateLabel= lsd.quasiPermanentLoadsCrackControl.label

#Possible arguments: 'getCF', 'getMaxSteelStress'
argument= 'getMaxSteelStress'


setDispRes=beamXSet   #set of linear elements to which display results 

setDisp=xcTotalSet    #set of elements (any type) to be displayed

diagram= cvd.ControlVarDiagram(scaleFactor= 1,fUnitConv= 100,sets=[setDispRes.elSet],attributeName= limitStateLabel,component= argument)
diagram.addDiagram()

defDisplay= vtk_FE_graphic.RecordDefDisplayEF()
 #predefined view names: 'XYZPos','XNeg','XPos','YNeg','YPos',
 #                        'ZNeg','ZPos'  (defaults to 'XYZPos')
#defDisplay.cameraParameters= vtk_graphic_base.CameraParameters('YPos') #Point of view.
defDisplay.setupGrid(setDisp.elSet)
defDisplay.defineMeshScene(None)
defDisplay.appendDiagram(diagram) #Append diagram to the scene.

caption= capTexts[limitStateLabel] + ', ' + capTexts[argument] + '. '+ setDispRes.genDescr.capitalize() + ', ' + setDispRes.sectDescr[0]
defDisplay.displayScene(caption)



