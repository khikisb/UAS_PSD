import pandas as pd
import pickle
import streamlit as st

# load the model from disk
model = pickle.load(open('knn_model.pkl', 'rb'))
model2 = pickle.load(open('naive_bayes_model.pkl', 'rb'))


# Define the prediction function
def predict(Open, High, Low, Close, Volume):
    prediction = model.predict(pd.DataFrame([[Open, High, Low, Close, Volume]], columns = ['"Open, High, Low, Close, Volume"',]))
    return prediction

st.set_page_config(
    page_title="Prediksi Nilai Saham Bank BRI",
    page_icon="👋",
)

st.title("")
st.sidebar.success("Pilih Halaman Yang Ingin Anda Tuju.")

st.title("Prediksi Nilai Saham Bank BRI")

tab1, tab2, tab3, tab4 = st.tabs(["Data", "Preprocessing Data", "Modeling", "Implementasi"])

with tab1:
   st.image("TabDD1.png")

with tab2:
   st.image("TabPP1.png")
    
with tab3:
   st.image("tabmodel.png")

with tab4:
   st.image("TI1.png")
   st.image("TI2.png")
    
st.header('Jawablah Semua Pertanyaan Berikut :')

Open = st.selectbox('Apakah anak-anak aman di antara anggota keluarga seperti kakek nenek, paman, bibi, sepupu', ['Setuju', 'Tidak Setuju'])
High = st.selectbox('Anak-anak paling sering dilecehkan oleh orang asing di masyarakat kita', ['Setuju', 'Tidak Setuju'])
Low = st.selectbox('Anak laki-laki tidak membutuhkan pengetahuan pencegahan pelecehan seksual', ['Setuju', 'Tidak Setuju'])
Close = st.selectbox('Mengajarkan pencegahan pelecehan seksual di sekolah tidak perlu. Itu akan membuat anak penasaran dengan seks', ['Setuju', 'Tidak Setuju'])
Volume = st.selectbox('Apakah anda tahu apa itu perawatan anak?', ['Iya Tahu', 'Tidak Tahu'])

if st.button('Prediksi'):
    prediksi = predict(Open, High, Low, Close, Volume)
    st.success(f'Prediksi harga penutupan: {prediksi}')
