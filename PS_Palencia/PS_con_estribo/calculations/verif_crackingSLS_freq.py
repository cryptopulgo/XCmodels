# -*- coding: utf-8 -*-
from postprocess import limit_state_data as lsd
from postprocess import RC_material_distribution
from materials.sia262 import SIA262_limit_state_checking as lschck  #Checking material for cracking limit state according to SIA262

execfile("../model_gen.py") #FE model generation
lsd.LimitStateData.envConfig= cfg

#choose env_config file:
execfile("../env_config_deck.py")
execfile("../env_config_abutment.py")
#
# variables that control the output of the checking (setCalc,
# appendToResFile .py [defaults to 'N'], listFile .tex [defaults to 'N']
outCfg= lsd.VerifOutVars(setCalc=decks,appendToResFile='N',listFile='N')

#Reinforced concrete sections on each element.
reinfConcreteSections= RC_material_distribution.loadRCMaterialDistribution()

#Checking material for limit state.
limitStress= 350e6 #XXX
limitStateLabel= lsd.freqLoadsCrackControl.label
lsd.freqLoadsCrackControl.controller= lschck.CrackControlSIA262PlanB(limitStateLabel,limitStress)
lsd.freqLoadsCrackControl.check(reinfConcreteSections,outCfg)



