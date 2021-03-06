# -*- coding: utf-8 -*-
from postprocess.reports import graphical_reports

execfile("../model_gen.py") #FE model generation
execfile('../load_state_data.py')
loadCasesToDisplay=[G1,Q1]

pathGrph= cfg.projectDirTree.getReportLoadsGrPath()   #directory to place the figures
                                  #(do not use ./text/....)'
texReportFile= cfg.projectDirTree.getReportLoadsFile()  #laTex file where to include the graphics 
#ordered list of load cases (from those defined in ../load_state_data.py
#or redefined lately) to be displayed:

textfl=open(texReportFile,'w')  #tex file to be generated
for lc in loadCasesToDisplay:
    lc.loadReports(FEcase=FEcase,pathGr=pathGrph,texFile=textfl,cfg= cfg)
    

textfl.close()
  
