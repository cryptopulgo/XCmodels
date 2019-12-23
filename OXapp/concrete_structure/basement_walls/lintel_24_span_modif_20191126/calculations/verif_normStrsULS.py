# -*- coding: utf-8 -*-
from postprocess import limit_state_data as lsd
from postprocess import RC_material_distribution
from materials.sia262 import SIA262_limit_state_checking as lscheck
#from materials.aci import ACI_limit_state_checking

#Results directories
execfile("../model_gen.py") #FE model generation
lsd.LimitStateData.envConfig= cfg

#Reinforced concrete sections on each element.
#reinfConcreteSections=RC_material_distribution.RCMaterialDistribution()
#reinfConcreteSections.mapSectionsFileName='./mapSectionsReinforcement.pkl'
reinfConcreteSections= RC_material_distribution.loadRCMaterialDistribution()

# variables that control the output of the checking (setCalc,
# appendToResFile .py [defaults to 'N'], listFile .tex [defaults to 'N']
outCfg= lsd.VerifOutVars(setCalc=overallSet,appendToResFile='N',listFile='N',calcMeanCF='N')

#limitStateLabel= lsd.normalStressesResistance.label

#lsd.normalStressesResistance.controller= ACI_limit_state_checking.BiaxialBendingNormalStressController(limitStateLabel)
limitState=lsd.normalStressesResistance
limitState.controller= lscheck.BiaxialBendingNormalStressController(limitState.label)

a=lsd.normalStressesResistance.check(reinfConcreteSections,outCfg)



