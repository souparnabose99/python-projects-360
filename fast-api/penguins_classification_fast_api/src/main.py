import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


data = pd.read_csv(r"data\input\penguins_lter.csv")
data = data.dropna()
le = preprocessing.LabelEncoder()

