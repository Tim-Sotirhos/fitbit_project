import requests
import warnings
warnings.filterwarnings('ignore')
import json
from pprint import pprint


from os import path

import matplotlib
import matplotlib.pyplot as plt

from datetime import timedelta, datetime

from statsmodels.tsa.api import ExponentialSmoothing, SimpleExpSmoothing, Holt
import statsmodels.api as sm
from statsmodels.tsa.ar_model import AR

from sklearn.model_selection import TimeSeriesSplit
from sklearn import metrics

import pandas as pd
import numpy as np

import math