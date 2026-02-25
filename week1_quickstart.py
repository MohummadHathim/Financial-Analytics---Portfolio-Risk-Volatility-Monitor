"""
Quick Start Guide - Week 1 Data Pipeline
AlphaPulse: Financial Analytics - Portfolio Risk & Volatility Monitor
"""

# ============================================================================
# QUICK START GUIDE
# ============================================================================

r"""
This script provides a simplified, interactive way to run the Week 1 pipeline.

REQUIREMENTS:
- Python 3.8 or higher
- pandas, numpy, matplotlib, seaborn

SETUP:
1. Ensure CSV files are in: c:\Users\mohum\Downloads\archive (3)
2. Run this script from the project directory

EXECUTION:
python week1_quickstart.py
"""

import sys
import os
from pathlib import Path

def print_header():
    """Print project header"""
    print("\n" + "╔" + "=" * 68 + "╗")
    print("║" + " " * 10 + "AlphaPulse - Week 1 Quick Start Guide" + " " * 21 + "║")
    print("║" + " " * 5 + "Financial Analytics - Portfolio Risk & Volatility Monitor" + " " * 4 + "║")
    print("╚" + "=" * 68 + "╝")
    print()

def check_dependencies():
    """Check if required packages are installed"""
    print("Checking dependencies...")
    
    required_packages = {
        'pandas': 'Data manipulation',
        'numpy': 'Numerical computing',
        'matplotlib': 'Visualization',
        'seaborn': 'Statistical plots',
    }
    
    missing = []
    for package, description in required_packages.items():
        try:
            __import__(package)
            print(f"  ✓ {package:15} - {description}")
        except ImportError:
            print(f"  ✗ {package:15} - {description} [MISSING]")
            missing.append(package)
    
    if missing:
        print(f"\n⚠ Missing packages detected: {', '.join(missing)}")
        print("\nInstall with:")
        print(f"  pip install {' '.join(missing)}")
        return False
    
    print("\n✓ All dependencies satisfied\n")
    return True

def check_data_files():
    """Verify data files exist"""
    print("Checking data files...")
    
    data_path = Path(r"c:\Users\mohum\Downloads\archive (3)")
    
    if not data_path.exists():
        print(f"✗ Data directory not found: {data_path}")
        return False
    
    csv_files = list(data_path.glob("*.csv"))
    print(f"  ✓ Found {len(csv_files)} CSV files")
    
    if len(csv_files) < 30:
        print(f"  ⚠ Expected 50+ CSV files, found only {len(csv_files)}")
    
    return True

def show_pipeline_steps():
    """Display the pipeline workflow"""
    print("\nPipeline Workflow:")
    print("""
    ┌─────────────────────────────────────────────────────┐
    │ STEP 1: DATA LOADING                                │
    │ Load all CSV files from source directory            │
    └─────────────────────────────────────────────────────┘
                            ↓
    ┌─────────────────────────────────────────────────────┐
    │ STEP 2: STRUCTURE INSPECTION                        │
    │ Examine columns, data types, sample records         │
    └─────────────────────────────────────────────────────┘
                            ↓
    ┌─────────────────────────────────────────────────────┐
    │ STEP 3: MISSING DATA HANDLING                       │
    │ Apply forward-fill strategy for missing values      │
    └─────────────────────────────────────────────────────┘
                            ↓
    ┌─────────────────────────────────────────────────────┐
    │ STEP 4: DATE VALIDATION                            │
    │ Standardize date formats and sort chronologically   │
    └─────────────────────────────────────────────────────┘
                            ↓
    ┌─────────────────────────────────────────────────────┐
    │ STEP 5: PRICE VALIDATION                           │
    │ Check for negative prices, anomalies               │
    └─────────────────────────────────────────────────────┘
                            ↓
    ┌─────────────────────────────────────────────────────┐
    │ STEP 6: CALCULATE RETURNS                          │
    │ Compute daily percentage returns                    │
    └─────────────────────────────────────────────────────┘
                            ↓
    ┌─────────────────────────────────────────────────────┐
    │ STEP 7: ANOMALY DETECTION                          │
    │ Flag potential stock splits & corporate actions    │
    └─────────────────────────────────────────────────────┘
                            ↓
    ┌─────────────────────────────────────────────────────┐
    │ STEP 8: VALIDATION REPORT                          │
    │ Generate comprehensive summary statistics          │
    └─────────────────────────────────────────────────────┘
                            ↓
    ┌─────────────────────────────────────────────────────┐
    │ STEP 9: SAVE DATA                                  │
    │ Export cleaned and processed files                  │
    └─────────────────────────────────────────────────────┘
    """)

def show_menu():
    """Display interactive menu"""
    print("\n" + "=" * 70)
    print("SELECT OPERATION")
    print("=" * 70)
    print("""
  1. Run Full Data Pipeline
     - Executes all 9 steps of data acquisition and validation
     - Generates processed data in processed_data/ directory
     - Duration: 2-5 minutes
    
  2. Run Detailed Analysis (requires pipeline execution first)
     - Calculate risk metrics
     - Data quality assessment
     - Correlation analysis
     - Generate visualizations
     - Duration: 1-2 minutes
    
  3. View Configuration
     - Display portfolio composition
     - Show sector allocation
     - List all stocks
    
  4. Generate Summary Report
     - Statistical overview
     - Data quality metrics
     - Risk classification
    
  5. Exit
    """)

