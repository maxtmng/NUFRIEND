"""
Utils
=====

Imports all required packages and sets global variables for file directories.
"""

# GENERAL
import os
import os.path
import math
import warnings
import pandas as pd
import geopandas as gpd
import numpy as np
import scipy as sp
from scipy.sparse import csr_matrix
from copy import deepcopy
from itertools import product, chain, combinations, islice
from datetime import date, datetime
import time
import pickle as pkl
import json
import geojson
from tqdm import tqdm
from multiprocess import pool
# OPTIMIZATION
import gurobipy as gp
from gurobipy import GRB
# NETWORKS
import networkx as nx
import osmnx as ox
from shapely.geometry import LineString, Point, Polygon, MultiLineString, shape
from shapely.ops import linemerge
from shapely.errors import ShapelyDeprecationWarning
# PLOTTING
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import plotly
import plotly.graph_objs
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio
from plotly.offline import iplot
import logging
# DASH
from dash import dash, dcc, html, Input, Output, State
from flask import request, jsonify
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
from flask_caching import Cache
import dash_loading_spinners as dls
import csv
import dash_auth
import traceback
from werkzeug.middleware.proxy_fix import ProxyFix # for nginx

warnings.filterwarnings("ignore", category=ShapelyDeprecationWarning)

sns.set_theme(palette='Set2')

pio.renderers.default = "browser"
tqdm.pandas()

# TODO: for publicly released version:
#  - have local directories for key input data; store template files in these as well as sample data files for example
#  - create example/test files and sample results so that users can run and compare on their computer

# GLOBAL PATHS
BASE_DIR = os.path.dirname(__file__)
# input directory
INPUT_DIR = os.path.join(BASE_DIR, 'input')
# input subdirectories
FLOW_DIR = os.path.join(INPUT_DIR, 'flow')
COMM_DIR = os.path.join(INPUT_DIR, 'commodity')
GEN_DIR = os.path.join(INPUT_DIR, 'general')
LCA_DIR = os.path.join(INPUT_DIR, 'LCA')
NX_DIR = os.path.join(INPUT_DIR, 'networks')
TEA_DIR = os.path.join(INPUT_DIR, 'TEA')
RR_DIR = os.path.join(INPUT_DIR, 'railroad')
SCENARIO_DIR = os.path.join(INPUT_DIR, 'scenario')
# TODO: remove these, do not use caching or deployment tables
DEP_TAB_DIR = os.path.join(INPUT_DIR, 'general')
# output directory
OUTPUT_DIR = os.path.join(BASE_DIR, 'output')
# output subdirectories
FIG_DIR = os.path.join(OUTPUT_DIR, 'figures')
MET_O_DIR = os.path.join(OUTPUT_DIR, 'metrics')
NODE_O_DIR = os.path.join(OUTPUT_DIR, 'nodes')
EDGE_O_DIR = os.path.join(OUTPUT_DIR, 'edges')
# TODO: remove
DEP_TAB_O_DIR = os.path.join(OUTPUT_DIR, 'Deployment')


# GLOBAL VARS
# filename shortcuts
FILES = {2017: 'WB2017_900_Unmasked.csv', 2018: 'WB2018_900_Unmasked.csv', 2019: 'WB2019_913_Unmasked.csv'}
KM2MI = 0.62137119  # miles / km
