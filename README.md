# 🚌 RedBus Route Recommendation System

An intelligent travel assistant that suggests optimal bus routes across Indian states based on real-time data insights. This project combines web scraping, data preprocessing, and machine learning to simplify travel planning within India.

## 🚀 Features

- 📍 **State-wise Bus Route Data**  
  Get curated bus route details for states like Kerala, Rajasthan, Goa, and more.

- 🧠 **Smart Recommendations**  
  ML-powered suggestions based on origin-destination and regional data.

- 📊 **Interactive Visualizations**  
  Explore patterns and insights through Streamlit-based dashboards.

- 🧹 **Clean, Modular Code**  
  Built using Python, Pandas, and Scikit-learn in a clean project structure.

---

## 📂 Project Structure

RED_BUS_project/
│
├── Bus_details/ # Preprocessed bus route data (per state)
├── csv_files/ # Raw scraped CSV files
├── scraper.ipynb # Web scraping code for RedBus
├── bus_details.ipynb # Data cleaning and integration
├── EDA&Sql_integration.ipynb # Exploratory Data Analysis + SQL patterns
├── redbus_app.py # Streamlit app for route recommendation
├── Route_details.csv # Final route mapping
├── .gitignore # Ignore unnecessary files like .venv/
└── requirements.txt # Python dependencies