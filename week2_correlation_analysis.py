import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

class PortfolioCorrelationAnalysis:
    
    def __init__(self, returns_file, cleaned_data_dir):
        self.returns_file = returns_file
        self.cleaned_data_dir = Path(cleaned_data_dir)
        self.portfolio_returns = None
        self.correlation_matrix = None
        self.sector_analysis = {}
        
    def load_portfolio_returns(self):
        print("=" * 70)
        print("STEP 1: LOAD PORTFOLIO RETURNS")
        print("=" * 70)
        
        if Path(self.returns_file).exists():
            self.portfolio_returns = pd.read_csv(
                self.returns_file, 
                index_col=0, 
                parse_dates=True
            )
            print(f"✓ Loaded portfolio returns")
            print(f"  - Stocks: {len(self.portfolio_returns.columns)}")
            print(f"  - Days: {len(self.portfolio_returns)}")
            print(f"  - Date Range: {self.portfolio_returns.index[0]} to {self.portfolio_returns.index[-1]}")
        else:
            print(f"✗ File not found: {self.returns_file}")
            return False
        
        print()
        return True
    
    def calculate_correlation_matrix(self):
        print("=" * 70)
        print("STEP 2: CALCULATE CORRELATION MATRIX")
        print("=" * 70)
        
        if self.portfolio_returns is None:
            print("✗ Portfolio returns not loaded")
            return None
        
        self.correlation_matrix = self.portfolio_returns.corr()
        
        print(f"✓ Correlation matrix calculated ({self.correlation_matrix.shape})")
        
        mask = np.triu(np.ones_like(self.correlation_matrix), k=1).astype(bool)
        corr_values = self.correlation_matrix.values[mask]
        
        print(f"\nCorrelation Statistics:")
        print(f"  - Mean Correlation:    {np.mean(corr_values):>8.4f}")
        print(f"  - Median Correlation:  {np.median(corr_values):>8.4f}")
        print(f"  - Min Correlation:     {np.min(corr_values):>8.4f}")
        print(f"  - Max Correlation:     {np.max(corr_values):>8.4f}")
        print(f"  - Std Dev:             {np.std(corr_values):>8.4f}")
        
        low_corr = (corr_values < 0.3).sum()
        mid_corr = ((corr_values >= 0.3) & (corr_values < 0.7)).sum()
        high_corr = (corr_values >= 0.7).sum()
        
        print(f"\nDiversification Analysis:")
        print(f"  - Low Corr (<0.3):     {low_corr:>8} pairs")
        print(f"  - Mid Corr (0.3-0.7):  {mid_corr:>8} pairs")
        print(f"  - High Corr (>0.7):    {high_corr:>8} pairs")
        
        print()
        
        return self.correlation_matrix
    
    def identify_correlation_clusters(self):
        print("=" * 70)
        print("STEP 3: IDENTIFY CORRELATION CLUSTERS")
        print("=" * 70)
        
        if self.correlation_matrix is None:
            print("✗ Correlation matrix not calculated")
            return
        
        print("\nHighly Correlated Pairs (>0.7):")
        
        high_corr_pairs = []
        for i in range(len(self.correlation_matrix.columns)):
            for j in range(i+1, len(self.correlation_matrix.columns)):
                corr_value = self.correlation_matrix.iloc[i, j]
                if corr_value > 0.7:
                    ticker1 = self.correlation_matrix.columns[i]
                    ticker2 = self.correlation_matrix.columns[j]
                    high_corr_pairs.append((ticker1, ticker2, corr_value))
        
        high_corr_pairs.sort(key=lambda x: x[2], reverse=True)
        
        if high_corr_pairs:
            for ticker1, ticker2, corr in high_corr_pairs[:10]:
                print(f"  - {ticker1} <-> {ticker2}: {corr:.4f}")
            if len(high_corr_pairs) > 10:
                print(f"  - ... and {len(high_corr_pairs) - 10} more pairs")
        else:
            print(f"  - No pairs with correlation > 0.7 found")
        
        print("\nLow Correlated Pairs (<0.3) - Diversification Opportunities:")
        
        low_corr_pairs = []
        for i in range(len(self.correlation_matrix.columns)):
            for j in range(i+1, len(self.correlation_matrix.columns)):
                corr_value = self.correlation_matrix.iloc[i, j]
                if corr_value < 0.3:
                    ticker1 = self.correlation_matrix.columns[i]
                    ticker2 = self.correlation_matrix.columns[j]
                    low_corr_pairs.append((ticker1, ticker2, corr_value))
        
        if low_corr_pairs:
            print(f"  - Total low correlation pairs: {len(low_corr_pairs)}")
            print(f"  - Best diversifiers (sample):")
            low_corr_pairs.sort(key=lambda x: x[2])
            for ticker1, ticker2, corr in low_corr_pairs[:5]:
                print(f"    - {ticker1} <-> {ticker2}: {corr:.4f}")
        
        print()
    
    def analyze_stock_average_correlation(self):
        print("=" * 70)
        print("STEP 4: STOCK AVERAGE CORRELATION ANALYSIS")
        print("=" * 70)
        
        if self.correlation_matrix is None:
            print("✗ Correlation matrix not calculated")
            return
        
        avg_corr = []
        for i, ticker in enumerate(self.correlation_matrix.columns):
            corr_values = self.correlation_matrix.iloc[i, :].values
            corr_values = corr_values[corr_values != 1.0]
            avg = np.mean(corr_values)
            avg_corr.append((ticker, avg))
        
        avg_corr.sort(key=lambda x: x[1])
        
        print("\nStocks with LOWEST average correlation (best diversifiers):")
        for ticker, avg in avg_corr[:10]:
            print(f"  - {ticker:15} {avg:.4f}")
        
        print("\nStocks with HIGHEST average correlation (market movers):")
        for ticker, avg in avg_corr[-10:]:
            print(f"  - {ticker:15} {avg:.4f}")
        
        print()
    
    def calculate_portfolio_metrics(self, weights=None):
        print("=" * 70)
        print("STEP 5: PORTFOLIO PERFORMANCE METRICS")
        print("=" * 70)
        
        if self.portfolio_returns is None:
            print("✗ Portfolio returns not loaded")
            return
        
        if weights is None:
            weights = np.ones(len(self.portfolio_returns.columns)) / len(self.portfolio_returns.columns)
        
        portfolio_ret = (self.portfolio_returns * weights).sum(axis=1)
        
        print(f"\nPortfolio (Equal Weighted):")
        print(f"  - Mean Daily Return:   {portfolio_ret.mean():>8.4f}%")
        print(f"  - Volatility (Std):    {portfolio_ret.std():>8.4f}%")
        print(f"  - Sharpe Ratio (0% RF): {(portfolio_ret.mean() / portfolio_ret.std() * np.sqrt(252)):>8.4f}")
        print(f"  - Max Drawdown:        {((portfolio_ret.cumsum()).min()):>8.4f}%")
        print(f"  - Total Return:        {portfolio_ret.sum():>8.4f}%")
        
        print()
    
    def generate_correlation_heatmap(self, output_dir="visualizations"):
        print("=" * 70)
        print("STEP 6: GENERATE CORRELATION HEATMAP")
        print("=" * 70)
        
        if self.correlation_matrix is None:
            print("✗ Correlation matrix not calculated")
            return
        
        try:
            Path(output_dir).mkdir(parents=True, exist_ok=True)
            
            if len(self.correlation_matrix) > 30:
                corr_subset = self.correlation_matrix.iloc[:30, :30]
            else:
                corr_subset = self.correlation_matrix
            
            fig, ax = plt.subplots(figsize=(14, 12))
            sns.heatmap(
                corr_subset,
                cmap='RdYlBu_r',
                center=0,
                vmin=-1,
                vmax=1,
                square=True,
                linewidths=0.5,
                cbar_kws={'label': 'Correlation Coefficient'},
                ax=ax,
                annot=False
            )
            ax.set_title('Portfolio Correlation Matrix (First 30 stocks)', fontsize=14, fontweight='bold')
            plt.tight_layout()
            plt.savefig(f'{output_dir}/correlation_heatmap_full.png', dpi=300, bbox_inches='tight')
            print(f"✓ Saved correlation_heatmap_full.png")
            plt.close()
            
            fig, ax = plt.subplots(figsize=(12, 10))
            if len(self.correlation_matrix) > 12:
                corr_sample = self.correlation_matrix.iloc[:12, :12]
            else:
                corr_sample = self.correlation_matrix
            
            sns.heatmap(
                corr_sample,
                cmap='RdYlBu_r',
                center=0,
                vmin=-1,
                vmax=1,
                square=True,
                linewidths=1,
                cbar_kws={'label': 'Correlation'},
                ax=ax,
                annot=True,
                fmt='.2f'
            )
            ax.set_title('Portfolio Correlation Matrix (Sample)', fontsize=14, fontweight='bold')
            plt.tight_layout()
            plt.savefig(f'{output_dir}/correlation_heatmap_sample.png', dpi=300, bbox_inches='tight')
            print(f"✓ Saved correlation_heatmap_sample.png")
            plt.close()
            
        except Exception as e:
            print(f"✗ Error generating visualization: {str(e)}")
        
        print()
    
    def save_correlation_analysis(self, output_dir="processed_data"):
        print("=" * 70)
        print("STEP 7: SAVE CORRELATION ANALYSIS")
        print("=" * 70)
        
        output_path = Path(output_dir) / "week2_analysis"
        output_path.mkdir(parents=True, exist_ok=True)
        
        if self.correlation_matrix is not None:
            corr_file = output_path / "correlation_matrix.csv"
            self.correlation_matrix.to_csv(corr_file)
            print(f"✓ Saved correlation_matrix.csv")
        
        report_file = output_path / "correlation_analysis.txt"
        with open(report_file, 'w') as f:
            f.write("CORRELATION ANALYSIS REPORT\n")
            f.write("=" * 70 + "\n")
            f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            if self.correlation_matrix is not None:
                mask = np.triu(np.ones_like(self.correlation_matrix), k=1).astype(bool)
                corr_values = self.correlation_matrix.values[mask]
                
                f.write("Correlation Statistics:\n")
                f.write(f"Mean: {np.mean(corr_values):.4f}\n")
                f.write(f"Std: {np.std(corr_values):.4f}\n")
                f.write(f"Min: {np.min(corr_values):.4f}\n")
                f.write(f"Max: {np.max(corr_values):.4f}\n\n")
                
                f.write("Diversification Metrics:\n")
                low = (corr_values < 0.3).sum()
                mid = ((corr_values >= 0.3) & (corr_values < 0.7)).sum()
                high = (corr_values >= 0.7).sum()
                f.write(f"Low Correlation Pairs: {low}\n")
                f.write(f"Mid Correlation Pairs: {mid}\n")
                f.write(f"High Correlation Pairs: {high}\n")
        
        print(f"✓ Saved correlation_analysis.txt")
        print()
    
    def run_full_analysis(self, output_dir="processed_data"):
        print("\n╔" + "=" * 68 + "╗")
        print("║" + " " * 8 + "WEEK 2 CORRELATION & PORTFOLIO ANALYSIS" + " " * 20 + "║")
        print("║" + " " * 15 + "Dynamic Correlation Structure" + " " * 23 + "║")
        print("╚" + "=" * 68 + "╝\n")
        
        if not self.load_portfolio_returns():
            return False
        
        self.calculate_correlation_matrix()
        self.identify_correlation_clusters()
        self.analyze_stock_average_correlation()
        self.calculate_portfolio_metrics()
        
        viz_dir = Path(output_dir).parent / "visualizations"
        self.generate_correlation_heatmap(str(viz_dir))
        
        self.save_correlation_analysis(output_dir)
        
        print("=" * 70)
        print("✓ CORRELATION ANALYSIS COMPLETE")
        print("=" * 70)
        print()
        
        return True


if __name__ == "__main__":
    PROCESSED_DATA_DIR = r"c:\Users\mohum\OneDrive\Desktop\Financial Analytics - Portfolio Risk & Volatility Monitor\processed_data"
    
    analyzer = PortfolioCorrelationAnalysis(
        returns_file=f"{PROCESSED_DATA_DIR}/portfolio_daily_returns.csv",
        cleaned_data_dir=f"{PROCESSED_DATA_DIR}/cleaned_data"
    )
    
    analyzer.run_full_analysis(output_dir=PROCESSED_DATA_DIR)
