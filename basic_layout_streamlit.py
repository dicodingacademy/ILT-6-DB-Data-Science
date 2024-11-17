import streamlit as st

# Title
st.title("Latihan Basic Layout di Streamlit")

# Sidebar
st.sidebar.title("1. Sidebar")
st.sidebar.write("Ini adalah sidebar. Anda dapat menambahkan elemen interaktif di sini, seperti tombol, slider, dan lainnya.")
sidebar_selection = st.sidebar.radio("Pilih opsi di sidebar:", options=["Home", "About", "Contact"])
st.sidebar.write(f"Anda memilih: {sidebar_selection}")

# Columns
st.header("2. Columns")
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Kolom 1")
    st.write("Konten untuk kolom pertama.")
    st.button("Tombol Kolom 1")

with col2:
    st.subheader("Kolom 2")
    st.write("Konten untuk kolom kedua.")
    st.slider("Slider Kolom 2", 0, 100)

with col3:
    st.subheader("Kolom 3")
    st.write("Konten untuk kolom ketiga.")
    st.selectbox("Pilih sesuatu:", options=["Option 1", "Option 2", "Option 3"])

# Tabs
st.header("3. Tabs")
tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])

with tab1:
    st.write("Ini adalah Tab 1.")
    st.text_area("Masukkan sesuatu untuk Tab 1")

with tab2:
    st.write("Ini adalah Tab 2.")
    st.date_input("Pilih tanggal di Tab 2")

with tab3:
    st.write("Ini adalah Tab 3.")
    st.checkbox("Centang untuk Tab 3")

# Container
st.header("4. Container")
with st.container():
    st.write("Ini adalah container. Anda dapat mengelompokkan elemen-elemen di dalamnya.")
    st.line_chart([1, 2, 3, 4, 5])

# Expander
st.header("5. Expander")
with st.expander("Klik untuk membuka Expander"):
    st.write("Ini adalah bagian yang tersembunyi di dalam expander.")
    st.file_uploader("Unggah file ke dalam expander:")
    st.radio("Pilih opsi:", options=["Pilihan A", "Pilihan B", "Pilihan C"])

# Closing
st.markdown("### **Latihan selesai! Nikmati eksplorasi layout di Streamlit! 🎉**")
