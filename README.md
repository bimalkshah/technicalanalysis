# tech_analysis

`tech_analysis` is a **pure Python**, dependency-free technical analysis library for financial markets. It includes a wide array of technical indicators, overlays, price action patterns, performance metrics, and risk management tools — designed for traders, quants, and researchers.

> No NumPy. No pandas. Just raw Python logic — fully portable and customizable.



---

## Features

- **Indicators**: RSI, MACD, ATR, CCI, TRIX, Bollinger Bands, ROC, Stochastic, etc.
- **Volume Tools**: OBV, PVT, MFI, Chaikin, Ease of Movement
- **Price Patterns**: is_inverted_hammer,
is_shooting_star,
is_morning_star,
is_evening_star,
is_bullish_harami,
is_bearish_harami,
is_three_white_soldiers,
is_three_black_crows,
is_tweezer_top,
is_tweezer_bottom,
is_piercing_line,
is_dark_cloud_cover,
is_rising_three_methods,
is_falling_three_methods,
is_inside_bar,
is_outside_bar,
is_marubozu,
is_inside_day_breakout,
break_of_structure,
- **Breadth Indicators**: Advance/Decline Line, A/D Ratio, New High-Low
- **Overlays**: SMA, EMA, Donchian Channels, MA Ribbons
- **Risk Management**: Kelly Criterion, Max Drawdown, Position Sizing, Monte Carlo
- **Performance Metrics**: Sharpe, Sortino, Calmar, CAGR, Beta, Volatility
- **forecast**: 

- **100% Pure Python**: No external packages required

---


```python
def greet():
    print("Hello, GitHub!")
greet()
```

# tech_analysis.breadth

This module provides market breadth indicators, which are used to evaluate the overall health or trend of a financial market based on the number of advancing and declining stocks. These indicators are essential for technical analysis and can help traders understand market dynamics.

1. advance_decline(advancing, declining)

Description
The advance_decline function computes the Advance-Decline Line (AD Line), which is a cumulative measure of the net advancing stocks. The AD Line is used to gauge the strength or weakness of market movements by tracking the difference between advancing and declining issues over time.

Parameters
advancing (list of float): A list of values representing the number of advancing stocks for each period.
declining (list of float): A list of values representing the number of declining stocks for each period.
Returns
list of float: A list of cumulative net advancing stocks (AD Line).
Example Usage
# Sample data: advancing and declining stocks for each period
advancing = [100, 120, 110]
declining = [80, 90, 105]

# Calculate the Advance-Decline Line
ad_line = advance_decline(advancing, declining)
print(ad_line)
# Output: [20, 50, 55]
Explanation
In the example:

Period 1: (100 advancing - 80 declining) = 20
Period 2: (120 advancing - 90 declining) = 30, cumulative AD Line = 20 + 30 = 50
Period 3: (110 advancing - 105 declining) = 5, cumulative AD Line = 50 + 5 = 55

2. advance_decline_ratio(advancing, declining)

Description
The advance_decline_ratio function calculates the Advance-Decline Ratio, which is the ratio of advancing stocks to declining stocks. This ratio is useful for gauging the relative strength of the market in terms of advancing and declining issues.

Parameters
advancing (list of float): A list of values representing the number of advancing stocks for each period.
declining (list of float): A list of values representing the number of declining stocks for each period.
Returns
list of float: A list containing the Advance-Decline Ratio for each period. If the declining value is 0, the ratio is set to 0.
Example Usage
# Sample data: advancing and declining stocks for each period
advancing = [100, 120]
declining = [50, 60]

# Calculate the Advance-Decline Ratio
adr = advance_decline_ratio(advancing, declining)
print(adr)
# Output: [2.0, 2.0]
Explanation
Period 1: (100 advancing / 50 declining) = 2.0
Period 2: (120 advancing / 60 declining) = 2.0

3. new_highs_lows(new_highs, new_lows)

Description
The new_highs_lows function calculates the difference between new highs and new lows over a given period. This indicator can be used to assess market strength based on the number of new highs versus new lows.

Parameters
new_highs (list of float): A list of values representing the number of new highs for each period.
new_lows (list of float): A list of values representing the number of new lows for each period.
Returns
list of float: A list representing the difference between new highs and new lows for each period.
Example Usage
# Sample data: new highs and new lows for each period
new_highs = [30, 50]
new_lows = [10, 60]

# Calculate the difference between new highs and new lows
highs_lows_diff = new_highs_lows(new_highs, new_lows)
print(highs_lows_diff)
# Output: [20, -10]
Explanation
Period 1: (30 new highs - 10 new lows) = 20
Period 2: (50 new highs - 60 new lows) = -10

4. trinar_indicator(advancing, declining, unchanged)

Description
The trinar_indicator function calculates the TRINAR Indicator (Trinary Advance Ratio), which is used to measure the market's internal strength by considering the number of advancing, declining, and unchanged stocks. This indicator can help determine whether the market is overbought or oversold.

Parameters
advancing (list of float): A list of values representing the number of advancing stocks for each period.
declining (list of float): A list of values representing the number of declining stocks for each period.
unchanged (list of float): A list of values representing the number of unchanged stocks for each period.
Returns
list of float: A list representing the TRINAR indicator value for each period. The value is calculated as (advancing - declining) / (advancing + declining + unchanged).
Example Usage
# Sample data: advancing, declining, and unchanged stocks for each period
advancing = [100, 120]
declining = [80, 60]
unchanged = [20, 20]

# Calculate the TRINAR Indicator
trinar = trinar_indicator(advancing, declining, unchanged)
print(trinar)
# Output: [0.2, 0.5]
Explanation
Period 1: (100 advancing - 80 declining) / (100 + 80 + 20 unchanged) = 0.2
Period 2: (120 advancing - 60 declining) / (120 + 60 + 20 unchanged) = 0.5
Conclusion

These functions in the tech_analysis.breadth module help analyze market breadth and provide insights into market trends by comparing the number of advancing, declining, unchanged, new highs, and new lows across various periods. By incorporating these indicators into a technical analysis strategy, traders and analysts can gain a deeper understanding of market strength or weakness.

