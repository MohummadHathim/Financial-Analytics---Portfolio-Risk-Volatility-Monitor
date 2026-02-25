"""
Configuration & Portfolio Metadata
Financial Analytics - AlphaPulse Project
"""

import json
from pathlib import Path

# ============================================================================
# PORTFOLIO CONFIGURATION
# ============================================================================

PORTFOLIO_CONFIG = {
    "project_name": "Financial Analytics - Portfolio Risk & Volatility Monitor",
    "product_brand": "AlphaPulse",
    "version": "1.0",
    "phase": "Week 1 - Data Acquisition & Validation",
    "description": "Real-time risk assessment tool for asset management firms"
}

# ============================================================================
# STOCK UNIVERSE
# ============================================================================

STOCKS = {
    "tech_it": [
        {"ticker": "TCS", "name": "Tata Consultancy Services", "sector": "Information Technology"},
        {"ticker": "INFY", "name": "Infosys Limited", "sector": "Information Technology"},
        {"ticker": "WIPRO", "name": "Wipro Limited", "sector": "Information Technology"},
        {"ticker": "TECHM", "name": "Tech Mahindra", "sector": "Information Technology"},
    ],
    "banking_finance": [
        {"ticker": "ICICIBANK", "name": "ICICI Bank", "sector": "Banking & Financial Services"},
        {"ticker": "AXISBANK", "name": "Axis Bank", "sector": "Banking & Financial Services"},
        {"ticker": "HDFCBANK", "name": "HDFC Bank", "sector": "Banking & Financial Services"},
        {"ticker": "SBIN", "name": "State Bank of India", "sector": "Banking & Financial Services"},
        {"ticker": "KOTAKBANK", "name": "Kotak Mahindra Bank", "sector": "Banking & Financial Services"},
    ],
    "energy": [
        {"ticker": "RELIANCE", "name": "Reliance Industries", "sector": "Energy"},
        {"ticker": "ONGC", "name": "Oil and Natural Gas Corp", "sector": "Energy"},
        {"ticker": "IOC", "name": "Indian Oil Corporation", "sector": "Energy"},
        {"ticker": "BPCL", "name": "Bharat Petroleum", "sector": "Energy"},
        {"ticker": "GAIL", "name": "Gas Authority of India", "sector": "Energy"},
    ],
    "heavy_industries": [
        {"ticker": "TATASTEEL", "name": "Tata Steel", "sector": "Heavy Industries & Construction"},
        {"ticker": "JSWSTEEL", "name": "JSW Steel", "sector": "Heavy Industries & Construction"},
        {"ticker": "HINDALCO", "name": "Hindalco Industries", "sector": "Heavy Industries & Construction"},
        {"ticker": "ULTRACEMCO", "name": "Ultratech Cement", "sector": "Heavy Industries & Construction"},
        {"ticker": "LT", "name": "Larsen & Toubro", "sector": "Heavy Industries & Construction"},
    ],
    "consumer": [
        {"ticker": "MARUTI", "name": "Maruti Suzuki", "sector": "Automobiles & Components"},
        {"ticker": "HEROMOTOCO", "name": "Hero MotoCorp", "sector": "Automobiles & Components"},
        {"ticker": "ITC", "name": "ITC Limited", "sector": "Consumer Goods"},
        {"ticker": "BRITANNIA", "name": "Britannia Industries", "sector": "Consumer Goods"},
        {"ticker": "NESTLEIND", "name": "Nestle India", "sector": "Consumer Goods"},
        {"ticker": "HINDUNILVR", "name": "Hindustan Unilever", "sector": "Consumer Goods"},
    ],
    "healthcare_pharma": [
        {"ticker": "CIPLA", "name": "Cipla Limited", "sector": "Pharmaceuticals"},
        {"ticker": "DRREDDY", "name": "Dr. Reddy's Laboratories", "sector": "Pharmaceuticals"},
        {"ticker": "SUNPHARMA", "name": "Sun Pharmaceutical", "sector": "Pharmaceuticals"},
    ],
    "automotive": [
        {"ticker": "BAJAJ-AUTO", "name": "Bajaj Auto", "sector": "Automobiles & Components"},
        {"ticker": "EICHERMOT", "name": "Eicher Motors", "sector": "Automobiles & Components"},
        {"ticker": "TATAMOTORS", "name": "Tata Motors", "sector": "Automobiles & Components"},
        {"ticker": "BAJAJFINSV", "name": "Bajaj Finserv", "sector": "Financial Services"},
        {"ticker": "BAJFINANCE", "name": "Bajaj Finance", "sector": "Financial Services"},
    ],
    "utilities": [
        {"ticker": "POWERGRID", "name": "Power Grid Corporation", "sector": "Utilities"},
        {"ticker": "NTPC", "name": "NTPC Limited", "sector": "Utilities"},
    ],
    "telecom": [
        {"ticker": "BHARTIARTL", "name": "Bharti Airtel", "sector": "Telecommunications"},
    ],
    "infrastructure": [
        {"ticker": "INFRATEL", "name": "Infratel (Vodafone Idea)", "sector": "Telecommunications"},
    ],
    "chemicals": [
        {"ticker": "GRASIM", "name": "Grasim Industries", "sector": "Chemicals"},
        {"ticker": "UPL", "name": "UPL Limited", "sector": "Chemicals"},
    ],
    "materials": [
        {"ticker": "VEDL", "name": "Vedanta Limited", "sector": "Materials"},
        {"ticker": "SHREECEM", "name": "Shree Cement", "sector": "Heavy Industries & Construction"},
        {"ticker": "MM", "name": "Manappuram Finance", "sector": "Financial Services"},
        {"ticker": "ASIANPAINT", "name": "Asian Paints", "sector": "Chemicals"},
        {"ticker": "ADANIPORTS", "name": "Adani Ports", "sector": "Transportation & Logistics"},
    ],
    "other": [
        {"ticker": "HDFC", "name": "HDFC (Housing Development)", "sector": "Financial Services"},
        {"ticker": "ZEEL", "name": "Zee Entertainment", "sector": "Media & Entertainment"},
        {"ticker": "TITAN", "name": "Titan Company", "sector": "Consumer Goods"},
        {"ticker": "COALINDIA", "name": "Coal India Limited", "sector": "Energy"},
    ],
    "benchmark": [
        {"ticker": "NIFTY50_all", "name": "NIFTY 50 Index", "sector": "Benchmark Index"},
    ]
}

