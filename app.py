import streamlit as st
import requests

# URL for VinoDine API
url = 'https://vinodine-dxr2er4ueq-ew.a.run.app/predict'


"""
# Input for VinoDine
"""
Type  = st.selectbox('Type of the wine', ['Red', 'White', 'Rose', 'Sparkling', 'Dessert/Port', 'Dessert'])
ABV = float(st.number_input('Alcohol percentage of wine'))
Body  = st.selectbox('Body of the wine', ['Very full-bodied','Full-bodied', 'Medium-bodied', 'Light-bodied','Very light-bodied'])
Acidity = st.selectbox('Acidity of the wine', ['High', 'Medium', 'Low'])

if st.button('Suggest food'):
    params = {'Type': Type,
            'ABV': ABV,
            'Body': Body,
            'Acidity': Acidity}

    # st.write(params)
    response = requests.get(url, params=params).json()['foods']

    '''
    # Suggested foods:
    '''
    i = 1
    for food in response:
        st.write(f'{i}. {food}')
        i += 1
