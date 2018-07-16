# -*- coding: utf-8 -*-

from postprocess import limit_state_data as lsd
from postprocess import RC_material_distribution
from materials.sia262 import SIA262_limit_state_checking

execfile("../projectDirs.py")

lsd.LimitStateData.internal_forces_results_directory= projectDirs.getInternalForcesResultsDirectory()
lsd.LimitStateData.check_results_directory= projectDirs.getCheckResultsDirectory()

#Reinforced concrete sections on each element.
reinfConcreteSections= RC_material_distribution.loadRCMaterialDistribution()

#Checking material for limit state.
limitStress= 500e6 #XXX 
limitStateLabel= lsd.quasiPermanentLoadsCrackControl.label
lsd.quasiPermanentLoadsCrackControl.controller= SIA262_limit_state_checking.CrackControlSIA262PlanB(limitStateLabel,limitStress)
meanFCs= lsd.quasiPermanentLoadsCrackControl.check(reinfConcreteSections)

