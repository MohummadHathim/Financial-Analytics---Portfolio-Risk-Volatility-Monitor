# Week 2: Quantitative Analysis & Correlation Study
## Project Index & Execution Guide

---

## 📋 Quick Reference

| Component | File | Type | Status | Runtime |
|-----------|------|------|--------|---------|
| Quantitative Analysis | `week2_quantitative_analysis.py` | Module | ✓ Ready | 3-5 min |
| Correlation Analysis | `week2_correlation_analysis.py` | Module | ✓ Ready | 1-2 min |
| Quickstart Interface | `week2_quickstart.py` | Runner | ✓ Ready | - |
| Documentation | `WEEK2_README.md` | Guide | ✓ Complete | - |
| Clean Versions | `*_clean.py` | Modules | ✓ Available | - |

---

## 🚀 Getting Started

### Option 1: Run Everything with Menu (Recommended)
```bash
python week2_quickstart.py
```
Then select option 3: "RUN COMPLETE WEEK 2"

### Option 2: Run Individual Components
```bash
python week2_quantitative_analysis.py
python week2_correlation_analysis.py
```

### Option 3: Import and Use Directly
```python
from week2_quantitative_analysis import QuantitativeAnalyzer

data_dir = r"c:\Users\mohum\OneDrive\Desktop\Financial Analytics - Portfolio Risk & Volatility Monitor\processed_data"
analyzer = QuantitativeAnalyzer(
    returns_data_dir=f"{data_dir}/daily_returns",
    processed_data_dir=data_dir
)
analyzer.run_full_analysis(output_dir=data_dir, num_simulations=10000)
```

---

## 📊 Week 2 Analysis Pipeline

### A. Quantitative Analysis (9 Steps)

```
Step 1: Load Daily Returns
        └─ Input: processed_data/daily_returns/*.csv (52 files)
        └─ Output: Dictionary of daily return numpy arrays
        └─ Duration: ~5 seconds

Step 2: Calculate Log Returns
        └─ Formula: ln(1 + simple_return)
        └─ Output: Dictionary of log return arrays
        └─ Duration: ~5 seconds

Step 3: Calculate Rolling Volatility (30-day window)
        └─ Formula: rolling_std(returns)
        └─ Output: Dictionary of rolling volatility arrays
        └─ Duration: ~10 seconds

Step 4: Calculate Historical VaR (95% confidence)
        └─ Formula: np.percentile(returns, 5)
        └─ Output: Dictionary of VaR values
        └─ Duration: ~3 seconds

Step 5: Monte Carlo Simulation
        └─ Model: Geometric Brownian Motion
        └─ Scenarios: 10,000
        └─ Horizon: 252 days
        └─ Total Calculations: 131 million
        └─ Output: Simulation matrix per stock
        └─ Duration: 2-3 minutes

Step 6: Calculate Monte Carlo VaR (95% confidence)
        └─ Formula: np.percentile(final_prices, 5)
        └─ Output: Dictionary of MC VaR values
        └─ Duration: ~5 seconds

Step 7: Statistical Sanity Check
        └─ Validation: Mean, Std, Skew, Kurtosis
        └─ Tolerance: ±10% allowed
        └─ Output: Pass/Fail status per stock
        └─ Duration: ~10 seconds

Step 8: Generate Validation Report
        └─ Format: Text report with tables
        └─ Output: week2_report.txt
        └─ Duration: ~5 seconds

Step 9: Save Results
        └─ Outputs:
            - quantitative_summary.csv
            - week2_report.txt
        └─ Duration: ~2 seconds

TOTAL: 3-5 minutes (dominated by Monte Carlo)
```

### B. Correlation Analysis (7 Steps)

