# -*- coding: utf-8 -*-


from postprocess import limit_state_data as lsd
from postprocess import RC_material_distribution
from materials.sia262 import SIA262_limit_state_checking

execfile("../projectDirs.py")

lsd.LimitStateData.internal_forces_results_directory= projectDirs.getInternalForcesResultsDirectory()
lsd.LimitStateData.check_results_directory= projectDirs.getCheckResultsDirectory()

#Reinforced concrete sections on each element.
reinfConcreteSections= RC_material_distribution.loadRCMaterialDistribution()

limitStateLabel= lsd.fatigueResistance.label
lsd.fatigueResistance.controller= SIA262_limit_state_checking.FatigueController(limitStateLabel)
lsd.fatigueResistance.check(reinfConcreteSections)


