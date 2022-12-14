# Stock_Info_Easy

This Python package is an implementation of the existing  _yfinance wrapper_, one of the  widely used yahoo finance API wrappers.<br>


The currently available Yahoo finance API wrappers take __company symbols__ as input queries instead of company names, and this often causes confusion as it is difficult to guess company symbols by heart. <br>
(eg. what is the abbreviation of the company _Apple, is it `APPL`? `AAPL`? or `APLE`?  (ans: In fact, the company symbol of apple is AAPL)_  

Therefore, this package aims to provide an improved functionality of querying by : 
<p align="center"> <b> making it possible for users to fetch stock data by company name(s) alone! </b> <br><br> </p>
Additionally, this package generates the stock data in dynamic formats, such as <i> visualizations, data table, stock price forecast, and an audio file with daily prime stock price. </i>
<br>

The fetched data table includes: <br>
* _`company name, open, high, low, close (closing price), adj close, volume, daily return, and PE ratios.`_<br>
<br>


## Installation

```bash
$ pip install stock_info_easy
```


## Usage

### 1. Fetch Stock Data
Insert the name of a company inside the `get_hist_data` function. _ex) ['amazon', 'apple', 'google', 'microsoft']_
```python

# By default, today's date will be used as an end date when not specified. 

>>> data_list, comp_names_abbr, company_list, comp_names = \
stock_info_easy.get_hist_data((['amazon', 'apple', 'google', 'microsoft']), \
start_date="01/04/2022", end_date = "2022-01-10") 

```

```python

# To view the stock data as a table, 
# Type "data_list" (to view all) or "company_list[i]", i = index of the company. 

# stock info of all queried companies.
>>> data_list 
```

<p align="center">
<img src="https://github.com/shaunahan/Stock_Info_Easy/blob/main/img/data_list.png" width="730" height="350"/>
</p>
<br>

```python

# first company info. (amazon)
>>> company_list[0]  
```
<p align="center">
<img src="https://github.com/shaunahan/Stock_Info_Easy/blob/main/img/company_list[0].png" width="730" height="350"/>
</p>
<br>

```python

# second company info. (apple)
>>> company_list[1]  
```
<p align="center">
<img src="https://github.com/shaunahan/Stock_Info_Easy/blob/main/img/company_list[1].png" width="730" height="350"/>
</p>
<br>


### 2. Visualization of Closing Price

```python

# To generate the visualization of Closing Price, copy-paste below function as it is.
>>> get_closing_price_viz(company_list, comp_names) 
```
<p align="center">
<img src="https://github.com/shaunahan/Stock_Info_Easy/blob/main/img/closing_price_.png" width="1000" height="450"/>
</p>
<br>

### 3. Visualization of Daily Return

```python

# To generate the visualization of Daily Return, copy-paste below function as it is.
>>> get_daily_return_viz(company_list, company_names)
```
<p align="center">
<img src="https://github.com/shaunahan/Stock_Info_Easy/blob/main/img/daily_return_.png" width="750" height="430" />
</p>

### 4. Prime Stock Info on Audio
This package provides key stock information such as PE ratio and basic company information of all queries companies in an audio format. 

```python

# To genrate an audio file, copy-paste below function. 
# Can customize the audio filename in the "audio_filename" parameter.
>>> generate_audio(comp_names_abbr, audio_filename='default1.mp3') 
```
<br>

### 5. Prediction on Closing Price
This package uses the time series LSTM vanila model to predict the closing price. 
LSTM model is built with two hidden LSTM layers followed by a standard feedforward output layer. 

```python
# Copy-paste the below function.
# The window size and prediction window size can be customized. 

>>> stock_info_easy.predict_future_price(data_list, comp_names_abbr, \
windown_size=30, predict_window_size=10, predict=True)

```
<p align="center">
<img src="https://github.com/shaunahan/Stock_Info_Easy/blob/main/img/predict_amazon.png", width="650" height="300" />
<img src="https://github.com/shaunahan/Stock_Info_Easy/blob/main/img/predict_apple.png", width="650" height="300" />
<img src="https://github.com/shaunahan/Stock_Info_Easy/blob/main/img/predict_google.png", width="650" height="300" />
<img src="https://github.com/shaunahan/Stock_Info_Easy/blob/main/img/predict_microsoft.png", width="650" height="300" />
</p>
<br>


## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`stock_info_easy` was created by Shauna Han. It is licensed under the terms of the MIT license.

## Credits

`stock_info_easy` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
