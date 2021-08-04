from sklearn.base import BaseEstimator,TransformerMixin
import numpy as np

class RareLabelEncoder(BaseEstimator,TransformerMixin):
  def __init__(self,categorical_features,tol_rate):
    if not isinstance(categorical_features,list):
      self.categorical_features = [categorical_features]
    else:
      self.categorical_features = categorical_features

    self.tol_rate = tol_rate
    self.frequent_labels = {}
    
  def fit(self,X,y=None):
    for feature in self.categorical_features:
      #gets a list of labels that appear more frequently than the tol rate
      higher_than_tol_rate = (X[feature].value_counts() / len(X)) > self.tol_rate
      frequent_labels = list(X[feature].value_counts()[higher_than_tol_rate].index)

      #attributes a list of the most frequent labels for each feature
      self.frequent_labels[feature] = frequent_labels
    return self

  def transform(self,X):
    X = X.copy()
    for feature in self.categorical_features:
      X[feature] = np.where(X[feature].isin(self.frequent_labels[feature]),X[feature],"Rare")
    return X

class CategoricalEncoder(BaseEstimator,TransformerMixin):
  def __init__(self,categorical_features):
    if not isinstance(categorical_features,list):
      self.categorical_features = [categorical_features]
    else:
      self.categorical_features = categorical_features

  def fit(self,X,y=None):
    from sklearn.preprocessing import OrdinalEncoder 
    self.encoder = OrdinalEncoder()
    self.encoder.fit(X[self.categorical_features])
    return self

  def transform(self,X):
    X = X.copy()
    X[self.categorical_features] = self.encoder.transform(X[self.categorical_features]).astype(int)
    return X