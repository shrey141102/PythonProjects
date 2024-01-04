from textblob import TextBlob
import pandas as pd 
import streamlit as st
import cleantext

st.header("Sentiment Analysis")
with st.expander('Analyze Text'):
    text = st.text_input('Text here: ')
    if text:
        blob = TextBlob(text)
        st.write('Polarity: ', round(blob.sentiment.polarity,2))
        st.write('Subjectivity: ',round(blob.sentiment.subjectivity,2))


    pre = st.text_input('Clean Text: ')
    if pre:
        st.write(cleantext.clean(pre,clean_all=False, extra_spaces =True,
                                 stopwords=True,lowercase=True,numbers=True,punct=True))
        
with st.expander("Analyze CSV"):
    upl = st.file_uploader('Upload file')

    def score(x):
        blob1 = TextBlob(x)
        return blob1.sentiment.polarity
    
    def analyze(x):
        if x>=0.5:
            return 'Positive'
        elif x<=0.5:
            return 'Negative'
        else:
            return 'Neutral'
    
    if upl: # data frame is a variable which takes and deals on the data as a table form
        df = pd.read_excel(upl,engine='xlrd')
        df = pd.read_excel('your_file.xlsx', engine='openpyxl')
        del df['Unnamed: 0']
        df['score'] = df['tweets'].apply(score)
        df['analysis'] = df['score'].apply(score)
        df['analysis'] = df['score'].apply(analyze)
        st.write(df.head(10))


        @st.cache
        def convert_df(df):
            return df.to_csv().encode('utf-8')
        
        csv = convert_df(df)

        st.download_button(
            label = "Download data as CSV",
            data =csv,
            file_name='sentiment.csv',
            mime='text/csv',
        )


