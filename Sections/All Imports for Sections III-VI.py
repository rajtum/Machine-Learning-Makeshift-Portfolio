import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# III. Imports
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

# IV. Imports
from mpl_toolkits import mplot3d
from sklearn.model_selection import cross_val_score, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import MinMaxScaler
from statistics import mean
import plotly.graph_objects as go
import plotly.express as px
import time

# V. Imports
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline


#VI. Imports
from xgboost import XGBRegressor
