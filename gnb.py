import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split

df = pd.read_csv('gender_equality_final.csv')

x = df.drop('Gender', axis=1)
y = df['Gender']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

numeric = x_train.select_dtypes(include=['int64', 'float64']).columns

numeric_transform = Pipeline(steps=[
    ('scaler', StandardScaler())
])

category = x_train.select_dtypes(include=['object']).columns

category_transform = Pipeline(steps=[
    ('onehot', OneHotEncoder())
])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transform, numeric),
        ('cat', category_transform, category)
    ]
)

class GaussianNB:
    def __init__(self): # Inisialisasi dictionary untuk menyimpan parameter statistik untuk setiap kelas
        self.parameters = {}

    def fit(self, X_train, y_train):
        # Konversi data pelatihan ke array NumPy untuk kemudahan pengolahan
        self.X_train = np.array(X_train)
        self.y_train = np.array(y_train)
        # Mengidentifikasi semua kelas unik dalam data target
        self.classes = np.unique(y_train)
        # Menghitung parameter untuk setiap kelas
        for c in self.classes:
            X_c = self.X_train[self.y_train == c] # Data fitur untuk kelas c
            self.parameters[c] = {
                'mean': X_c.mean(axis=0), # Menghitung mean dari fitur untuk kelas c
                'std': X_c.std(axis=0) + 1e-6  # Menambahkan epsilon ke std untuk menghindari pembagian dengan nol.
            }

    def _calculate_likelihood(self, x, mean, std):
        # Menghitung nilai eksponensial dari Gaussian function
        exponent = np.exp(-((x - mean) ** 2) / (2 * (std ** 2)))
        # Mengembalikan hasil kali dari probabilitas Gaussian untuk setiap fitur
        return np.prod((1 / np.sqrt(2 * np.pi * (std ** 2))) * exponent)

    def _calculate_prior(self, c):
        # Menghitung prior probability dari kelas c sebagai rasio jumlah contoh kelas c terhadap semua contoh
        return len(self.X_train[self.y_train == c]) / len(self.X_train)
        
        

    def _calculate_posterior(self, x):
        posteriors = {}
        for c in self.classes:
            # Menghitung likelihood dari sampel x untuk kelas c
            likelihood = self._calculate_likelihood(x, self.parameters[c]['mean'], self.parameters[c]['std'])
            # Menghitung prior probability dari kelas c
            prior = self._calculate_prior(c)
            # Menghitung posterior probability dari kelas c
            posteriors[c] = likelihood * prior
        return posteriors

    def predict(self, X_test):
        # Konversi data uji ke array NumPy
        X_test = np.array(X_test)
        predictions = []
        for x in X_test:
            # Menghitung posterior probability untuk setiap kelas
            posteriors = self._calculate_posterior(x)
            # Memilih kelas dengan posterior probability tertinggi
            predictions.append(max(posteriors, key=posteriors.get))
        return predictions

pipeline_gnb = Pipeline(steps=[('preprocessor', preprocessor),
                               ('classifier', GaussianNB())])

pipeline_gnb.fit(x_train, y_train)
# Inisialisasi model
# gnb = GaussianNB()
