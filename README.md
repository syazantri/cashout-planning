# 💸 - Cash Out Planning Simulation (using Indonesian Investment Data)

This project explores how quarterly foreign direct investment (FDI) data in Indonesia can provide insight into simple cash out planning scenarios. I used publicly available data to practice basic forecasting and simulate cash allocation across quarters using simple assumptions. The goal is to better understand how economic indicators might relate to financial planning through data analysis, visualization, and automation.

### 📌 - Project Goals

- Analyze foreign investment data to identify quarterly trends
- Forecast investment levels in the upcoming quarters
- Build a dashboard and simulation tool to recommend:
  - **When** major cash outflows should be executed
  - **How much** cash should be allocated per quarter

### 📊 - Data Source

Data was obtained from **Badan Pusat Statistik (BPS)**:

- 🗂️ [`Realisasi Investasi Penanaman Modal Asing 2024`](https://www.bps.go.id/id/statistics-table/2/MjM4NCMy/realisasi-investasi-penanaman-modal-luar-negeri-triwulanan-menurut-negara---jumlah-investasi--juta-us--.html)

### ⚙️ - Tools Used

- 📈 **Excel + VBA** for simulation dashboard and reporting
- 🐍 Python (Pandas, Prophet, Matplotlib) for data preprocessing and forecasting
- 🖥️ Streamlit for interactive visualization

### 🧠 - Features

- 📊 Time series forecast of quarterly FDI
- 📋 Simulation of cash out allocation based on percentage input
- 📁 Excel-based dashboard with VBA macro for report generation
- 📈 Streamlit dashboard with forecast and recommendations

### 📂 - Project Structure

- `/data`: Raw CSV data
- `/cleaned`: Cleaned CSV data for analysis
- `/scripts`: Python scripts for cleaning and forecasting
- `/dashboard`: Streamlit app and Excel dashboard
- `/assets`: Plots and forecast outputs
