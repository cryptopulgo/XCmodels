# -*- coding: utf-8 -*-
from postprocess.config import default_config

home= '/home/ana/projects/XCmodels/PS_Palencia/PS_1/'
path_model_slab_bridge='/home/ana/projects/XCmodels/generic_bridges/model_slab_bridge/'
path_loads_def='/home/ana/projects/XCmodels/generic_bridges/loads_bridge_2_notional_lanes/'

# Default configuration of environment variables.
cfg=default_config.envConfig(language='en',intForcPath= home + 'results/internalForces/',verifPath= home + 'results/verifications/',annexPath= home + 'annex/',grWidth='120mm')
