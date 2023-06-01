import streamlit as st
import pandas as pd
import pickle


pickle_in = open("E:/rf1.pkl", "rb") 
classifier = pickle.load(pickle_in)

def predict_note_authentication(chroma_stft, rmse, spectral_bandwidth, rolloff, mfcc1, mfcc3, mfcc4, mfcc9, mfcc17, mfcc12, mfcc6, spectral_centroid):
    prediction = classifier.predict([[chroma_stft, rmse, spectral_bandwidth, rolloff, mfcc1, mfcc3, mfcc4, mfcc9, mfcc17, mfcc12, mfcc6, spectral_centroid]])
    print(prediction)
    return prediction


def main():

    st.title("Music Genre Predictor")

    html_temp = """
    <div style="background-color:green;padding:10px">
    <h2 style="color:white;text-align:center;">Predict The Genre Of Music </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)

    chroma_stft  =  st.number_input("Enter value for Chorma of Music", step=0.1000)

    rmse = st.number_input("Enter Value for RMSE", step=0.1000)

    spectral_bandwidth = st.number_input("Enter Bandwidth", step=0.1000)

    rolloff = st.number_input("Enter Rolloff", step=0.1000)

    mfcc1 = st.number_input("MFCC1", step=0.1000)

    mfcc3 = st.number_input("MFCC3", step=0.1000)

    mfcc4 = st.number_input("MFCC4", step=0.1000)

    mfcc9 = st.number_input("MFCC9", step=0.1000)

    mfcc17 = st.number_input("MFCC17", step=0.1000)

    mfcc12 = st.number_input("MFCC12", step=0.1000)

    mfcc6 = st.number_input("MFCC6", step=0.1000)

    spectral_centroid = st.number_input("spectral_centroid", step=0.1000)

    result= ""

    if st.button("Predict"):
        result = predict_note_authentication(chroma_stft, rmse, spectral_bandwidth, rolloff, mfcc1, mfcc3, mfcc4, mfcc9, mfcc17, mfcc12,mfcc6,spectral_centroid)
    #st.success('Music Genre is {}'.format(result))
    
    if result == 0:
        st.success('Music Genre is Blues')
    elif result == 1:
        st.success("Music Genre is Classical")
    elif result == 2:
        st.success("Music Genre is Country")
    elif result == 3:
        st.success("Music Genre is Disco")
    elif result == 4:
        st.success("Music Genre is Hiphop")
    elif result == 5:
        st.success("Music Genre is Jazz")
    elif result == 6:
        st.success("Music Genre is Metal")
    elif result == 7:
        st.success("Music Genre is Pop")
    elif result == 8:
        st.success("Music Genre is Reggae")
    elif result == 9:
        st.success("Music Genre is Rock")



if __name__=='__main__':
    main()