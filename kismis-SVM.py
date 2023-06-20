import pickle
import streamlit as st
import numpy as np

# membaca model
model = pickle.load(open('kismis.sav', 'rb'))
scaler = pickle.load(open('scaler.sav','rb'))

#judul web
st.title('Prediksi Kategori kismis')

#membagi kolom
col1, col2 = st.columns(2)

with col1 :
    Area = st.number_input('Input nilai Area zona kismis  dan jumlah piksel di dalam batas-batasnya.')
    MajorAxisLength = st.number_input('Input nilai Jarak antara ujung garis terpanjang yang dapat ditarik dari sebuah bean.')
    MinorAxisLength = st.number_input('Input nilai Garis terpanjang yang bisa ditarik dari kismis  sambil berdiri tegak lurus pada sumbu utama.')
    
with col2 :
    Eccentricity = st.number_input('Input nilai Eksentrisitas elips yang memiliki momen yang sama dengan wilayahnya')
    ConvexArea = st.number_input('Input nilai Jumlah piksel dalam poligon cembung terkecil yang dapat memuat area kismis kismis .')
    Extent = st.number_input('Input nilai Rasio piksel dalam kotak pembatas terhadap area kismis.')
    Perimeter = st.number_input('Input nilai Keliling kismis')

# code untuk prediksi
prediction = ''
input_data = (Area,MajorAxisLength,MinorAxisLength,Eccentricity,ConvexArea,Extent,Perimeter)

input_data_as_numpy_array = np.array(input_data)

input_data_reshape = input_data_as_numpy_array.reshape(1,-1)

std_data = scaler.transform(input_data_reshape)

# membuat tombol untuk prediksi
if st.button('Test'):
    drybean_prediction = model.predict(std_data)
    if(drybean_prediction[0] == 0):
        prediction = 'kismis tersebut termasuk kedalam kategori Kecimen'
    else:
        prediction = 'kismis tersebut termasuk kedalam kategori Besni'
    st.success(prediction)
