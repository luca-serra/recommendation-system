# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 10:07:52 2020

@author: lucas
"""

import pandas as pd
from surprise import Dataset
from surprise import KNNWithMeans
from surprise.model_selection import GridSearchCV
from surprise import SVD

data = Dataset.load_builtin("ml-100k") #Dataset.load_from_df()

#%% memory-based approach

sim_options = {
    "name": ["msd", "cosine"],
    "min_support": [3, 4, 5],
    "user_based": [False, True],
}

param_grid = {"sim_options": sim_options}

gs = GridSearchCV(KNNWithMeans, param_grid, measures=["rmse", "mae"], cv=3)
gs.fit(data)
#
print(gs.best_score["rmse"])
print(gs.best_params["rmse"])

#%% model-based approach

param_grid_2 = {
    "n_epochs": [5, 10],
    "lr_all": [0.002, 0.005],
    "reg_all": [0.4, 0.6]
}
gs_2 = GridSearchCV(SVD, param_grid_2, measures=["rmse", "mae"], cv=3)

gs_2.fit(data)

print(f'The optimal configuration is: {gs_2.best_params["rmse"]}')
print(f'The associated best score is: {gs_2.best_score["rmse"]:.3f}')

