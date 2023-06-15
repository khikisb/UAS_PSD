import pandas as pd
import pickle
import streamlit as st

# load the model from disk
model = pickle.load(open('knn_model.pkl', 'rb'))
model2 = pickle.load(open('naive_bayes_model.pkl', 'rb'))

st.set_page_config(
    page_title="Prediksi Nilai Saham Bank BRI",
    page_icon="👋",
)

st.title("")
st.sidebar.success("Pilih Halaman Yang Ingin Anda Tuju.")

st.title("Prediksi Nilai Saham Bank BRI")

tab1, tab2, tab3, tab4 = st.tabs(["Data", "Preprocessing Data", "Modeling", "Implementasi"])

with tab1:
   st.image("data.png")

with tab2:
   st.write("Reduksi Dimensi")
   st.image("ReduksiDimensi.png")
   st.write("MinMax Scaller")
   st.image("MMScaler.png")
    
with tab3:
   st.write("Metode KNN")
   st.image("AkurasiKNN.png")
   st.write("Metode Naive Bayes")
   st.image("AkurasiNB.png")

with tab4:
    # Define the prediction function
    def predict(Open, High, Low, Close, Volume):
        prediction = model.predict(pd.DataFrame([[Open, High, Low, Close, Volume]], columns = ['"Open, High, Low, Close, Volume"',]))
        return prediction

    def predict2(Open, High, Low, Close, Volume):
        prediction2 = model2.predict2(pd.DataFrame([[Open, High, Low, Close, Volume]], columns = ['"Open, High, Low, Close, Volume"',]))
        return prediction2
    
    st.header('Jawablah Semua Pertanyaan Berikut :')

    Open = st.selectbox('Apakah anak-anak aman di antara anggota keluarga seperti kakek nenek, paman, bibi, sepupu', ['Setuju', 'Tidak Setuju'])
    High = st.selectbox('Anak-anak paling sering dilecehkan oleh orang asing di masyarakat kita', ['Setuju', 'Tidak Setuju'])
    Low = st.selectbox('Anak laki-laki tidak membutuhkan pengetahuan pencegahan pelecehan seksual', ['Setuju', 'Tidak Setuju'])
    Close = st.selectbox('Mengajarkan pencegahan pelecehan seksual di sekolah tidak perlu. Itu akan membuat anak penasaran dengan seks', ['Setuju', 'Tidak Setuju'])
    Volume = st.selectbox('Apakah anda tahu apa itu perawatan anak?', ['Iya Tahu', 'Tidak Tahu'])

    if st.button('Prediksi'):
        prediksi = predict(Open, High, Low, Close, Volume)
        prediksi2 = predict2(Open, High, Low, Close, Volume)
        st.success(f'Prediksi harga penutupan KNN: {prediksi}')
        st.success(f'Prediksi harga penutupan Menggunakan Naive Bayes: {prediksi2}')
