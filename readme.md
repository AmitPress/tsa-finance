# End to End Time Series Analysis of Stock Data
> This is a demonstration of how Time Series Analysis can help us forecast various
> financial parameters which we always need to project for our financial analysis.

#### Overview




> visit: [Github Repo](https://cutt.ly/zr0IzZYs) for the reference
---
In this particular blog, we will go through some eternal tenets of time-series analysis (TSA). We will try to start from the ancient statistical models and go beyond machine learning.

#### Why use TSA?
TSA can be very much helpful in terms of business or scientific discoveries and tests. This can help us get insights about Sales, Inventory, Returns, Warehouse, Operating Profit Margins, Wages Expense, Depreciation/Amortization Rate etc. Being a finance guy, I can ensure that it is widely used and anticipated techniques to use in real life. Not just finance, medical and other professionals do also use it heavilty.

#### Can we predict stock?
No, it is counter-intuitive even to taking the scenario of predicting the stocks movement. But we can guess. A speculative guess can be called gambling but an educated guess is what they called brilliance. We better stick to that part of applications.

#### How do I approach?
Here,
- I have mentioned all the dependencies in the requirements.txt
- You may install them inside a virtual environment
- Head on to the data folder to generate and store data. I have provided a notebook that will help you bootstrap the process.
- Then I have trained several stats models based on AR, MA and their combination
- After that I have trained the facebook prophet model
- Finally, trained the deep learning model based on LSTM

#### To begin with
I have chosen a stock to get start with. The ticker of the stock is `DAL` traded in the `NYSE`.
Again, I have not just chosen it but I cared to pre-process it each time for each models that I worked with.
Current market scenario of the stock is as seen below,
![DAL_overall_market.png](https://raw.githubusercontent.com/AmitPress/tinymind-blog/main/assets/images/2025-10-04/1759599178952.png)

As we can see, there is no irregularity, no white-noisy attributes and no stationarity.
We better care to make it stationary, because it will help us forecast the behavior with the AR, MA, ARMA and ARIMA model.

#### ARMA vs ARIMA
Lets have a look at the ARMA model first.
![arma.png](https://raw.githubusercontent.com/AmitPress/tinymind-blog/main/assets/images/2025-10-04/1759599347088.png)
As we can see above it is just randomly forecasting base on the pattern it sees in the data and cannot do better.
Lets have a look at the ARIMA model now.
![arima.png](https://raw.githubusercontent.com/AmitPress/tinymind-blog/main/assets/images/2025-10-04/1759599463435.png)
This model is actually showing somewhat same level of diligence that of the previous ARMA model.

So, one thing that we can say the statistical models have their own restrictions and way of dealing the data. It is not that we can't do any better with them, in fact if we pay enough attention, we might come up with a very good model.

#### Facebook Prophet
This prophet model has a very good promise to keep. But in our case the result is not that satisfactory due to the fact that we didn't care about tuning the model accordingly. If tuned fine, we might have better result.
![prophet.png](https://raw.githubusercontent.com/AmitPress/tinymind-blog/main/assets/images/2025-10-04/1759599661390.png)

#### LSTM (the elephant in the room)
LSTM is a deep neural network based approach. I see it as a very good estimator as it can take a large memory into account to predict some future values for use. And if we see it closely it has the magnitude to do a lot of things.
We have chosen it for our final run-down for the analysis and to the expectation it did amazing. We must put our horses together before having a complex model. I have chosen a very simple model to go with. And the model performed much better compared to the above once.
![lstm.png](https://raw.githubusercontent.com/AmitPress/tinymind-blog/main/assets/images/2025-10-04/1759599885190.png)


## Recommendation:
If you want to have a model that you can control to the fullest, go with the statistical ones. If you want a battle tested and favorite to academia go for the facebook one. And lastly, if you think neural networks are amazing, they will figure out the solution, congrats LSTM has got you covered. 

# Steps that I have followed
In this practice, I made sure the full process is well organized and documented.
- I have mentioned all the dependencies in the `requirements.txt`
- You may install them inside a virtual environment
- Head on to the data folder to generate and store data. I have provided a notebook that will help you bootstrap the process.
- Then I have trained several stats models based on AR, MA and their combination
- After that I have trained the facebook prophet model
- Finally, trained the deep learning model based on LSTM

# Findings and Comment
After going through all the process, I found out that deep learning models actually generalize better and have the minimum amount of error.
It will be best to have a deep learning model fine tuned to do all the predictions and forecastings.

I have deployed a working version of the deep learning model. Please checkout the description of this repo to find out the link to that.
