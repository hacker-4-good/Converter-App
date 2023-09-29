import streamlit as st 
import pickle as pk 
import pandas as pd


def model_api(age, cash, accuracy, altitude, location):
    model = pk.load(open('Streamlit/BranchApp/model.pkl', 'rb'))
    custom = pd.DataFrame({'age':[int(age)], 'cash_incoming_30days':[float(cash)], 'accuracy':[float(accuracy)], 'altitude':[float(altitude)], 'location_provider':[int(location)]})
    prediction = model.predict(custom)
    if prediction==0:
        st.text('Prediction: Defaulted')
    else:
        st.text('Prediction: Repaid')


if __name__=='__main__':
    st.title('Loan Predictor')
    age = st.text_input('Age: ', placeholder='Enter your age')
    incoming_cash = st.text_input('Incoming Cash: ', placeholder='Enter incoming cash')
    accuracy = st.text_input('Accuracy: ', placeholder='Enter accuracy of coordinate')
    altitude = st.text_input('Altitude: ', placeholder='Enter place altitude')
    location = st.text_input('Location provider', placeholder='Enter location provider (0->fused, 1->gps, 2->local database, 3->network)')
    if st.button('Submit'):
        model_api(age, incoming_cash, accuracy, altitude, location)