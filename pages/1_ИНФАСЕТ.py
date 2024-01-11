import streamlit as st
import pandas as pd
import numpy as np

data2= pd.read_csv("Data4_preprocessed.csv")
df2 = pd.DataFrame(data2)

st.title('Информация о датасетe')

st.header('Датасет для классификации - "Опасность космических объектов"')
st.markdown('---')
st.dataframe(df2)
st.subheader('Unnamed: 0')
st.markdown('Столбец с нумерацией')

st.subheader('est_diameter_min')
st.markdown('Минимальный расчетный диаметр в километрах')

st.subheader('est_diameter_max')
st.markdown('Максимальный расчетный диаметр в километрах')

st.subheader('relative_velocity')
st.markdown('Скорость относительно Земли')

st.subheader('miss_distance')
st.markdown('Пропущенное расстояние в километрах')

st.subheader('absolute_magnitude')
st.markdown('Описывает внутреннюю светимость')

st.subheader('hazardous')
st.markdown('Опасность объекта: 1 - опасность, 0 - безопасность')
