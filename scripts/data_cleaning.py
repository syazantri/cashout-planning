import pandas as pd
import os

CLEANED_DIR = "./cleaned"
os.makedirs(CLEANED_DIR, exist_ok=True)

def clean_investasi_pma():
    path = "./data/Realisasi_Investasi_Penanaman_Modal_Luar_Negeri_Triwulanan_Menurut_Negara_Jumlah_Investasi_2024.csv"
    df = pd.read_csv(path, skiprows=3)
    df.columns = ["Negara", "Triwulan I", "Triwulan II", "Triwulan III", "Triwulan IV", "Tahunan"]
    df.to_csv(f"{CLEANED_DIR}/investasi_pma_2024.csv", index=False)
    print("Cleaned: Investasi PMA")

def main():
    clean_investasi_pma()
    print("All files cleaned and saved to './cleaned/'")

if __name__ == "__main__":
    main()
