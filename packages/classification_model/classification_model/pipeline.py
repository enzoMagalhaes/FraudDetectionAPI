from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
import numpy as np

from classification_model.processors import preprocessors as p
from classification_model.config import config as c

from sklearn.ensemble import RandomForestClassifier


pipeline = Pipeline([
          ("impute rare labels",p.RareLabelEncoder(c.CATEGORICAL_FEATURE,tol_rate=0.01)),
          ("categorical imputer",p.CategoricalEncoder(c.CATEGORICAL_FEATURE)),
          ("scaler",StandardScaler()),
          ("model",RandomForestClassifier(random_state=0))
])