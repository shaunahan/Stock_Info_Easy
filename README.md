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
  - **Stock Price Forecasts** using a Time Series LSTM Model.
  - An audio summary file containing daily key stock information.

## Machine Learning Model

This package leverages a **Long Short-Term Memory (LSTM) Model**, a type of recurrent neural network commonly used for time series predictions, to forecast future stock prices. The model is trained on historical stock data to predict trends. Key parameters of the model include:

- **Sliding Window Size**: Determines the historical data window used for training.
- **Prediction Window Size**: Specifies how many days ahead to predict.
- The ML model generates a visualization comparing predicted stock prices with actual historical prices.

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

## Audio Summary

An audio file is generated using Text-to-Speech (TTS) technology, providing a daily update on key stock information. The summary includes:

- **Company's Full Name**
- **PE Ratio**
- **Sector and Industry**
- **Daily Stock Price Information**

## Installation

To install the package, use the following command:

```bash
pip install stock-info-easy
