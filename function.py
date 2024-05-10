import streamlit as st
import seaborn as sns
from googletrans import Translator
import matplotlib.pyplot as plt

def translate_text(text, target_language='id'):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language)
    return translated_text.text

def distribution(df):
    colors = ['#ff179f', '#2986cc']
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.countplot(x='region', hue='Gender', data=df, palette=colors)
    plt.title('Distribusi Gender Berdasarkan Region')
    plt.xlabel('Region')
    plt.ylabel('Count')

    fig1, ax1 = plt.subplots(figsize=(8, 6))
    sns.histplot(df['age'], kde=True)
    plt.title('Distribusi Usia')

    fig2, ax2 = plt.subplots(figsize=(8, 6))
    colors = ['#ab53d9', '#81d953']
    sns.countplot(x='Gender', hue='smoker', data=df, palette=colors)
    plt.title('Frekuensi Smoker Berdasarkan Gender')

    col1, col2 = st.columns(2)
    with col1:
        st.pyplot(fig)
        st.pyplot(fig1)
    with col2:
        st.pyplot(fig2)

    translate = st.checkbox("Translate to Indonesia")
    text = (""" 
        The bar graph illustrates gender population percentages by region:

        - In the Southwest, women constitute 64.4% and men 35.4%.
        - The Southeast has 70.6% men and 29.6% women.
        - In the Northwest, women make up 80.1% and men 19.9%.
        - The Northeast shows 84.7% men and 15.3% women.
            
        Another graph displays age distribution, with the 30-50 age group being the most frequent (around 60%). Frequencies decrease for age groups under 30 and over 50, with under 20 at 10% and over 60 at 20%.
        Lastly, a bar graph presents smoking frequency by gender. More women are non-smokers, while more men do not smoke. Women have a slightly higher non-smoking frequency at 50.8% compared to men at 49.2%.
            """)
    if translate:
        translated_text = translate_text(text)
        if translated_text:
            text = translated_text
    st.markdown(text)

def comparison(df):
    fig, ax = plt.subplots(figsize=(8, 6))
    color = ['red', 'blue']
    result_counts = df.groupby(['Driving test result', 'Gender']).size().unstack()
    sns.lineplot(data=result_counts, marker='o', palette=color)
    plt.title('Jumlah Driving Test Result Berdasarkan Gender')

    fig1, ax1 = plt.subplots(figsize=(8, 6))
    colors = ['#ff179f', '#2986cc']
    sns.barplot(x='Childeren', y='Bmi', hue='Gender', data=df, palette=colors)
    plt.title('Rata-rata BMI Berdasarkan Jumlah Anak')

    fig2, ax2 = plt.subplots(figsize=(8, 6))
    colors = ['#ab53d9', '#81d953']
    sns.barplot(x='Gender', y='Bmi', hue='smoker', data=df, palette=colors)
    plt.title('Perbandingan BMI Berdasarkan Gender dan Kebiasaan Merokok')

    col1, col2 = st.columns(2)
    with col1:
        st.pyplot(fig)
        st.pyplot(fig1)
    with col2:
        st.pyplot(fig2)

    translate = st.checkbox("Translate to Indonesia")
    text = (""" 
        The bar graph displays the total number of men and women who took driving tests, with men achieving a higher pass rate overall.
        A line graph compares average heights by gender and number of children, revealing that women consistently have higher average heights than men across all child count categories.
        Lastly, a bar graph compares smoking percentages by gender, showing that slightly more women (50.8%) smoke compared to men (49.2%).
            """)
    if translate:
        translated_text = translate_text(text)
        if translated_text:
            text = translated_text
    st.markdown(text)

def composition(df):
    fig, ax = plt.subplots(figsize=(8, 6))
    gender_counts = df['Gender'].value_counts()
    labels = gender_counts.index.tolist()
    sizes = gender_counts.values.tolist()
    colors = ['#ff179f', '#2986cc']
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    plt.title('Proporsi Sebaran Jenis Kelamin')

    fig1, ax1 = plt.subplots(figsize=(8, 6))
    visual_region = df['region'].value_counts()
    visual_region.plot(kind='pie', autopct='%1.1f%%', startangle=0, colors=colors)
    plt.title('Region')

    fig2, ax2 = plt.subplots(figsize=(8, 6))
    colors = ['#ab53d9', '#81d953']
    visual_smoker = df['smoker'].value_counts()
    visual_smoker.plot(kind='pie', autopct='%1.1f%%', startangle=0, colors=colors)
    plt.title('Smoker')

    col1, col2 = st.columns(2)
    with col1:
        st.pyplot(fig)
        st.pyplot(fig1)
    with col2:
        st.pyplot(fig2)

    translate = st.checkbox("Translate to Indonesia")
    text = (""" 
        This pie chart illustrates smoking prevalence in the US: 72.9% are non-smokers, while 27.1% smoke.
        Another diagram depicts regional population distribution: the Southeast dominates with 28.8%, while the Northeast, Northwest, and Southwest each have 23.7%.
        Lastly, a pie chart shows gender distribution: 50.8% are women, and 49.2% are men.
        """)
    if translate:
        translated_text = translate_text(text)
        if translated_text:
            text = translated_text
    st.markdown(text)

def relationship(df):
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.scatterplot(x='Salary', y='age', hue='Gender', data=df)
    plt.title('Korelasi antara Usia dan Gaji Berdasarkan Gender')

    st.pyplot(fig)

    translate = st.checkbox("Translate to Indonesia")
    text = (""" 
        Each dot represents one person, with age plotted on the X-axis and salary plotted on the Y-axis. The color of the dot indicates the person's gender: blue for women and orange for men. The scatter plot shows that there is a positive correlation between age and salary for both genders. This means that in general, the older the person, the higher the salary.
        """)
    if translate:
        translated_text = translate_text(text)
        if translated_text:
            text = translated_text
    st.markdown(text)
