"""
INDEX & MASTER GUIDE
Week 1: Data Acquisition & Validation
AlphaPulse - Portfolio Risk & Volatility Monitor
"""

# ============================================================================
# FILE STRUCTURE & WHAT EACH FILE DOES
# ============================================================================

PROJECT_FILES_GUIDE = """
PROJECT DIRECTORY STRUCTURE
════════════════════════════════════════════════════════════════════════════

📁 Financial Analytics - Portfolio Risk & Volatility Monitor/
│
├── 📄 week1_quickstart.py
│   ├─ PURPOSE: Interactive menu-driven interface
│   ├─ RUN: python week1_quickstart.py
│   ├─ OPTIONS: 
│   │  1. Run full pipeline
│   │  2. Run analysis
│   │  3. View configuration
│   │  4. Generate report
│   └─ BEST FOR: First-time users, quick execution
│
├── 📄 week1_data_acquisition.py ⭐ MAIN SCRIPT
│   ├─ PURPOSE: Core data pipeline
│   ├─ CLASS: DataAcquisitionPipeline
│   ├─ METHODS:
│   │  • load_data() - Load CSV files
│   │  • inspect_data_structure() - Examine data
│   │  • handle_missing_data() - Forward-fill strategy
│   │  • validate_date_format() - Standardize dates
│   │  • validate_price_data() - Check anomalies
│   │  • calculate_daily_returns() - Compute returns
│   │  • detect_stock_splits_dividends() - Flag issues
│   │  • generate_validation_report() - Summary report
│   │  • save_cleaned_data() - Export processed files
│   ├─ OUTPUT:
│   │  processed_data/
│   │  ├── cleaned_data/
│   │  ├── daily_returns/
│   │  └── portfolio_daily_returns.csv
│   └─ RUN: python week1_data_acquisition.py
│
├── 📄 week1_analysis_notebook.py
│   ├─ PURPOSE: Deep analysis of processed data
│   ├─ CLASSES:
│   │  • PortfolioAnalyzer - Risk metrics & correlations
│   ├─ OUTPUTS:
│   │  • Risk metrics per stock
│   │  • Data quality assessment
│   │  • Correlation analysis
│   │  • Visualizations
│   ├─ REQUIRES: Pipeline to be run first
│   └─ RUN: python week1_analysis_notebook.py
│
├── 📄 config.py
│   ├─ PURPOSE: Configuration & metadata
│   ├─ CONTAINS:
│   │  • Portal composition (50+ stocks)
│   │  • Sector allocation
│   │  • Validation rules
│   │  • Statistical thresholds
│   │  • Simulation parameters
│   │  • File paths
│   ├─ FUNCTIONS:
│   │  • get_all_tickers()
│   │  • get_sector_stocks(sector)
│   │  • get_stock_info(ticker)
│   │  • save_config_as_json()
│   └─ RUN: python config.py (to print summary)
│
└── 📄 WEEK1_README.md
    ├─ PURPOSE: Comprehensive documentation
    ├─ SECTIONS:
    │  • Overview & objectives
    │  • Deliverables checklist
    │  • Dataset information
    │  • Implementation details
    │  • Usage instructions
    │  • Output file formats
    │  • Key metrics explained
    │  • Troubleshooting guide
    └─ FORMAT: Markdown (read in any text editor)

════════════════════════════════════════════════════════════════════════════
"""

# ============================================================================
# QUICK START PATHS
# ============================================================================

QUICK_START = """
🚀 QUICK START (5 MINUTES)
════════════════════════════════════════════════════════════════════════════

1. OPTION A: Interactive Menu (RECOMMENDED FOR BEGINNERS)
   
   > python week1_quickstart.py
   
   Then select option 1 to run pipeline
   Sit back and watch the magic happen! ✨

2. OPTION B: Command Line (RECOMMENDED FOR POWER USERS)
   
   > python week1_data_acquisition.py
   
   Runs pipeline immediately with detailed output

3. OPTION C: Custom Script
   
   from week1_data_acquisition import DataAcquisitionPipeline
   
   pipeline = DataAcquisitionPipeline(r"c:\path\to\data")
   pipeline.run_full_pipeline()

════════════════════════════════════════════════════════════════════════════
"""

