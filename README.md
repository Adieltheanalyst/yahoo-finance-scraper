# Yahoo Finance Web Scraping Project

## Overview
This project automates the extraction of financial data from Yahoo Finance, focusing on different asset categories such as equities, ETFs, indexes, and mutual funds. The extracted data is saved in multiple formats, including JSON, CSV, and Excel, for further analysis and visualization.

## Features
- **Web Scraping**: Uses Python scripts to scrape financial data.
- **Data Processing**: Extracted data is structured and formatted into JSON, CSV, and Excel.
- **Multiple Asset Categories**: Supports Equities, ETFs, Indexes, and Mutual Funds.
- **Automated Execution**: Scripts efficiently fetch and convert data.

## Project Structure
```
project_root/
│── converted_files/            # Directory for output files
│   ├── equity_data.csv         # Equity data (CSV)
│   ├── equity_data.xlsx        # Equity data (Excel)
│   ├── index_data.csv          # Index data (CSV)
│   ├── index_data.xlsx         # Index data (Excel)
│   ├── mutual_funds_data.csv   # Mutual funds data (CSV)
│   ├── mutual_funds_data.xlsx  # Mutual funds data (Excel)
│   ├── refined_etf_data.csv    # ETF data (CSV)
│   ├── refined_etf_data.xlsx   # ETF data (Excel)
│   ├── equity_data.json        # Equity data (JSON)
│   ├── index_data.json         # Index data (JSON)
│   ├── mutual_funds_data.json  # Mutual funds data (JSON)
│   ├── refined_etf_data.json   # ETF data (JSON)
│── equity.py                   # Scraping script for equities
│── etfs.py                     # Scraping script for ETFs
│── index.py                    # Scraping script for indexes
│── mutual_funds.py             # Scraping script for mutual funds
│── scraping.py                 # Main script for handling scraping
│── .venv/                       # Virtual environment (optional)
```

## Installation & Usage
### Prerequisites
- Python 3.x
- Required libraries: `requests`, `BeautifulSoup`, `pandas`, `openpyxl`

### Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/yahoo-finance-scraper.git
   cd yahoo-finance-scraper
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

### Running the Scripts
To scrape data for a specific asset class, run the corresponding script. Example:
```sh
python equity.py
```
This will fetch and store the latest equity data in JSON, CSV, and Excel formats.

## Outputs
- JSON files for structured data storage.
- CSV and Excel files for easy data analysis and sharing.

## Future Improvements
- Expand scraping to include additional financial metrics.
- Implement real-time data fetching with scheduling.
- Add a GUI for user-friendly interactions.

## License
MIT License.

---

Feel free to update your GitHub repository with this README and let me know if you'd like any modifications! 🚀