Example Workflow
To use these indicators in a market analysis:

# Sample data for advancing, declining, unchanged, new highs, and new lows
advancing = [100, 120, 110]
declining = [80, 90, 105]
unchanged = [20, 20, 15]
new_highs = [30, 50, 45]
new_lows = [10, 60, 25]

# Calculate breadth indicators
ad_line = advance_decline(advancing, declining)
adr = advance_decline_ratio(advancing, declining)
highs_lows = new_highs_lows(new_highs, new_lows)
trinar = trinar_indicator(advancing, declining, unchanged)

# Print results
print(f"Advance-Decline Line: {ad_line}")
print(f"Advance-Decline Ratio: {adr}")
print(f"New Highs-Lows Difference: {highs_lows}")
print(f"TRINAR Indicator: {trinar}")


# tech_analysis.overlays

This module provides Moving Average functions to smooth out price data and identify trends in financial markets. The two most common types of moving averages are Simple Moving Average (SMA) and Exponential Moving Average (EMA). Both are used extensively in technical analysis for trend-following strategies.

1. sma(data, period)
Description

The sma function computes the Simple Moving Average (SMA) of a time series. The SMA is the arithmetic mean of the prices over a specified number of periods. It is used to smooth data, reducing short-term fluctuations, and highlighting longer-term trends.

Parameters

data (list of float): A list of numerical values (typically closing prices) representing the time series data for which the moving average is to be calculated.
period (int): The number of periods over which the average is calculated.
Returns

list of float or None: A list of SMA values for each period. For periods before the full window is reached, None is returned (as the moving average cannot be computed for those periods).
Example Usage

# Sample data: closing prices of a stock for 10 days
data = [100, 102, 104, 105, 107, 109, 110, 112, 113, 115]

# Calculate the 3-period Simple Moving Average (SMA)
sma_vals = sma(data, 3)
print(sma_vals)
# Output: [None, None, 102.0, 103.66666666666667, 105.33333333333333, 106.66666666666667, 108.66666666666667, 110.33333333333333, 111.33333333333333, 112.66666666666667]
Explanation

Period 1 and 2: No SMA value is returned because there are not enough data points to calculate the average.
Period 3: The SMA is calculated as the average of the first three data points: (100 + 102 + 104) / 3 = 102.0
This process continues, and the SMA values for subsequent periods are calculated by averaging the closing prices over the previous 3 periods.

2. ema(data, period)
Description

The ema function computes the Exponential Moving Average (EMA), which is a more advanced type of moving average that gives more weight to recent prices. The EMA reacts more quickly to recent price changes than the SMA, making it useful for more responsive trend-following strategies.

Parameters

data (list of float): A list of numerical values (typically closing prices) representing the time series data for which the moving average is to be calculated.
period (int): The number of periods over which the EMA is calculated.
Returns

list of float: A list of EMA values for each period. The first value is just the price itself (no moving average is calculated for the first data point).
Example Usage

# Sample data: closing prices of a stock for 10 days
data = [100, 102, 104, 105, 107, 109, 110, 112, 113, 115]

# Calculate the 3-period Exponential Moving Average (EMA)
ema_vals = ema(data, 3)
print(ema_vals)
# Output: [100, 101.0, 102.0, 103.0, 104.0, 105.0, 106.0, 107.0, 108.0, 109.0]


# Sample data: closing prices of a stock for 10 days
data = [100, 102, 104, 105, 107, 109, 110, 112, 113, 115]

# Calculate the 3-period Simple Moving Average (SMA)
sma_vals = sma(data, 3)
print("SMA:", sma_vals)

# Calculate the 3-period Exponential Moving Average (EMA)
ema_vals = ema(data, 3)
print("EMA:", ema_vals)
Output:
SMA: [None, None, 102.0, 103.66666666666667, 105.33333333333333, 106.66666666666667, 108.66666666666667, 110.33333333333333, 111.33333333333333, 112.66666666666667]
EMA: [100, 101.0, 102.0, 103.0, 104.0, 105.0, 106.0, 107.0, 108.0, 109.0]
In this example, the SMA and EMA values allow you to compare how each moving average reacts to the price data.



# tech_analysis.forecasting 

This module provides functions for performing forecasting using linear regression and moving averages. It also includes error metrics and ASCII visualization of the forecasts.

1. linear_regression(x, y)
Description

The linear_regression function calculates the linear regression parameters (slope b and intercept a) using the least squares method. This method fits a straight line to the data points represented by x (independent variable) and y (dependent variable).

Parameters

x (list of float): A list of independent variable values (e.g., time or index values).
y (list of float): A list of dependent variable values (e.g., stock prices or other measured quantities).
Returns

a (float): The intercept of the regression line.
b (float): The slope of the regression line.
Example Usage

x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]

a, b = linear_regression(x, y)
print(f"Intercept: {a}, Slope: {b}")
# Output: Intercept: 2.2, Slope: 0.4
Explanation

This function computes the best-fit line for the provided data points using the formulas for the slope (b) and intercept (a) of a linear regression model.

2. predict_linear(x, a, b)
Description

The predict_linear function uses the calculated linear regression parameters (a and b) to predict the values of y for given x values.

Parameters

x (list of float): A list of independent variable values (e.g., time or index values).
a (float): The intercept of the regression line.
b (float): The slope of the regression line.
Returns

list of float: A list of predicted values of the dependent variable.
Example Usage

x = [1, 2, 3, 4, 5]
a = 2.2
b = 0.4

predictions = predict_linear(x, a, b)
print(predictions)
# Output: [2.6, 3.0, 3.4, 3.8, 4.2]

3. moving_average(series, window=5)
Description

The moving_average function calculates the Simple Moving Average (SMA) for a time series with a specified window size. The moving average smooths out fluctuations in the data by averaging values over a rolling window.

Parameters

