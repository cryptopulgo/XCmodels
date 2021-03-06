# -*- coding: utf-8 -*-
from postprocess.control_vars import *
from postprocess import limit_state_data as lsd
from postprocess.reports import graphical_reports

execfile("../model_gen.py") #FE model generation

#Load properties to display:
execfile("../env_config_deck.py")
execfile(cfg.projectDirTree.getVerifCrackFreqFile())

limitStateLabel= lsd.freqLoadsCrackControl.label


# Ordered list of sets (defined in model_data.py as instances of
# utils_display.setToDisplay) to be included in the report
setsShEl=[decks]
# Ordered list of arguments to be included in the report
# Possible arguments: 'getMaxSteelStress', 'getCF'
argsShEl= ['getMaxSteelStress']
# Ordered list of lists [set of beam elements, view to represent this set] to
# be included in the report. 
# The sets are defined in model_data.py as instances of
# utils_display.setToDisplay and the possible views are: 'XYZPos','XNeg','XPos',
# 'YNeg','YPos','ZNeg','ZPos'  (defaults to 'XYZPos')
setsBmElView=[[beamXconcr,'XYZPos']]
setsBmElView=[]

# Ordered list of lists [arguments, scale to represent the argument] to be
# included in the report for beam elements
# Possible arguments: 'getMaxSteelStress', 'getCF'
argsBmElScale=[['getCF',1],['getMaxSteelStress',1]]
argsBmElScale=[]


graphical_reports.checksReports(limitStateLabel=limitStateLabel,setsShEl=setsShEl,argsShEl=argsShEl,capTexts= cfg.capTexts,pathGr= cfg.reportCrackFreqGrPath,texReportFile= cfg.reportCrackFreqFile,grWdt= cfg.grWidth,setsBmElView=setsBmElView,argsBmElScale=argsBmElScale)

