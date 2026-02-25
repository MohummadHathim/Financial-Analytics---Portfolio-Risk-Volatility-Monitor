"""
Financial Analytics - Portfolio Risk & Volatility Monitor (AlphaPulse)
Week 1: Data Acquisition & Validation
Purpose: Load, clean, validate, and prepare historical stock data for analysis
"""

import pandas as pd
import numpy as np
import os
from pathlib import Path
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

class DataAcquisitionPipeline:
    """
    Handles data loading, cleaning, and validation for the portfolio analysis
    """
    
    def __init__(self, data_source_path):
        """
        Initialize the pipeline with data source directory
        
        Args:
            data_source_path: Path to directory containing CSV files
        """
        self.data_source_path = data_source_path
        self.raw_data = {}
        self.cleaned_data = {}
        self.daily_returns = {}
        self.validation_report = {}
        
    def load_data(self):
        """
        Load all CSV files from the specified directory
        """
        print("=" * 70)
        print("STEP 1: DATA LOADING")
        print("=" * 70)
        
        csv_files = list(Path(self.data_source_path).glob('*.csv'))
        
        if not csv_files:
            print(f"No CSV files found in {self.data_source_path}")
            return False
        
        print(f"Found {len(csv_files)} CSV files")
        
        for file_path in csv_files:
            try:
                filename = file_path.stem  # Get filename without extension
                df = pd.read_csv(file_path)
                self.raw_data[filename] = df
                print(f"✓ Loaded {filename}: {df.shape[0]} rows × {df.shape[1]} columns")
            except Exception as e:
                print(f"✗ Error loading {file_path.name}: {str(e)}")
        
        print(f"\nSuccessfully loaded {len(self.raw_data)} datasets\n")
        return True
    
    def inspect_data_structure(self):
        """
        Inspect the structure of loaded datasets
        """
        print("=" * 70)
        print("STEP 2: DATA STRUCTURE INSPECTION")
        print("=" * 70)
        
        # Examine first stock dataset
        sample_stock = list(self.raw_data.keys())[0]
        df_sample = self.raw_data[sample_stock]
        
        print(f"\nSample Dataset: {sample_stock}")
        print(f"Shape: {df_sample.shape}")
        print(f"\nColumns: {list(df_sample.columns)}")
        print(f"\nData Types:\n{df_sample.dtypes}")
        print(f"\nFirst 3 rows:\n{df_sample.head(3)}")
        print(f"\nBasic Statistics:\n{df_sample.describe()}")
        print()
    
    def handle_missing_data(self, method='forward_fill'):
        """
        Handle missing data using specified method
        
        Args:
            method: 'forward_fill' or 'drop'
        """
        print("=" * 70)
        print("STEP 3: HANDLING MISSING DATA")
        print("=" * 70)
        
        for ticker, df in self.raw_data.items():
            # Check for missing values
            missing_before = df.isnull().sum().sum()
            
            if missing_before > 0:
                if method == 'forward_fill':
                    df_filled = df.fillna(method='ffill').fillna(method='bfill')
                    missing_after = df_filled.isnull().sum().sum()
                    print(f"✓ {ticker}: {missing_before} missing values → {missing_after} (Forward Fill)")
                    self.cleaned_data[ticker] = df_filled
                elif method == 'drop':
                    df_dropped = df.dropna()
                    rows_removed = len(df) - len(df_dropped)
                    print(f"✓ {ticker}: Dropped {rows_removed} rows with missing values")
                    self.cleaned_data[ticker] = df_dropped
            else:
                print(f"✓ {ticker}: No missing values found")
                self.cleaned_data[ticker] = df
        
        print()
    
    def validate_date_format(self):
        """
        Validate and standardize date formats
        """
        print("=" * 70)
        print("STEP 4: DATE FORMAT VALIDATION")
        print("=" * 70)
        
        for ticker, df in self.cleaned_data.items():
            # Find date column (common names: 'Date', 'date', 'DATE')
            date_col = None
            for col in df.columns:
                if col.lower() == 'date':
                    date_col = col
                    break
            
            if date_col is None:
                print(f"⚠ {ticker}: No date column found")
                continue
            
            try:
                # Convert to datetime
                df[date_col] = pd.to_datetime(df[date_col])
                df_sorted = df.sort_values(by=date_col)
                self.cleaned_data[ticker] = df_sorted
                
                date_range = f"{df_sorted[date_col].min().date()} to {df_sorted[date_col].max().date()}"
                print(f"✓ {ticker}: Date range: {date_range}")
            except Exception as e:
                print(f"✗ {ticker}: Error converting dates: {str(e)}")
        
        print()
    
    def validate_price_data(self):
        """
        Validate price data for anomalies and outliers
        """
        print("=" * 70)
        print("STEP 5: PRICE DATA VALIDATION")
        print("=" * 70)
        
        issues_found = {}
        
        for ticker, df in self.cleaned_data.items():
            issues = []
            
            # Identify price columns
            price_cols = [col for col in df.columns if col.lower() in ['close', 'open', 'high', 'low']]
            
            for col in price_cols:
                if df[col].dtype in ['float64', 'int64']:
                    # Check for negative prices
                    if (df[col] < 0).any():
                        neg_count = (df[col] < 0).sum()
                        issues.append(f"  - {col}: {neg_count} negative prices")
                    
                    # Check for zero prices
                    if (df[col] == 0).any():
                        zero_count = (df[col] == 0).sum()
                        issues.append(f"  - {col}: {zero_count} zero prices")
            
            if issues:
                issues_found[ticker] = issues
                print(f"⚠ {ticker}:")
                for issue in issues:
                    print(issue)
            else:
                print(f"✓ {ticker}: All price data valid")
        
        print()
        return issues_found
    
    def calculate_daily_returns(self):
        """
        Calculate daily percentage returns
        Formula: Daily Return = (Close_t - Close_t-1) / Close_t-1 * 100
        """
        print("=" * 70)
        print("STEP 6: CALCULATE DAILY RETURNS")
        print("=" * 70)
        
        for ticker, df in self.cleaned_data.items():
            # Find close price column
            close_col = None
            for col in df.columns:
                if col.lower() == 'close':
                    close_col = col
                    break
            
            if close_col is None:
                print(f"⚠ {ticker}: No 'Close' column found for returns calculation")
                continue
            
            try:
                # Calculate daily returns
                df_copy = df.copy()
                df_copy['Daily_Return'] = df_copy[close_col].pct_change() * 100
                
                # Remove first row (NaN return)
                df_copy = df_copy.dropna(subset=['Daily_Return'])
                
                self.daily_returns[ticker] = df_copy[['Daily_Return']]
                
                # Summary statistics
                mean_return = df_copy['Daily_Return'].mean()
                std_return = df_copy['Daily_Return'].std()
                min_return = df_copy['Daily_Return'].min()
                max_return = df_copy['Daily_Return'].max()
                
                print(f"✓ {ticker}:")
                print(f"  - Mean Daily Return: {mean_return:>8.4f}%")
                print(f"  - Std Deviation:     {std_return:>8.4f}%")
                print(f"  - Min Return:        {min_return:>8.4f}%")
                print(f"  - Max Return:        {max_return:>8.4f}%")
                
            except Exception as e:
                print(f"✗ {ticker}: Error calculating returns: {str(e)}")
        
        print()
    
    def detect_stock_splits_dividends(self):
        """
        Detect potential stock splits and unusual price movements
        Stock splits typically cause sharp price drops (20-50%)
        """
        print("=" * 70)
        print("STEP 7: DETECT ANOMALIES (Stock Splits & Dividends)")
        print("=" * 70)
        
        anomalies_detected = {}
        
        for ticker, df in self.cleaned_data.items():
            # Find close column
            close_col = None
            for col in df.columns:
                if col.lower() == 'close':
                    close_col = col
                    break
            
            if close_col is None:
                continue
            
            anomalies = []
            
            # Calculate day-to-day price changes
            price_changes = df[close_col].pct_change() * 100
            
            # Detect unusual movements (potential stock splits)
            # Threshold: price drops > 20% or increases > 20%
            threshold = 20
            unusual_days = price_changes[abs(price_changes) > threshold]
            
            if len(unusual_days) > 0:
                for date, change in unusual_days.items():
                    anomalies.append((date, df.loc[date, close_col], change))
            
            if anomalies:
                anomalies_detected[ticker] = anomalies
                print(f"⚠ {ticker}: {len(anomalies)} anomalies detected")
                for date, price, change in anomalies[:3]:  # Show first 3
                    print(f"  - {date}: Price Change: {change:>7.2f}% (Close: {price:.2f})")
                if len(anomalies) > 3:
                    print(f"  - ... and {len(anomalies) - 3} more")
            else:
                print(f"✓ {ticker}: No anomalies detected")
        
        print()
        return anomalies_detected
    
    def generate_validation_report(self):
        """
        Generate comprehensive validation report
        """
        print("=" * 70)
        print("STEP 8: DATA VALIDATION SUMMARY REPORT")
        print("=" * 70)
        
        report = {
            'Total Datasets Loaded': len(self.raw_data),
            'Datasets After Cleaning': len(self.cleaned_data),
            'Daily Returns Calculated': len(self.daily_returns),
            'Timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        # Portfolio composition
        portfolio_tickers = list(self.cleaned_data.keys())
        
        print(f"\nPortfolio Composition ({len(portfolio_tickers)} stocks):")
        for ticker in sorted(portfolio_tickers)[:10]:
            print(f"  - {ticker}")
        if len(portfolio_tickers) > 10:
            print(f"  ... and {len(portfolio_tickers) - 10} more")
        
        # Sector breakdown (based on ticker categories)
        print(f"\nTotal Stocks in Portfolio: {len(portfolio_tickers)}")
        
        # Date range statistics
        all_dates = []
        for ticker, df in self.cleaned_data.items():
            date_col = [col for col in df.columns if col.lower() == 'date']
            if date_col:
                all_dates.extend(df[date_col[0]].unique())
        
        if all_dates:
            min_date = min(pd.to_datetime(all_dates))
            max_date = max(pd.to_datetime(all_dates))
            print(f"\nData Coverage:")
            print(f"  - Earliest Date: {min_date.date()}")
            print(f"  - Latest Date:   {max_date.date()}")
            print(f"  - Span:          {(max_date - min_date).days} days")
        
        print()
        return report
    
    def save_cleaned_data(self, output_dir):
        """
        Save cleaned data and daily returns for next phase
        """
        print("=" * 70)
        print("STEP 9: SAVE PROCESSED DATA")
        print("=" * 70)
        
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        
        # Save cleaned data
        cleaned_dir = output_path / "cleaned_data"
        cleaned_dir.mkdir(exist_ok=True)
        
        for ticker, df in self.cleaned_data.items():
            output_file = cleaned_dir / f"{ticker}_cleaned.csv"
            df.to_csv(output_file, index=False)
            print(f"✓ Saved {ticker}_cleaned.csv")
        
        # Save daily returns
        returns_dir = output_path / "daily_returns"
        returns_dir.mkdir(exist_ok=True)
        
        for ticker, df in self.daily_returns.items():
            output_file = returns_dir / f"{ticker}_returns.csv"
            df.to_csv(output_file, index=True)
            print(f"✓ Saved {ticker}_returns.csv")
        
        # Save consolidated returns dataframe for correlation analysis
        if self.daily_returns:
            returns_combined = pd.concat(self.daily_returns, axis=1)
            returns_combined.columns = self.daily_returns.keys()
            returns_combined.to_csv(output_path / "portfolio_daily_returns.csv", index=True)
            print(f"✓ Saved portfolio_daily_returns.csv")
        
        print()
    
    def run_full_pipeline(self, output_dir="processed_data"):
        """
        Execute the complete data acquisition and validation pipeline
        """
        print("\n")
        print("╔" + "=" * 68 + "╗")
        print("║" + " " * 10 + "FINANCIAL ANALYTICS - WEEK 1 DATA PIPELINE" + " " * 17 + "║")
        print("║" + " " * 15 + "AlphaPulse: Portfolio Risk & Volatility" + " " * 16 + "║")
        print("╚" + "=" * 68 + "╝")
        print()
        
        # Execute pipeline steps
        if not self.load_data():
            return False
        
        self.inspect_data_structure()
        self.handle_missing_data(method='forward_fill')
        self.validate_date_format()
        self.validate_price_data()
        self.calculate_daily_returns()
        self.detect_stock_splits_dividends()
        self.generate_validation_report()
        self.save_cleaned_data(output_dir)
        
        print("=" * 70)
        print("✓ PIPELINE EXECUTION COMPLETE")
        print("=" * 70)
        print()
        
        return True


# ============================================================================
# EXECUTION
# ============================================================================

if __name__ == "__main__":
    # Update this path to your data directory
    DATA_SOURCE_PATH = r"c:\Users\mohum\Downloads\archive (3)"
    
    # Initialize and run pipeline
    pipeline = DataAcquisitionPipeline(DATA_SOURCE_PATH)
    pipeline.run_full_pipeline()