series (list of float): A list of numerical values (e.g., stock prices) representing the time series data.
window (int): The number of periods (data points) to use in calculating the moving average (default is 5).
Returns

list of float: A list of the moving average values for the time series.
Example Usage

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ma = moving_average(data, window=3)
print(ma)
# Output: [2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
Explanation

This function computes the average of the last window number of elements in the series for each point in time. For the first window-1 periods, it doesn't compute the moving average (i.e., it returns None).

3.  mean_squared_error(y_true, y_pred)
Description

The mean_squared_error function calculates the Mean Squared Error (MSE), which is a common metric used to measure the accuracy of a prediction model. MSE computes the average of the squared differences between actual and predicted values.

Parameters

y_true (list of float): A list of true values (actual values).
y_pred (list of float): A list of predicted values.
Returns

float: The Mean Squared Error (MSE) between the actual and predicted values.
Example Usage

y_true = [3, -0.5, 2, 7]
y_pred = [2.5, 0.0, 2, 8]

mse = mean_squared_error(y_true, y_pred)
print(mse)
# Output: 0.375

4. visualize_ascii(actual, predicted, step=5)
Description

The visualize_ascii function provides a simple ASCII visualization of the actual and predicted values. This function is helpful to visually assess how well the predicted values match the actual values over time.

Parameters

actual (list of float): A list of actual values (e.g., true stock prices).
predicted (list of float): A list of predicted values.
step (int): The step size for displaying every step-th value (default is 5).
Returns

None. It prints the ASCII visualization.
Example Usage

actual = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
predicted = [2.1, 3.0, 3.9, 5.1, 6.0, 6.9, 7.9, 9.0, 9.9, 11.1]

visualize_ascii(actual, predicted, step=2)
Explanation

For each pair of actual and predicted values, the function prints an ASCII graph to visually compare the two. Asterisks (*) represent the actual values, while dashes (-) represent the predicted values.

5. forecast_stock(data, method="linear", window=5)
Description

The forecast_stock function forecasts future stock prices using either linear regression or a moving average method. It returns the actual and predicted values along with the Mean Squared Error (MSE) for the predictions.

Parameters

data (list of float): A list of stock prices or other time-series data.
method (str): The forecasting method to use. Valid options are "linear" for linear regression or "moving_avg" for a moving average. Default is "linear".
window (int): The window size for the moving average (used if method="moving_avg"). Default is 5.
Returns

dict: A dictionary with the actual values, predicted values, and the mean squared error (MSE) of the prediction.
Example Usage

data = [100, 102, 105, 110, 115, 120, 125, 130, 135, 140]

# Forecast using linear regression
forecast = forecast_stock(data, method="linear")
print(forecast)

# Forecast using moving average
forecast = forecast_stock(data, method="moving_avg", window=3)
print(forecast)
Explanation

If method="linear", the function uses linear regression to predict future values based on the provided time-series data.
If method="moving_avg", it computes the moving average over the last window periods.
Conclusion
These functions help you perform various types of stock price forecasting and prediction tasks:

Linear Regression for trend modeling.
Moving Average for smoothing and trend-following.
Mean Squared Error (MSE) to evaluate prediction accuracy.
ASCII Visualization to visually compare predictions with actual values.


# tech_analysis.overlay

This module provides functions to compute various technical analysis indicators, including Simple Moving Averages (SMA), Exponential Moving Averages (EMA), and Donchian Channels.

1. moving_average_overlay(prices, periods=[20, 50, 200])
Description

The moving_average_overlay function calculates Simple Moving Averages (SMA) for a given list of prices over multiple periods. The function returns a dictionary where the keys are the period lengths and the values are the corresponding SMA values.

Parameters

prices (list of float): A list of numerical values representing the prices (e.g., closing prices of a stock).
periods (list of int, optional): A list of periods for which the moving averages will be calculated. Default is [20, 50, 200].
Returns

dict: A dictionary with the period as the key and the corresponding SMA values as the value.
Example Usage

prices = [100, 102, 104, 105, 107, 109, 110, 112, 113, 115]
overlay = moving_average_overlay(prices, periods=[3, 5])
print(overlay)
# Output: {3: [None, None, 102.0, 103.66666666666667, 105.33333333333333, 106.66666666666667, 108.66666666666667, 110.33333333333333, 111.33333333333333, 112.66666666666667], 
#          5: [None, None, None, None, 104.0, 105.4, 106.8, 107.8, 109.2, 110.2]}
Explanation

The function calculates the SMA for the provided periods (20, 50, and 200 by default).
For each period, the moving average is calculated by averaging the prices over the specified number of days.
For periods shorter than the given period (e.g., first few days), None is returned as the moving average cannot be computed.

2. exponential_moving_average_overlay(prices, periods=[20, 50, 200])
Description

The exponential_moving_average_overlay function calculates Exponential Moving Averages (EMA) for a given list of prices over multiple periods. The function returns a dictionary where the keys are the period lengths and the values are the corresponding EMA values.

Parameters

prices (list of float): A list of numerical values representing the prices (e.g., closing prices of a stock).
periods (list of int, optional): A list of periods for which the exponential moving averages will be calculated. Default is [20, 50, 200].
Returns

dict: A dictionary with the period as the key and the corresponding EMA values as the value.
Example Usage

prices = [100, 102, 104, 105, 107, 109, 110, 112, 113, 115]
ema_overlay = exponential_moving_average_overlay(prices, periods=[3, 5])
print(ema_overlay)
# Output: {3: [100, 101.0, 102.0, 103.0, 104.0, 105.0, 106.0, 107.0, 108.0, 109.0], 
#          5: [100, 101.0, 102.0, 103.0, 104.0, 105.0, 106.0, 107.0, 108.0, 109.0]}
Explanation

The function calculates the EMA for the provided periods (20, 50, and 200 by default).
The EMA places more weight on recent prices, making it more responsive to price changes than the SMA.
The first value for the EMA will always be the first price, as there's no previous value to start the smoothing.

3. donchian_channel(highs, lows, period=20)
Description

