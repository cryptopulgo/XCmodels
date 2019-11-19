# -*- coding: utf-8 -*-
import os
from postprocess import limit_state_data as lsd
from postprocess import RC_material_distribution


#Project directory structure
execfile('../../generic_bridges/voided_slab_bridge/env_config.py')
lsd.LimitStateData.internal_forces_results_directory= cfg.projectDirTree.intForcPath
#FE model generation
execfile("../model_data.py")
#Limit states
execfile("../../generic_bridges/voided_slab_bridge/loadComb.py")

#Reinforced concrete sections on each element.
reinfConcreteSections= RC_material_distribution.loadRCMaterialDistribution()

#Set of entities for which checking is going to be performed.
setCalc= supTablero

loadCombinations= preprocessor.getLoadHandler.getLoadCombinations

#Limit states to calculate internal forces for.
limitStates= [#lsd.normalStressesResistance, # Normal stresses resistance.
#lsd.shearResistance, # Shear stresses resistance (IS THE SAME AS NORMAL STRESSES, THIS IS WHY IT'S COMMENTED OUT).
lsd.freqLoadsCrackControl, # RC crack control under frequent loads
#lsd.quasiPermanentLoadsCrackControl, # RC crack control under quasi-permanent loads
#lsd.fatigueResistance # Fatigue resistance.
] 

#limitStates= [lsd.freqLoadsCrackControl]

for ls in limitStates:
  ls.saveAll(FEcase,combContainer,setCalc)
  print 'combinations for ', ls.label, ': ', loadCombinations.getKeys()


