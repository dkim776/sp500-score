from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt

ts = TimeSeries(key='6ZZDQUNK7YMNQSUL', output_format='pandas')
data, meta_data = ts.get_daily(symbol='.INX')
data['4. close'].plot()
plt.title('Intraday Times Series')
plt.show()
