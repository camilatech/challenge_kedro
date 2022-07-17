"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.1
"""
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

def slip_data (df, test_size=0.3, random_state=999) -> pd.DataFrame:
    """Slip the data into train and test datasets
    """
    validate = df[df['TimeElapsed']==265].drop('FinalMandates', axis=1)
    X_all = df[df['TimeElapsed']!=265].drop('FinalMandates', axis=1)
    y_all = df[df['TimeElapsed']!=265]['FinalMandates']

    X_train, X_test, y_train, y_test = train_test_split (
        X_all, y_all, test_size=test_size, random_state=random_state, stratify=y_all
        )
    return X_train, X_test, y_train, y_test,validate

def fit_model (X_train, X_test, y_train, y_test):
    """ Fits a model using the training dataset
    """
    linear_regression = LinearRegression()
    linear_regression.fit(X_train, y_train)
    y_predicted = linear_regression.predict(X_test)
    print(r2_score(y_test,y_predicted))

    return linear_regression