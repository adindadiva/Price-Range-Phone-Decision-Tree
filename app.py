from sklearn import model_selection
import streamlit as st
import pandas as pd 
from PIL import Image 
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import seaborn as sns 
import pickle 

#import model 
dtc = pickle.load(open('dtc.pkl','rb'))

#load dataset
data = pd.read_excel("Price Range Phone Dataset.xlsx")
#data = data.drop(data.columns[0],axis=1)

st.title('Estimasi Harga HandPhone')

if st.checkbox("Tentang Dataset"):
    html_layout2 ="""
    <br>
    """
    st.markdown(html_layout2,unsafe_allow_html=True)
    st.subheader('Dataset')
    st.write(data.head(10))
    st.subheader('Describe dataset')
    st.write(data.describe())

sns.set_style('darkgrid')

if st.checkbox('EDa'):
    pr =ProfileReport(data,explorative=True)
    st.header('**Input Dataframe**')
    st.write(data)
    st.write('---')
    st.header('**Profiling Report**')
    st_profile_report(pr)


baterry = st.number_input('Input Battery Power')
clock_speed = st.number_input('Input Clock Speed')
ram = st.number_input('Input Ram')
primary_camera = st.number_input('Input Primary Camera Megapixels')
int_memory = st.number_input('Input Memory Internal')


predict = ''

if st.button('Estimasi Harga'):
    predict = dtc.predict(
        [[baterry, clock_speed, ram, primary_camera, int_memory]]
    )
    st.write('Estimasi Harga HandPhone dalam Ponds : ', predict)