# ============================================================================
# EXECUTION FLOW
# ============================================================================

EXECUTION_FLOW = """
📊 DATA PIPELINE EXECUTION FLOW
════════════════════════════════════════════════════════════════════════════

INPUT: CSV Files in c:\Users\mohum\Downloads\archive (3)\
├─ HCLTECH.csv
├─ HDFC.csv
├─ HDFCBANK.csv
├─ HEROMOTOCO.csv
├─ ... (50+ stock files)
└─ NIFTY50_all.csv

                        ↓ PIPELINE STARTS ↓

STEP 1: DATA LOADING
├─ Read all CSV files
├─ Parse columns: Date, Open, High, Low, Close, Volume, Adj Close
├─ Store in memory as pandas DataFrames
└─ Count: 50+ datasets loaded ✓

STEP 2: STRUCTURE INSPECTION
├─ Examine first dataset
├─ Display columns, dtypes, sample data
├─ Show basic statistics
└─ Understand data layout

STEP 3: MISSING DATA HANDLING
├─ Identify NaN values
├─ Apply forward-fill method (ffill)
├─ Backfill remaining NaN (bfill)
├─ Report: X values imputed, Y rows retained
└─ Clean data preserved ✓

STEP 4: DATE VALIDATION
├─ Convert strings to datetime
├─ Verify format: YYYY-MM-DD
├─ Sort by date chronologically
├─ Display date range per stock
└─ Temporal order ensured ✓

STEP 5: PRICE VALIDATION
├─ Check for negative prices → Flag if found
├─ Check for zero prices → Check if ex-dividend
├─ Verify: High ≥ Close ≥ Low
├─ Verify: High ≥ Open ≥ Low
└─ Data integrity validated ✓

STEP 6: CALCULATE DAILY RETURNS
├─ Formula: (Close_t - Close_t-1) / Close_t-1 × 100%
├─ Calculate for each stock
├─ Remove first NaN row (no previous price)
├─ Statistics: Mean, Std Dev, Min, Max
└─ Returns calculated ✓

STEP 7: ANOMALY DETECTION
├─ Find price changes > ±20% (stock split indicator)
├─ Find price changes > ±15% (potential dividend)
├─ Log with date and percentage
├─ Flag for manual review
└─ Anomalies documented ✓

STEP 8: VALIDATION REPORT
├─ Portfolio composition (50+ stocks)
├─ Date coverage statistics
├─ Data completeness metrics
├─ Risk classification
├─ Summary statistics
└─ Report generated ✓

STEP 9: SAVE PROCESSED DATA
├─ Save cleaned data: processed_data/cleaned_data/{TICKER}_cleaned.csv
├─ Save daily returns: processed_data/daily_returns/{TICKER}_returns.csv
├─ Save consolidated: processed_data/portfolio_daily_returns.csv
├─ Create backup copies
└─ All outputs saved ✓

                        ↓ PIPELINE COMPLETE ↓

OUTPUT: Processed Data Files
├─ processed_data/
│  ├─ cleaned_data/
│  │  ├─ HCLTECH_cleaned.csv
│  │  ├─ HDFC_cleaned.csv
│  │  └─ ... (50+ files)
│  ├─ daily_returns/
│  │  ├─ HCLTECH_returns.csv
│  │  ├─ HDFC_returns.csv
│  │  └─ ... (50+ files)
│  ├─ portfolio_daily_returns.csv ⭐ Master file for analysis
│  └─ data_validation_report.txt
│
└─ visualizations/
   ├─ returns_distribution.png
   ├─ correlation_heatmap.png
   └─ ... (additional plots)

════════════════════════════════════════════════════════════════════════════
"""

