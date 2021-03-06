# -*- coding: utf-8 -*-
from postprocess.control_vars import *
from postprocess import limit_state_data as lsd
from postprocess.xcVtk import vtk_graphic_base
from postprocess import output_handler

execfile("../model_gen.py") #FE model generation

#choose env_config file:
execfile("../env_config_deck.py")
#execfile("../env_config_abutment.py")
#
#Load properties to display:
execfile(cfg.projectDirTree.getVerifShearFile())


#  Config
argument= 'CF'       #Possible arguments: 'CF', 'N', 'My', 'Mz', 'Mu', 'Vy',
                     #'Vz', 'theta', 'Vcu', 'Vsu', 'Vu'
setDisp= setArmados
#setDisp= setArmLosa
#setDisp=setArmCart
#setDisp= setArmVol
#setDisp=setArmREstr
#setDisp=setArmLosa+setArmCart+setArmVol
#setDisp=sets_arm_losa[3]
setDisp= setArmZ4

#setDisp=setArmadosEstr


cameraParameters= vtk_graphic_base.CameraParameters('XYZPos')
rgMinMax=None     #truncate values to be included in the range
                     #(if None -> don't truncate)
#  End config 


oh= output_handler.OutputHandler(modelSpace)
oh.outputStyle.cameraParameters= cameraParameters
oh.displayFieldDirs1and2(limitStateLabel=lsd.shearResistance.label,argument=argument,setToDisplay=setDisp,component=None,fileName=None,defFScale=0.0,rgMinMax=rgMinMax)




