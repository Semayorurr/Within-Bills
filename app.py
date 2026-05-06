import streamlit as st

st.title("📄 AutoEntry AI - Fatura Okuyucu")

st.write("Fatura veya fiş yükleyin, veriler otomatik çıkarılsın.")

uploaded_file = st.file_uploader("Dosya yükle", type=["jpg", "png", "pdf"])

if uploaded_file is not None:
    st.success("Dosya başarıyla yüklendi!")
    st.write("Dosya adı:", uploaded_file.name)