# Week 2: Quantitative Analysis & Correlation Study

## Overview

Week 2 implements advanced quantitative analysis and correlation studies for the AlphaPulse portfolio. This phase builds on the cleaned data produced by Week 1, focusing on:

- **Log Returns Calculation**: Transform daily price returns to logarithmic returns
- **Rolling Volatility**: 30-day moving standard deviation
- **Value at Risk (VaR)**: 95% confidence loss threshold using historical and Monte Carlo methods
- **Monte Carlo Simulation**: 10,000 scenarios over 252-day horizon
- **Statistical Sanity Checks**: Validate Monte Carlo results against historical performance
- **Correlation Analysis**: Identify diversification opportunities and stock clustering

## Quick Start

### Run Complete Week 2 Analysis
```bash
python week2_quickstart.py
```

Then select option 3: "RUN COMPLETE WEEK 2 (1 + 2)"

### Run Individual Components

**Quantitative Analysis Only:**
```bash
python week2_quantitative_analysis.py
```

**Correlation Analysis Only:**
```bash
python week2_correlation_analysis.py
```

## Key Metrics Explained

### Log Returns
- **Formula**: R_log = ln(1 + R_simple)
- **Purpose**: Linearizes returns for time-series analysis
- **Advantage**: Additive over time (whereas simple returns are multiplicative)

### Rolling Volatility
- **Window**: 30 trading days
- **Formula**: σ_30d = std(returns[-30:])
- **Usage**: Detect volatility clusters and risk regimes
- **Output**: 52 time series of rolling volatility

### Value at Risk (VaR) at 95% Confidence
- **Definition**: Maximum potential loss with 95% probability
- **Formula**: VaR(95%) = np.percentile(returns, 5)
- **Interpretation**: In 1 of 20 days (5% of time), loss exceeds this threshold
- **Two Methods**:
  - **Historical VaR**: Uses past 20 years of actual returns
  - **Monte Carlo VaR**: Uses 10,000 simulated future scenarios

### Monte Carlo Simulation
- **Model**: Geometric Brownian Motion (GBM)
- **Formula**: S(t+1) = S(t) * exp((μ - σ²/2) * dt + σ * dW)
- **Scenarios**: 10,000 independent simulations
- **Horizon**: 252 trading days (1 year)
- **Output**: Distribution of future portfolio values
- **Advantage**: Captures non-normal tail risks and fat tails

### Statistical Sanity Check
- **Purpose**: Verify Monte Carlo results match historical data
- **Validations**:
  - Mean return: Simulated ≈ Historical
  - Standard deviation: Simulated ≈ Historical
  - Skewness: Simulated ≈ Historical
  - Kurtosis: Simulated ≈ Historical
- **Tolerance**: ±10% difference is acceptable

### Correlation Analysis
- **Correlation Matrix**: 52×52 matrix of pairwise correlations
- **High Correlation (>0.7)**: Stocks move together (redundancy)
- **Low Correlation (<0.3)**: Diversification opportunity
- **Average Correlation**: Stock's diversification quality
- **Clusters**: Groups of correlated stocks (sector dynamics)

## Detailed Output Files

### Quantitative Analysis Outputs

**1. quantitative_summary.csv**
```
Stock,Mean_Log_Return,Rolling_Vol_AVG,Historical_VaR_95,MC_VaR_95,VaR_Difference_%
INFY,0.000523,0.0247,-0.0386,-0.0389,0.78
TCS,0.000891,0.0234,-0.0367,-0.0371,1.09
HDFC,0.000456,0.0289,-0.0451,-0.0448,-0.66
...
PORTFOLIO,-0.000012,0.0198,-0.0312,-0.0315,0.96
```

**2. week2_report.txt**
```
WEEK 2 QUANTITATIVE ANALYSIS REPORT
====================================

Portfolio Summary:
  Stocks Analyzed: 52
  Time Period: Jan 2000 - Apr 2021
  Trading Days: 7,788
  Avg Daily Return: 0.03%
  Avg Volatility: 2.5%

Value at Risk (95% Confidence):
  Historical VaR: -3.12%
  Monte Carlo VaR: -3.15%
  Difference: 0.96%

Monte Carlo Simulation Results:
  Scenarios: 10,000
  Time Horizon: 252 days (1 year)
  Mean Expected Return: 8.5%
  Std Dev (Year-Ahead): 12.3%
  VaR(95%): -15.2% (Potential 1-yr loss)

Statistical Sanity Checks: ✓ PASSED
  Mean difference: -0.12% (acceptable)
  Volatility difference: 1.45% (acceptable)
  Skewness difference: 0.08 (acceptable)
```

