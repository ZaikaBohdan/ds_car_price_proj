# Data Science project "Building a car price prediction model for the CarDekho website"
<p align="center">
  <img src="https://github.com/ZaikaBohdan/ds_car_price_proj/blob/main/imgs/car_dekho.jpg?raw=true" />
</p>

## About the project
[CarDekho](https://www.cardekho.com/) is India's leading car search venture that helps users buy cars. Its website and app carry rich automotive content such as expert reviews, detailed specs and prices, comparisons as well as videos and pictures of all car brands and models available in India. The company has tie-ups with many auto manufacturers, more than 4000 car dealers and numerous financial institutions to facilitate the purchase of vehicles.

In this project, we'll collect data about used cars from the CarDekho website, build a price prediction model and deploy it in a web app. The app may later be used by CarDekho users for evaluating the price of put up for sale vehicles or exploring collected data on their own.

The project is separated into 2 notebooks and the web app:
* [Part 1: Data collection and splitting into train and validation datasets](https://nbviewer.org/github/ZaikaBohdan/ds_car_price_proj/blob/main/car_price_part_1.ipynb) (Jupyter notebook)
* [Part 2: Data preparation and model building](https://nbviewer.org/github/ZaikaBohdan/ds_car_price_proj/blob/main/car_price_part_2.ipynb) (Jupyter notebook)
* [Web App "Used car price prediction for the CarDekho website"](https://share.streamlit.io/zaikabohdan/ds_car_price_proj/main/app/app.py)

## Table of Contents
1. [File Descriptions](#File_Description)
2. [Technologies Used](#Technologies_Used)    
3. [Structure of Notebooks](#Structure_of_Notebooks)
4. [Future Improvements](#Future_Improvements)

## File Descriptions
<details>
<a name="File_Description"></a>
<summary>Show/Hide</summary>
<br>

* **[app](https://github.com/ZaikaBohdan/ds_car_price_proj/tree/main/app)**: folder containing files for creating the [web app](https://share.streamlit.io/zaikabohdan/ds_car_price_proj/main/app/app.py)
  * **app.py**: file with code related to app interface
  * **func.py**: file with code related to data processing and predicting car prices
  * **requirements.txt**: file with list of required Python lybraries for the web app 
* **[data](https://github.com/ZaikaBohdan/ds_car_price_proj/tree/main/data)**: folder containing all data files
  * **Car details v3.csv**: [Vehicle dataset](https://www.kaggle.com/nehalbirla/vehicle-dataset-from-cardekho?select=Car+details+v3.csv) from Kaggle
  * **Cardekho_Extract.csv**: [Used Car Prices in India](https://www.kaggle.com/saisaathvik/used-cars-dataset-from-cardekhocom?select=Cardekho_Extract.csv) dataset from Kaggle
  * **train.csv**, **valid.csv**: splitted pre-cleaned (with methods that don't cause data leakage) data, result of the first notebook  [Part 1: Data collection and splitting into train and validation datasets](https://nbviewer.org/github/ZaikaBohdan/ds_car_price_proj/blob/main/car_price_part_2.ipynb)
  * **clean_train.csv**: cleaned train dataset used for model building
  * **valid_without_price.csv**: validation dataset without car price column (*selling_price_inr*)
* **[imgs](https://github.com/ZaikaBohdan/ds_car_price_proj/tree/main/imgs)**: folder with images used in jupyter notebooks and README
* **[model](https://github.com/ZaikaBohdan/ds_car_price_proj/tree/main/model)**: folder containing trained Random Forest Regression model saved with pickle
* **[car_price_part_1.ipynb](https://nbviewer.org/github/ZaikaBohdan/ds_car_price_proj/blob/main/car_price_part_1.ipynb)**: notebook with data collection and splitting
* **[car_price_part_2.ipynb](https://nbviewer.org/github/ZaikaBohdan/ds_car_price_proj/blob/main/car_price_part_2.ipynb)**: notebook with data preparation and model building
</details>
  
## Tecnologies Used
<details>
<a name="Technologies_Used"></a>
<summary>Show/Hide</summary>
<br>
    
* **Python**
* **Pandas**
* **Numpy**
* **Matplotlib**
* **Seaborn**
* **Scikit-Learn**
* **Streamlit**
</details>

## Structure of Notebooks
<details>
<a name="Structure_of_Notebooks"></a>
<summary>Show/Hide</summary>
<br>
    
[Part 1: Data collection and splitting into train and validation datasets](https://nbviewer.org/github/ZaikaBohdan/ds_car_price_proj/blob/main/car_price_part_1.ipynb)
  * Data Collection
  * Create train and validation datasets
    * Find corresponding and non-corresponding columns of both datasets
    * Data cleaning of [Vehicle dataset](https://www.kaggle.com/nehalbirla/vehicle-dataset-from-cardekho?select=Car+details+v3.csv)
    * Data cleaning of [Used Car Prices in India](https://www.kaggle.com/saisaathvik/used-cars-dataset-from-cardekhocom?select=Cardekho_Extract.csv)
    * Combine the datasets
    * Manage duplicate rows, outliers and null values (with methods that don't cause data leakage for future train/validation split)
    * Split data into train and validation datasets


[Part 2: Data preparation and model building](https://nbviewer.org/github/ZaikaBohdan/ds_car_price_proj/blob/main/car_price_part_2.ipynb)
  * Data cleaning of train dataset
  * Exploratory data analysis
  * Feature Engineering
  * Model Building
</details>

## Future Improvements
<details>
<a name="Future_Improvements"></a>
<summary>Show/Hide</summary>
<br>

* Add feature selection
* Try using different regression models
