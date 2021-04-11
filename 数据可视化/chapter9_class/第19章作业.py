import tushare as ts
ticker = '600028'
f=ts.get_hist_data(ticker, '20', '2020-03-23')  #获取个股历史交易数据
f.head()