The donchian_channel function calculates the Donchian Channel for a given set of high and low prices. The Donchian Channel consists of an upper band (the highest high over a given period) and a lower band (the lowest low over the same period). It is typically used to define price breakout levels.

Parameters

highs (list of float): A list of high prices for each time period.
lows (list of float): A list of low prices for each time period.
period (int, optional): The period length over which to calculate the Donchian Channel. Default is 20.
Returns

tuple of lists: A tuple containing two lists:
upper: The upper band of the Donchian Channel.
lower: The lower band of the Donchian Channel.
Example Usage

highs = [120, 122, 125, 128, 130, 135, 140, 145, 148, 150]
lows = [115, 118, 120, 123, 125, 128, 130, 135, 138, 140]

upper, lower = donchian_channel(highs, lows, period=3)
print("Upper:", upper)
print("Lower:", lower)
# Output:
# Upper: [None, None, 125, 128, 130, 135, 140, 145, 148, 150]
# Lower: [None, None, 120, 123, 125, 128, 130, 135, 138, 140]
Explanation

For each time period, the upper band is calculated as the maximum value of the highs over the given period (period=20 by default).
The lower band is calculated as the minimum value of the lows over the same period.
For the first few periods where there aren't enough data points to form a complete period, None is returned.
Conclusion
These functions are essential for technical analysis and are commonly used in trend-following strategies:

Simple Moving Averages (SMA) and Exponential Moving Averages (EMA) are used to smooth price data and identify trends.
The Donchian Channel is used to track price breakouts by defining the highest high and lowest low over a given period.
These overlays and channels are crucial for understanding price movements and forecasting potential breakout levels in markets.


# tech_analysis.candlestick_patterns

This module contains functions that detect different candlestick patterns such as Doji, Engulfing, Hammer, and more. These patterns help traders identify potential price movements and trends in the market.

1. is_doji(open_, close, threshold=0.1)
Description

The is_doji function detects Doji candlesticks, where the open and close prices are very close to each other. It returns True when the absolute difference between the open and close prices is below a certain threshold relative to the price range.

Parameters

open_ (list of float): A list of opening prices.
close (list of float): A list of closing prices.
threshold (float, optional): The percentage threshold for detecting a Doji candlestick. Default is 0.1.
Returns

list of bool: A list of boolean values indicating whether each candlestick is a Doji.
Example Usage

open_prices = [100, 105, 103]
close_prices = [100.1, 104, 102.9]
doji = is_doji(open_prices, close_prices)
print(doji)  # [True, False, True]

2. is_hammer(open_, high, low, close)
Description

The is_hammer function detects Hammer candlesticks, characterized by a small body near the top of the candlestick and a long lower shadow. This pattern indicates a potential reversal after a downtrend.

Parameters

open_ (list of float): A list of opening prices.
high (list of float): A list of high prices.
low (list of float): A list of low prices.
close (list of float): A list of closing prices.
Returns

list of bool: A list of boolean values indicating whether each candlestick is a Hammer.
Example Usage

open_prices = [100, 105, 103]
high_prices = [110, 107, 108]
low_prices = [95, 100, 99]
close_prices = [100, 104, 102]
hammer = is_hammer(open_prices, high_prices, low_prices, close_prices)
print(hammer)  # [True, False, False]

3. is_inverted_hammer(open_, high, low, close)
Description

The is_inverted_hammer function detects Inverted Hammer candlesticks, which have a small body near the bottom and a long upper shadow. This pattern suggests a possible reversal after a downtrend.

Parameters

open_ (list of float): A list of opening prices.
high (list of float): A list of high prices.
low (list of float): A list of low prices.
close (list of float): A list of closing prices.
Returns

list of bool: A list of boolean values indicating whether each candlestick is an Inverted Hammer.
Example Usage

inverted_hammer = is_inverted_hammer(open_prices, high_prices, low_prices, close_prices)
print(inverted_hammer)  # [False, True, False]

4. is_shooting_star(open_, high, low, close)
Description

The is_shooting_star function detects Shooting Star candlesticks, which have the same shape as the Inverted Hammer, but the pattern appears after an uptrend, signaling a possible reversal.

Parameters

open_ (list of float): A list of opening prices.
high (list of float): A list of high prices.
low (list of float): A list of low prices.
close (list of float): A list of closing prices.
Returns

list of bool: A list of boolean values indicating whether each candlestick is a Shooting Star.
Example Usage

shooting_star = is_shooting_star(open_prices, high_prices, low_prices, close_prices)
print(shooting_star)  # [False, True, False]

5. is_bullish_engulfing(open_, close)
Description

The is_bullish_engulfing function detects a Bullish Engulfing pattern, where the current candlestick's body completely engulfs the previous candlestick's body and the price closes higher than the open. This pattern signals potential upward momentum.

Parameters

open_ (list of float): A list of opening prices.
close (list of float): A list of closing prices.
Returns

list of bool: A list of boolean values indicating whether each candlestick is part of a Bullish Engulfing pattern.
Example Usage

bullish_engulfing = is_bullish_engulfing(open_prices, close_prices)
print(bullish_engulfing)  # [False, True, False]
6. is_bearish_engulfing(open_, close)
Description

The is_bearish_engulfing function detects a Bearish Engulfing pattern, where the current candlestick's body completely engulfs the previous candlestick's body, and the price closes lower than the open. This pattern signals potential downward momentum.

Parameters

open_ (list of float): A list of opening prices.
close (list of float): A list of closing prices.
Returns

list of bool: A list of boolean values indicating whether each candlestick is part of a Bearish Engulfing pattern.
Example Usage

bearish_engulfing = is_bearish_engulfing(open_prices, close_prices)
print(bearish_engulfing)  # [False, False, True]

7. is_bullish_harami(open_, close)
Description

The is_bullish_harami function detects a Bullish Harami pattern, which occurs when a small candlestick with a close higher than the open is contained within the body of the previous larger candlestick. It signals a potential reversal after a downtrend.

Parameters