# ============================================================================
# EXAMPLE OUTPUT
# ============================================================================

EXAMPLE_OUTPUT = """
📈 EXAMPLE OUTPUT FROM PIPELINE
════════════════════════════════════════════════════════════════════════════

============================================================================
STEP 1: DATA LOADING
============================================================================
Found 51 CSV files
✓ Loaded HCLTECH: 2500 rows × 7 columns
✓ Loaded HDFC: 2500 rows × 7 columns
✓ Loaded HDFCBANK: 2500 rows × 7 columns
... (47 more files)
Successfully loaded 51 datasets

============================================================================
STEP 3: HANDLING MISSING DATA
============================================================================
✓ HCLTECH: No missing values found
✓ HDFC: 5 missing values → 0 (Forward Fill)
✓ HDFCBANK: 2 missing values → 0 (Forward Fill)

============================================================================
STEP 6: CALCULATE DAILY RETURNS
============================================================================
✓ HCLTECH:
  - Mean Daily Return:     0.0234%
  - Std Deviation:         2.3456%
  - Min Return:          -8.5234%
  - Max Return:           7.8923%

✓ HDFC:
  - Mean Daily Return:     0.0145%
  - Std Deviation:         1.9234%
  - Min Return:           -6.4532%
  - Max Return:            5.3421%

============================================================================
STEP 7: DETECT ANOMALIES (Stock Splits & Dividends)
============================================================================
⚠ HCLTECH: 1 anomalies detected
  - 2023-06-15: Price Change: -22.50% (Close: 450.25)
✓ HDFC: No anomalies detected
✓ HDFCBANK: No anomalies detected

============================================================================
STEP 8: DATA VALIDATION SUMMARY REPORT
============================================================================
Total Datasets Loaded: 51
Datasets After Cleaning: 51
Daily Returns Calculated: 51
Timestamp: 2026-02-25 14:32:15

Portfolio Composition (51 stocks):
  - ADANIPORTS
  - ASIANPAINT
  - AXISBANK
  ... and 48 more

Data Coverage:
  - Earliest Date: 2020-01-02
  - Latest Date:   2026-02-24
  - Span:          2234 days

════════════════════════════════════════════════════════════════════════════
"""

# ============================================================================
# DATA TYPES & FORMATS
# ============================================================================

DATA_SPECIFICATIONS = """
📊 DATA SPECIFICATIONS & FORMATS
════════════════════════════════════════════════════════════════════════════

INPUT CSV FORMAT (Original):
────────────────────────────────────────────────────────────────────────────
Date,Open,High,Low,Close,Volume,Adj Close
2023-12-01,1234.50,1245.20,1230.80,1242.00,2345678,1242.00
2023-12-04,1242.00,1255.30,1240.90,1250.00,2567890,1250.00
2023-12-05,1250.00,1253.20,1248.50,1252.00,1234567,1252.00

Column Definitions:
• Date:        Trading day (YYYY-MM-DD)
• Open:        Opening price (₹)
• High:        Highest price (₹)
• Low:         Lowest price (₹)
• Close:       Closing price (₹) ← Used for returns
• Volume:      Number of shares traded
• Adj Close:   Adjusted for dividends/splits (₹)

────────────────────────────────────────────────────────────────────────────

OUTPUT CLEANED DATA FORMAT:
────────────────────────────────────────────────────────────────────────────
Date,Open,High,Low,Close,Volume,Adjusted Close
2023-12-01,1234.50,1245.20,1230.80,1242.00,2345678,1242.00
2023-12-04,1242.00,1255.30,1240.90,1250.00,2567890,1250.00
2023-12-05,1250.00,1253.20,1248.50,1252.00,1234567,1252.00

✓ Date formatted & sorted
✓ Missing values filled
✓ Data validated
✓ Ready for analysis

────────────────────────────────────────────────────────────────────────────

OUTPUT RETURNS FORMAT:
────────────────────────────────────────────────────────────────────────────
Date,Daily_Return
2023-12-04,0.6469
2023-12-05,0.1600
2023-12-06,-0.2398

Calculation Example:
  Return = (1250.00 - 1242.00) / 1242.00 × 100% = 0.6469%

────────────────────────────────────────────────────────────────────────────

PORTFOLIO CONSOLIDATED RETURNS:
────────────────────────────────────────────────────────────────────────────
,HCLTECH,HDFC,HDFCBANK,HEROMOTOCO,HINDALCO,...
2023-12-04,0.6469,0.5234,0.3421,-0.1234,0.8765,...
2023-12-05,0.1600,-0.4234,0.5678,0.2341,-0.3421,...
2023-12-06,-0.2398,0.1234,-0.1234,0.6789,0.4321,...

• Index: Date
• Columns: Ticker symbols (50+ stocks)
• Values: Daily returns (%)
• Used for: Correlation, VaR, Monte Carlo simulations

════════════════════════════════════════════════════════════════════════════
"""

