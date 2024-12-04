import streamlit as st
import joblib

st.title("Kassalikka chalinish extimoli")

# Foydalanuvchidan ma'lumotlarni kiritishni so'rash
pregnancies = st.number_input("Bemorning kassalik shastotasi", min_value=0, max_value=20, value=1, step=1)
glucose = st.number_input("Glyukoza darajasini kiriting", min_value=0, max_value=200, value=120, step=1)
blood_pressure = st.number_input("Qon bosimini kiriting", min_value=0, max_value=150, value=70, step=1)
skin_thickness = st.number_input("Teri qalinligini kiriting", min_value=0, max_value=100, value=20, step=1)
insulin = st.number_input("Insulin darajasini kiriting", min_value=0, max_value=900, value=80, step=1)
bmi = st.number_input("BMI ni kiriting", min_value=0.0, max_value=70.0, value=25.0, step=0.1)
diabetes_pedigree_function = st.number_input("Kasallik Funksiyasini kiriting", min_value=0.0, max_value=3.0, value=0.5, step=0.01)
age = st.number_input("Yoshni kiriting", min_value=0, max_value=120, value=25, step=1)

# Modelni yuklash va bashorat qilish
if st.button("Kassaliklikka chalinish extimoli darajasi"):
    # Kiritilgan ma'lumotlarni model formatiga o'tkazish
    model_input = [[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]]
    
    # Modelni yuklash
    model = joblib.load('decision_tree_model.pkl')  

    # Bashorat qilish
    outcome = model.predict(model_input)

    # Natijani ko'rsatish
    if outcome[0] == 1:
        st.write(" Kassallikka chalinish extimoli darajasi yuqori")
    else:
        st.write("Kassallikka chalinish extimoli darajasi past")

