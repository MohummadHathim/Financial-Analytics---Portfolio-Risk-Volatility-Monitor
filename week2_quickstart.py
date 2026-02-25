import sys
from pathlib import Path

def print_header():
    print("\n" + "╔" + "=" * 68 + "╗")
    print("║" + " " * 10 + "AlphaPulse - Week 2 Analysis" + " " * 30 + "║")
    print("║" + " " * 5 + "Quantitative Analysis & Monte Carlo Simulation" + " " * 14 + "║")
    print("╚" + "=" * 68 + "╝")
    print()

def show_menu():
    print("\n" + "=" * 70)
    print("WEEK 2 ANALYSIS OPTIONS")
    print("=" * 70)
    print("""
  1. QUANTITATIVE ANALYSIS
     - Calculate log returns
     - 30-day rolling volatility
     - Historical Value at Risk (95%)
     - 10,000 Monte Carlo simulations
     - Statistical sanity checks
     Duration: 3-5 minutes
    
  2. CORRELATION ANALYSIS
     - Build correlation matrix
     - Partner cluster identification
     - Diversification opportunities
     - Portfolio metrics
     - Generate heatmaps
     Duration: 1-2 minutes
    
  3. RUN COMPLETE WEEK 2 (1 + 2)
     - Full quantitative analysis
     - Complete correlation study
     - All visualizations
     Duration: 4-7 minutes
    
  4. BACK TO MAIN MENU
    """)

def run_quantitative_analysis():
    print("\nStarting Quantitative Analysis...")
    print("This includes Monte Carlo simulations (may take a few minutes)...\n")
    
    try:
        from week2_quantitative_analysis import QuantitativeAnalyzer
        
        data_dir = r"c:\Users\mohum\OneDrive\Desktop\Financial Analytics - Portfolio Risk & Volatility Monitor\processed_data"
        
        analyzer = QuantitativeAnalyzer(
            returns_data_dir=f"{data_dir}/daily_returns",
            processed_data_dir=data_dir
        )
        
        analyzer.run_full_analysis(
            output_dir=data_dir,
            num_simulations=10000
        )
        
        print("✓ Quantitative Analysis COMPLETE")
        return True
        
    except Exception as e:
        print(f"✗ Error: {str(e)}")
        return False

def run_correlation_analysis():
    print("\nStarting Correlation Analysis...\n")
    
    try:
        from week2_correlation_analysis import PortfolioCorrelationAnalysis
        
        data_dir = r"c:\Users\mohum\OneDrive\Desktop\Financial Analytics - Portfolio Risk & Volatility Monitor\processed_data"
        
        analyzer = PortfolioCorrelationAnalysis(
            returns_file=f"{data_dir}/portfolio_daily_returns.csv",
            cleaned_data_dir=f"{data_dir}/cleaned_data"
        )
        
        analyzer.run_full_analysis(output_dir=data_dir)
        
        print("✓ Correlation Analysis COMPLETE")
        return True
        
    except Exception as e:
        print(f"✗ Error: {str(e)}")
        return False

def run_complete_week2_analysis():
    print("\nRunning COMPLETE Week 2 Analysis...")
    print("This will run both quantitative and correlation analysis.\n")
    
    print("=" * 70)
    print("Part 1: QUANTITATIVE ANALYSIS")
    print("=" * 70)
    
    quant_success = run_quantitative_analysis()
    
    if not quant_success:
        print("✗ Quantitative analysis failed")
        return False
    
    print("\n" + "=" * 70)
    print("Part 2: CORRELATION ANALYSIS")
    print("=" * 70)
    
    corr_success = run_correlation_analysis()
    
    if not corr_success:
        print("✗ Correlation analysis failed")
        return False
    
    print("\n" + "=" * 70)
    print("✓ WEEK 2 COMPLETE ANALYSIS FINISHED")
    print("=" * 70)
    
    print("\nGenerated Files:")
    print("  📊 Quantitative Metrics:")
    print("    - quantitative_summary.csv")
    print("    - week2_report.txt")
    print()
    print("  📈 Correlation Analysis:")
    print("    - correlation_matrix.csv")
    print("    - correlation_analysis.txt")
    print("    - correlation_heatmap_full.png")
    print("    - correlation_heatmap_sample.png")
    print()
    
    return True

def show_week2_info():
    print("\n" + "=" * 70)
    print("WEEK 2: QUANTITATIVE ANALYSIS & CORRELATION STUDY")
    print("=" * 70)
    
    info = """
DELIVERABLES:

1. QUANTITATIVE ANALYSIS
   ✓ Daily Log Returns Calculation
   ✓ Historical Volatility (30-day rolling)
   ✓ Value at Risk (95% confidence)
   ✓ Monte Carlo Simulation (10,000 scenarios)
   ✓ Statistical Sanity Checks
   
2. CORRELATION ANALYSIS
   ✓ Correlation Matrix (52 stocks)
   ✓ Stock Clustering (correlation groups)
   ✓ Diversification Opportunities
   ✓ Portfolio Metrics
   ✓ Heatmap Visualizations

KEY METRICS:
   • Log Returns: ln(1 + daily_return)
   • Rolling VOL: 30-day moving std deviation
   • VaR(95%): Loss threshold at 95% confidence
   • Monte Carlo: 252-day horizon, 10K simulations
   • Correlation: -1 to +1 (co-movement measure)
   
OUTPUT FILES:
   📁 processed_data/week2_analysis/
   ├── quantitative_summary.csv
   ├── week2_report.txt
   ├── correlation_matrix.csv
   ├── correlation_analysis.txt
   └── visualizations/
       ├── correlation_heatmap_full.png
       └── correlation_heatmap_sample.png
"""
    
    print(info)

def main():
    print_header()
    
    data_dir = Path(r"c:\Users\mohum\OneDrive\Desktop\Financial Analytics - Portfolio Risk & Volatility Monitor\processed_data")
    
    if not (data_dir / "daily_returns").exists():
        print("✗ Week 1 data not found!")
        print("Please run Week 1 pipeline first:")
        print("  python week1_data_acquisition.py")
        return
    
    print("✓ Week 1 data found")
    print(f"✓ Returns files: {len(list((data_dir / 'daily_returns').glob('*.csv')))}")
    print()
    
    show_week2_info()
    
    while True:
        show_menu()
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '1':
            run_quantitative_analysis()
        elif choice == '2':
            run_correlation_analysis()
        elif choice == '3':
            run_complete_week2_analysis()
        elif choice == '4':
            print("\n✓ Returning to main menu")
            break
        else:
            print("\n✗ Invalid choice. Please enter 1-4")
    
    print("\n✓ Week 2 Analysis Tool Closed")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n✗ Program interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ Error: {str(e)}")
        sys.exit(1)
