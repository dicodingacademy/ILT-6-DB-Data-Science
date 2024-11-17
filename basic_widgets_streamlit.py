import streamlit as st
import datetime

# Title
st.title("Latihan Input dan Button Widget di Streamlit")

# Input Widgets
st.header("1. Input Widgets")

# Text Input
name = st.text_input("Masukkan nama Anda:", placeholder="Nama lengkap...")
st.write(f"Nama Anda adalah: **{name}**" if name else "Silakan masukkan nama Anda.")

# Text Area
feedback = st.text_area("Masukkan feedback Anda:", placeholder="Ketikkan sesuatu di sini...")
if feedback:
    st.write("Feedback Anda:", feedback)

# Number Input
age = st.number_input("Masukkan usia Anda:", min_value=1, max_value=120, value=18)
st.write(f"Usia Anda adalah: **{age} tahun**")

# Date Input
date = st.date_input("Pilih tanggal lahir Anda:", value=datetime.date(2000, 1, 1))
st.write(f"Tanggal lahir Anda: **{date.strftime('%d-%m-%Y')}**")

# File Uploader
uploaded_file = st.file_uploader("Unggah file:", type=["txt", "csv", "jpg", "png"])
if uploaded_file:
    st.write(f"File yang diunggah: **{uploaded_file.name}**")

# Camera Input
photo = st.camera_input("Ambil foto dengan kamera Anda (opsional):")
if photo:
    st.image(photo, caption="Foto Anda", use_column_width=True)

# Interactive Buttons
st.header("2. Button Widgets")

# Button
if st.button("Klik saya"):
    st.success("Tombol berhasil diklik!")

# Checkbox
show_secret = st.checkbox("Tampilkan rahasia?")
if show_secret:
    st.write("🎉 Rahasianya adalah: **Streamlit itu seru banget!**")

# Radio
color = st.radio("Pilih warna favorit Anda:", options=["Merah", "Hijau", "Biru"])
st.write(f"Warna favorit Anda adalah: **{color}**")

# Selectbox
fruit = st.selectbox("Pilih buah favorit Anda:", options=["Apel", "Pisang", "Jeruk"])
st.write(f"Buah favorit Anda adalah: **{fruit}**")

# Multiselect
hobbies = st.multiselect("Pilih hobi Anda:", options=["Membaca", "Olahraga", "Musik", "Gaming"])
st.write(f"Hobi Anda: **{', '.join(hobbies) if hobbies else 'Belum memilih'}**")

# Slider
rating = st.slider("Berikan rating aplikasi ini (1-10):", min_value=1, max_value=10, value=5)
st.write(f"Rating Anda: **{rating}**")

# Closing
st.markdown("### **Terima Kasih!** 🚀")