def run_pipeline():
    """Execute the data acquisition pipeline"""
    print("\nStarting data acquisition pipeline...")
    print("This may take a few minutes depending on your system...\n")
    
    try:
        from week1_data_acquisition import DataAcquisitionPipeline
        
        data_source = r"c:\Users\mohum\Downloads\archive (3)"
        pipeline = DataAcquisitionPipeline(data_source)
        success = pipeline.run_full_pipeline()
        
        if success:
            print("\n✓ Pipeline execution SUCCESSFUL")
            print(f"\nOutput Location:")
            print(f"  {Path.cwd()}/processed_data/")
            return True
        else:
            print("\n✗ Pipeline execution FAILED")
            return False
            
    except ImportError as e:
        print(f"\n✗ Error importing pipeline module: {e}")
        print("Make sure week1_data_acquisition.py is in the project directory")
        return False
    except Exception as e:
        print(f"\n✗ Error during pipeline execution: {e}")
        return False

def run_analysis():
    """Execute the detailed analysis"""
    print("\nStarting detailed analysis...")
    print("This requires the pipeline to have been run first...\n")
    
    try:
        from week1_analysis_notebook import PortfolioAnalyzer, create_summary_visualizations
        import pandas as pd
        
        data_dir = r"c:\Users\mohum\OneDrive\Desktop\Financial Analytics - Portfolio Risk & Volatility Monitor\processed_data"
        
        analyzer = PortfolioAnalyzer(
            cleaned_data_dir=f"{data_dir}/cleaned_data",
            returns_data_dir=f"{data_dir}/daily_returns"
        )
        
        analyzer.load_processed_data()
        analyzer.calculate_risk_metrics()
        analyzer.analyze_data_quality()
        analyzer.correlation_analysis()
        analyzer.temporal_analysis()
        
        # Try to generate visualizations
        if analyzer.portfolio_returns is not None:
            create_summary_visualizations(analyzer.portfolio_returns)
            print("\n✓ Visualizations generated in visualizations/ directory")
        
        print("\n✓ Analysis COMPLETE")
        return True
        
    except FileNotFoundError as e:
        print(f"\n✗ Error: {e}")
        print("Please run the data pipeline first (Option 1)")
        return False
    except Exception as e:
        print(f"\n✗ Error during analysis: {e}")
        return False

def show_config():
    """Display configuration information"""
    try:
        from config import (
            STOCKS, SECTOR_ALLOCATION, PORTFOLIO_CONFIG, 
            print_portfolio_summary, get_all_tickers
        )
        
        print("\n" + "=" * 70)
        print("PORTFOLIO CONFIGURATION")
        print("=" * 70)
        print(f"\nProduct: {PORTFOLIO_CONFIG['product_brand']}")
        print(f"Project: {PORTFOLIO_CONFIG['project_name']}")
        print(f"Phase: {PORTFOLIO_CONFIG['phase']}")
        
        tickers = get_all_tickers()
        print(f"\nTotal Stocks: {len(tickers)}")
        
        print("\nSector Allocation:")
        for sector, allocation in SECTOR_ALLOCATION.items():
            bar_length = int(allocation * 50)
            bar = "█" * bar_length
            print(f"  {sector:40} {bar:<50} {allocation*100:>5.1f}%")
        
        print("\nAll Tickers:")
        for i, ticker in enumerate(tickers, 1):
            print(f"  {ticker:15}", end="")
            if i % 4 == 0:
                print()
        if len(tickers) % 4 != 0:
            print()
            
    except ImportError:
        print("\n✗ Could not load configuration module")

def generate_report():
    """Generate a summary report"""
    print("\n" + "=" * 70)
    print("WEEK 1 SUMMARY REPORT")
    print("=" * 70)
    
    print("""
PROJECT OBJECTIVES:
✓ Data Acquisition from CSV files
✓ Data cleaning (missing values, formatting)
✓ Data validation (price checks, anomalies)
✓ Daily returns calculation
✓ Corporate action detection
✓ Comprehensive validation report

KEY METRICS GENERATED:
• Daily returns (%)
• Volatility (standard deviation)
• Value at Risk (VaR) at 95% and 99% confidence
• Skewness and Kurtosis
• Correlation between stocks
• Data completeness metrics

OUTPUT FILES:
• processed_data/cleaned_data/*.csv
• processed_data/daily_returns/*.csv
• processed_data/portfolio_daily_returns.csv
• All visualizations in visualizations/

NEXT STEPS (Week 2-4):
1. Rolling volatility calculations
2. Correlation heatmaps
3. Monte Carlo simulations
4. Stress testing & scenario analysis

TECHNOLOGY STACK:
• Python 3.8+
• Pandas for data manipulation
• NumPy for numerical operations
• Matplotlib/Seaborn for visualization
    """)
    print("=" * 70)

def main():
    """Main program flow"""
    print_header()
    
    # Check dependencies
    if not check_dependencies():
        print("\n⚠ Install dependencies and retry")
        return
    
    # Check data files
    if not check_data_files():
        print("\n⚠ Please verify data file location")
        return
    
    print()
    show_pipeline_steps()
    
    # Main loop
    while True:
        show_menu()
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == '1':
            run_pipeline()
        elif choice == '2':
            run_analysis()
        elif choice == '3':
            show_config()
        elif choice == '4':
            generate_report()
        elif choice == '5':
            print("\n✓ Exiting AlphaPulse Quick Start Guide")
            print("Thank you for using AlphaPulse!\n")
            break
        else:
            print("\n✗ Invalid choice. Please enter 1-5")

# ============================================================================
# EXECUTION
# ============================================================================

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n✗ Program interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}")
        sys.exit(1)
