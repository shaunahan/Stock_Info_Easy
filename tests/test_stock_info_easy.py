from stock_info_easy import stock_info_easy
import pytest

# test the function that converts a company name into a symbol.
def test_get_symbol():

    actual1 = stock_info_easy.get_symbol('apple')
    expected1 = 'AAPL'
    actual2 = stock_info_easy.get_symbol('APPLE INC.')
    expected2 = 'AAPL'
    actual3 = stock_info_easy.get_symbol('APPLE company')
    expected3 = 'No Symbol Found'
    assert actual1 == expected1
    assert actual2 == expected2
    assert actual3 == expected3

    try:
        actual5 = stock_info_easy.get_symbol('')
    except KeyError:
        print("A key Error: Insert an input.")
    try:
        actual6 = stock_info_easy.get_symbol()
    except TypeError:
        print("Type Error: A parameter is missing.")


def test_get_hist_data():
    
    comp_names = ['amazon', 'apple', 'google', 'microsoft']
    col_list = ['Open','High','Low','Close','Adj Close','Volume','company_name', 'company_fullname']

    # test 1:
    actual = stock_info_easy.get_hist_data(comp_names)[0]
    for c in actual.columns:
        if c not in col_list:
            raise ValueError("Column name not found")

    # test 2:
    actual1 = stock_info_easy.get_hist_data(comp_names)[1]
    expected_comp_name_abbr = ['AMZN', 'AAPL', 'GOOG', 'MSFT']
    assert actual1 == expected_comp_name_abbr

    # test 3:
    comp_names2 = ['lg electronics', 'samsung electronics']
    actual2 = stock_info_easy.get_hist_data(comp_names2)[1]
    expected2 = ['066570.KS', '005930.KS']
    assert actual2 == expected2
    assert len(stock_info_easy.get_hist_data(comp_names2)[1]) == 2
   

    