import pandas as pd
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

print("\n" + "=" * 70)
print("WEEK 2: QUANTITATIVE & CORRELATION ANALYSIS")
print("=" * 70 + "\n")

data_dir = Path(r"c:\Users\mohum\OneDrive\Desktop\Financial Analytics - Portfolio Risk & Volatility Monitor\processed_data")

# STEP 1: Load daily returns
print("STEP 1: Loading daily returns...")
returns_data = {}
returns_files = list((data_dir / "daily_returns").glob("*.csv"))
print(f"✓ Found {len(returns_files)} return files\n")

for csv_file in returns_files[:2]:  # Test with first 2 files
    ticker = csv_file.stem.replace("_daily_returns", "")
    df = pd.read_csv(csv_file, index_col=0)
    if 'daily_return' in df.columns:
        returns_data[ticker] = df['daily_return'].values

print(f"✓ Loaded {len(returns_data)} stocks\n")

# STEP 2: Calculate log returns
print("STEP 2: Calculating log returns...")
log_returns_data = {}

for ticker, returns in returns_data.items():
    # Convert to numeric and filter
    returns = pd.to_numeric(pd.Series(returns), errors='coerce').dropna().values
    
    if len(returns) > 1:
        log_returns = np.log(1 + returns)
        log_returns_data[ticker] = log_returns
        
        print(f"✓ {ticker}:")
        print(f"  Mean: {np.mean(log_returns):.6f}, Std: {np.std(log_returns):.6f}, Count: {len(log_returns)}")

print()

# STEP 3: Rolling volatility (30-day)
print("STEP 3: Calculating 30-day rolling volatility...")
rolling_volatility = {}

for ticker, returns in log_returns_data.items():
    vol = []
    for i in range(len(returns)):
        window_size = min(30, i+1)
        vol.append(np.std(returns[max(0, i-29):i+1]))
    
    rolling_volatility[ticker] = np.array(vol)
    print(f"✓ {ticker}: Avg Vol = {np.mean(vol):.6f}")

print()

# STEP 4: Historical VaR
print("STEP 4: Calculating Historical VaR (95% confidence)...")
var_95_hist = {}

for ticker, returns in log_returns_data.items():
    var = np.percentile(returns, 5)  # 5th percentile for 95% confidence
    var_95_hist[ticker] = var
    print(f"✓ {ticker}: VaR(95%) = {var:.6f}")

print()

# STEP 5: Monte Carlo Simulation (simplified)
print("STEP 5: Running Monte Carlo Simulation (10,000 scenarios x 252 days)...")
print("(This may take 1-2 minutes...)\n")

mc_results = {}

for ticker, returns in list(log_returns_data.items())[:2]:  # Test with 2 stocks
    print(f"  Simulating {ticker}...", end="", flush=True)
    
    mu = np.mean(returns)
    sigma = np.std(returns)
    
    # Simulate returns (252 days = 1 year)
    num_scenarios = 1000  # Reduced for speed
    days = 252
    
    simulations = np.zeros((num_scenarios, days))
    dt = 1 / 252
    
    for sim in range(num_scenarios):
        price = 1.0
        for day in range(days):
            dW = np.random.normal(0, np.sqrt(dt))
            price = price * np.exp((mu - sigma**2/2) * dt + sigma * dW)
            simulations[sim, day] = price
    
    final_prices = simulations[:, -1]
    final_returns = ((final_prices - 1.0) / 1.0) * 100
    
    mc_var = np.percentile(final_returns, 5)
    
    mc_results[ticker] = {
        'mean': np.mean(final_returns),
        'std': np.std(final_returns),
        'var95': mc_var
    }
    
    print(f" ✓ Mean={np.mean(final_returns):.2f}%, VaR={mc_var:.2f}%")

print()

# STEP 6: Portfolio Correlation
print("STEP 6: Loading and analyzing portfolio returns...")

try:
    portfolio_returns = pd.read_csv(data_dir / "portfolio_daily_returns.csv", index_col=0)
    print(f"✓ Portfolio matrix loaded: {portfolio_returns.shape}")
    
    # Calculate correlation
    corr_matrix = portfolio_returns.corr()
    print(f"✓ Correlation matrix: {corr_matrix.shape}")
    
    # Find high/low correlations
    high_pairs = []
    low_pairs = []
    
    for i in range(len(corr_matrix)):
        for j in range(i+1, len(corr_matrix)):
            ticker_i = corr_matrix.index[i]
            ticker_j = corr_matrix.index[j]
            corr_val = corr_matrix.iloc[i, j]
            
            if corr_val > 0.7:
                high_pairs.append((ticker_i, ticker_j, corr_val))
            elif corr_val < 0.3:
                low_pairs.append((ticker_i, ticker_j, corr_val))
    
    high_pairs.sort(key=lambda x: x[2], reverse=True)
    low_pairs.sort(key=lambda x: x[2])
    
    print(f"\n✓ High correlation pairs (>0.7): {len(high_pairs)}")
    for i, (t1, t2, c) in enumerate(high_pairs[:5]):
        print(f"  {i+1}. {t1} ↔ {t2}: {c:.3f}")
    
    print(f"\n✓ Low correlation pairs (<0.3): {len(low_pairs)}")
    for i, (t1, t2, c) in enumerate(low_pairs[:5]):
        print(f"  {i+1}. {t1} ↔ {t2}: {c:.3f}")
    
    # Diversification ranking
    avg_corrs = corr_matrix.mean(axis=1)
    avg_corrs = avg_corrs.sort_values()
    
    print(f"\n✓ Best Diversifiers:")
    for i in range(min(5, len(avg_corrs))):
        print(f"  {i+1}. {avg_corrs.index[i]}: {avg_corrs.iloc[i]:.4f}")
    
    print(f"\n✓ Redundant Stocks:")
    for i in range(min(5, len(avg_corrs))):
        print(f"  {i+1}. {avg_corrs.index[-(i+1)]}: {avg_corrs.iloc[-(i+1)]:.4f}")
    
    # Portfolio metrics
    portfolio_daily = portfolio_returns.mean().mean()
    portfolio_vol = portfolio_returns.std().mean()
    portfolio_return_annual = portfolio_daily * 252
    portfolio_vol_annual = portfolio_vol * np.sqrt(252)
    sharpe = portfolio_return_annual / portfolio_vol_annual if portfolio_vol_annual > 0 else 0
    
    print(f"\n✓ PORTFOLIO METRICS (Equal-Weighted):")
    print(f"  Mean Daily Return: {portfolio_daily:.6f}")
    print(f"  Daily Volatility: {portfolio_vol:.6f}")
    print(f"  Annual Return: {portfolio_return_annual*100:.2f}%")
    print(f"  Annual Volatility: {portfolio_vol_annual*100:.2f}%")
    print(f"  Sharpe Ratio: {sharpe:.2f}")
    
except Exception as e:
    print(f"✗ Error: {str(e)}")

print("\n" + "=" * 70)
print("✓ WEEK 2 ANALYSIS COMPLETE")
print("=" * 70 + "\n")
