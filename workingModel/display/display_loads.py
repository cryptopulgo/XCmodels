# -*- coding: utf-8 -*-

execfile("../model_gen.py") #FE model generation


execfile('../load_state_data.py')

from postprocess.xcVtk.FE_model import quick_graphics as qg

#ordered list of load cases (from those defined in ../load_state_data.py
#or redefined lately) to be displayed:
loadCasesToDisplay=[G1,Q1,Q2,Q8,Q10,Q11]
#loadCasesToDisplay=[LS1,LS2]

for lc in loadCasesToDisplay:
    lcs= qg.LoadCaseResults(FEcase, loadCaseName=lc.loadCaseName, loadCaseExpr= lc.loadCaseExpr)
    for st in lc.setsToDispLoads:
#        capt=lc.loadCaseDescr + ', ' + st.genDescr + ', '  + lc.unitsLoads
        capt=lc.loadCaseDescr + ', '  + lc.unitsLoads
        lcs.displayLoadVectors(setToDisplay=st,caption= capt,fileName=None,defFScale=1.0)



