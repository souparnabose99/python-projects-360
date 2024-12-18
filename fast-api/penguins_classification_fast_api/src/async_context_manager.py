from fastapi import FastAPI
from contextlib import asynccontextmanager
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
ml_models = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    data = pd.read_csv('penguins.csv')
    data = data.dropna()
    le = preprocessing.LabelEncoder()
    X = data[["bill_length_mm", "flipper_length_mm"]]
    le.fit(data["species"])
    y = le.transform(data["species"])
    X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=0)
    clf = Pipeline(
        steps=[("scaler", StandardScaler()), ("knn", KNeighborsClassifier(n_neighbors=11))]
    )
    clf.set_params().fit(X_train, y_train)
    ml_models["clf"] = clf
    ml_models["le"] = le
    yield
    ml_models.clear()

