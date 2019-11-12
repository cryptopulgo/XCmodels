# -*- coding: utf-8 -*-
from postprocess.reports import graphical_reports

execfile('../model_data.py')
execfile('../loadStateData.py')
execfile('../captionTexts.py')

pathGrph= cfg.projectDirTree.getReportLoadsGrPath()   #directory to place the figures
                                  #(do not use ./text/....)'
texReportFile= cfg.projectDirTree.getReportLoadsFile()  #laTex file where to include the graphics 
#ordered list of load cases (from those defined in ../loadStateData.py
#or redefined lately) to be displayed:
loadCasesToDisplay=[G1,G2,G3,Q1ayb,Q1a,Q1b,Q2ayb,Q2a,Q2b]
cfg.grWidth='120mm'   #width of the graphics for the tex file

textfl=open(texReportFile,'w')  #tex file to be generated
for lc in loadCasesToDisplay:
    lc.loadReports(gridmodl=model,pathGr=pathGrph,texFile=textfl,grWdt= cfg.grWidth)

textfl.close()
  
