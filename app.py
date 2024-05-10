import streamlit as st
import pandas as pd
import joblib

from streamlit_option_menu import *
from function import *
from gnb import pipeline_gnb

URL = 'gender_equality_final.csv'
df1 = pd.read_csv(URL)
df = pd.read_csv('dataset.csv')

with st.sidebar:
    selected = option_menu('Gender Equality', ['👩‍🚀 Introducing', '📊 Visualization', '📋 Gender Equality Analysis'], default_index=0)

if selected == '👩‍🚀 Introducing':
    st.title("Welcome to Dashboard")
    st.title("The Importance of Gender Equality")

    st.title("Introducing")
    text = ("""
    Gender equality is the view that all people, both men and women, should receive equal treatment and there should be no discrimination based on their gender.
    We use the "Male vs Female" Dataset containing a comprehensive set of information that aims to provide insight into the similarities and differences between women and men across various domains. This dataset has been curated to facilitate analysis and exploration of characteristics, traits, preferences, and other factors that may differ between the two genders.
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

if selected == '📊 Visualization':
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

if selected == '📋 Gender Equality Analysis':
    st.title("Gender Prediction App")
    st.write("This app predicts the gender based on user input.")
    st.header("Gender Prediction")

    joblib.dump(pipeline_gnb, 'gnb.pkl')

    with open('gnb.pkl', 'rb') as f:
        clf = joblib.load(f)

    age = st.slider('Age', 0, 100, 20)
    age_category = st.selectbox('Age Category', ['Child', 'Young Adults', 'Middle-aged Adults', 'Old-aged Adults'])
    Driving = int(st.number_input('Driving Test Result', 0, 10, 0))
    children = int(st.number_input('Children', 0, 10, 0))
    bmi = int(st.number_input('BMI (Body Mass Index)', 0, 100, 0))
    bmi_category = st.selectbox('BMI Category', ['Underweight', 'Normal', 'Overweight', 'Obesity'])
    salary = int(st.number_input('Salary', 0, 100000, 0))
    smoker = st.radio('Smoker', ['no', 'yes'])
    region = st.selectbox('Region', ['northeast', 'northwest', 'southeast', 'southwest'])

    # Convert categorical variables to numerical values
    age_category_map = {'Child': 0, 'Young Adults': 1, 'Middle-aged Adults': 2, 'Old-aged Adults': 3}
    bmi_category_map = {'Underweight': 0, 'Normal': 1, 'Overweight': 2, 'Obesity': 3}

    age_category = age_category_map.get(age_category, 0)
    bmi_category = bmi_category_map.get(bmi_category, 0)

    # Convert smoker to numerical value
    smoker = 1 if smoker == 'yes' else 0

    prediction_state = st.markdown('Calculating...')

    gender = pd.DataFrame({
        'age': [age],
        'Driving test result': [Driving],
        'Bmi': [bmi],
        'Childeren': [children],
        'Salary': [salary],
        'smoker': [smoker],
        'Region': [region],
        'AgeCategory': [age_category],
        'BMI Category': [bmi_category]
    })

    predict_gender = clf.predict(gender)

    if st.button("Predict"):
        if predict_gender[0] == 0:
            msg = 'The predicted gender is Female.'
        else:
            msg = 'The predicted gender is Male.'


        prediction_state.markdown(msg)
