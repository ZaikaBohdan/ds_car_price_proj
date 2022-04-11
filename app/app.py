import pandas as pd

import pickle
import requests

import streamlit as st

# <==================== Set up ====================>
# For loading model only once
if 'rfr_model' not in st.session_state:
    #r = requests.get('https://github.com/ZaikaBohdan/ds_car_price_proj/blob/main/app/rfr_model.sav?raw=true')
    #st.session_state.rfr_model = r.text
    #pickle.load(open(, 'rb'))
    pass





# <==================== Interface ====================>
st.set_page_config(
    page_title='Used car price prediction for the CarDekho website',
    page_icon='🚗',
    layout='centered'
)

st.write("# Used car price prediction for the CarDekho website")

web_pages = [
    'About the app', 
    'Predict the price of one car', 
    'Predict prices for a file with cars',
    'Explore car prices'
    ]
curr_web_page = st.sidebar.selectbox('Navigaton', web_pages)

#st.write(st.session_state.rfr_model)




# >>>>>>>>>> 'About the app' <<<<<<<<<<
if curr_web_page == 'About the app':
    st.markdown("""
    ## About the app
    This application is a part of the data science project ["Building a car price prediction model for the CarDekho website"](https://github.com/ZaikaBohdan/ds_car_price_proj). Through the "Navigation" in the sidebar, you can choose one of three options:
    1. **'Predict the price of one car'**: Manually enter vehicle characteristics to evaluate its price;
    2. **'Predict prices for a file with cars'**: Upload csv file with the characteristics of cars to evaluate their prices. If the column 'selling_price_inr" is present in the given file, then also *MAE, MSE* and *R^2* metrics will be calculated and shown.
    3. **'Explore car prices'**: Explore selling prices in collected data with the help of visualizations.
 
    ## Disclaimer
    This web app is a part of the **personal non-commercial project** ([link to GitHub repository](https://github.com/ZaikaBohdan/ds_car_price_proj)) and **wasn't developed by [CarDekho](https://www.cardekho.com/)**.
    """)




# >>>>>>>>>> 'Predict prices for a file with cars' <<<<<<<<<<
if curr_web_page == 'Predict prices for a file with cars':
    st.markdown("## Predict prices for a file with cars")

    with st.sidebar.header('1. Upload input file'):
        uploaded_file = st.sidebar.file_uploader(
            "Upload a CSV file with car characteristics",
            type=["csv"]
            )
        st.sidebar.markdown("""
            [Example of required file](https://github.com/ZaikaBohdan/ds_car_price_proj/blob/main/data/valid.csv)
            """)

    if uploaded_file is not None:
        st.markdown("### Input data")
        df = pd.read_csv(uploaded_file)
        st.dataframe(df)
        st.markdown("### Predicted prices")
        

        #with st.sidebar.header('1. Upload input file'):
    
    else:
        st.info('Awaiting for csv file with car characteristics to be uploaded in the sidebar.')
    