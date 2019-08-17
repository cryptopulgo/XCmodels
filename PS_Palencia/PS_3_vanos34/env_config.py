# -*- coding: utf-8 -*-
from postprocess.config import default_config

home= '/home/ana/projects/XCmodels/PS_Palencia/'
path_model_slab_bridge='/home/ana/projects/XCmodels/generic_bridges/model_slab_bridge/'
path_loads_def='/home/ana/projects/XCmodels/generic_bridges/loads_bridge_2_notional_lanes/'
path_gen_results='/home/ana/projects/XCmodels/generic_bridges/gen_results/'

# Default configuration of environment variables.
cfg=default_config.envConfig(language='en',intForcPath= home + 'PS_3_vanos34/results/internalForces/',verifPath= home + 'PS_3_vanos34/results/verifications/',annexPath= home + 'PS_3_vanos34/annex/',grWidth='120mm')
