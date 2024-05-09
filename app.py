import streamlit as st
import pandas as pd

from streamlit_option_menu import *
from function import *

URL = 'gender_equality_final.csv'
df1 = pd.read_csv(URL)
df = pd.read_csv('dataset.csv')

with st.sidebar :
    selected = option_menu('Gender Equality',['👩‍🚀 Introducing', '📊 Visualization', '📋 Gender Equality Analysis'],default_index=0)

if (selected == '👩‍🚀 Introducing'):
    st.title("Welcome to Dashboard")
    st.title("The Importance of Gender Equality")

    st.title("Introducing")
    text = ("""
    Gender equality is the view that all people both men and women, should receive equal treatment and there should be no discrimination based on their gender.
    We use the "Male vs Female" Dataset containing a comprehensive set of information that aims to provide insight into the similarities and differences between women and men across various domains. This data set has been curated to facilitate analysis and exploration of characteristics, traits, preferences and other factors that may differ between the two genders.
    """)
    translate = st.checkbox("Translate to Indonesia")
    if translate:
        translated_text = translate_text(text)
        if translated_text:
            text = translated_text
    st.markdown(text)

    st.header("Gender Equality Dataset That Has Not Been Cleaned")
    st.write(df1)

    st.header("Gender Equality Dataset That Has Been Cleaned")
    st.write(df)

if (selected == '📊 Visualization'):
    st.title("Visualization of Gender Equality Analysis")
    option = st.sidebar.selectbox(
            'Visualization :',
            ('Distribution', 'Composition', 'Comparison', 'Relationship')
        )
    
    if option == 'Distribution':
        distribution(df)
        
    elif option == 'Composition':
        composition(df)

    elif option == 'Comparison':
        comparison(df)

    elif option == 'Relationship':
        relationship(df)

if (selected == '📋 Gender Equality Analysis'):
    def predict_gender():
        st.header("Gender Prediction")

        # Tampilkan form input untuk data pengguna
        st.subheader("Enter User Data:")
        age = st.number_input('Age', 0, 120, 20)
        driving_test_result = st.number_input('Driving Test Result', 0, 10, 0)
        children = st.number_input('Children', 0, 10, 0)
        bmi = st.number_input('BMI (Body Mass Index)', 0.0, 100.0, 0.0)
        salary = st.number_input('Salary', 0, 100000, 0)
        smoker = st.selectbox('Smoker', ['no', 'yes'])
        region = st.selectbox('Region', ['northeast', 'northwest', 'southeast', 'southwest'])

        # Ubah nilai 'smoker' menjadi numerik
        smoker_numeric = {'no': 0, 'yes': 1}
        smoker = smoker_numeric[smoker]

        # Lakukan klasifikasi gender
        gender = predict_gender_from_input(age, driving_test_result, children, bmi, salary, smoker, region)

        # Tampilkan hasil prediksi
        st.subheader("Prediction:")
        st.write("Predicted Gender:", gender)

    def predict_gender_from_input(age, driving_test_result, children, bmi, salary, smoker, region):
        # Muat model yang sudah dilatih
        file_path = 'gnb.pkl'
        with open(file_path , 'rb') as f:
            clf = joblib.load(f)

        # Lakukan prediksi gender
        age_category = determine_age_category(age)
        bmi_category = determine_bmi_category(bmi)

        # Konversi 'smoker' menjadi numerik
        smoker_numeric = {'no': 0, 'yes': 1}

        # Lakukan prediksi gender
        gender_data = pd.DataFrame({
            'age': [age],
            'Driving test result': [driving_test_result],
            'Bmi': [bmi],
            'Childeren': [children],
            'Salary': [salary],
            'smoker': [smoker_numeric[smoker]],
            'region': [region],
            'AgeCategory': [age_category],
            'BMI Category': [bmi_category]
        })
        predicted_gender = clf.predict(gender_data)
        if predicted_gender[0] == 0:
            return 'Female'
        else:
            return 'Male'


    def determine_age_category(age):
        if age < 17:
            return 'Child'
        elif 17 <= age < 40:
            return 'Young Adults'
        elif 40 <= age < 60:
            return 'Middle-aged Adults'
        else:
            return 'Old-aged Adults'

    def determine_bmi_category(bmi):
        if bmi < 18.5:
            return 'Underweight'
        elif 18.5 <= bmi < 25:
            return 'Normal'
        elif 25 <= bmi < 30:
            return 'Overweight'
        else:
            return 'Obesity'

    def main():
        # Tampilkan judul dan deskripsi aplikasi
        st.title("Gender Prediction App")
        st.write("This app predicts the gender based on user input.")

        # Tampilkan pilihan untuk melakukan prediksi gender
        selected_option = st.radio("Select an option:", ["Predict Gender"])
        if selected_option == "Predict Gender":
            predict_gender()

    if __name__ == "__main__":
        main()