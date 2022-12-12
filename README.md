# stock_info_easy

This Python package is an implementation of the existing yfinance wrapper, one of the  widely used yahoo finance API wrapper.
One drawback of the existing yahoo finance API wrapper was its inability to fetch a company's using the company name; it can only fetch stock data with company symbol registered on the Yahoo Finance. <br>
To improve the functionality of the previous wrapper, this package enables a user to query a company with its full name.
By simply typing a company name, this pacakage will generate today's stock information for the company of interest. 

The fetched data includes: <br>
<p align="center"> _company name, open, high, low, close (closing price), adj close, volume, daily return, and PE ratios._ <br>
The stock information will be provided in dynamic formats with the use of __visualizations, a data table, a stock forecast and an audio file__. 

## Installation

```bash
$ pip install stock_info_easy
```


## Usage
To execute the package, __simply type the names of companies__. <br>
In the terminal, type:  
```python
>>> # Example 1: Only specify a company name(s) to query, using all other parameters as default.
>>> stock_info_easy.py --comp_names amazon, apple, microsoft, google 

>>> # Example 2: Specify a company name and a start date. 
>>> stock_info_easy.py --comp_names amazon --start_date 11/11/2022  # end_date is today's date by default.

>>> # Example 3: Specify whether to include a closing price forecast or not.
>>> stock_info_easy.py --comp_names amazon --start_date 11/11/2022  --end_date 12/12/2022 --predict_future_price True
```
## Output

#### 1. Visualization of Closing Price
<p align="center">
<img src="https://github.com/shaunahan/Stock_Info_Easy/blob/main/img/closing_price.png" style="zoom:50%;" />
</p>
<br>

#### 2. Visualization of Daily Return
<p align="center">
<img src="https://github.com/shaunahan/Stock_Info_Easy/blob/main/img/daily_return.png" style="zoom:50%;" />
</p>
<br>

#### 3. Audio file on Stock Info
This package provides key stock information such as PE ratio and basic company information of all queries companies in an audio format. 
```python
>>> stock_info_easy.py --audio_filename hello.mp3
```

#### 4. Prediction on Closing Price
This package uses the time series LSTM vanila model to predict the closing price. 
LSTM model is built with two hidden LSTM layers followed by a standard feedforward output layer. 
To disable the prediction function, set `--predict_future_price False`.

```python
>>> # Example 1: Set `--predict_future_price False` to skip the stock forecasting step. 
>>> stock_info_easy.py --comp_names google --start_date 11/11/2022  --end_date 12/12/2022 --predict_future_price False

>>> # Example 2: A query made using all parameters.
>>> stock_info_easy.py --comp_names google --start_date 09/01/2022 -end_date 12/10/2022 --window_size 15 --prediction_window_size 3 --predict_future_price True --audio_filename hello.mp3
```
<p align="center">
<img src="https://github.com/shaunahan/Stock_Info_Easy/blob/main/img/closing_price_forecast.png" style="zoom:50%;" />
</p>
<br>


## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`stock_info_easy` was created by Shauna Han. It is licensed under the terms of the MIT license.

## Credits

`stock_info_easy` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
