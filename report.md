---
title: A thorough analysis on time series data (stocks)
date: 2025-10-04
Author: Amit Malaker
---

# A thorough analysis on time series data (stocks)
> Stocks are unpredictable but educated guess can help you know the dynamics
#### Data preparation
I have used `DAL` stock accross the analysis. You can find more on this in the notebook that I have used for data processing.
I made sure to address `Seasonality`, `Stationarity` and `Irregularity` of data for statistical experiments. As I have approached towards higher level models from lower level models, it was evident that this data criteria matters very less as we ascend.

#### Statistical Analysis and Model Comparison
Let us look at the below table
| Model             | RMSE   | R2      |
|-------------------|--------|---------|
| ARMA              | 6.19   | -0.32   |
| ARIMA             | 6.25   | -0.34   |
| Facebook Prophet  | 7.57   | -0.973  |
| LSTM              | 0.0491 | 0.7291  |


We can see `ARMA` and `ARIMA` is doing the same with the same order. In `ARIMA`, I just have put an extra parameter for integrating the differences. Facebook prophet is not that bad given that it can be tuned right very easily if we pay a little bit more attention to that. We can tune the `changepoint_prior_scale` hyper parameter to have a better result. LSTM, as expected, done a lot better due to the fact that it could estimate the neural functions very easily with the data pattern. I must say LSTM did a tremendous job in terms of labor to output.
As we can see above as we ascend towards the higher model the error gets lowered. Not that its not possible to do better with the lower baseline models. It can be but my measure of angle was to see, `If I go affortlessly, how well the model can do.

#### Verdict
This may seem comparing apples to oranges as you can nail down it saying, they don't have any metric that binds them together for a comparison. But I would say my view point of benchmarking is based on the criteria of `how easy it is to have a model that can predict`.
Here, I am not building the best model for the business but finding out the one that can be tweaked to get the job in the long run.