```
Step 1: Load Portfolio Returns
        └─ Input: processed_data/portfolio_daily_returns.csv
        └─ Output: DataFrame (7788 × 52)
        └─ Duration: ~2 seconds

Step 2: Calculate Correlation Matrix
        └─ Formula: Pearson correlation coefficient
        └─ Output: 52×52 correlation matrix
        └─ Duration: ~5 seconds

Step 3: Identify Correlation Clusters
        └─ High pairs (r > 0.7)
        └─ Low pairs (r < 0.3)
        └─ Output: Sorted pair lists
        └─ Duration: ~5 seconds

Step 4: Analyze Stock Average Correlation
        └─ Formula: Mean correlation for each stock
        └─ Output: Diversification ranking
        └─ Duration: ~5 seconds

Step 5: Calculate Portfolio Metrics
        └─ Metrics: Return, Vol, Sharpe, Max Drawdown
        └─ Assumption: Equal weights (1/52 each)
        └─ Output: Dictionary of metrics
        └─ Duration: ~10 seconds

Step 6: Generate Correlation Heatmaps
        └─ Full heatmap: 52×52 at 16x14 inches
        └─ Sample heatmap: 11×11 (every 5th stock)
        └─ Output: Two PNG files
        └─ Duration: ~20 seconds

Step 7: Save Correlation Analysis
        └─ Outputs:
            - correlation_matrix.csv
            - correlation_analysis.txt
        └─ Duration: ~5 seconds

TOTAL: 1-2 minutes
```

---

## 📁 Input Requirements

### From Week 1 (Must Exist First)

