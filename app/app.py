import pandas as pd
from sklearn.ensemble import RandomForestRegressor

from func import *

import streamlit as st

# <==================== Set up ====================>
# For loading model only once
if 'rfr_model' not in st.session_state:
    df = read_csv_file('https://raw.githubusercontent.com/ZaikaBohdan/ds_car_price_proj/main/data/clean_train.csv')
    # Feature Engineering
    fe_df = all_col_to_col_flg(df)
    fe_df = brand_by_mean_price(fe_df, df)
    # Features/target split
    X, y = xy_split(fe_df)
    # Model fitting
    rfr = RandomForestRegressor(
        max_features='sqrt', 
        n_estimators=50, 
        random_state=0
        )
    rfr.fit(X, y)

    st.session_state.known_df = df
    st.session_state.rfr_model = rfr




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




# >>>>>>>>>> 'Predict the price of one car' <<<<<<<<<<
if curr_web_page == 'Predict the price of one car':
    st.markdown("## Predict the price of one car")

    selectbox_vals = {
        'fuel': ['Petrol', 'Diesel', 'CNG', 'LPG'],
        'seller_type': ['Individual', 'Dealer'],
        'transmission': ['Manual', 'Automatic'],
        'owner': ['First Owner', 'Second Owner', 'Third Owner', 'Fourth & Above Owner'],
        'seats': ['2', '4', '5', '6', '7', '8', '9', '10'],
        'brand': ['Hyundai', 'Mahindra', 'Chevrolet', 'Honda', 'Ford', 'Tata', 'Toyota', 'Maruti', 'BMW', 'Volkswagen', 'Audi', 'Nissan', 'Skoda', 'Mercedes-Benz', 'Datsun', 'Renault', 'Fiat', 'MG', 'Jeep', 'Volvo', 'Kia', 'Land Rover', 'Mitsubishi', 'Jaguar', 'Porsche', 'Mini Cooper', 'ISUZU']
    }
    
    c1, c2 = st.columns(2)

    brand = c1.selectbox('Brand', selectbox_vals['brand'])
    fuel = c1.selectbox('Fuel', selectbox_vals['fuel'])
    engine_cc = c1.number_input('Capacity of the engine (cc)', min_value=624.0, max_value=6752.0)
    max_power_bhp = c1.number_input('Engine power (bhp)', min_value=25.4, max_value=626.0)
    transmission = c1.radio('Transmission', selectbox_vals['transmission'])    

    seats = c2.selectbox('Number of seats', selectbox_vals['seats'])
    owner = c2.selectbox('Owner', selectbox_vals['owner'])
    year = c2.number_input('Year', min_value=1983, max_value=2021, value=2021)
    km_driven = c2.number_input('Kilometers driven', min_value=100, max_value=3800000)
    seller_type = c2.radio('Seller', selectbox_vals['seller_type'])

    all_vals = {
        'brand': brand,
        'fuel': fuel,
        'engine_cc': engine_cc, 
        'max_power_bhp': max_power_bhp, 
        'transmission': transmission,
        'seats': seats,
        'owner': owner,
        'year': year,
        'km_driven': km_driven,
        'seller_type': seller_type 
        }
    df = pd.DataFrame(all_vals, index=[0])

    # solution for centring the button
    col_but = st.columns(5)
    pred_button = col_but[2].button('Evaluate price')
    if pred_button:
        with st.spinner():
            result = data_prep_and_predict(
                df, 
                st.session_state.known_df, 
                st.session_state.rfr_model, 
                return_drop=False, 
                skip_dc=True
                )
        st.write(f'#### Evaluated price of the car: ₹ {result[0]:,.2f}') 




# >>>>>>>>>> 'Predict prices for a file with cars' <<<<<<<<<<
if curr_web_page == 'Predict prices for a file with cars':
    st.markdown("## Predict prices for a file with cars")

    with st.sidebar.header('Upload input file'):
        uploaded_file = st.sidebar.file_uploader(
            "Upload a CSV file with car characteristics",
            type=["csv"]
            )
        st.sidebar.markdown("""
            [Example of required file](https://github.com/ZaikaBohdan/ds_car_price_proj/blob/main/data/valid.csv)
            """)

    if uploaded_file is not None:
        st.markdown("### Input data")
        
        valid_df = read_csv_file(uploaded_file)
        st.dataframe(valid_df)
        
        st.markdown("### Predicted prices")

        with st.spinner():
            result = data_prep_and_predict(
                valid_df, 
                st.session_state.known_df, 
                st.session_state.rfr_model, 
                'selling_price_inr' in list(valid_df.columns)
                )
        
        pred_df = predict_df(valid_df, result[0])
        st.dataframe(pred_df)

        csv_file = convert_df(pred_df)
        st.download_button(
            label='📥 Download .csv file with predicted prices',
            data=csv_file, 
            file_name= 'predicted_car_prices.csv'
            )
        
        if len(result) == 3:
            st.markdown("#### Model scores")
            st.dataframe(result[2])

        if not result[1].empty:
            st.markdown("#### Dropped rows from input file")
            st.dataframe(result[1])
    
    else:
        st.info('Awaiting for csv file with car characteristics to be uploaded in the sidebar.')




# >>>>>>>>>> 'Explore car prices' <<<<<<<<<<
def graphic(col_group):
    pass


if curr_web_page == 'Explore car prices':
    st.markdown("## Explore car prices")

    cols_dict = {
        'Name': 'name',
        'Brand': 'brand',
        'Fuel': 'fuel',
        'Capacity of the engine (cc)': 'engine_cc', 
        'Engine power (bhp)': 'max_power_bhp', 
        'Transmission': 'transmission',
        'Number of seats': 'seats',
        'Owner': 'owner',
        'Year': 'year',
        'Kilometers driven': 'km_driven',
        'Seller': 'seller_type' 
        }
    cols_list = sorted(list(cols_dict.keys()))

    col_group_by = st.selectbox('Choose car characteristic for grouping prices', cols_list)
    graphic(col_group_by)
    