import streamlit as st
import pickle
import numpy as np
model=pickle.load(open('model.py','rb'))


def predict(title,author,text):
    input=np.array([[title,author,text]]).astype(np.str)
    prediction=model.predict_proba(input)
    pred='{0:.{1}f}'.format(prediction[0][0], 2)
    return float(pred)

def main():
    st.title("FAKE-NEWS DETECTOR")
    html_temp = """
    <div style="background-color:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">Forest Fire Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    title = st.text_input("title","Type Here")
    author = st.text_input("author","Type Here")
    text = st.text_input("text","Type Here")
    safe_html="""  
      <div style="background-color:#F4D03F;padding:10px >
       <h2 style="color:white;text-align:center;"> News is True</h2>
       </div>
    """
    danger_html="""  
      <div style="background-color:#F08080;padding:10px >
       <h2 style="color:black ;text-align:center;"> News is Fake</h2>
       </div>
    """

    if st.button("Predict"):
        output=predict(title,author,text)
        st.success('probability that this is a fake news is {}'.format(output))

        if output > 0.5:
            st.markdown(danger_html,unsafe_allow_html=True)
        else:
            st.markdown(safe_html,unsafe_allow_html=True)

if __name__=='__main__':
    main()
