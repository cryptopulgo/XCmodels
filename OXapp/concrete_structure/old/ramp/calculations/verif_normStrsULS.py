# -*- coding: utf-8 -*-
from postprocess.config import output_config as oc
from postprocess import limit_state_data as lsd
from postprocess import RC_material_distribution
#from materials.sia262 import SIA262_limit_state_checking as lscheck
from materials.aci import ACI_limit_state_checking

#Results directories
execfile("../model_gen.py") #FE model generation

#Reinforced concrete sections on each element.
#reinfConcreteSections=RC_material_distribution.RCMaterialDistribution()
#reinfConcreteSections.mapSectionsFileName='./mapSectionsReinforcement.pkl'
reinfConcreteSections= RC_material_distribution.loadRCMaterialDistribution()

# variables that control the output of the checking (setCalc,
# appendToResFile .py [defaults to 'N'], listFile .tex [defaults to 'N']
outCfg=oc.verifOutVars(setCalc=ramp,appendToResFile='N',listFile='N',calcMeanCF='Y')

limitStateLabel= lsd.normalStressesResistance.label
lsd.normalStressesResistance.controller= ACI_limit_state_checking.BiaxialBendingNormalStressController(limitStateLabel)
lsd.normalStressesResistance.check(reinfConcreteSections,outCfg)





