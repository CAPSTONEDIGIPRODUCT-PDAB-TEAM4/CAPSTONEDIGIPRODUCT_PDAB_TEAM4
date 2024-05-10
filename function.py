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
    fig, ax = plt.subplots()
    sns.countplot(x='region', hue='Gender', data=df, palette=colors)
    plt.title('Distribusi Gender Berdasarkan Region')
    plt.xlabel('Region')
    plt.ylabel('Count')

    st.pyplot(fig)

    translate = st.checkbox("Translate to Indonesia")
    text = (""" 
        This bar graph compares gender population percentages by region. The graph is divided into four bars viz

        The southwest has a population of more women than men, namely women 64.4% and men 35.4%
        Southeast has a population of more men than women, namely men 70.6% and women 29.6%
        The northwest has a population of more women than men, namely women 80.1% and men 19.9%
        The northeast has a population of more men than women, namely men 84.7% and women 15.3%
        """)
    if translate:
        translated_text = translate_text(text)
        if translated_text:
            text = translated_text
    st.markdown(text)

    fig1, ax = plt.subplots()
    sns.histplot(df['age'], kde=True)
    plt.title('Distribusi Usia')
    plt.xlabel('Usia')
    plt.ylabel('Frekuensi')
    
    st.pyplot(fig1)

    translate = st.checkbox("Translate to Indonesia (Age)")
    text = (""" 
        This graph distributes the age distribution of the city's population concentrated in the 30-50 year age group. This age group reaches the highest frequency, namely around 60%. Age groups under 30 years and over 50 years have a lower frequency. The age group under 20 years only reaches a frequency of around 10%, while the age group over 60 years only reaches a frequency of around 20%.
        """)
    if translate:
        translated_text = translate_text(text)
        if translated_text:
            text = translated_text
    st.markdown(text)

    fig, ax = plt.subplots()
    colors = ['#ab53d9', '#81d953']
    sns.countplot(x='Gender', hue='smoker', data=df, palette=colors)
    plt.title('Frekuensi Smoker Berdasarkan Gender')
    plt.xlabel('Gender')
    plt.ylabel('Frekuensi')
    
    st.pyplot(fig)

    translate = st.checkbox("Translate to Indonesia (Smoker)")
    text = (""" 
        This bar graph shows the frequency of smoking by gender in a population, it can be divided into two bars, one for women and one for men. In the bar graph of women, it can be seen that there are more non-smokers than smokers. Likewise, in the bar graph, men who do not smoke are more dominant than smokers. So it can be concluded that there is a small difference between the frequency of non-smoking for women and men. Women are slightly more likely to not smoke than men, with a percentage of 50.8% compared to 49.2%.
        """)
    if translate:
        translated_text = translate_text(text)
        if translated_text:
            text = translated_text
    st.markdown(text)
    