open_ (list of float): A list of opening prices.
close (list of float): A list of closing prices.
Returns

list of bool: A list of boolean values indicating whether each candlestick is part of a Bullish Harami pattern.
Example Usage

bullish_harami = is_bullish_harami(open_prices, close_prices)
print(bullish_harami)  # [False, True, False]

8. is_bearish_harami(open_, close)
Description

The is_bearish_harami function detects a Bearish Harami pattern, which occurs when a small candlestick with a close lower than the open is contained within the body of the previous larger candlestick. It signals a potential reversal after an uptrend.

Parameters

open_ (list of float): A list of opening prices.
close (list of float): A list of closing prices.
Returns

list of bool: A list of boolean values indicating whether each candlestick is part of a Bearish Harami pattern.
Example Usage

bearish_harami = is_bearish_harami(open_prices, close_prices)
print(bearish_harami)  # [False, False, True]

9. is_morning_star(open_, close)
Description

The is_morning_star function detects a Morning Star pattern, which consists of three candles: a large bearish candle, a small indecisive candle, and a large bullish candle. It signals a potential reversal from a downtrend to an uptrend.

Parameters

open_ (list of float): A list of opening prices.
close (list of float): A list of closing prices.
Returns

list of bool: A list of boolean values indicating whether each candlestick is part of a Morning Star pattern.
Example Usage

morning_star = is_morning_star(open_prices, close_prices)
print(morning_star)  # [False, True, False]

10. is_evening_star(open_, close)
Description

The is_evening_star function detects an Evening Star pattern, which consists of three candles: a large bullish candle, a small indecisive candle, and a large bearish candle. It signals a potential reversal from an uptrend to a downtrend.

Parameters

open_ (list of float): A list of opening prices.
close (list of float): A list of closing prices.
Returns

list of bool: A list of boolean values indicating whether each candlestick is part of an Evening Star pattern.
Example Usage

evening_star = is_evening_star(open_prices, close_prices)
print(evening_star)  # [False, False, True]

11. is_three_white_soldiers(open_, close)
Description

The is_three_white_soldiers function detects the Three White Soldiers pattern, which consists of three consecutive bullish candles. It signals strong upward momentum and potential continuation of an uptrend.

Parameters

open_ (list of float): A list of opening prices.
close (list of float): A list of closing prices.
Returns

list of bool: A list of boolean values indicating whether each candlestick is part of the Three White Soldiers pattern.
Example Usage

three_white_soldiers = is_three_white_soldiers(open_prices, close_prices)
print(three_white_soldiers)  # [False, False, True]

12. is_three_black_crows(open_, close)
Description

The is_three_black_crows function detects the Three Black Crows pattern, which consists of three consecutive bearish candles. It signals strong downward momentum and potential continuation of a downtrend.

Parameters

open_ (list of float): A list of opening prices.
close (list of float): A list of closing prices.
Returns

list of bool: A list of boolean values indicating whether each candlestick is part of the Three Black Crows pattern.
Example Usage

three_black_crows = is_three_black_crows(open_prices, close_prices)
print(three_black_crows)  # [False, True, False]

13. is_tweezer_top(open_, close)
Description

The is_tweezer_top function detects the Tweezer Top pattern, which consists of two consecutive candles with similar highs and bearish closes. It signals a potential reversal after an uptrend.

Parameters

open_ (list of float): A list of opening prices.
close (list of float): A list of closing prices.
Returns

list of bool: A list of boolean values indicating whether each candlestick is part of the Tweezer Top pattern.
Example Usage

tweezer_top = is_tweezer_top(open_prices, close_prices)
print(tweezer_top)  # [False, True, False]

14. is_tweezer_bottom(open_, close)
Description

The is_tweezer_bottom function detects the Tweezer Bottom pattern, which consists of two consecutive candles with similar lows and bullish closes. It signals a potential reversal after a downtrend.

Parameters

open_ (list of float): A list of opening prices.
close (list of float): A list of closing prices.
Returns

list of bool: A list of boolean values indicating whether each candlestick is part of the Tweezer Bottom pattern.
Example Usage

tweezer_bottom = is_tweezer_bottom(open_prices, close_prices)
print(tweezer_bottom)  # [False, True, False]


# tech_analysis.risk 

This module contains various functions for calculating important performance metrics and risk ratios commonly used in finance and investment analysis. The functions help in evaluating asset performance and risk, including metrics like Sharpe Ratio, Sortino Ratio, and others.

1. sharpe_ratio(returns, risk_free=0.0)
Description

The sharpe_ratio function calculates the Sharpe Ratio, which is a measure of the risk-adjusted return of an asset or portfolio. It compares the excess return of the asset over a risk-free rate with the standard deviation of returns.

Parameters

returns (list of float): A list of periodic returns (e.g., daily, monthly).
risk_free (float, optional): The risk-free rate. Default is 0.0.
Returns

float: The Sharpe Ratio, calculated as the average excess return divided by the standard deviation of excess returns.
Example Usage

returns = [0.05, 0.02, -0.01, 0.03, 0.04]
sharpe = sharpe_ratio(returns)
print(sharpe)  # Output: Sharpe Ratio value

2. sortino_ratio(returns, risk_free=0.0)
Description

The sortino_ratio function calculates the Sortino Ratio, a variation of the Sharpe ratio that only considers the downside risk (i.e., negative returns). This makes it a more relevant measure for evaluating assets with skewed risk profiles.

Parameters

returns (list of float): A list of periodic returns.
risk_free (float, optional): The risk-free rate. Default is 0.0.
Returns

float: The Sortino Ratio, calculated as the average excess return divided by the downside deviation.
Example Usage

returns = [0.05, 0.02, -0.01, 0.03, 0.04]
sortino = sortino_ratio(returns)
print(sortino)  # Output: Sortino Ratio value

3. cagr(values, periods_per_year)
Description

The cagr function calculates the Compound Annual Growth Rate (CAGR), which measures the mean annual growth rate of an investment over a specified period of time.

Parameters