# ============================================================================
# KEY METRICS EXPLAINED
# ============================================================================

KEY_METRICS = """
📏 KEY METRICS EXPLAINED
════════════════════════════════════════════════════════════════════════════

1. DAILY RETURN
   ──────────────────────────────────────────────────────────────────────
   Definition: Percentage change in closing price
   Formula: R_t = (P_t - P_{t-1}) / P_{t-1} × 100%
   
   Example:
   • Yesterday's Close: ₹1000
   • Today's Close:     ₹1050
   • Daily Return:      (1050-1000)/1000 × 100% = 5.00%
   
   Use: Foundation for all risk calculations

2. VOLATILITY (STANDARD DEVIATION)
   ──────────────────────────────────────────────────────────────────────
   Definition: Measure of price variability
   Formula: σ = √(Σ(R_i - R̄)² / n)
   
   Classification:
   • Low:              0-1.5% (stable, less risk)
   • Medium:           1.5-3.0% (moderate)
   • High:             3.0-5.0% (risky)
   • Very High:        >5.0% (highly volatile)
   
   Use: Risk assessment, portfolio allocation

3. VALUE AT RISK (VaR)
   ──────────────────────────────────────────────────────────────────────
   Definition: Maximum expected loss at confidence level
   
   VaR(95%): Daily loss exceeds this with 5% probability
   VaR(99%): Daily loss exceeds this with 1% probability
   
   Example:
   • VaR(95%) = -2.50%: 95% chance loss won't exceed 2.50% per day
   • VaR(99%) = -4.20%: 99% chance loss won't exceed 4.20% per day
   
   Use: Risk management, position sizing

4. SKEWNESS
   ──────────────────────────────────────────────────────────────────────
   Definition: Asymmetry of return distribution
   
   Interpretation:
   • Negative (-): Left tail (large drops more likely)
   • Zero (0):    Symmetric distribution
   • Positive (+): Right tail (large gains more likely)
   
   Range: -3 to +3 (typical)
   
   Use: Understand downside/upside risk

5. KURTOSIS
   ──────────────────────────────────────────────────────────────────────
   Definition: Thickness of distribution tails
   
   Interpretation:
   • < 3:  Thin tails (smaller extreme events)
   • ≈ 3:  Normal distribution
   • > 3:  Fat tails (larger extreme events)
   
   Use: Tail risk assessment

6. CORRELATION
   ──────────────────────────────────────────────────────────────────────
   Definition: Co-movement between two stocks
   
   Range: -1 to +1
   • +1.0:  Perfect positive (move together)
   • +0.7:  Strong positive
   • +0.3:  Weak positive
   •  0.0:  No correlation
   • -0.3:  Weak negative
   • -0.7:  Strong negative
   • -1.0:  Perfect negative (opposite movement)
   
   Portfolio Implications:
   • Low correlation  → Better diversification ✓
   • High correlation → Redundant exposure ✗
   
   Use: Portfolio optimization, diversification

════════════════════════════════════════════════════════════════════════════
"""