def comparison(df):
    fig, ax = plt.subplots()
    color = ['red', 'blue']
    result_counts = df.groupby(['Driving test result', 'Gender']).size().unstack()
    sns.lineplot(data=result_counts, marker='o', palette=color)

    plt.title('Jumlah Driving Test Result Berdasarkan Gender')
    plt.xlabel('Driving test result')
    plt.ylabel('Count')
    plt.grid(True)
    plt.legend(title='Gender')
    st.pyplot(fig)

    translate = st.checkbox("Translate to Indonesia")
    text = (""" 
        This graph shows the total number of men and women who took driving tests. Men have a higher overall pass rate than women in driving tests.
    """)
    if translate:
        translated_text = translate_text(text)
        if translated_text:
            text = translated_text
    st.markdown(text)

    fig, ax = plt.subplots()
    colors = ['#ff179f', '#2986cc']
    sns.barplot(x='Childeren', y='Bmi', hue='Gender', data=df, palette=colors)
    plt.title('Rata-rata BMI Berdasarkan Jumlah Anak')
    plt.xlabel('Jumlah Anak')
    plt.ylabel('Rata-rata BMI')
    st.pyplot(fig)

    translate = st.checkbox("Translate to Indonesia (BMI and Children)")
    text = (""" 
            This line graph compares average height by gender and number of children. The average height of women is consistently higher than the average height of men at all values for the number of children. The average height level for women decreases as the number of children increases.
            """)
    if translate:
        translated_text = translate_text(text)
        if translated_text:
            text = translated_text
    st.markdown(text)

    fig, ax = plt.subplots()
    colors = ['#ab53d9', '#81d953']
    sns.barplot(x='Gender', y='Bmi', hue='smoker', data=df, palette=colors)
    plt.title('Perbandingan BMI Berdasarkan Gender dan Kebiasaan Merokok')
    plt.xlabel('Gender')
    plt.ylabel('BMI')
    plt.legend(title='Smoker', loc='upper right')
    st.pyplot(fig)

    translate = st.checkbox("Translate to Indonesia (BMI and Smoker)")
    text = (""" 
            This bar graph compares the percentage of people who smoke by gender. The graph is divided into two bars, one for women and one for men. The graph shows that the majority of smokers are women, namely 50.8% of smokers, with a slightly higher percentage than men, namely 49.2% of smokers.
            """)
        
    if translate:
        translated_text = translate_text(text)
        if translated_text:
            text = translated_text
    st.markdown(text)

def composition(df):
    fig, ax = plt.subplots()
    gender_counts = df['Gender'].value_counts()
    labels = gender_counts.index.tolist()
    sizes = gender_counts.values.tolist()
    colors = ['#ff179f', '#2986cc']
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    plt.title('Proporsi Sebaran Jenis Kelamin')
    plt.axis('equal')
    st.pyplot(fig)

    translate = st.checkbox("Translate to Indonesia")
    text = (""" 
        This pie chart shows the proportion of men and women presented in a circular graph. Of which 50.8% are women and 49.2% are men.
        """)
    if translate:
        translated_text = translate_text(text)
        if translated_text:
            text = translated_text
    st.markdown(text)

    fig, ax = plt.subplots()
    visual_region = df['region'].value_counts()
    visual_region.plot(kind='pie', autopct='%1.1f%%', startangle=0, colors=colors)
    plt.title('Region')
    st.pyplot(fig)

    translate = st.checkbox("Translate to Indonesia (Region)")
    text = (""" 
        This diagram shows the percentage of population living in each region of the United States which is divided into four parts.

        The Southeast is the largest population section in the diagram, representing 28.8% of the population
        The North East, North West and Southwest have the same population in the diagram, representing 23.7% of the population.
        """)
    if translate:
        translated_text = translate_text(text)
        if translated_text:
            text = translated_text
    st.markdown(text)

    fig, ax = plt.subplots()
    colors = ['#ab53d9', '#81d953']

    visual_smoker = df['smoker'].value_counts()
    visual_smoker.plot(kind='pie', autopct='%1.1f%%', startangle=0, colors=colors)
    plt.title('Smoker')
    st.pyplot(fig)

    translate = st.checkbox("Translate to Indonesia (Smoker)")
    text = (""" 
        This chart shows the percentage of people who smoke in the United States. The larger part of the diagram shows the number of non-smokers, who represent 72.9% of the population. Meanwhile, the smaller diagram shows the number of people who smoke, which represents 27.1% of the population. So it can be seen that the majority of the United States population does not smoke.
        """)
    if translate:
        translated_text = translate_text(text)
        if translated_text:
            text = translated_text
    st.markdown(text)

def relationship(df):
    fig, ax = plt.subplots()
    sns.scatterplot(x='Salary', y='age', hue='Gender', data=df)
    plt.title('Korelasi antara Usia dan Gaji Berdasarkan Gender')
    plt.xlabel('Gaji')
    plt.ylabel('Usia')
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