values (list of float): A list of asset values at each period (e.g., closing prices over time).
periods_per_year (int): The number of periods in one year (e.g., 252 for daily data).
Returns

float: The Compound Annual Growth Rate (CAGR).
Example Usage

values = [100, 120, 140, 160, 180]
cagr_value = cagr(values, periods_per_year=252)
print(cagr_value)  # Output: CAGR value

4. max_return(values)
Description

The max_return function calculates the maximum return over the entire history of asset values by finding the largest difference between any two points in time (i.e., the largest possible profit between two prices).

Parameters

values (list of float): A list of asset values (e.g., historical closing prices).
Returns

float: The maximum return (the largest difference between two values).
Example Usage

values = [100, 120, 110, 140, 130]
max_ret = max_return(values)
print(max_ret)  # Output: Maximum return value

5. volatility(returns)
Description

The volatility function calculates the volatility (standard deviation) of asset returns, which is a measure of the variability or risk of the asset's returns.

Parameters

returns (list of float): A list of periodic returns (e.g., daily returns).
Returns

float: The volatility (standard deviation) of the returns.
Example Usage

returns = [0.05, -0.02, 0.03, 0.04, -0.01]
volatility_value = volatility(returns)
print(volatility_value)  # Output: Volatility value

6. calmar_ratio(returns, values)
Description

The calmar_ratio function calculates the Calmar Ratio, which is a performance metric that compares the risk-adjusted return of an asset. It uses the CAGR and Maximum Drawdown (MDD) to measure the return per unit of risk.

Parameters

returns (list of float): A list of periodic returns (not directly used in the formula).
values (list of float): A list of asset values (e.g., closing prices).
Returns

float: The Calmar Ratio, calculated as the ratio of CAGR to the maximum drawdown.
Example Usage

values = [100, 110, 120, 115, 130]
calmar = calmar_ratio(returns=[], values=values)  # returns not needed for this function
print(calmar)  # Output: Calmar Ratio value

7. beta(asset_returns, benchmark_returns)
Description

The beta function calculates the beta coefficient of an asset, which measures its sensitivity to market movements (i.e., its correlation with a benchmark index). A beta greater than 1 indicates that the asset is more volatile than the benchmark, while a beta less than 1 suggests lower volatility.

Parameters

asset_returns (list of float): A list of returns for the asset.
benchmark_returns (list of float): A list of returns for the benchmark index.
Returns

float: The beta coefficient of the asset.
Example Usage

asset_returns = [0.05, 0.02, -0.01, 0.03, 0.04]
benchmark_returns = [0.04, 0.03, 0.01, 0.02, 0.03]
beta_value = beta(asset_returns, benchmark_returns)
print(beta_value)  # Output: Beta value

# Technical Indicators Functions

1. rsi(prices, period=14)
Description

The rsi function calculates the Relative Strength Index (RSI), a momentum oscillator that measures the speed and change of price movements. RSI oscillates between 0 and 100 and is typically used to identify overbought or oversold conditions in a market.

Parameters

prices (list of float): A list of asset prices (e.g., closing prices).
period (int, optional): The number of periods to calculate the RSI (default is 14).
Returns

list of float: The RSI values, with None values for the initial periods before enough data points are available.
Example Usage

prices = [100, 105, 103, 106, 110, 108, 107]
rsi_values = rsi(prices)
print(rsi_values)  # Output: RSI values

2. macd(prices, fast=12, slow=26, signal=9)
Description

The macd function calculates the Moving Average Convergence Divergence (MACD), a trend-following momentum indicator that shows the relationship between two moving averages of an asset's price. The MACD consists of a MACD line, a signal line, and a histogram.

Parameters

prices (list of float): A list of asset prices.
fast (int, optional): The period for the fast EMA (default is 12).
slow (int, optional): The period for the slow EMA (default is 26).
signal (int, optional): The period for the signal line (default is 9).
Returns

A tuple containing:
list of float: MACD line values.
list of float: Signal line values.
list of float: Histogram values (difference between MACD and signal line).
Example Usage

prices = [100, 105, 103, 106, 110, 108, 107]
macd_line, signal_line, histogram = macd(prices)
print(macd_line, signal_line, histogram)  # Output: MACD, Signal, Histogram values

3. bollinger_bands(prices, period=20, multiplier=2)
Description

The bollinger_bands function calculates the Bollinger Bands, which consist of a simple moving average (SMA) and two standard deviation bands. These bands expand or contract based on the volatility of the asset.

Parameters

prices (list of float): A list of asset prices (e.g., closing prices).
period (int, optional): The period for calculating the SMA (default is 20).
multiplier (float, optional): The multiplier for the standard deviation (default is 2).
Returns

A tuple containing:
list of float: Upper Bollinger Band values.
list of float: Lower Bollinger Band values.
Example Usage

prices = [100, 105, 103, 106, 110, 108, 107]
upper_band, lower_band = bollinger_bands(prices)
print(upper_band, lower_band)  # Output: Upper and Lower Bollinger Bands

4. stochastic_oscillator(highs, lows, closes, k_period=14, d_period=3)
Description

The stochastic_oscillator function calculates the Stochastic Oscillator (SO), which is a momentum indicator that compares the closing price of an asset to its price range over a specified period.

Parameters

highs (list of float): A list of high prices.
lows (list of float): A list of low prices.
closes (list of float): A list of closing prices.
k_period (int, optional): The period for the %K line (default is 14).
d_period (int, optional): The period for the %D line (default is 3).
Returns

A tuple containing:
list of float: The %K values.
list of float: The %D values.
Example Usage

highs = [110, 112, 115, 118, 120]
lows = [100, 101, 103, 106, 107]
closes = [105, 108, 110, 113, 115]
k_values, d_values = stochastic_oscillator(highs, lows, closes)
print(k_values, d_values)  # Output: Stochastic %K and %D values

5. williams_r(highs, lows, closes, period=14)
Description

The williams_r function calculates the Williams %R, a momentum indicator that measures overbought or oversold conditions. It compares the current closing price to the highest high and the lowest low over a specified period.

