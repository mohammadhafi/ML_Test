import pandas as pd
from datetime import datetime
from datetime import datetime
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

data=pd.read_csv('sphist.csv')
data['Date']=pd.to_datetime(data['Date'])
data=data.sort_values('Date',ascending=True)
data=data[data['Date']>datetime(year=1951,month=1,day=3)]
#make rolling!
data['day_5'] = 000
data['day_5'] =data['Close'].rolling(5).mean()
data['day_5'] =data['day_5'].shift()
data=data.dropna(axis=0)
#make train & test 
train=data[data['Date']<datetime(year=2013,month=1,day=1)]
test=data[data['Date']>datetime(year=2013,month=1,day=1)]
#ML model
model=LinearRegression()
model.fit(train[['day_5']],train[['Close']])
prediction=model.predict(test[['day_5']])
error=mean_squared_error(test['Close'],prediction)
print(error)