### Correlation Analysis Outputs

**3. correlation_matrix.csv**
```
Ticker,INFY,TCS,HDFC,ICICI,RELIANCE,...
INFY,1.000,0.754,0.423,0.512,0.238,...
TCS,0.754,1.000,0.389,0.498,0.201,...
HDFC,0.423,0.389,1.000,0.745,0.512,...
ICICI,0.512,0.498,0.745,1.000,0.487,...
...
```

**4. correlation_analysis.txt**
```
CORRELATION ANALYSIS REPORT
============================

Portfolio Overview:
  Stocks: 52
  Average Correlation: 0.421
  Correlation Range: -0.156 to 0.892

High Correlation Pairs (r > 0.7):
  TCS ↔ INFY (0.754) - Tech sector co-movement
  ICICI ↔ HDFC (0.745) - Banking sector
  MARUTI ↔ AUTO (0.823) - Auto sector
  [13 similar pairs identified]

Low Correlation Pairs (r < 0.3):
  RELIANCE ↔ INFY (0.238) - Different sectors
  COALINDIA ↔ INFOTECH (0.156) - Weak linkage
  [22 similar pairs identified]

Stock Diversification Ranking:
  Best Diversifiers (lowest avg correlation):
    1. COALINDIA (0.251)
    2. RELIANCE (0.298)
    3. AUROPHARMA (0.312)
  
  Highest Correlation (potential redundancy):
    1. ICICIBANK (0.654)
    2. TATASTEEL (0.641)
    3. INFY (0.638)

Portfolio Metrics (Equal-Weighted):
  Mean Return: 0.0345% daily
  Volatility: 0.0198% daily (1.98% annualized assumed)
  Sharpe Ratio: 1.74
  Max Drawdown: -47.8%
```

**5. correlation_heatmap_full.png**
- 52×52 color grid showing all correlations
- Red: High correlation (>0.7)
- Yellow: Moderate correlation (0.4-0.7)
- Blue: Low correlation (<0.3)

**6. correlation_heatmap_sample.png**
- 10×10 subset heatmap (selected stocks)
- Better readability for presentation

## File Structure

```
Financial Analytics - Portfolio Risk & Volatility Monitor/
├── week2_quantitative_analysis.py          (Main analysis module)
├── week2_correlation_analysis.py           (Correlation study module)
├── week2_quickstart.py                     (Interactive menu)
├── WEEK2_README.md                         (This file)
│
└── processed_data/
    ├── cleaned_data/                        (52 cleaned CSV files)
    ├── daily_returns/                       (52 daily return CSV files)
    ├── portfolio_daily_returns.csv          (Consolidated return matrix)
    │
    └── week2_analysis/                      (Week 2 outputs)
        ├── quantitative_summary.csv
        ├── week2_report.txt
        ├── correlation_matrix.csv
        ├── correlation_analysis.txt
        └── visualizations/
            ├── correlation_heatmap_full.png
            └── correlation_heatmap_sample.png
```

## Computational Complexity

### Quantitative Analysis
- **Per Stock**: 
  - Log returns: O(n) where n = 7,788 days
  - Rolling volatility: O(n)
  - VaR calculation: O(n)
  - Total: ~0.5 seconds per stock
  
- **Monte Carlo**:
  - 52 stocks × 10,000 scenarios × 252 days
  - 131 million calculations
  - Duration: 2-3 minutes (vectorized NumPy)

### Correlation Analysis
- **Correlation Matrix**: O(52²) = 2,704 pairwise calculations
- **Cluster Identification**: O(52² ) for pair search
- **Heatmap Generation**: Matplotlib rendering
- **Total Duration**: 1-2 minutes

**Total Week 2 Runtime**: 4-7 minutes

## Dependencies

