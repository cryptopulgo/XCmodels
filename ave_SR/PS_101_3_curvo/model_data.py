# -*- coding: utf-8 -*-
from __future__ import division

import os
import xc_base
import geom
import xc
import math
from model import predefined_spaces
from model.geometry import grid_model as gm


fullProjPath='/home/ana/projects/XCmodels/ave_SR/PS_101_3_curvo/'
execfile(fullProjPath+'env_config.py')

execfile('../basic_data.py')
execfile('../basic_geom.py')
execfile('../../PSs/model_constr.py')
