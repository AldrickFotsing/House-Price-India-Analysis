import streamlit as st
import joblib
import numpy as np
import pandas as pd

model = joblib.load("model.pkl")
st.title("House Price India Prediction App 🏠")
st.write("Application réalisée par Aldrick Fotsing")

st.divider()
st.write("Cette application utilise le machine learning pour prédire le prix d'une maison en Inde en fonction de ses caractéristiques. Pour utiliser cette application, vous pouvez saisir les données depuis cette interface utilisateur, puis utiliser le bouton << Prédiction >>.")

st.divider()

# 2. Interface utilisateur (Inputs)
bedrooms = st.number_input("Nombre de chambres", min_value = 0, value = 0)
bathroom = st.number_input("Nombre de salle de bain", min_value = 0, value = 0)
livingarea = st.number_input("Surface habitable en mètre carré", min_value = 0, value = 2000)
total_house_area = st.number_input("Surface totale du terrain en mètre carré", min_value = 0, value = 7500)
grade = st.slider("Niveau de la maison", 4, 13, 7)
latittude = st.number_input("Latitude", min_value = 0, value = 53)
living_area_renov  = st.number_input("Superficie habitable de la maison après rénovation en mètre carré", min_value = 0, value = 1900)
number_of_views = st.radio("Nombre de fois où le bien a été consulté", [0, 1, 2, 3, 4])
house_age = st.number_input("L'âge de la maison (en année)", min_value = 0, value = 53)
years_since_renovation = st.slider("Années depuis la dernière rénovation", 0, 100, 0)
is_renovated = st.radio("La maison a-t-elle été rénovée ?", [0, 1], help="0 = Non, 1 = Oui")

# Calculs automatiques pour correspondre aux attentes du modèle

living_area_log = np.log(livingarea + 1)
living_area_renov_log = np.log(living_area_renov + 1)
lot_house_ratio = total_house_area / (livingarea + 1)

# 3. Prédiction

st.divider()
X = [bedrooms, bathroom, living_area_log, total_house_area, grade, latittude, living_area_renov_log, number_of_views, house_age, years_since_renovation, is_renovated, lot_house_ratio]
predictButton = st.button("Prediction")

if predictButton:
    
    st.balloons()
    
    X_array = np.array(X).reshape(1, -1)
    
    prediction = model.predict(X_array)
    # On extrait la première valeur avec [0]
    prediction = prediction[0]

    st.write(f"Le prix est: {int(prediction)} Lakhs (₹), soit l'équivalent de {int(prediction * 760000)} FCFA")
    
else:
    st.write("S'il vous plait, utilisez le button prédiction après avoir saisi les valeurs")

# PIED DE PAGE
st.divider()
st.caption("© 2026 Aldrick Fotsing | Data Scientist/Data Analyst Junior")
