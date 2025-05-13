import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

forecast_df = pd.read_csv("./assets/forecast_investasi.csv")
raw_investasi = pd.read_csv("./cleaned/investasi_pma_2024.csv")

st.set_page_config(page_title="Cash Out Planning Dashboard", layout="centered")

st.title("💸 Cash Out Planning Dashboard")
st.markdown("Forecast dan simulasi strategi pengeluaran kas berdasarkan data investasi PMA 2024.")

st.subheader("📊 Forecast Investasi PMA (Juta US$)")

fig, ax = plt.subplots()
ax.plot(forecast_df["ds"], forecast_df["yhat"], label="Prediksi", marker='o')
ax.fill_between(forecast_df["ds"], forecast_df["yhat_lower"], forecast_df["yhat_upper"], color='gray', alpha=0.3, label="Confidence Interval")
ax.set_ylabel("Investasi (Juta US$)")
ax.set_xlabel("Waktu")
ax.set_title("Forecast Investasi Kuartalan")
ax.grid(True)
ax.legend()
st.pyplot(fig)

st.subheader("💡 Rekomendasi Strategi Pengeluaran")

st.markdown("""
- Kuartal dengan prediksi investasi **tinggi** → disarankan untuk **alokasi kas yang lebih besar** (ekspansi, pengadaan, dll).
- Kuartal dengan prediksi investasi **rendah** atau **ketidakpastian tinggi** → lebih baik **hemat kas** atau tunda belanja besar.
""")

st.write("📋 Tabel Forecast:")
st.dataframe(forecast_df[["ds", "yhat", "yhat_lower", "yhat_upper"]].rename(columns={
    "ds": "Kuartal",
    "yhat": "Prediksi Investasi",
    "yhat_lower": "Batas Bawah",
    "yhat_upper": "Batas Atas"
}))

st.subheader("🌍 Negara Penyumbang Investasi Tertinggi (2024)")
top_countries = raw_investasi.copy()
top_countries["Total"] = top_countries[["Triwulan I", "Triwulan II", "Triwulan III", "Triwulan IV"]].sum(axis=1)
top_5 = top_countries.sort_values("Total", ascending=False).head(5)

st.bar_chart(top_5.set_index("Negara")["Total"])

