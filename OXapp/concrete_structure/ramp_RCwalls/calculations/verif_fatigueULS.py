# -*- coding: utf-8 -*-
from materials.sia262 import SIA262_limit_state_checking
from miscUtils import LogMessages as lmsg

execfile('../env_config.py')

lmsg.warning('Implementation pending. Do not use.')
quit()
# variables that control the output of the checking (setCalc,
# appendToResFile .py [defaults to 'N'], listFile .tex [defaults to 'N']
outCfg= lsd.VerifOutVars(setCalc=beamX,appendToResFile='N',listFile='N')

#Reinforced concrete sections on each element.
reinfConcreteSections= RC_material_distribution.loadRCMaterialDistribution()

limitStateLabel= lsd.fatigueResistance.label
lsd.fatigueResistance.controller= SIA262_limit_state_checking.FatigueController(limitStateLabel)
lsd.fatigueResistance.check(reinfConcreteSections,outCfg)


