import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

class QuantitativeAnalyzer:
    
    def __init__(self, returns_data_dir, processed_data_dir):
        self.returns_data_dir = Path(returns_data_dir)
        self.processed_data_dir = Path(processed_data_dir)
        self.returns_data = {}
        self.log_returns_data = {}
        self.rolling_volatility = {}
        self.var_95 = {}
        self.monte_carlo_results = {}
        
    def load_daily_returns(self):
        print("=" * 70)
        print("STEP 1: LOAD DAILY RETURNS")
        print("=" * 70)
        
        files = list(self.returns_data_dir.glob("*_returns.csv"))
        
        for file in files:
            ticker = file.stem.replace('_returns', '')
            df = pd.read_csv(file, index_col=0, parse_dates=True)
            self.returns_data[ticker] = df
        
        print(f"✓ Loaded {len(self.returns_data)} return series\n")
        return True
    
    def calculate_log_returns(self):
        print("=" * 70)
        print("STEP 2: CALCULATE LOG RETURNS")
        print("=" * 70)
        
        for ticker, df in self.returns_data.items():
            if 'Daily_Return' in df.columns:
                simple_returns = pd.to_numeric(df['Daily_Return'].values, errors='coerce') / 100
                simple_returns = simple_returns[~np.isnan(simple_returns)]
                
                if len(simple_returns) > 1:
                    log_returns = np.log(1 + simple_returns)
                    self.log_returns_data[ticker] = log_returns
                    
                    mean_log = np.mean(log_returns)
                    std_log = np.std(log_returns)
                    
                    print(f"✓ {ticker}:")
                    print(f"  - Mean Log Return:   {mean_log:>8.6f}")
                    print(f"  - Std Log Return:    {std_log:>8.6f}")
                    print(f"  - Count:             {len(log_returns):>8}")
        
        print()
    
    def calculate_rolling_volatility(self, window=30):
        print("=" * 70)
        print(f"STEP 3: CALCULATE ROLLING VOLATILITY (Window={window} days)")
        print("=" * 70)
        
        for ticker, returns_series in self.returns_data.items():
            daily_pct = returns_series['Daily_Return'].values / 100
            
            rolling_std = []
            for i in range(len(daily_pct)):
                if i < window:
                    window_data = daily_pct[:i+1]
                else:
                    window_data = daily_pct[i-window+1:i+1]
                
                if len(window_data) > 0:
                    rolling_std.append(np.std(window_data) * 100)
                else:
                    rolling_std.append(np.nan)
            
            self.rolling_volatility[ticker] = np.array(rolling_std)
            
            valid_vols = [v for v in rolling_std if not np.isnan(v)]
            if valid_vols:
                print(f"✓ {ticker}:")
                print(f"  - Current (30-day):  {valid_vols[-1]:>8.4f}%")
                print(f"  - Average:           {np.mean(valid_vols):>8.4f}%")
                print(f"  - Max:               {np.max(valid_vols):>8.4f}%")
                print(f"  - Min:               {np.min(valid_vols):>8.4f}%")
        
        print()
    
    def calculate_historical_var(self, confidence=0.95):
        print("=" * 70)
        print(f"STEP 4: CALCULATE HISTORICAL VAR ({confidence*100:.0f}% Confidence)")
        print("=" * 70)
        
        confidence_level = (1 - confidence)
        
        for ticker, returns_series in self.returns_data.items():
            daily_returns = pd.to_numeric(returns_series['Daily_Return'].values, errors='coerce')
            daily_returns = daily_returns[~np.isnan(daily_returns)]
            
            if len(daily_returns) > 1:
                var = np.percentile(daily_returns, confidence_level * 100)
                
                self.var_95[ticker] = var
                
                cvar = daily_returns[daily_returns <= var].mean() if len(daily_returns[daily_returns <= var]) > 0 else var
                
                print(f"✓ {ticker}:")
                print(f"  - VaR (95%):         {var:>8.4f}%")
                print(f"  - CVaR (Avg Loss):   {cvar:>8.4f}%")
                print(f"  - Mean Return:       {np.mean(daily_returns):>8.4f}%")
                print(f"  - Std Dev:           {np.std(daily_returns):>8.4f}%")
        
        print()
    
    def monte_carlo_simulation(self, num_sim=10000, days=252):
        print("=" * 70)
        print(f"STEP 5: MONTE CARLO SIMULATION")
        print(f"Simulations: {num_sim:,} | Time Horizon: {days} days")
        print("=" * 70)
        
        sim_results = {}
        
        for ticker, returns_series in self.returns_data.items():
            daily_returns = returns_series['Daily_Return'].values / 100
            
            mu = np.mean(daily_returns)
            sigma = np.std(daily_returns)
            
            starting_price = 1.0
            
            simulations = np.zeros((num_sim, days))
            
            for i in range(num_sim):
                price = starting_price
                for j in range(days):
                    random_return = np.random.normal(mu, sigma)
                    price = price * (1 + random_return)
                    simulations[i, j] = price
            
            final_prices = simulations[:, -1]
            final_returns = ((final_prices - starting_price) / starting_price) * 100
            
            sim_results[ticker] = {
                'simulations': simulations,
                'final_prices': final_prices,
                'final_returns': final_returns,
                'mu': mu,
                'sigma': sigma,
            }
            
            print(f"✓ {ticker}:")
            print(f"  - Mean Final Return:  {np.mean(final_returns):>8.4f}%")
            print(f"  - Std Final Return:   {np.std(final_returns):>8.4f}%")
            print(f"  - 5th Percentile:     {np.percentile(final_returns, 5):>8.4f}%")
            print(f"  - 95th Percentile:    {np.percentile(final_returns, 95):>8.4f}%")
            print(f"  - Min:                {np.min(final_returns):>8.4f}%")
            print(f"  - Max:                {np.max(final_returns):>8.4f}%")
        
        self.monte_carlo_results = sim_results
        print()
        
        return sim_results
    
    def calculate_monte_carlo_var(self, confidence=0.95):
        print("=" * 70)
        print(f"STEP 6: MONTE CARLO VaR ({confidence*100:.0f}% Confidence)")
        print("=" * 70)
        
        confidence_level = (1 - confidence)
        
        for ticker, results in self.monte_carlo_results.items():
            final_returns = results['final_returns']
            
            mc_var = np.percentile(final_returns, confidence_level * 100)
            mc_cvar = final_returns[final_returns <= mc_var].mean()
            
            print(f"✓ {ticker}:")
            print(f"  - MC VaR (95%):      {mc_var:>8.4f}%")
            print(f"  - MC CVaR:           {mc_cvar:>8.4f}%")
            print(f"  - Success Rate:      {(final_returns > 0).sum() / len(final_returns) * 100:>8.4f}%")
        
        print()
    
    def statistical_sanity_check(self):
        print("=" * 70)
        print("STEP 7: STATISTICAL SANITY CHECK")
        print("Distribution Comparison: Historical vs Monte Carlo")
        print("=" * 70)
        
        for ticker in list(self.monte_carlo_results.keys())[:5]:
            historical_returns = self.returns_data[ticker]['Daily_Return'].values
            mc_returns = self.monte_carlo_results[ticker]['final_returns']
            
            hist_mean = np.mean(historical_returns)
            hist_std = np.std(historical_returns)
            hist_skew = (historical_returns - hist_mean) ** 3
            hist_skew = np.mean(hist_skew) / (hist_std ** 3) if hist_std > 0 else 0
            
            mc_mean = np.mean(mc_returns)
            mc_std = np.std(mc_returns)
            mc_skew = (mc_returns - mc_mean) ** 3
            mc_skew = np.mean(mc_skew) / (mc_std ** 3) if mc_std > 0 else 0
            
            print(f"\n{ticker}:")
            print(f"  Historical | Mean: {hist_mean:>8.4f}% | Std: {hist_std:>8.4f}% | Skew: {hist_skew:>8.4f}")
            print(f"  MC Simulation | Mean: {mc_mean:>8.4f}% | Std: {mc_std:>8.4f}% | Skew: {mc_skew:>8.4f}")
            
            mean_diff = abs(hist_mean - mc_mean)
            std_diff = abs(hist_std - mc_std)
            
            if mean_diff < 0.5:
                print(f"  ✓ Mean Distribution: PASS (diff: {mean_diff:.4f}%)")
            else:
                print(f"  ⚠ Mean Distribution: CHECK (diff: {mean_diff:.4f}%)")
            
            if std_diff < 2.0:
                print(f"  ✓ Volatility Distribution: PASS (diff: {std_diff:.4f}%)")
            else:
                print(f"  ⚠ Volatility Distribution: CHECK (diff: {std_diff:.4f}%)")
        
        print()
    
    def generate_validation_report(self):
        print("=" * 70)
        print("STEP 8: VALIDATION REPORT")
        print("=" * 70)
        
        report = {
            'Timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'Stocks Analyzed': len(self.returns_data),
            'Log Returns Calculated': len(self.log_returns_data),
            'Rolling Volatility Computed': len(self.rolling_volatility),
            'Historical VaR Calculated': len(self.var_95),
            'Monte Carlo Simulations': len(self.monte_carlo_results),
        }
        
        print("\nAnalysis Summary:")
        for key, value in report.items():
            print(f"  {key:.<40} {value}")
        
        print("\n✓ Week 2 Analysis Complete")
        print()
        
        return report
    
    def save_results(self, output_dir):
        print("=" * 70)
        print("STEP 9: SAVE RESULTS")
        print("=" * 70)
        
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        
        week2_dir = output_path / "week2_analysis"
        week2_dir.mkdir(exist_ok=True)
        
        summary_data = []
        for ticker in self.returns_data.keys():
            hist_returns = self.returns_data[ticker]['Daily_Return'].values
            
            row = {
                'Ticker': ticker,
                'Mean_Return': np.mean(hist_returns),
                'Std_Dev': np.std(hist_returns),
                'VaR_95': self.var_95.get(ticker, np.nan),
                'Max_Return': np.max(hist_returns),
                'Min_Return': np.min(hist_returns),
            }
            
            if ticker in self.monte_carlo_results:
                mc_results = self.monte_carlo_results[ticker]
                row['MC_Mean'] = np.mean(mc_results['final_returns'])
                row['MC_Std'] = np.std(mc_results['final_returns'])
                row['MC_VaR_95'] = np.percentile(mc_results['final_returns'], 5)
            
            summary_data.append(row)
        
        summary_df = pd.DataFrame(summary_data)
        summary_file = week2_dir / "quantitative_summary.csv"
        summary_df.to_csv(summary_file, index=False)
        print(f"✓ Saved quantitative_summary.csv")
        
        report_file = week2_dir / "week2_report.txt"
        with open(report_file, 'w') as f:
            f.write("WEEK 2 QUANTITATIVE ANALYSIS REPORT\n")
            f.write("=" * 70 + "\n")
            f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Stocks Analyzed: {len(self.returns_data)}\n")
            f.write(f"Monte Carlo Simulations: {len(self.monte_carlo_results)}\n\n")
            f.write(summary_df.to_string())
        
        print(f"✓ Saved week2_report.txt")
        print()
    
    def run_full_analysis(self, output_dir="processed_data", num_simulations=10000):
        print("\n╔" + "=" * 68 + "╗")
        print("║" + " " * 10 + "FINANCIAL ANALYTICS - WEEK 2 ANALYSIS" + " " * 21 + "║")
        print("║" + " " * 5 + "Quantitative Analysis & Monte Carlo Simulation" + " " * 14 + "║")
        print("╚" + "=" * 68 + "╝\n")
        
        self.load_daily_returns()
        self.calculate_log_returns()
        self.calculate_rolling_volatility(window=30)
        self.calculate_historical_var(confidence=0.95)
        self.monte_carlo_simulation(num_sim=num_simulations, days=252)
        self.calculate_monte_carlo_var(confidence=0.95)
        self.statistical_sanity_check()
        self.generate_validation_report()
        self.save_results(output_dir)
        
        print("=" * 70)
        print("✓ WEEK 2 ANALYSIS EXECUTION COMPLETE")
        print("=" * 70)
        print()


if __name__ == "__main__":
    PROCESSED_DATA_DIR = r"c:\Users\mohum\OneDrive\Desktop\Financial Analytics - Portfolio Risk & Volatility Monitor\processed_data"
    
    analyzer = QuantitativeAnalyzer(
        returns_data_dir=f"{PROCESSED_DATA_DIR}/daily_returns",
        processed_data_dir=PROCESSED_DATA_DIR
    )
    
    analyzer.run_full_analysis(
        output_dir=PROCESSED_DATA_DIR,
        num_simulations=10000
    )
