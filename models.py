import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import pickle

def powerPrediction(day,hour,min):
    df=pd.read_csv('/content/tceApril.csv')

    newDf=df
    # pd.to_datetime(newDf['Time']) "Will return the DF series into Datetime format" Eg:2018-04-16 15:56:00
    newDf['Day']=pd.to_datetime(newDf['Time']).dt.day
    newDf['Month']=pd.to_datetime(newDf['Time']).dt.month
    newDf['Year']=pd.to_datetime(newDf['Time']).dt.year
    newDf['Hour']=pd.to_datetime(newDf['Time']).dt.hour
    newDf['Minute']=pd.to_datetime(newDf['Time']).dt.minute

    cols=[1,6,9,10]
    df1=df[df.columns[cols]]

    XCols = [1,2,3]
    YCols = [0]
    X = df1[df1[XCols]]
    Y = df1[df1[YCols]]

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,random_state=1)

    rfc = RandomForestRegressor()
    rfc.fit(X_train,Y_train)

    pickle.dump(rfc,open("model.pkl",'wb'))
    return (rfc.predict([[day,hour,min]])[0])