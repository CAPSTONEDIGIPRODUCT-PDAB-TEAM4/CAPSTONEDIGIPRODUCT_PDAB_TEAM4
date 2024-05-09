import streamlit as st
import seaborn as sns
from googletrans import Translator
import matplotlib.pyplot as plt
import pickle
import joblib

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
        The visualization above shows the distribution of release years of Korean dramas. This diagram is a horizontal histogram with year of release on the x-axis and the number of Korean dramas released each year on the y-axis.
        Based on the visualization results according to the year of Korean drama release, the Korean drama industry has experienced significant growth in the last few years, namely there was a significant increase after 2010. Based on the visualization above, it can be seen that 2020 and 2022 have the highest number of Korean dramas. released a lot, with a total of 30 and 35 Korean dramas. Followed by 2012 and 2015 which had the same number of dramas, namely 25 Korean dramas. Meanwhile, 2002 had the least number of dramas, namely 5 dramas and this trend shows that Korean dramas are increasingly popular throughout the world. Fluctuations in the number of Korean dramas released each year are likely caused by various factors. In addition, the years 2002, 2005, 2007, and 2010 also showed a slight decrease in the number of Korean dramas released.    
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
        The visualization above shows the distribution of release years of Korean dramas. This diagram is a horizontal histogram with year of release on the x-axis and the number of Korean dramas released each year on the y-axis.
        Based on the visualization results according to the year of Korean drama release, the Korean drama industry has experienced significant growth in the last few years, namely there was a significant increase after 2010. Based on the visualization above, it can be seen that 2020 and 2022 have the highest number of Korean dramas. released a lot, with a total of 30 and 35 Korean dramas. Followed by 2012 and 2015 which had the same number of dramas, namely 25 Korean dramas. Meanwhile, 2002 had the least number of dramas, namely 5 dramas and this trend shows that Korean dramas are increasingly popular throughout the world. Fluctuations in the number of Korean dramas released each year are likely caused by various factors. In addition, the years 2002, 2005, 2007, and 2010 also showed a slight decrease in the number of Korean dramas released.    
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
        The visualization above shows the popularity trend of Korean dramas over several years. This diagram is a horizontal histogram with release year on the x-axis and ratings of Korean dramas released each year on the y-axis.
        Based on the visualization above, we can see that the popularity of Korean dramas continues to increase from 2002 to 2022. This trend shows that Korean dramas are becoming increasingly popular every year.
        From the visualization above, it is found that:

        1. 2016 and 2022 have the highest popularity of Korean dramas, with an average rating of 8.6.
        2. 2015 and 2020 were in second place with an average rating of 8.5.
        3. 2002 had the lowest popularity of Korean dramas, with an average rating of 8.3.
        4. 2003 and 2004 had the same drama popularity, namely with an average rating of 8.4.
            
        By looking at the popularity trend of Korean dramas, we can make decisions about producing or watching Korean dramas with genres that are popular that year.""")
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
        The visualization above shows the popularity trend of Korean dramas over several years. This diagram is a horizontal histogram with release year on the x-axis and ratings of Korean dramas released each year on the y-axis.
        Based on the visualization above, we can see that the popularity of Korean dramas continues to increase from 2002 to 2022. This trend shows that Korean dramas are becoming increasingly popular every year.
        From the visualization above, it is found that:

        1. 2016 and 2022 have the highest popularity of Korean dramas, with an average rating of 8.6.
        2. 2015 and 2020 were in second place with an average rating of 8.5.
        3. 2002 had the lowest popularity of Korean dramas, with an average rating of 8.3.
        4. 2003 and 2004 had the same drama popularity, namely with an average rating of 8.4.
            
        By looking at the popularity trend of Korean dramas, we can make decisions about producing or watching Korean dramas with genres that are popular that year.""")
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
        The visualization above shows the popularity trend of Korean dramas over several years. This diagram is a horizontal histogram with release year on the x-axis and ratings of Korean dramas released each year on the y-axis.
        Based on the visualization above, we can see that the popularity of Korean dramas continues to increase from 2002 to 2022. This trend shows that Korean dramas are becoming increasingly popular every year.
        From the visualization above, it is found that:

        1. 2016 and 2022 have the highest popularity of Korean dramas, with an average rating of 8.6.
        2. 2015 and 2020 were in second place with an average rating of 8.5.
        3. 2002 had the lowest popularity of Korean dramas, with an average rating of 8.3.
        4. 2003 and 2004 had the same drama popularity, namely with an average rating of 8.4.
            
        By looking at the popularity trend of Korean dramas, we can make decisions about producing or watching Korean dramas with genres that are popular that year.""")
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
        Based on the visualization above, the following results are obtained.

        1. The distribution of Korean drama ratings is uneven.
        2. There are many Korean dramas with a rating of 8.0 to 8.5.
        3. The number of Korean dramas with ratings of 7.0 and 10.0 is relatively fewer.
        4. There has been an increasing trend in the number of Korean dramas with high ratings (8.5 - 10.0) in recent years. This shows that the overall quality of Korean dramas is increasing.
        5. We can also see that the number of Korean dramas with ratings of 9.1 and 9.0 is quite high, namely 9 and 8 dramas. This shows that Korean dramas with high ratings are still popular today.
        
        By looking at the distribution trend of Korean drama ratings, we can make decisions about producing or watching Korean dramas that are relevant to that rating. This can help us understand trends among our audience and maximize opportunities to take advantage of those trends.
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
        Based on the visualization above, the following results are obtained.

        1. The distribution of Korean drama ratings is uneven.
        2. There are many Korean dramas with a rating of 8.0 to 8.5.
        3. The number of Korean dramas with ratings of 7.0 and 10.0 is relatively fewer.
        4. There has been an increasing trend in the number of Korean dramas with high ratings (8.5 - 10.0) in recent years. This shows that the overall quality of Korean dramas is increasing.
        5. We can also see that the number of Korean dramas with ratings of 9.1 and 9.0 is quite high, namely 9 and 8 dramas. This shows that Korean dramas with high ratings are still popular today.
        
        By looking at the distribution trend of Korean drama ratings, we can make decisions about producing or watching Korean dramas that are relevant to that rating. This can help us understand trends among our audience and maximize opportunities to take advantage of those trends.
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
        Based on the visualization above, the following results are obtained.

        1. The distribution of Korean drama ratings is uneven.
        2. There are many Korean dramas with a rating of 8.0 to 8.5.
        3. The number of Korean dramas with ratings of 7.0 and 10.0 is relatively fewer.
        4. There has been an increasing trend in the number of Korean dramas with high ratings (8.5 - 10.0) in recent years. This shows that the overall quality of Korean dramas is increasing.
        5. We can also see that the number of Korean dramas with ratings of 9.1 and 9.0 is quite high, namely 9 and 8 dramas. This shows that Korean dramas with high ratings are still popular today.
        
        By looking at the distribution trend of Korean drama ratings, we can make decisions about producing or watching Korean dramas that are relevant to that rating. This can help us understand trends among our audience and maximize opportunities to take advantage of those trends.
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
        From this visualization, we can see that Korean dramas released in 2017.5 have the highest rating with an average of 8.8. Apart from that, we can also see that Korean dramas released in the years 2015.0, 2017.5, and 2022.5 have a higher average rating compared to other years. This shows that Korean drama producers produced more dramas with higher ratings in those years.
        We can also see that the years 2002.5, 2005.0, 2007.5, and 2010.0 have lower average ratings compared to other years. This shows that Korean drama producers produced fewer dramas with higher ratings in those years.
            """)
    if translate:
        translated_text = translate_text(text)
        if translated_text:
            text = translated_text
    st.markdown(text)

def predict(df):
    st.title("TTT")