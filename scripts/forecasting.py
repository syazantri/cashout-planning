import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt
import os

CLEANED_PATH = "./cleaned/investasi_pma_2024.csv"
OUTPUT_DIR = "./assets"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def load_and_prepare_data():
    df = pd.read_csv(CLEANED_PATH)

    for col in ["Triwulan I", "Triwulan II", "Triwulan III", "Triwulan IV"]:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    totals = df[["Triwulan I", "Triwulan II", "Triwulan III", "Triwulan IV"]].sum()
    totals.index = ["2024-Q1", "2024-Q2", "2024-Q3", "2024-Q4"]

    ts_df = pd.DataFrame({
        "ds": pd.to_datetime(totals.index, errors='coerce'),
        "y": totals.values
    })

    return ts_df


def run_forecast(df):
    model = Prophet(interval_width=0.95, seasonality_mode='additive')
    model.fit(df)

    future = model.make_future_dataframe(periods=4, freq='Q')
    forecast = model.predict(future)

    forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].to_csv(f"{OUTPUT_DIR}/forecast_investasi.csv", index=False)

    fig = model.plot(forecast)
    plt.title("Forecast Investasi PMA (Juta US$)")
    plt.xlabel("Quarter")
    plt.ylabel("Investasi")
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/forecast_investasi_plot.png")
    plt.show()

    return forecast

def main():
    ts_df = load_and_prepare_data()
    print("Time series data siap digunakan.")
    forecast = run_forecast(ts_df)
    print("Forecast selesai dan disimpan ke './assets/'")

if __name__ == "__main__":
    main()
