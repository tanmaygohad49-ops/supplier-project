# Supplier Data Pipeline (B2B Data Engineering Project)

## Problem Statement
Businesses often need structured supplier and product data, but this data is usually scattered and unstructured on the web.

## Solution
This project builds an end-to-end data pipeline that:
- Scrapes supplier/product data from public sources
- Cleans and standardizes the data
- Stores it in structured format (CSV/JSON)
- Exposes it via a FastAPI REST API

## Tech Stack
- Python
- FastAPI
- Pandas
- Uvicorn

## Project Structure
- scraper/ → Web scraping scripts
- pipeline/ → Data cleaning scripts
- data_raw.json → Raw scraped data
- clean_data.csv → Cleaned dataset
- api.py → FastAPI server

## How to Run

### Install dependencies
pip install -r requirements.txt

### Run API
uvicorn api:app --reload

## API Endpoints
- GET / → API health check
- GET /products → Returns cleaned product data

## Output
Returns structured supplier/product data in JSON format for business use.