# ============================================================================
# TROUBLESHOOTING
# ============================================================================

TROUBLESHOOTING = """
🔧 TROUBLESHOOTING GUIDE
════════════════════════════════════════════════════════════════════════════

ISSUE 1: "No CSV files found"
──────────────────────────────────────────────────────────────────────────
❌ Error:
   Error loading: No CSV files found in c:\path\to\data

✓ Solution:
   1. Verify path is correct
   2. Ensure files have .csv extension (lowercase)
   3. Check file permissions
   4. Update path in week1_data_acquisition.py:
      
      DATA_SOURCE_PATH = r"c:\correct\path"

────────────────────────────────────────────────────────────────────────────

ISSUE 2: "ModuleNotFoundError: No module named 'pandas'"
──────────────────────────────────────────────────────────────────────────
❌ Error:
   ModuleNotFoundError: No module named 'pandas'

✓ Solution:
   1. Install missing package:
      > pip install pandas numpy matplotlib seaborn
   
   2. Or install all at once:
      > pip install -r requirements.txt

────────────────────────────────────────────────────────────────────────────

ISSUE 3: "Date column not found"
──────────────────────────────────────────────────────────────────────────
❌ Error:
   Date column not found in dataset

✓ Solution:
   1. Check actual column names in CSV
   2. Update validate_date_format() method
   3. Common variations:
      - 'Date' vs 'date' vs 'DATE'
      - 'DateTime' vs 'Timestamp'

────────────────────────────────────────────────────────────────────────────

ISSUE 4: "Memory error / Slow execution"
──────────────────────────────────────────────────────────────────────────
❌ Error:
   MemoryError or very slow processing

✓ Solution:
   1. Close other applications
   2. Process files in batches (modify config.py)
   3. Reduce sample size for testing
   4. Use 64-bit Python if using 32-bit

────────────────────────────────────────────────────────────────────────────

ISSUE 5: "Negative prices detected"
──────────────────────────────────────────────────────────────────────────
❌ Error:
   ⚠ TICKER: {X} negative prices detected

✓ Solution:
   1. Check source data for errors
   2. Contact data provider
   3. Document in validation report
   4. Consider excluding from analysis

════════════════════════════════════════════════════════════════════════════
"""

# ============================================================================
# PRINTING GUIDE
# ============================================================================

def print_all_guides():
    """Print all guides"""
    print(PROJECT_FILES_GUIDE)
    print(QUICK_START)
    print(EXECUTION_FLOW)
    print(EXAMPLE_OUTPUT)
    print(DATA_SPECIFICATIONS)
    print(KEY_METRICS)
    print(TROUBLESHOOTING)

def print_section(section_name):
    """Print specific section"""
    sections = {
        'files': PROJECT_FILES_GUIDE,
        'quickstart': QUICK_START,
        'flow': EXECUTION_FLOW,
        'example': EXAMPLE_OUTPUT,
        'specs': DATA_SPECIFICATIONS,
        'metrics': KEY_METRICS,
        'troubleshoot': TROUBLESHOOTING,
    }
    
    if section_name.lower() in sections:
        print(sections[section_name.lower()])
    else:
        print("Available sections:")
        for key in sections.keys():
            print(f"  - {key}")

# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    import sys
    
    print("\n🎯 AlphaPulse - Week 1 Master Guide\n")
    
    if len(sys.argv) > 1:
        print_section(sys.argv[1])
    else:
        print("Usage: python index.py [section]")
        print("\nAvailable sections:")
        print("  - all         : Print all guides")
        print("  - files       : File structure guide")
        print("  - quickstart  : Quick start instructions")
        print("  - flow        : Pipeline execution flow")
        print("  - example     : Example output")
        print("  - specs       : Data specifications")
        print("  - metrics     : Key metrics explained")
        print("  - troubleshoot: Troubleshooting guide")
        print("\nExample: python index.py quickstart")
