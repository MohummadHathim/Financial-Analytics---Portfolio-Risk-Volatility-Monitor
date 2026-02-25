"""
Week 1 Data Acquisition & Validation - Interactive Analysis
Enhanced analysis with visualizations and deeper insights
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

# ============================================================================
# ENHANCED ANALYSIS SECTION
# ============================================================================

class PortfolioAnalyzer:
    """
    Perform detailed analysis on cleaned portfolio data
    """
    
    def __init__(self, cleaned_data_dir, returns_data_dir):
        """
        Initialize analyzer with data directories
        """
        self.cleaned_data_dir = Path(cleaned_data_dir)
        self.returns_data_dir = Path(returns_data_dir)
        self.portfolio_returns = None
        self.price_data = {}
        self.returns_data = {}
        
    def load_processed_data(self):
        """
        Load the processed data from Week 1 pipeline
        """
        print("Loading processed data...")
        
        # Load daily returns
        returns_file = self.returns_data_dir.parent / "portfolio_daily_returns.csv"
        if returns_file.exists():
            self.portfolio_returns = pd.read_csv(returns_file, index_col=0, parse_dates=True)
            print(f"✓ Loaded portfolio returns: {self.portfolio_returns.shape}")
        
        # Load individual returns
        for file in self.returns_data_dir.glob("*_returns.csv"):
            ticker = file.stem.replace('_returns', '')
            self.returns_data[ticker] = pd.read_csv(file, index_col=0, parse_dates=True)
        
        print(f"✓ Loaded {len(self.returns_data)} stock returns")
    
    def calculate_risk_metrics(self):
        """
        Calculate key risk metrics for the portfolio
        """
        print("\n" + "=" * 70)
        print("RISK METRICS ANALYSIS")
        print("=" * 70)
        
        risk_metrics = {}
        
        for ticker in list(self.returns_data.keys())[:5]:  # First 5 for demo
            returns = self.returns_data[ticker]['Daily_Return'].dropna()
            
            metrics = {
                'Mean_Return': returns.mean(),
                'Std_Dev': returns.std(),
                'Variance': returns.var(),
                'Skewness': returns.skew(),
                'Kurtosis': returns.kurtosis(),
                'Min': returns.min(),
                'Max': returns.max(),
                'VaR_95': np.percentile(returns, 5),  # 95% confidence
                'VaR_99': np.percentile(returns, 1),  # 99% confidence
            }
            
            risk_metrics[ticker] = metrics
            
            print(f"\n{ticker}:")
            print(f"  Mean Return:    {metrics['Mean_Return']:>8.4f}%")
            print(f"  Std Dev:        {metrics['Std_Dev']:>8.4f}%")
            print(f"  Skewness:       {metrics['Skewness']:>8.4f}")
            print(f"  Kurtosis:       {metrics['Kurtosis']:>8.4f}")
            print(f"  VaR (95%):      {metrics['VaR_95']:>8.4f}%")
            print(f"  VaR (99%):      {metrics['VaR_99']:>8.4f}%")
        
        return risk_metrics
    
    def analyze_data_quality(self):
        """
        Detailed data quality assessment
        """
        print("\n" + "=" * 70)
        print("DATA QUALITY ASSESSMENT")
        print("=" * 70)
        
        quality_report = {}
        
        for ticker, df in self.returns_data.items():
            returns = df['Daily_Return'].dropna()
            
            quality = {
                'Total_Records': len(df),
                'Valid_Records': len(returns),
                'Missing_Pct': (len(df) - len(returns)) / len(df) * 100,
                'Duplicate_Count': df.duplicated().sum(),
            }
            
            quality_report[ticker] = quality
        
        # Summary
        avg_missing = np.mean([v['Missing_Pct'] for v in quality_report.values()])
        avg_valid = np.mean([v['Valid_Records'] for v in quality_report.values()])
        
        print(f"\nAverage Valid Records per Stock: {avg_valid:>8.0f}")
        print(f"Average Missing Data:           {avg_missing:>8.4f}%")
        
        return quality_report
    
    def correlation_analysis(self):
        """
        Analyze correlation between stocks
        """
        print("\n" + "=" * 70)
        print("CORRELATION STRUCTURE ANALYSIS")
        print("=" * 70)
        
        if self.portfolio_returns is not None:
            corr_matrix = self.portfolio_returns.corr()
            
            print(f"\nPortfolio consists of {len(corr_matrix)} stocks")
            print(f"\nCorrelation Statistics:")
            
            # Extract correlations (excluding diagonal)
            mask = np.triu(np.ones_like(corr_matrix), k=1).astype(bool)
            corr_values = corr_matrix.values[mask]
            
            print(f"  Average Correlation:  {np.mean(corr_values):>8.4f}")
            print(f"  Min Correlation:      {np.min(corr_values):>8.4f}")
            print(f"  Max Correlation:      {np.max(corr_values):>8.4f}")
            print(f"  Std Dev:              {np.std(corr_values):>8.4f}")
            
            # Identify diversification opportunities
            low_corr = (corr_values < 0.3).sum()
            high_corr = (corr_values > 0.7).sum()
            
            print(f"\n  Diversification:")
            print(f"    - Low Correlation Pairs (<0.3):  {low_corr}")
            print(f"    - High Correlation Pairs (>0.7): {high_corr}")
            
            return corr_matrix
        
        return None
    
    def temporal_analysis(self):
        """
        Analyze temporal patterns and trends
        """
        print("\n" + "=" * 70)
        print("TEMPORAL ANALYSIS")
        print("=" * 70)
        
        if self.portfolio_returns is not None:
            print(f"\nData Coverage:")
            print(f"  Start Date: {self.portfolio_returns.index[0]}")
            print(f"  End Date:   {self.portfolio_returns.index[-1]}")
            print(f"  Duration:   {(self.portfolio_returns.index[-1] - self.portfolio_returns.index[0]).days} days")
            print(f"  Records:    {len(self.portfolio_returns)}")
            
            # Analyze returns by period
            portfolio_returns_summary = self.portfolio_returns.mean(axis=1)
            
            print(f"\nPortfolio Average Daily Return: {portfolio_returns_summary.mean():>8.4f}%")
            print(f"Portfolio Return Std Dev:       {portfolio_returns_summary.std():>8.4f}%")


# ============================================================================
# VISUALIZATION FUNCTIONS
# ============================================================================

def create_summary_visualizations(returns_df, output_dir="visualizations"):
    """
    Create key visualizations for Week 1 analysis
    """
    Path(output_dir).mkdir(exist_ok=True)
    
    print("\nGenerating visualizations...")
    
    try:
        # 1. Daily Returns Distribution
        fig, axes = plt.subplots(2, 2, figsize=(14, 10))
        
        # Histogram of returns
        sample_stocks = list(returns_df.columns)[:4]
        for idx, ticker in enumerate(sample_stocks):
            ax = axes[idx // 2, idx % 2]
            ax.hist(returns_df[ticker].dropna(), bins=50, alpha=0.7, color='blue', edgecolor='black')
            ax.set_title(f'{ticker} - Daily Returns Distribution', fontsize=12, fontweight='bold')
            ax.set_xlabel('Daily Return (%)')
            ax.set_ylabel('Frequency')
            ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig(f'{output_dir}/returns_distribution.png', dpi=300, bbox_inches='tight')
        print("✓ Saved: returns_distribution.png")
        plt.close()
        
        # 2. Correlation Heatmap
        corr_matrix = returns_df.corr()
        
        fig, ax = plt.subplots(figsize=(12, 10))
        sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm', center=0, 
                   square=True, ax=ax, cbar_kws={'label': 'Correlation Coefficient'})
        ax.set_title('Portfolio Correlation Matrix', fontsize=14, fontweight='bold')
        plt.tight_layout()
        plt.savefig(f'{output_dir}/correlation_heatmap.png', dpi=300, bbox_inches='tight')
        print("✓ Saved: correlation_heatmap.png")
        plt.close()
        
    except Exception as e:
        print(f"Note: Could not generate visualizations: {str(e)}")


# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    print("\n╔" + "=" * 68 + "╗")
    print("║" + " " * 15 + "WEEK 1 DETAILED ANALYSIS - AlphaPulse" + " " * 16 + "║")
    print("╚" + "=" * 68 + "╝\n")
    
    DATA_DIR = r"c:\Users\mohum\OneDrive\Desktop\Financial Analytics - Portfolio Risk & Volatility Monitor\processed_data"
    
    # Initialize analyzer
    analyzer = PortfolioAnalyzer(
        cleaned_data_dir=f"{DATA_DIR}/cleaned_data",
        returns_data_dir=f"{DATA_DIR}/daily_returns"
    )
    
    # Run analyses
    try:
        analyzer.load_processed_data()
        risk_metrics = analyzer.calculate_risk_metrics()
        quality_report = analyzer.analyze_data_quality()
        corr_matrix = analyzer.correlation_analysis()
        analyzer.temporal_analysis()
        
        # Generate visualizations
        if analyzer.portfolio_returns is not None:
            create_summary_visualizations(analyzer.portfolio_returns)
        
        print("\n✓ WEEK 1 ANALYSIS COMPLETE")
        
    except Exception as e:
        print(f"\nNote: Some analyses could not be completed: {str(e)}")
        print("This may be due to the pipeline not being run first.")
        print("\nPlease run week1_data_acquisition.py first to process the data.")
