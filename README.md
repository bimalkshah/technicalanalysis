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


# Breadth 
Market breadth indicators assess the overall strength or weakness of the market by comparing the number of advancing and declining stocks.

1. Advance-Decline Line (AD Line)
The Advance-Decline Line (AD Line) is a cumulative measure of net advancing stocks over time.

Function: advance_decline(advancing, declining)

Parameters:

advancing: List of float values representing the number of advancing stocks for each period.
declining: List of float values representing the number of declining stocks for each period.
Returns:

List of float: Cumulative net advancing stocks (AD Line) for each period.
Example:
```
advancing = [100, 120, 110]
declining = [80, 90, 105]
ad_line = advance_decline(advancing, declining)
print(ad_line)  # Output: [20, 50, 55]
```

2. Advance-Decline Ratio
The Advance-Decline Ratio is the ratio of advancing stocks to declining stocks. It helps gauge the relative strength of the market.

Function: advance_decline_ratio(advancing, declining)

Parameters:

advancing: List of float values representing the number of advancing stocks.
declining: List of float values representing the number of declining stocks.
Returns:

List of float: Advance-Decline Ratio for each period.
Example:
```
advancing = [100, 120]
declining = [50, 60]
adr = advance_decline_ratio(advancing, declining)
print(adr)  # Output: [2.0, 2.0]
```

3. New Highs-Lows
The New Highs-Lows function calculates the difference between the number of new highs and new lows.

Function: new_highs_lows(new_highs, new_lows)

Parameters:

new_highs: List of float values representing the number of new highs.
new_lows: List of float values representing the number of new lows.
Returns:

List of float: Difference between new highs and new lows for each period.
Example:
```
new_highs = [30, 50]
new_lows = [10, 60]
highs_lows_diff = new_highs_lows(new_highs, new_lows)
print(highs_lows_diff)  # Output: [20, -10]
```

4. TRINAR Indicator
The TRINAR Indicator (Trinary Advance Ratio) measures market strength by considering advancing, declining, and unchanged stocks.

Function: trinar_indicator(advancing, declining, unchanged)

Parameters:

advancing: List of float values representing the number of advancing stocks.
declining: List of float values representing the number of declining stocks.
unchanged: List of float values representing the number of unchanged stocks.
Returns:

List of float: TRINAR indicator values for each period.
Example:
```
advancing = [100, 120]
declining = [80, 60]
unchanged = [20, 20]
trinar = trinar_indicator(advancing, declining, unchanged)
print(trinar)  # Output: [0.2, 0.5]
```
5. Moving Averages

Moving averages help smooth out price data and identify trends.

Simple Moving Average (SMA)
The Simple Moving Average (SMA) is the arithmetic mean of prices over a specified period.

Function: sma(data, period)

Parameters:

data: List of float values (e.g., stock closing prices).
period: The number of periods for the moving average calculation.
Returns:

List of float: SMA values for each period.

6. Exponential Moving Average (EMA)
The Exponential Moving Average (EMA) gives more weight to recent prices, making it more responsive to price changes.

Function: ema(data, period)

Parameters:

data: List of float values (e.g., stock closing prices).
period: The number of periods for the EMA calculation.
Returns:

List of float: EMA values for each period.
Example:
```
data = [100, 102, 104, 105, 107, 109, 110, 112, 113, 115]
ema_vals = ema(data, 3)
print(ema_vals) # Output: [100, 101.0, 102.0, 103.0, 104.0, 105.0, 106.0, 107.0, 108.0, 109.0]
```
# Forecasting

Forecasting methods help predict future values based on past data.

1. Linear Regression
The Linear Regression function calculates the slope and intercept of a linear trend.

Function: linear_regression(x, y)

Parameters:

x: List of independent variable values.
y: List of dependent variable values.
Returns:

a: Intercept of the regression line.
b: Slope of the regression line.
Example:
```
x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]
a, b = linear_regression(x, y)
print(f"Intercept: {a}, Slope: {b}")
```
2. Moving Average Forecasting
The Moving Average function computes the average of a time series over a rolling window.

Function: moving_average(series, window=5)

Parameters:

series: List of float values representing the time series data.
window: The number of periods for the moving average (default is 5).
Returns:

List of float: Moving average values for the series.
Example:
```
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ma = moving_average(data, window=3)
print(ma)
# Output: [2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
```

3. Mean Squared Error (MSE)
The Mean Squared Error function computes the accuracy of a prediction model.

Function: mean_squared_error(y_true, y_pred)

Parameters:

y_true: List of true values.
y_pred: List of predicted values.
Returns:

mse: The Mean Squared Error.
Example:
```
y_true = [3, -0.5, 2, 7]
y_pred = [2.5, 0.0, 2, 8]
mse = mean_squared_error(y_true, y_pred)
print(mse)  # Output: 0.375
```
4. Stock Forecasting
The Stock Forecasting function predicts future stock prices using linear regression or a moving average.

Function: forecast_stock(data, method="linear", window=5)

Parameters:

data: List of stock prices.
method: Forecasting method to use ("linear" or "moving_avg").
window: Window size for moving average (if using method="moving_avg").
Returns:

Dictionary with actual values, predicted values, and MSE.
Example:
```
data = [100, 102, 105, 110, 115, 120, 125, 130, 135, 140]
forecast = forecast_stock(data, method="linear")
print(forecast)
```

# Overlays

Overlays are used to smooth price data and identify trends.

1. Moving Average Overlay
The Moving Average Overlay function calculates SMA for different periods.

Function: moving_average_overlay(prices, periods=[20, 50, 200])

Parameters:

prices: List of float values representing the stock prices.
periods: List of integers representing different periods for the moving averages.
Returns:

Dictionary with SMA for each period.
Example:
```
prices = [100, 102, 104, 105, 107, 109, 110, 112, 113, 115]
overlay = moving_average_overlay(prices, periods=[3, 5])
print(overlay)
```

2. Exponential Moving Average Overlay
Similar to the simple moving average overlay but uses EMAs instead.
Function: exponential_moving_average_overlay(prices, periods=[20, 50, 200])

Parameters:

prices: List of float values representing stock prices.
periods: List of periods for the EMAs.
Returns:

Dictionary with EMA for each period.
