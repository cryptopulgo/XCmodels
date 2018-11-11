# -*- coding: utf-8 -*-
from postprocess.control_vars import *
from postprocess import limit_state_data as lsd
from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import vtk_display_limit_state as dls


modelDataInputFile= "model_data.py" #data for FE model generation
execfile(modelDataInputFile)


#Load properties to display:
preprocessor= FEcase.getPreprocessor
execfile('results/verifications/verifRsl_shearULS.py')
execfile('captionTexts.py')


limitStateLabel= lsd.shearResistance.label
#attributeName= limitStateLabel + 'Sect1'   #Shear limit state direction 1.
#attributeName= limitStateLabel + 'Sect2'   #Shear limit state direction 2


#Possible arguments: 'CF', 'N', 'My', 'Mz', 'Mu', 'Vy', 'Vz', 'theta', 'Vcu', 'Vsu', 'Vu'
argument= 'Vu'


# #Flatten values.
# if( "FCCP" in attributeName):
#   extrapolate_elem_attr.flatten_attribute(elemSet,attributeName,1,2)


setDisp= parapetHeadSet #parapetBodySet #parapetHeadSet
dls.displayFieldDirs1and2(limitStateLabel,argument,setDisp,None,1.0,None,capTexts,viewDef= vtk_graphic_base.CameraParameters("-X+Y+Z"),defFScale=0.0)



