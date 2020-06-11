# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 19:45:46 2020

@author: Skalvis Paliulis

exam project for PROG-DS, Programming for Data Science (Spring 2020)

the following code is used to implement K-means algorithm  

"""
#importing relevant libraries for data manipulation, ploting and partial
# function creation 

import numpy as np
import pandas as pd
import seaborn as sb
import random

#Importing data from personal GIT repository
#binary data file "dna_amp_chr_17.data"
bi = pd.read_csv('https://raw.githubusercontent.com/Skalvis/PROG-DS_VT2020/master/dna_amp_chr_17.data', sep=' ', header=None, skipinitialspace=True)

#numerical,continuous data file "measurements.data"
df = pd.read_csv('https://raw.githubusercontent.com/Skalvis/PROG-DS_VT2020/master/measurements.data', sep=' ', header=None, skipinitialspace=True)

#getting dimensions of both datasets 
d_bi=np.shape(bi)
d_df=np.shape(df)

#declaring initial k set of prototypes (cluster centers)
k=6

#creating sample sets for further dispatch  function
df_s=df.sample(k)
bi_s=bi.sample(k)

#dispatch function. Takes samples and tests data within taken randomly
#depending on outcome fuction will call Euclidean or Jaccard function. 
def dispatch(df_s):
    if pd.Index(df_s).dtype == 'float64': 
        Euclid(df_s) #all float types redirected to Euclidean
    elif pd.Index(df_s).dtype == 'int64': 
        if all(np.min(df_s)) == 0 and all(np.max(df_s)) ==1: #checks whether all min are 0 and max 1
            Jaccard(df_s) #uses Jaccard if true
        else:
            Euclid(df_s) 
    else:
        i=0
        for i in range(len(df_s.columns)):
            if df_s.dtypes[i] == 'bool': 
                continue
            else:
                print('can`t process data') #cant process if data is object-like and not boolean
                break
        else:
            Jaccard(df_s) #if is boolean
            
def norm(df_s): #function to make numerical data have 0 mean and unit variance of 1
    s=(df_s - np.mean(df_s))/np.std(df_s)
    return s 

#Euclidean distance function, used for numerical and continuous data
def Euclid(df,k):
    print('Euclidean used')
    random.seed(27) #seed for testing
    df=norm(np.array(df)) #converting to normalized numPy array for easier manipulation
    k_centers=np.random.randint(np.min(df), high=np.max(df), size=(k,np.size(df,1))) #generating random k mean prototype vector centers
    max_it=0            #standin varianble for max iterations count 
    while max_it!=100000:
        i=0
        n_rows_dv=np.size(df,0)
        min_id=np.random.randint(np.max(df),size=(n_rows_dv,1), dtype='int')  
        min_id_2=np.random.randint(np.max(df)+1,size=(n_rows_dv,1), dtype='int') #used to checked whether any changes occur
        for i in range(0,n_rows_dv-1):  #iterates through data vector`s rows
            x=0
            for x in range(0,k-1): #iterates one row from data vector through 
                min_d=99999           
                dist=np.sqrt(np.sum((df[i]-k_centers[x])**2))
                if  dist<min_d:
                    min_d=dist
                    min_id[i]=x #assigns ID number to label array
                else:
                    continue
                if i==n_rows_dv: #checks whether full cycle has been performed
                    d=0
                    if all(min_id.flat == min_id_2.flat): #checks if label arrays are identical
                        break
                    else:
                        d=0
                        temp=np.append(df,min_id, axis=1) #temporary array to filter values accordingly 
                        avg=np.array([])
                        for d in range(0,k-1): # iterating through cluster center array
                            c=0
                            for c in range(0,n_rows_dv-1): #iterating to find mean of all values with label 2 from last column 
                                if temp[c][np.size(temp,1)-1] ==d:
                                    avg=np.append(temp[c])
                                elif c==n_rows_dv:
                                     k_centers[d]= np.mean(avg, axis=0) #calculates averages of each d row
                                     break
                                else:
                                     continue
        else:
            if i==n_rows_dv:
                max_it+=i
                i=0
                continue
            else:
                max_it=100000
                break
    else:
        print('max iterations run: ',max_it)
    return(k_centers, min_id)
                
#Jaccard distance function, used for binary data
def Jaccard(df,k):
    print('Jaccard used')
    random.seed(27) #seed for testing
    df=np.array(df) #converting to np numPy array for easier manipulation
    k_centers=np.random.randint(np.min(df), high=np.max(df), size=(k,np.size(df,1))) #generating random k mean prototype vector centers
    max_it=0            #standin varianble for max iterations count 
    while max_it!=100000:
        i=0
        n_rows_dv=np.size(df,0)
        min_id=np.empty([n_rows_dv,1], dtype='int')  #our label array
        min_id_2=np.empty([n_rows_dv,1],dtype='int') #used to check whether any changes occur
        while all(min_id.flat != min_id_2.flat): #checks whether label comparison arrays are identical
            for i in range(0,n_rows_dv-1):  #iterates through data vector`s rows
                x=0
                for x in range(0,k-1):  #iterates through cluster centers
                    min_d=0 
                    set_dv = {df[i]}
                    set_cc = {k_centers[x]}
                    dist= 1 -len(set_dv.intersection(set_cc)) / len(set_dv.union(set_cc))
                    
        
        
    else:
        print('max iterations run: ',max_it)
    
    
    
    
    return()