# ============================================================================
# DATA VALIDATION RULES
# ============================================================================

DATA_VALIDATION_RULES = {
    "price_rules": {
        "min_price": 0.01,  # Minimum valid price
        "max_price": 100000,  # Maximum valid price (adjust based on data)
        "high_low_check": True,  # High should be >= Low
        "close_range_check": True,  # Close should be between High and Low
    },
    "volume_rules": {
        "min_volume": 0,
        "volume_zero_allowed": False,  # Can volume be zero?
    },
    "date_rules": {
        "trading_days_only": True,
        "allow_weekends": False,
        "allow_holidays": False,
    },
    "anomaly_detection": {
        "price_change_threshold": 20,  # % change to flag (potential stock split)
        "volume_spike_threshold": 3,  # 3x average volume
    }
}

# ============================================================================
# STATISTICAL THRESHOLDS
# ============================================================================

STATISTICAL_THRESHOLDS = {
    "var_confidence_levels": {
        "low": 0.90,    # 90% confidence
        "medium": 0.95,  # 95% confidence
        "high": 0.99,    # 99% confidence
    },
    "correlation_ranges": {
        "perfect_positive": (0.8, 1.0),
        "strong_positive": (0.6, 0.8),
        "moderate_positive": (0.4, 0.6),
        "weak_positive": (0.2, 0.4),
        "negligible": (-0.2, 0.2),
        "weak_negative": (-0.4, -0.2),
        "moderate_negative": (-0.6, -0.4),
        "strong_negative": (-0.8, -0.6),
        "perfect_negative": (-1.0, -0.8),
    },
    "risk_classification": {
        "low_volatility": (0, 1.5),      # % daily return std dev
        "medium_volatility": (1.5, 3.0),
        "high_volatility": (3.0, 5.0),
        "very_high_volatility": (5.0, 100),
    }
}

# ============================================================================
# MONTE CARLO SIMULATION PARAMETERS
# ============================================================================

SIMULATION_PARAMS = {
    "num_simulations": 10000,
    "time_horizon": 252,  # Trading days (1 year)
    "confidence_level": 0.95,
    "time_steps": 252,
    "use_historical_correlation": True,
}

# ============================================================================
# VISUALIZATION SETTINGS
# ============================================================================

VISUALIZATION_CONFIG = {
    "figure_size": (14, 8),
    "dpi": 300,
    "font_size": 10,
    "colors": {
        "positive": "#2E7D32",  # Green
        "negative": "#C62828",  # Red
        "neutral": "#1565C0",   # Blue
        "correlation_positive": "#E74C3C",  # Red
        "correlation_negative": "#3498DB", # Blue
    },
    "heatmap_cmap": "RdYlBu_r",  # Red-Yellow-Blue reversed
}