Parameters

highs (list of float): A list of high prices.
lows (list of float): A list of low prices.
closes (list of float): A list of closing prices.
period (int, optional): The period for the calculation (default is 14).
Returns

list of float: Williams %R values, with None values for the initial periods before enough data points are available.
Example Usage

highs = [110, 112, 115, 118, 120]
lows = [100, 101, 103, 106, 107]
closes = [105, 108, 110, 113, 115]
williams_values = williams_r(highs, lows, closes)
print(williams_values)  # Output: Williams %R values

6. atr(highs, lows, closes, period=14)
Description

The atr function calculates the Average True Range (ATR), a volatility indicator that measures the average of the true ranges (the difference between the high and low prices) over a specified period.

Parameters

highs (list of float): A list of high prices.
lows (list of float): A list of low prices.
closes (list of float): A list of closing prices.
period (int, optional): The period for the ATR (default is 14).
Returns

list of float: The ATR values, with None values for the initial periods before enough data points are available.
Example Usage

highs = [110, 112, 115, 118, 120]
lows = [100, 101, 103, 106, 107]
closes = [105, 108, 110, 113, 115]
atr_values = atr(highs, lows, closes)
print(atr_values)  # Output: ATR values

7. roc(prices, period=12)
Description

The roc function calculates the Rate of Change (ROC), which measures the percentage change in price over a specified period. It is used to identify the momentum of an asset.

Parameters

prices (list of float): A list of asset prices (e.g., closing prices).
period (int, optional): The period for the ROC (default is 12).
Returns

list of float: The Rate of Change values, with None values for the initial periods before enough data points are available.
Example Usage

prices = [100, 105, 110, 120, 125]
roc_values = roc(prices)
print(roc_values)  # Output: ROC values

8. trix(prices, period=15)
Description

The trix function calculates the TRIX indicator, which is a momentum oscillator that shows the rate of change in a triple-smoothed exponential moving average (EMA).

Parameters

prices (list of float): A list of asset prices (e.g., closing prices).
period (int, optional): The period for the TRIX (default is 15).
Returns

list of float: The TRIX values, with None values for the initial periods before enough data points are available.
Example Usage

prices = [100, 105, 110, 120, 125]
trix_values = trix(prices)
print(trix_values)  # Output: TRIX values

9. cci(highs, lows, closes, period=20)
Description

The cci function calculates the Commodity Channel Index (CCI), which measures the deviation of the price from a moving average. The CCI is typically used to identify cyclical trends in the market.

Parameters

highs (list of float): A list of high prices.
lows (list of float): A list of low prices.
closes (list of float): A list of closing prices.
period (int, optional): The period for the CCI (default is 20).
Returns

list of float: The CCI values, with None values for the initial periods before enough data points are available.
Example Usage

highs = [110, 112, 115, 118, 120]
lows = [100, 101, 103, 106, 107]
closes = [105, 108, 110, 113, 115]
cci_values = cci(highs, lows, closes)
print(cci_values)  # Output: CCI values


# Risk Management Functions

1. position_size(account_size, risk_per_trade, stop_loss_pips, pip_value)
Description

The position_size function calculates the size of the position to take in a trade based on the account size, the risk per trade (as a percentage), the stop-loss in pips, and the pip value (the value of each pip in the asset being traded).

Parameters

account_size (float): The total account size (e.g., $10,000).
risk_per_trade (float): The percentage of the account size to risk on each trade (e.g., 0.02 for 2% risk).
stop_loss_pips (int): The distance of the stop-loss from the entry point in pips.
pip_value (float): The monetary value of one pip (e.g., $0.10 per pip).
Returns

int: The position size (the number of units or contracts to trade).
Example Usage

account_size = 10000
risk_per_trade = 0.02  # 2% of account size
stop_loss_pips = 50
pip_value = 0.10
position = position_size(account_size, risk_per_trade, stop_loss_pips, pip_value)
print(position)  # Output: 40

2. max_drawdown(values)
Description

The max_drawdown function calculates the maximum drawdown (MDD) of a series of values (e.g., portfolio balance over time). Maximum drawdown is the largest peak-to-trough decline in value, which helps assess risk.

Parameters

values (list of float): A list of values (e.g., portfolio balances or asset prices) over time.
Returns

float: The maximum drawdown value (as a percentage of the peak value).
Example Usage

values = [1000, 950, 920, 980, 1050, 990]
mdd = max_drawdown(values)
print(mdd)  # Output: 0.14 (14% drawdown)

3. value_at_risk(returns, confidence=0.95)
Description

The value_at_risk (VaR) function calculates the Value at Risk at a given confidence level. VaR estimates the potential loss in a portfolio over a given period of time at a certain confidence level (e.g., 95% confidence).

Parameters

returns (list of float): A list of asset or portfolio returns.
confidence (float, optional): The confidence level (default is 0.95, which corresponds to a 95% confidence interval).
Returns

float: The Value at Risk (VaR), representing the estimated loss at the given confidence level.
Example Usage

returns = [0.02, 0.01, -0.03, 0.05, -0.02, -0.01]
var = value_at_risk(returns, confidence=0.95)
print(var)  # Output: 0.03 (3% VaR)

4. kelly_criterion(win_prob, win_loss_ratio)
Description

The Kelly Criterion is a formula used to determine the optimal size of a series of bets (or trades) in order to maximize long-term capital growth while minimizing the risk of losing the entire bankroll. It considers both the win probability and the win-to-loss ratio.

Parameters

win_prob (float): The probability of winning a trade (e.g., 0.55 for a 55% win rate).
win_loss_ratio (float): The ratio of the average win to the average loss (e.g., 2 for a 2:1 win-to-loss ratio).
Returns

float: The proportion of the account to risk on each trade according to the Kelly criterion.
Example Usage

win_prob = 0.55
win_loss_ratio = 2
kelly = kelly_criterion(win_prob, win_loss_ratio)
print(kelly)  # Output: 0.15 (15% of the account to risk per trade)

