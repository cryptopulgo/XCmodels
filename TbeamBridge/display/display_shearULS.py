# -*- coding: utf-8 -*-
from postprocess.control_vars import *
from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import vtk_FE_graphic
from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import Fields

model_path="../"
#Project directory structure
execfile(model_path+'env_config.py')

modelDataInputFile=model_path+"model_data.py" #data for FE model generation
execfile(modelDataInputFile)


#Load properties to display:
preprocessor= model.getPreprocessor()
fName=  cfg.projectDirTree.getVerifShearFile()
execfile(fName)


#xcSet= deckSet
#xcSet= foundationSet
#xcSet= wallsSet

limitStateLabel= lsd.shearResistance.label
#attributeName= limitStateLabel + 'Sect1'   #Shear limit state direction 1.
#attributeName= limitStateLabel + 'Sect2'   #Shear limit state direction 2


#Possible arguments: 'CF', 'N', 'My', 'Mz', 'Mu', 'Vy', 'Vz', 'theta', 'Vcu', 'Vsu', 'Vu'
argument= 'CF'


# #Flatten values.
# if( "FCCP" in attributeName):
#   extrapolate_elem_attr.flatten_attribute(elemSet,attributeName,1,2)


displaySettings= vtk_FE_graphic.DisplaySettingsFE()
xcSet= deckSet
attributeName= limitStateLabel + 'Sect1'
field= Fields.getScalarFieldFromControlVar(attributeName,argument,xcSet,None,1.0)
field.plot(displaySettings,caption= 'Shear check '+ attributeName + '  '+xcSet.name+ '  '+argument)
attributeName= limitStateLabel + 'Sect2'
field= Fields.getScalarFieldFromControlVar(attributeName,argument,xcSet,None,1.0)
field.plot(displaySettings,caption= 'Shear check '+ attributeName + ' '+xcSet.name+ '  '+argument)
xcSet= foundationSet
attributeName= limitStateLabel + 'Sect1'
field= Fields.getScalarFieldFromControlVar(attributeName,argument,xcSet,None,1.0)
field.plot(displaySettings,caption= 'Shear check '+ attributeName + ' '+xcSet.name+ '  '+argument)
attributeName= limitStateLabel + 'Sect2'
field= Fields.getScalarFieldFromControlVar(attributeName,argument,xcSet,None,1.0)
field.plot(displaySettings,caption= 'Shear check '+ attributeName + ' '+xcSet.name+ '  '+argument)
xcSet= wallsSet
attributeName= limitStateLabel + 'Sect1'
field= Fields.getScalarFieldFromControlVar(attributeName,argument,xcSet,None,1.0)
field.plot(displaySettings,caption= 'Shear check '+ attributeName + ' '+xcSet.name+ '  '+argument)
attributeName= limitStateLabel + 'Sect2'
field= Fields.getScalarFieldFromControlVar(attributeName,argument,xcSet,None,1.0)
field.plot(displaySettings,caption= 'Shear check '+ attributeName + ' '+xcSet.name+ '  '+argument)

