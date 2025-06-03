import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

url = "Stars.csv"
df = pd.read_csv(url)

print(df.head(10))

# ['Temperature', 'Luminosity', 'Radius', 'Absolute magnitude', 'Star type', 'Star color', 'Spectral Class']

X = df[['Temperature', 'L', 'R', 'A_M', 'Spectral_Class']]
y = df['Type']


categorical_features = ['Spectral_Class']
numeric_features = ['Temperature', 'L', 'R', 'A_M']

preprocessor = ColumnTransformer(
    transformers=[
        ('categorical', OneHotEncoder(categories=[list("OBAFGKM")]), categorical_features),
        ('numeric', 'passthrough', numeric_features)
    ])

pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(n_estimators=100, random_state=42))
])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

pipeline.fit(X_train, y_train)

# Запазване на модела
joblib.dump(pipeline, "star_model.pkl")

print("Model saved as star_model.pkl")