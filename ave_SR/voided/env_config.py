# -*- coding: utf-8 -*-
from postprocess.config import default_config
workingDirectory=default_config.findWorkingDirectory()+'/'

abutment='Y' #if abutment is modelled 'Y'
pile_found='Y'

# Default configuration of environment variables.
cfg=default_config.envConfig(language='sp',intForcPath= 'results/internalForces/',verifPath= 'results/verifications/',annexPath= 'annex/',grWidth='120mm')
if abutment.lower()[0]=='y':
    path_model_abutment=workingDirectory + '../../generic_bridges/model_abutment/'
    path_loads_abutment=workingDirectory + '../../generic_bridges/loads_abutment/'
if pile_found.lower()[0]=='y':
     path_foundation=workingDirectory + '../../generic_bridges/model_foundation/'
