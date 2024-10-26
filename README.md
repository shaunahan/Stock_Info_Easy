# Stock Info Easy

## Overview

This Python package builds upon the popular `yfinance` wrapper, a widely-used interface for the Yahoo Finance API. While many existing Yahoo Finance API wrappers require company symbols as input, this package offers enhanced functionality by allowing users to query stock data directly using company names.

## Motivation

Standard Yahoo Finance API wrappers often require precise company symbols, which can be confusing and difficult to recall. For example, identifying Apple's symbol—whether it's `APPL`, `AAPL`, or `APLE`—is not intuitive. (Answer: Apple's symbol is `AAPL`).

To address this challenge, this package simplifies stock data retrieval by enabling queries through company names, making it more user-friendly.

## Key Features

- **Company Name Queries**: Retrieve stock data using company names, eliminating the need to remember or look up company symbols.
- **Dynamic Data Output**: The package generates stock data in multiple formats, including:
  - Visualizations of stock trends.
  - A comprehensive data table with key financial metrics.
  - Stock price forecasts.
  - An audio summary file containing daily key stock information.

## Data Table Details

The fetched data includes:

- **Company Name**
- **Open** (Opening Price)
- **High** (Highest Price of the Day)
- **Low** (Lowest Price of the Day)
- **Close** (Closing Price)
- **Adj Close** (Adjusted Closing Price)
- **Volume** (Trading Volume)
- **Daily Return** (Percentage Change)
- **PE Ratios** (Price-to-Earnings Ratios)

This package is designed to make financial data more accessible, intuitive, and dynamic for users.
