# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 22:44:41 2019

@author: 18136
"""
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


movie_titles_df =pd.read_csv("Movie_Id_Titles")
movie_ratings_df=pd.read_csv("u.data",sep="\t",names=["user_id","item_id","rating","timestamp"])

#Dropping timestamp Column
movie_ratings_df.drop(["timestamp"],axis=1,inplace=True)

#Analuysing the ratings column
movie_ratings_df.describe()
movie_ratings_df.info()
#Data is Non Null too

#Merging both DFs
movie_ratings_df= pd.merge(movie_ratings_df,movie_titles_df,on="item_id")