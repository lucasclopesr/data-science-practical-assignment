import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn import preprocessing
import numpy as np
def get_brazil_covid():
    df = pd.read_csv("data/brazil_covid19.csv")
    df.loc[:, "date"] = pd.to_datetime(df["date"],format="%Y-%m-%d")
    df.loc[:, "state"] = df.state.astype("category")
    df.loc[:, "region"] = df.region.astype("category")
    return df

# def get_world_covid():
#     df_world = pd.read_csv("data/world.csv")
#     df_world.loc[:, "Date_reported"] = pd.to_datetime(df_world.loc[:, "Date_reported"], format="%Y-%m-%d")
#     df_world.loc[:, " Country_code"] = df_world.loc[:, " Country_code"].astype("category")
#     df_world.loc[:, " Country"] = df_world.loc[:, " Country"].astype("category")
#     df_world.loc[:, " WHO_region"] = df_world.loc[:, " WHO_region"].astype("category")
#     return df_world

# Altered to get formatted and treated world data about the disease's spread
def get_world_covid():
    df_world = pd.read_csv("data/worldCovid_v2.csv")
    df_world.loc[:, "Date_reported"] = pd.to_datetime(df_world.loc[:, "Date_reported"], format="%Y-%m-%d")
    df_world.loc[:, "Country"] = df_world.loc[:, "Country"].astype("category")
    return df_world

def get_world_social():
    df_world_soc = pd.read_csv("data/worldInfo_v2.csv")
    df_world_soc.loc[:, "Country"] = df_world_soc.loc[:, "Country"].astype("category")
    return df_world_soc
