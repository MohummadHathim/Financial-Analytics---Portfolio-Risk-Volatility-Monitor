# Week 1: Data Acquisition & Validation
## Financial Analytics - Portfolio Risk & Volatility Monitor (AlphaPulse)

---

## 📋 Overview
Week 1 focuses on the foundational stage of the portfolio risk analysis project. The primary objective is to **acquire, clean, validate, and prepare** historical stock data for subsequent advanced analysis phases (Monte Carlo simulations, correlation analysis, volatility calculations).

---

## 🎯 Week 1 Deliverables

### 1. **Data Acquisition** ✓
- Load 50+ NSE stocks historical data from CSV files
- Support multiple data formats and inconsistencies
- Portfolio covers diverse sectors: Technology, Healthcare, Finance, Energy, Consumer, etc.

### 2. **Data Cleaning Strategy** ✓
- **Missing Data Handling**: Forward-fill methodology to preserve temporal continuity
- **Outlier Detection**: Identify potential corporate actions (stock splits, dividends)
- **Data Type Standardization**: Ensure numeric consistency across all price columns
- **Duplicate Removal**: Eliminate redundant records

### 3. **Data Validation** ✓
- **Date Format Standardization**: Convert to ISO 8601 format (YYYY-MM-DD)
- **Price Data Validation**: Check for negative/zero prices, logical inconsistencies
- **Temporal Continuity**: Verify continuous trading records
- **Data Completeness**: Report coverage for each stock

### 4. **Daily Returns Calculation** ✓
- Formula: $R_t = \frac{P_t - P_{t-1}}{P_{t-1}} \times 100\%$
- Essential for risk metrics: volatility, VaR, correlation analysis
- Enables financial time-series analysis

### 5. **Data Integrity Report** ✓
- Summary statistics per stock
- Quality metrics: completeness, timeliness, accuracy
- Anomaly detection: identifies potential corporate actions

---

## 📦 Dataset Information

### Stocks Included (50+ stocks)
- **Tech & IT**: TCS, Infosys (INFY), Wipro, Tech Mahindra (TECHM)
- **Banking & Finance**: ICICIBANK, AXISBANK, HDFCBANK, SBIN, Kotak (KOTAKBANK)
- **Energy**: RELIANCE, ONGC, IOC, BPCL, GAIL
- **Heavy Industries**: Tata Steel (TATASTEEL), JSW Steel (JSWSTEEL), Hindalco (HINDALCO)
- **Consumer**: Maruti (MARUTI), Heromotoco (HEROMOTOCO), ITC, Britannia (BRITANNIA)
- **Healthcare**: Cipla (CIPLA), Dr. Reddy (DRREDDY), Sun Pharma (SUNPHARMA)
- **Automotive**: Eicher Motors (EICHERMOT), Bajaj Auto (BAJAJ-AUTO)
- **Index**: NIFTY50_all (benchmark)

### Data Characteristics
- **Time Period**: Multiple years of historical daily OHLCV data
- **Columns**: Open, High, Low, Close, Volume, Adjusted Close
- **Frequency**: Daily (trading days only)
- **Format**: CSV with standard financial data layout

---

## 🔧 Implementation Details

### Technology Stack
```
├── Python 3.8+
│   ├── pandas (Data manipulation & analysis)
│   ├── numpy (Vectorized operations)
│   ├── matplotlib (Basic visualization)
│   └── seaborn (Statistical plots)
└── File I/O (CSV format)
```

### Key Classes & Functions

#### `DataAcquisitionPipeline`
Main orchestrator class that manages the entire data pipeline:
- **Methods**:
  - `load_data()`: Load CSV files from directory
  - `inspect_data_structure()`: Display dataset characteristics
  - `handle_missing_data()`: Apply forward-fill or drop strategy
  - `validate_date_format()`: Standardize dates
  - `validate_price_data()`: Check for anomalies
  - `calculate_daily_returns()`: Compute percentage returns
  - `detect_stock_splits_dividends()`: Flag unusual price movements
  - `generate_validation_report()`: Create summary report
  - `save_cleaned_data()`: Export processed data

#### `PortfolioAnalyzer`
Secondary analysis class for deeper insights:
- Risk metric calculations (VaR, skewness, kurtosis)
- Data quality assessment
- Correlation structure analysis
- Temporal pattern identification

---

## 📊 Data Quality Metrics

### Completeness
- **Target**: 99%+ of trading days present
- **Validation**: Check for missing dates in trading calendar
- **Action**: Forward-fill for isolated missing days

### Accuracy
- **Negative Prices**: Should be 0
- **Zero Prices**: Acceptable only on ex-dividend dates
- **Price Logic**: High ≥ Close ≥ Low, High ≥ Open ≥ Low

### Consistency
- **Date Format**: Standardized to YYYY-MM-DD
- **Decimal Places**: 2 decimals for price, 6 for returns
- **Volume**: Should be positive integer

### Timeliness
- **Data Currency**: Latest trading day included
- **Update Frequency**: Daily after market close

---

## 🚀 Usage Instructions

### Step 1: Install Dependencies
```bash
pip install pandas numpy matplotlib seaborn
```

### Step 2: Run Data Acquisition Pipeline
```bash
python week1_data_acquisition.py
```

**Expected Output**:
- Processed 50+ CSV files
- Created cleaned datasets directory: `processed_data/cleaned_data/`
- Created daily returns directory: `processed_data/daily_returns/`
- Generated consolidated returns file: `portfolio_daily_returns.csv`
- Summary statistics and validation report

### Step 3: Run Detailed Analysis (Optional)
```bash
python week1_analysis_notebook.py
```

**Outputs**:
- Risk metrics per stock (mean, std dev, VaR)
- Data quality report
- Correlation analysis and insights
- Visualizations: distribution plots, correlation heatmap