```python
import pandas as pd          # Data manipulation
import numpy as np           # Numerical calculations
import matplotlib.pyplot as plt  # Visualization
import seaborn as sns        # Enhanced heatmaps
from pathlib import Path     # File management
from scipy import stats      # Statistical functions
```

## Input Requirements

✓ Week 1 completion (all files must exist):
- `processed_data/daily_returns/` - 52 CSV files with daily log returns
- `processed_data/portfolio_daily_returns.csv` - Master portfolio return matrix
- `processed_data/cleaned_data/` - 52 cleaned price datasets

## Execution Notes

1. **First Run**: Takes 5-10 minutes (Monte Carlo simulations)
2. **Subsequent Runs**: Overwrites previous outputs
3. **No Parameters Needed**: Uses default values from config
4. **Error Handling**: Detailed error messages if files missing
5. **Progress Output**: Real-time step completion messages

## Validation Checks

Each component runs validation:

```
Quantitative Analysis Checks:
✓ Input data dimensions (52 × 7,788)
✓ Log returns range (-1 to +1): ISO-compliant
✓ Volatility positivity: All σ > 0
✓ VaR ordering: MC_VaR ≥ Historical_VaR
✓ Distribution normality: KS test p-value
✓ Sanity check thresholds: <10% deviation

Correlation Analysis Checks:
✓ Matrix symmetry: r[i,j] = r[j,i]
✓ Diagonal values: All = 1.0 (perfect self-correlation)
✓ Range validation: All r ∈ [-1, 1]
✓ Positive semi-definite: Eigenvalues ≥ 0
✓ File saves: All outputs written successfully
```

## Troubleshooting

**Problem**: "Week 1 data not found"
- **Solution**: Run Week 1 first: `python week1_data_acquisition.py`

**Problem**: "File not found" error for specific stock
- **Solution**: Verify file exists in `processed_data/daily_returns/`
- **Check**: `ls processed_data/daily_returns/ | wc -l` should show 52

**Problem**: Monte Carlo takes too long (>10 minutes)
- **Solution**: Reduce num_simulations to 5000 in code
- **Impact**: Slightly less accurate but 2x faster

**Problem**: Heatmap visualization fails
- **Solution**: Ensure matplotlib backend configured
- **Fix**: Add `import matplotlib; matplotlib.use('Agg')`

**Problem**: Correlation matrix shows NaN values
- **Solution**: Check for missing price gaps in Week 1 cleaned data
- **Verify**: Run Week 1 validation report

## Next Steps (Week 3 Preview)

Week 3 will use Week 2 outputs for:
- **Monte Carlo Stress Testing**: Market shock scenarios
- **Scenario Analysis**: Best/base/worst case outcomes
- **Drawdown Analysis**: Maximum recovery times
- **Risk Decomposition**: Factor contribution analysis

## Performance Tips

1. **Vectorization**: All loops use NumPy (not Python loops)
2. **Memory**: Uses generators for large matrices where possible
3. **Disk I/O**: Single read from portfolio returns matrix
4. **Caching**: Intermediate results stored in memory during execution
5. **Parallelization**: Can be extended with multiprocessing (not needed yet)

## Metrics Reference Library

### Finance Metrics
- **Log Return**: Continuous compounding return
- **Volatility (σ)**: Standard deviation of returns
- **Value at Risk**: Loss quantile at confidence level
- **Sharpe Ratio**: Return per unit of risk
- **Max Drawdown**: Largest peak-to-trough decline
- **Correlation**: -1 (opposite), 0 (independent), +1 (identical)

### Statistics Terms
- **Skewness**: Distribution asymmetry (0=symmetric)
- **Kurtosis**: Tail thickness relative to normal (3=normal)
- **Percentile**: Value below which X% of data falls
- **Mean**: Average value
- **Std Dev**: Spread around mean

## Contact & Issues

For issues or questions:
1. Check [SETUP_GUIDE.md](SETUP_GUIDE.md) for environment setup
2. Review [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) for architecture
3. Run diagnostics: `python week1_quickstart.py` → Option 5 (Check Config)

## File Versions

- **Current Release**: Week 2 Final
- **Last Updated**: 2024
- **Python Version**: 3.8+
- **Status**: Production Ready

---

**AlphaPulse © 2024**
*Building Tomorrow's Risk Intelligence Today*