5. risk_of_ruin(win_rate, loss_rate, avg_win, avg_loss)
Description

The risk_of_ruin function calculates the risk of ruin, which is the probability of losing your entire capital based on your win rate, loss rate, and average win/loss size.

Parameters

win_rate (float): The probability of winning a trade (e.g., 0.55 for a 55% win rate).
loss_rate (float): The probability of losing a trade (e.g., 0.45 for a 45% loss rate).
avg_win (float): The average win size (e.g., $200).
avg_loss (float): The average loss size (e.g., $150).
Returns

float: The risk of ruin, a measure of how likely it is that you will lose all your capital.
Example Usage

win_rate = 0.55
loss_rate = 0.45
avg_win = 200
avg_loss = 150
ruin_risk = risk_of_ruin(win_rate, loss_rate, avg_win, avg_loss)
print(ruin_risk)  # Output: 0.274 (27.4% risk of ruin)

6. monte_carlo_simulation(initial_balance, trades, simulations=1000)
Description

The monte_carlo_simulation function performs a Monte Carlo simulation to simulate the outcomes of a trading strategy over multiple simulations. It randomly selects a trade outcome from the provided list of returns (could be positive or negative) for each simulation and computes the final balance after all trades.

Parameters

initial_balance (float): The initial balance of the account.
trades (list of float): A list of returns for each trade (positive for wins, negative for losses).
simulations (int, optional): The number of Monte Carlo simulations to run (default is 1000).
Returns

list of float: A list of final balances for each simulation.
Example Usage

initial_balance = 10000
trades = [100, -50, 150, -100, 200]  # List of returns per trade
simulated_balances = monte_carlo_simulation(initial_balance, trades, simulations=500)
print(simulated_balances)  # Output: List of final balances after each simulation



# Volume-Based Indicator Functions

1. obv(prices, volume)
Description

The On-Balance Volume (OBV) indicator is a cumulative measure of volume that adds or subtracts volume based on whether the price goes up or down. It helps to assess the strength of a price trend based on trading volume.

Parameters

prices (list of float): A list of price values (usually closing prices).
volume (list of float): A list of volume values corresponding to the prices.
Returns

list of float: The On-Balance Volume values for each period.
Example Usage

prices = [100, 102, 101, 105, 107]
volume = [1000, 1500, 1200, 1300, 1100]
obv_values = obv(prices, volume)
print(obv_values)
# Output: [0, 1500, 1500, 2800, 4200]

2. pvt(prices, volume)
Description

The Price Volume Trend (PVT) indicator combines price and volume to create a cumulative line. Unlike OBV, PVT adjusts the volume based on the percentage change in price, which makes it more sensitive to price changes.

Parameters

prices (list of float): A list of price values (usually closing prices).
volume (list of float): A list of volume values corresponding to the prices.
Returns

list of float: The Price Volume Trend values for each period.
Example Usage

prices = [100, 102, 101, 105, 107]
volume = [1000, 1500, 1200, 1300, 1100]
pvt_values = pvt(prices, volume)
print(pvt_values)
# Output: [0, 30.0, 38.64, 89.85, 130.87]

3. mfi(highs, lows, closes, volume, period=14)
Description

The Money Flow Index (MFI) is a volume-weighted version of the Relative Strength Index (RSI). It incorporates both price and volume data to show whether a security is overbought or oversold.

Parameters

highs (list of float): A list of high prices.
lows (list of float): A list of low prices.
closes (list of float): A list of closing prices.
volume (list of float): A list of volume values.
period (int, optional): The period for calculating MFI (default is 14).
Returns

list of float or None: The Money Flow Index values for each period. Returns None for values that can't be calculated (i.e., for the first 14 periods).
Example Usage

highs = [101, 102, 103, 105, 107]
lows = [98, 99, 100, 102, 103]
closes = [100, 101, 102, 104, 106]
volume = [1000, 1500, 1200, 1300, 1100]
mfi_values = mfi(highs, lows, closes, volume, period=14)
print(mfi_values)
# Output: [None, None, None, None, None]
(Note: The mfi function requires 14 periods of data before it can start returning values.)

4. chaikin_money_flow(highs, lows, closes, volumes, period=20)
Description

The Chaikin Money Flow (CMF) indicator measures the accumulation and distribution of money flow over a specified period, typically 20 periods. It considers the close price relative to the high-low range and multiplies it by volume.

Parameters

highs (list of float): A list of high prices.
lows (list of float): A list of low prices.
closes (list of float): A list of closing prices.
volumes (list of float): A list of volume values.
period (int, optional): The period for calculating CMF (default is 20).
Returns

list of float or None: The Chaikin Money Flow values for each period.
Example Usage

highs = [101, 102, 103, 105, 107]
lows = [98, 99, 100, 102, 103]
closes = [100, 101, 102, 104, 106]
volumes = [1000, 1500, 1200, 1300, 1100]
cmf_values = chaikin_money_flow(highs, lows, closes, volumes, period=20)
print(cmf_values)
# Output: [None, None, None, None, None] (Since period is 20, it will return None until enough data is available)

5. ease_of_movement(highs, lows, volumes, period=14)
Description

The Ease of Movement (EMV) indicator is a volume-based indicator that measures the relationship between price movement and volume. It highlights when price movements are easy (significant moves with relatively low volume) or difficult (small moves with high volume).

Parameters

highs (list of float): A list of high prices.
lows (list of float): A list of low prices.
volumes (list of float): A list of volume values.
period (int, optional): The period for calculating the EMV (default is 14).
Returns

list of float or None: The Ease of Movement values for each period.
Example Usage

highs = [101, 102, 103, 105, 107]
lows = [98, 99, 100, 102, 103]
volumes = [1000, 1500, 1200, 1300, 1100]
emv_values = ease_of_movement(highs, lows, volumes, period=14)
print(emv_values)
# Output: [None, None, None, None, None] (The first 14 periods will be None)


## Installation

```bash
pip install tech_analysis
