# -*- coding: utf-8 -*-
from postprocess.config import output_config as oc
from postprocess import limit_state_data as lsd
from postprocess import RC_material_distribution
#from materials.ehe import EHE_limit_state_checking as lscheck  #Checking material for shear limit state according to EHE08
from materials.sia262 import SIA262_limit_state_checking as lscheck

#choose env_config file:
execfile("../env_config_deck.py")
#execfile("../env_config_abutment.py")
#
execfile("../model_gen.py") #FE model generation

#Reinforced concrete sections on each element.
#reinfConcreteSections=RC_material_distribution.RCMaterialDistribution()
#reinfConcreteSections.mapSectionsFileName='./mapSectionsReinforcement.pkl'
reinfConcreteSections= RC_material_distribution.loadRCMaterialDistribution()
#stcalc=setArmadosEstr
#stcalc=setArmVol
#stcalc=setArmCart
#stcalc=setArmLosa
#stcalc=setArmPil
stcalc=setArmados
#stcalc=setArmadosEstr
#stcalc=setArmZapEstr
#stcalc=setArmMurEstr
# variables that control the output of the checking (setCalc,
# appendToResFile .py [defaults to 'N'], listFile .tex [defaults to 'N']
outCfg=oc.verifOutVars(setCalc=stcalc,appendToResFile='N',listFile='N',calcMeanCF='N')

limitState=lsd.normalStressesResistance
limitState.controller= lscheck.BiaxialBendingNormalStressController(limitState.label)
lsd.normalStressesResistance.check(reinfConcreteSections,outCfg)




