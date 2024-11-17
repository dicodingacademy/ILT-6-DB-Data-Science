import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Title
st.title("Latihan Dasar Streamlit")

# Header
st.header("1. Elemen Write")
st.write("Dengan `st.write()`, kita dapat menampilkan berbagai jenis output seperti teks, tabel, grafik, dan lainnya.")

# Subheader
st.subheader("2. Elemen Text")
st.text("Ini adalah teks sederhana menggunakan `st.text()`.")
st.markdown("Markdown: **Teks dengan gaya tebal** atau *miring*.")

# Caption
st.caption("Caption ini berguna untuk memberi deskripsi tambahan.")

# Code
st.code("""
# Ini adalah contoh kode Python
import streamlit as st
st.write("Hello, Streamlit!")
""", language="python")

# LaTeX
st.subheader("3. Elemen LaTeX")
st.latex(r"E = mc^2")

# Data Display
st.subheader("4. Elemen Data Display")
# Dataframe
data = pd.DataFrame(
    np.random.randn(10, 3),
    columns=["Kolom A", "Kolom B", "Kolom C"]
)
st.dataframe(data, width=700, height=300)  # Menampilkan dataframe interaktif

# Table
st.table(data.head())  # Menampilkan tabel statis

# JSON
st.json({"key1": "value1", "key2": "value2", "key3": "value3"})

# Metric
st.metric(label="Progress", value="75%", delta="+5%")

# Chart
st.subheader("5. Elemen Chart")
# Pyplot
fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [10, 20, 25, 30], marker="o", linestyle="-")
ax.set_title("Contoh Plot Matplotlib")
st.pyplot(fig)

# Closing
st.markdown("### **Selamat Belajar!** 🎉")