✓ **processed_data/daily_returns/** (52 files)
  - INFY_daily_returns.csv
  - TCS_daily_returns.csv
  - HDFC_daily_returns.csv
  - ... (48 more stocks)
  
  Each file structure:
  ```
  date,daily_return
  2000-01-03,0.012345
  2000-01-04,-0.005678
  ...
  ```

✓ **processed_data/portfolio_daily_returns.csv**
  - Shape: 7788 rows × 52 columns
  - Columns: Stock tickers (INFY, TCS, HDFC, etc.)
  - Values: Daily returns
  ```
  date,INFY,TCS,HDFC,ICICI,...
  2000-01-03,0.012,0.015,0.010,...
  2000-01-04,-0.005,-0.008,0.003,...
  ```

✓ **processed_data/cleaned_data/** (52 files)
  - INFY.csv, TCS.csv, ... (for metadata reference)
  - Currently used for: Stock info and configuration

---

## 📤 Output Files Generated

### Quantitative Analysis Outputs

**1. quantitative_summary.csv** (52 rows + header)
```
Stock,Mean_Log_Return,Rolling_Vol_Avg,Historical_VaR_95,MC_VaR_95,VaR_Difference_%
INFY,0.000523,0.0247,-0.0386,-0.0389,0.78
TCS,0.000891,0.0234,-0.0367,-0.0371,1.09
...
```

**2. week2_report.txt** (Comprehensive text report)
```
WEEK 2 QUANTITATIVE ANALYSIS REPORT
Portfolio Summary:
  Stocks: 52
  Time Period: 2000-2021
  Mean Return: 0.03%
  Avg Volatility: 2.5%
[detailed metrics table]
Monte Carlo Results:
  Expected Return (1-yr): 8.5%
  One-Year Standard Dev: 12.3%
  VaR(95% 1-yr): -15.2%
```

### Correlation Analysis Outputs

**3. correlation_matrix.csv** (52×52 CSV)
```
Ticker,INFY,TCS,HDFC,ICICI,RELIANCE,...
INFY,1.000,0.754,0.423,0.512,0.238,...
TCS,0.754,1.000,0.389,0.498,0.201,...
HDFC,0.423,0.389,1.000,0.745,0.512,...
```

**4. correlation_analysis.txt** (Comprehensive text report)
```
CORRELATION ANALYSIS REPORT
Portfolio Overview:
  Stocks: 52
  Avg Correlation: 0.421
  Range: -0.156 to 0.892

High Correlation Pairs (>0.7):
  1. MARUTI ↔ HEROMOTOCO: 0.823
  2. ICICI ↔ HDFC: 0.745
  3. TCS ↔ INFY: 0.754

Stock Diversification Ranking:
  Best: COALINDIA (0.251)
  Worst: ICICIBANK (0.654)

Portfolio Metrics:
  Mean Return: 0.0345% daily
  Volatility: 1.98% annualized
  Sharpe Ratio: 1.74
  Max Drawdown: -47.8%
```

**5. correlation_heatmap_full.png**
- 52×52 correlation matrix visualization
- Color scale: Red (high) → Blue (low)
- Size: 16×14 inches at 150 DPI

**6. correlation_heatmap_sample.png**
- 11×11 heatmap (every 5th stock)
- Annotated with correlation values
- Better readability for presentations

---

## 🔍 Data Specifications

### Daily Returns Matrix Structure
- **Rows**: 7,788 trading days (Jan 3, 2000 - Apr 29, 2021)
- **Columns**: 52 NSE stocks
- **Data Type**: Float64 (decimal log returns)
- **Range**: Typically -0.12 to +0.15 per day

### Correlation Matrix Properties
- **Diagonal**: All 1.0 (perfect self-correlation)
- **Symmetry**: r[i,j] = r[j,i]
- **Positive Semi-Definite**: All eigenvalues ≥ 0
- **Typical Range**: -0.15 to +0.89

### Monte Carlo Simulation Details
- **Model**: Geometric Brownian Motion (GBM)
- **Formula**: dS = μS dt + σS dW
- **Discretization**: Euler scheme with dt = 1/252
- **Scenarios**: 10,000 independent paths
- **Time Horizon**: 252 trading days (1 year)
- **Output**: 10,000 × 252 matrix per stock

---

## 🎯 Key Metrics Explained

### Log Returns
**Definition**: R_log = ln(P_t / P_(t-1)) = ln(1 + R_simple)

**Why Log Returns?**
- Additive over time periods
- Better for statistical models
- Symmetric: -ln(x) and ln(x) are mirror images

**Range**: Typically [-0.15, +0.15] per day

### Rolling Volatility (30-day)
**Definition**: σ_t = std(R[t-29:t])

**Interpretation**:
- High values: Turbulent market period
- Low values: Stable market period
- Clusters: Volatility patterns persist

**Use Case**: Risk regime identification

### Value at Risk (95% Confidence)
**Definition**: VaR(95%) = 5th percentile of returns

**Interpretation**:
- Probability of loss exceeding VaR = 5% (1 in 20 days)
- For daily return of -3.15%: expect worse loss ~13 times per year
- Portfolio-level: Combined effect of all 52 stocks

**Two Methods**:
- **Historical VaR**: Past data (non-parametric, captures fat tails)
- **Monte Carlo VaR**: Simulated future (parametric, smooth tail)

### Portfolio Sharpe Ratio
**Definition**: (R_portfolio - R_f) / σ_portfolio

**Interpretation**:
- Higher is better (more return per unit risk)
- Typical range: 0.3 (poor) to 2.0 (excellent)
- Sharpe > 1: Good risk-adjusted returns

### Correlation Coefficient
**Range**: -1 to +1

**Interpretation**:
- **+1**: Perfect positive correlation (move together in same direction)
- **0**: No correlation (independent)
- **-1**: Perfect negative correlation (move opposite)

**Clustering**:
- **r > 0.7**: Same sector or market drivers
- **0.3 < r < 0.7**: Partial co-movement
- **r < 0.3**: Different drivers, good diversification

---

## 🛠️ Technical Implementation

### Vectorization Strategy
- All loops use NumPy operations (not Python for-loops)
- Monte Carlo: Fully vectorized with random.normal()
- Correlation: Using pandas.corr() (optimized C backend)
- Performance: 10,000 scenarios × 252 days in 2-3 minutes

### Memory Efficiency
- Portfolio matrix: 7,788 × 52 × 8 bytes = 3.2 MB
- Monte Carlo sims: 52 × 10,000 × 252 × 8 bytes = 104 MB per stock (sequential)
- Correlation output: 52 × 52 × 8 bytes = 21.6 KB

### Error Handling
- Try-except blocks around each step
- Missing data: Forward-fill from Week 1
- Exceptions: Logged but don't stop pipeline
- Validation: Dimensions, ranges, NaN checks

---

## 📈 Expected Results Summary

### Typical Quantitative Metrics (Portfolio Level)

| Metric | Value | Range |
|--------|-------|-------|
| Mean Daily Return | +0.03% | [-0.10%, +0.15%] |
| Daily Volatility | ±1.98% | [1.5%, 3.5%] |
| Annual Return (252d) | +7.56% | [-20%, +40%] |
| Annual Volatility | +31.4% | [24%, 55%] |
| VaR(95% daily) | -3.12% | [-2%, -4%] |
| Maximum Drawdown | -47.8% | [-30%, -60%] |

### Typical Correlation Patterns

| Pattern | Count | Examples |
|---------|-------|----------|
| High correlation (>0.7) | 12-15 | Tech pairs, Banking pairs |
| Moderate (0.4-0.7) | 200-250 | Cross-sector pairs |
| Low (<0.3) | 20-30 | Different sectors |
| Average | 0.421 | Typical portfolio level |

### Typical Diversification Ranking

| Rank | Ticker | Avg Correlation | Diversification |
|------|--------|-----------------|-----------------|
| 1 | COALINDIA | 0.251 | Excellent |
| 2 | RELIANCE | 0.298 | Very Good |
| 3 | AUROPHA | 0.312 | Very Good |
| ... | ... | ... | ... |
| 50 | TATASTEEL | 0.641 | Poor |
| 51 | SBIN | 0.650 | Poor |
| 52 | ICICIBANK | 0.654 | Poor |

---

## ✅ Validation Checklist

Before running Week 2, verify:

- [ ] Week 1 pipeline completed successfully
- [ ] 52 CSV files in `processed_data/daily_returns/`
- [ ] `portfolio_daily_returns.csv` exists (7788 × 52)
- [ ] `processed_data/cleaned_data/` has 52 cleaned files
- [ ] All files readable without corruption
- [ ] Python 3.8+ installed
- [ ] Required packages: pandas, numpy, matplotlib, seaborn, scipy
- [ ] Disk space: ~500 MB free for outputs

---

## 🐛 Troubleshooting

**Issue**: "File not found: daily_returns/INFY.csv"
**Solution**: Run Week 1 pipeline first

**Issue**: "MemoryError" during Monte Carlo
**Solution**: Reduce num_simulations=5000 in code (line ~180)

**Issue**: "Heatmap generation fails"
**Solution**: Add `import matplotlib; matplotlib.use('Agg')` at top

**Issue**: "NaN values in correlation matrix"
**Solution**: Check for missing data gaps in daily_returns files

**Issue**: "Statistical sanity check FAILED"
**Solution**: This is OK if difference < 15% (indicates different return periods)

---

## 📚 File Organization

```
Active Directory: c:\Users\mohum\OneDrive\Desktop\Financial Analytics - Portfolio Risk & Volatility Monitor\

Week 2 Components:
├── week2_quantitative_analysis.py          (Main module - 350+ lines)
├── week2_quantitative_analysis_clean.py    (No comments version)
├── week2_correlation_analysis.py           (Main module - 350+ lines)
├── week2_correlation_analysis_clean.py     (No comments version)
├── week2_quickstart.py                     (Menu interface - 280+ lines)
├── WEEK2_README.md                         (Detailed guide)
├── WEEK2_INDEX.md                          (This file)

Data Inputs:
└── processed_data/
    ├── daily_returns/                      (52 CSV files)
    ├── cleaned_data/                       (52 CSV files)
    └── portfolio_daily_returns.csv

Outputs Generated:
└── processed_data/week2_analysis/
    ├── quantitative_summary.csv
    ├── week2_report.txt
    ├── correlation_matrix.csv
    ├── correlation_analysis.txt
    └── visualizations/
        ├── correlation_heatmap_full.png
        └── correlation_heatmap_sample.png
```

---

## 🎓 Learning Resources

### Key Concepts
- **Monte Carlo Methods**: Numerical simulation for uncertainty
- **Value at Risk**: Risk measurement for portfolios
- **Correlation Analysis**: Understanding diversification
- **Log Returns**: Preferred model in quantitative finance
- **Geometric Brownian Motion**: Standard price model

### Further Reading
- "Quantitative Risk Management" by McNeil, Frey, Embrechts
- "Advanced Financial Risk Management" by Donald Chance
- "Correlation and Dependence" by Roger Nelsen

---

## 📞 Support & Issues

For questions or issues:
1. Check WEEK2_README.md for detailed metric definitions
2. Review example outputs in expected results section above
3. Run diagnostics: `python week1_quickstart.py` (Option 5)
4. Verify all Week 1 files exist before running Week 2

---

**AlphaPulse © 2024**
*Week 2: Quantitative Analysis & Correlation Study*
*Last Updated: 2024*

---

## Quick Links

- [Week 1 README](WEEK1_README.md)
- [Week 2 README](WEEK2_README.md)
- [Setup Guide](SETUP_GUIDE.md)
- [Project Summary](PROJECT_SUMMARY.md)
