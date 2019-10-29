# -*- coding: utf-8 -*-

execfile("../model_gen.py") #FE model generation


execfile('../load_state_data.py')

from postprocess.xcVtk.FE_model import quick_graphics as qg

#ordered list of load cases (from those defined in ../load_state_data.py
#or redefined lately) to be displayed:

'''
loadCasesToDisplay=[ULS1]

for lc in loadCasesToDisplay:
    lcs= qg.LoadCaseResults(FEcase, loadCaseName=lc.loadCaseName, loadCaseExpr= lc.loadCaseExpr)
    lcs.solve()
    for st in lc.setsToDispLoads:
#        capt=lc.loadCaseDescr + ', ' + st.genDescr + ', '  + lc.unitsLoads
        capt=lc.loadCaseDescr + ', '  + lc.unitsLoads
        lcs.displayLoadVectors(setToDisplay=st,caption= capt,fileName=None,defFScale=1.0)
'''
lcs.displayLoadVectors(setToDisplay=overallSet,loadCaseNm='ULS1',unitsScale=1e-3)