---

## 📈 Output Files Structure

```
processed_data/
├── cleaned_data/
│   ├── HCLTECH_cleaned.csv
│   ├── HDFC_cleaned.csv
│   ├── HDFCBANK_cleaned.csv
│   └── ... (50+ files)
├── daily_returns/
│   ├── HCLTECH_returns.csv
│   ├── HDFC_returns.csv
│   ├── HDFCBANK_returns.csv
│   └── ... (50+ files)
├── portfolio_daily_returns.csv      # Master returns matrix
├── data_validation_report.txt
└── README.md
```

### File Formats

**Cleaned Data CSV**:
```
Date,Open,High,Low,Close,Volume,Adjusted Close
2023-01-02,100.50,101.20,99.80,101.00,1234567,101.00
2023-01-03,101.00,102.30,100.90,102.00,1567890,102.00
```

**Daily Returns CSV**:
```
Date,Daily_Return
2023-01-03,0.9901
2023-01-04,1.2345
```

**Portfolio Returns CSV** (consolidated):
```
,HCLTECH,HDFC,HDFCBANK,HEROMOTOCO,...
2023-01-03,0.9901,1.2345,0.8765,...
2023-01-04,1.2345,0.9876,1.1234,...
```

---

## 📊 Key Metrics Generated

### Per-Stock Metrics
- **Mean Daily Return** (%): Average daily percentage return
- **Volatility (Std Dev)** (%): Daily return standard deviation
- **Value at Risk (VaR)**:
  - 95% Confidence Level: Daily loss threshold at 95% confidence
  - 99% Confidence Level: Daily loss threshold at 99% confidence
- **Skewness**: Distribution asymmetry (-1.5 to +1.5 typical)
- **Kurtosis**: Distribution tail behavior (3 = normal, >3 = fat tails)

### Portfolio Metrics
- **Average Correlation**: How stocks move together on average
- **Correlation Range**: Min to max correlation pairs
- **Low Correlation Pairs**: Diversification opportunities (<0.3)
- **High Correlation Pairs**: Redundant exposure (>0.7)

### Data Quality Metrics
- **Completeness**: % of days with valid data
- **Duplicate Records**: Count of repeated entries
- **Missing Values**: Count and handling method applied
- **Date Coverage**: Earliest to latest date in dataset

---

## 🔍 Anomaly Detection & Corporate Actions

### Detection Thresholds
- **Stock Split Indicator**: Single-day price change > ±20%
- **Dividend Impact**: Often causes 1-3% price drops on ex-dividend date
- **Corporate Action**: Sharp unexpected price movements

### Detected Anomalies
```
⚠ STOCK_NAME: 3 anomalies detected
  - 2023-06-15: Price Change: -22.50% (Close: 450.25)
  - 2023-12-20: Price Change: +18.75% (Close: 520.00)
```

### Handling Strategy
- **Forward-fill**: Subsequent calculations adjusted by system
- **Documentation**: Anomalies logged for manual review
- **Normalization**: Optional adjustment in advanced phases

---

## ✅ Validation Checklist

- [ ] All 50+ CSV files successfully loaded
- [ ] Date columns converted to datetime format
- [ ] No negative prices in dataset
- [ ] Missing data handled via forward-fill
- [ ] Daily returns calculated correctly
- [ ] Correlation matrix generated properly
- [ ] All processed files saved successfully
- [ ] Validation report generated

---

## ⚠️ Known Limitations & Considerations

1. **Weekend/Holiday Data**: CSV files contain only trading days
2. **Adjusted Closing Prices**: Used for return calculations
3. **Corporate Actions**: Not automatically adjusted; flagged for review
4. **Survivorship Bias**: Only currently listed stocks included
5. **Data Frequency**: Limited to daily; intraday data not included

---

## 🔄 Next Steps (Week 2-4)

1. **Week 2**: Rolling Volatility & Moving Averages
   - Calculate 30-day moving standard deviation
   - Trend analysis and momentum indicators

2. **Week 3**: Correlation & Portfolio Structure
   - Build dynamic correlation matrices
   - Sector-level analysis

3. **Week 4**: Monte Carlo Simulation & VaR
   - Run 10,000+ simulations
   - Portfolio distribution forecasting
   - Stress testing scenarios

---

## 💡 Tips & Best Practices

### Data Validation
- Always verify date ranges before analysis
- Check for consistency between files
- Validate total records match expected trading days

### Performance Optimization
- Use vectorized operations (NumPy, Pandas) over loops
- Cache correlation matrices if recalculating frequently
- Consider sampling for very large datasets

### Error Handling
- Use try-except blocks for robust code
- Log errors with timestamps and file names
- Implement data backup before processing

---

## 📞 Troubleshooting

### Issue: "No CSV files found"
**Solution**: Verify path to data directory is correct and files have .csv extension

### Issue: "Date column not found"
**Solution**: Check column names - may be 'Date', 'date', 'DATE', or similar. Update code accordingly.

### Issue: "Memory error with large datasets"
**Solution**: Process files in batches or sample data for testing

### Issue: "Negative prices detected"
**Solution**: Manually review flagged stocks - likely data quality issue from source

---

## 📚 References & Resources

- **Pandas Documentation**: https://pandas.pydata.org/docs/
- **NumPy Guide**: https://numpy.org/doc/
- **Financial Statistics**: https://en.wikipedia.org/wiki/Financial_risk
- **Value at Risk**: https://en.wikipedia.org/wiki/Value_at_risk

---

**Project**: Financial Analytics - Portfolio Risk & Volatility Monitor  
**Phase**: Week 1 - Data Acquisition & Validation  
**Version**: 1.0  
**Last Updated**: February 2026