# ============================================================================
# FILE PATHS
# ============================================================================

DATA_PATHS = {
    "source_data": r"c:\Users\mohum\Downloads\archive (3)",
    "processed_base": r"c:\Users\mohum\OneDrive\Desktop\Financial Analytics - Portfolio Risk & Volatility Monitor\processed_data",
    "cleaned_data": r"c:\Users\mohum\OneDrive\Desktop\Financial Analytics - Portfolio Risk & Volatility Monitor\processed_data\cleaned_data",
    "daily_returns": r"c:\Users\mohum\OneDrive\Desktop\Financial Analytics - Portfolio Risk & Volatility Monitor\processed_data\daily_returns",
    "visualizations": r"c:\Users\mohum\OneDrive\Desktop\Financial Analytics - Portfolio Risk & Volatility Monitor\visualizations",
}

# ============================================================================
# SECTOR ALLOCATION (STRATEGIC WEIGHTS)
# ============================================================================

SECTOR_ALLOCATION = {
    "Information Technology": 0.15,      # 15%
    "Banking & Financial Services": 0.20,  # 20%
    "Energy": 0.12,                      # 12%
    "Heavy Industries & Construction": 0.12,  # 12%
    "Consumer Goods": 0.12,              # 12%
    "Automobiles & Components": 0.10,    # 10%
    "Pharmaceuticals": 0.08,             # 8%
    "Utilities": 0.05,                   # 5%
    "Telecommunications": 0.03,          # 3%
    "Other": 0.03,                       # 3%
}

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def get_all_tickers():
    """Extract all ticker symbols from STOCKS dictionary"""
    tickers = []
    for category, stocks_list in STOCKS.items():
        tickers.extend([stock['ticker'] for stock in stocks_list])
    return tickers

def get_sector_stocks(sector_name):
    """Get all stocks in a specific sector"""
    sector_stocks = []
    for category, stocks_list in STOCKS.items():
        sector_stocks.extend([
            stock for stock in stocks_list 
            if stock['sector'].lower() == sector_name.lower()
        ])
    return sector_stocks

def get_stock_info(ticker):
    """Get detailed information about a specific stock"""
    for category, stocks_list in STOCKS.items():
        for stock in stocks_list:
            if stock['ticker'] == ticker:
                return stock
    return None

def save_config_as_json(output_path=None):
    """Save configuration to JSON file"""
    if output_path is None:
        output_path = Path(DATA_PATHS['processed_base']) / 'config.json'
    
    config = {
        'portfolio_config': PORTFOLIO_CONFIG,
        'stocks': STOCKS,
        'validation_rules': DATA_VALIDATION_RULES,
        'statistical_thresholds': STATISTICAL_THRESHOLDS,
        'simulation_params': SIMULATION_PARAMS,
    }
    
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w') as f:
        json.dump(config, f, indent=2)
    
    return output_path

# ============================================================================
# SUMMARY STATISTICS
# ============================================================================

def print_portfolio_summary():
    """Print portfolio composition summary"""
    print("\n" + "=" * 70)
    print("PORTFOLIO COMPOSITION - AlphaPulse")
    print("=" * 70)
    
    total_stocks = sum(len(stocks) for stocks in STOCKS.values())
    print(f"\nTotal Stocks: {total_stocks}")
    
    print("\nStocks by Sector:")
    for category, stocks_list in STOCKS.items():
        if stocks_list and category != 'benchmark':
            print(f"  {category.upper()}: {len(stocks_list)} stocks")
            for stock in stocks_list:
                print(f"    - {stock['ticker']:15} ({stock['name']})")
    
    print("\n" + "=" * 70)

# ============================================================================
# EXECUTION
# ============================================================================

if __name__ == "__main__":
    print("Portfolio Configuration Module")
    print(f"Product: {PORTFOLIO_CONFIG['product_brand']}")
    print(f"Version: {PORTFOLIO_CONFIG['version']}")
    
    # Print summary
    print_portfolio_summary()
    
    # Print sample information
    print("\nSample Stock Information:")
    print(f"TCS: {get_stock_info('TCS')}")
    
    print("\nTechnology Stocks:")
    tech_stocks = get_sector_stocks("Information Technology")
    for stock in tech_stocks:
        print(f"  - {stock['ticker']}")
    
    print("\nAllocation by Sector:")
    for sector, allocation in SECTOR_ALLOCATION.items():
        print(f"  {sector:40} {allocation*100:>5.1f}%")
    
    # Save configuration
    config_path = save_config_as_json()
    print(f"\n✓ Configuration saved to: {config_path}")
