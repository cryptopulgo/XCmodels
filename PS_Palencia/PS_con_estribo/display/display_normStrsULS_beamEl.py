# -*- coding: utf-8 -*-
from postprocess.control_vars import *
from postprocess import limit_state_data as lsd
from postprocess.xcVtk import vtk_graphic_base
from postprocess.xcVtk.FE_model import quick_graphics as qg

execfile("../model_gen.py") #FE model generation

#choose env_config file:
execfile("../env_config_deck.py")
#execfile("../env_config_abutment.py")
#

#Load properties to display:
execfile(cfg.projectDirTree.getVerifNormStrFile())

#  Config
argument= 'CF'       #Possible arguments:
                     #RC elem: 'CF', 'N', 'My', 'Mz'
                     #steel elem: 'CF', 'N', 'My', 'Mz','Ncrd','McRdy','McRdz',
                     #            'MvRdz','MbRdz','chiLT'
setDispRes=setArmPil   #set of linear elements to display results
setDisp=setArmPil   #set of elements (any type) to be displayed
scaleFactor=1        #scale factor to apply to the auto-scales diagram (can be negative)
fUnitConv=1          #unit conversion factor (i.e N->kN => fUnitConv= 1e-3)
#  End config 

caption= cfg.capTexts[lsd.normalStressesResistance.label] + ', ' + cfg.capTexts[argument] + '. '#+ setsDispRes[0].description.capitalize() + ', ' 

lcs= qg.LoadCaseResults(FEcase)
lcs.displayBeamResult(attributeName=lsd.normalStressesResistance.label,itemToDisp=argument,beamSetDispRes=setDispRes,setToDisplay=setDisp,caption=caption,fileName=None,defFScale=0.0)



