import pandas as pd
import numpy as np
import os
from sklearn.model_selection import train_test_split, StratifiedShuffleSplit, cross_val_score, cross_val_predict
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import mean_squared_error, precision_score, recall_score
from sklearn.pipeline import Pipeline
import matplotlib.pyplot as plt
from future_encoders import ColumnTransformer
from sklearn.preprocessing import Imputer, OneHotEncoder, LabelEncoder, StandardScaler

# load data
def load_transaction_data():
    return pd.read_csv("creditcardcsvpresent.csv")

transaction_data = load_transaction_data()
print("------------------------------Transaction Dataset------------------------------")
print(transaction_data.head())

print("------------------------------Dataset Info------------------------------")
print(transaction_data.info())

# transform
print("------------------------------Transform------------------------------")
transaction_data = transaction_data.drop('Transaction date', axis=1) # this column is null completely so....
cat_attribs = ['Is declined', 'isForeignTransaction', 'isHighRiskCountry', 'isFradulent']
lab_encoder = LabelEncoder()
cat_encoder = OneHotEncoder(sparse=False)

# label encoder
transaction_enc_declined = lab_encoder.fit_transform(transaction_data['Is declined'])
transaction_enc_foreign = lab_encoder.fit_transform(transaction_data['isForeignTransaction'])
transaction_enc_risk = lab_encoder.fit_transform(transaction_data['isHighRiskCountry'])
transaction_enc_fradulent = lab_encoder.fit_transform(transaction_data['isFradulent'])

# cat encoder (OneHotEncoder)
transaction_cat_declined_hot = cat_encoder.fit_transform(transaction_enc_declined.reshape(-1,1))
transaction_cat_foreign_hot = cat_encoder.fit_transform(transaction_enc_foreign.reshape(-1,1))
transaction_cat_risk_hot = cat_encoder.fit_transform(transaction_enc_risk.reshape(-1,1))
transaction_cat_fradulent_hot = cat_encoder.fit_transform(transaction_enc_fradulent.reshape(-1,1))


transaction_data_prepared = transaction_data
transaction_data_prepared['Is declined'] = transaction_cat_declined_hot
transaction_data_prepared['isForeignTransaction'] = transaction_cat_foreign_hot
transaction_data_prepared['isHighRiskCountry'] = transaction_cat_risk_hot
transaction_data_prepared['isFradulent'] = transaction_cat_fradulent_hot

print("------------------------------Prepared dataset------------------------------")
print(transaction_data_prepared.head())     


# clean data, remove missing values 
print("------------------------------Imputer------------------------------")
# cat_attribs = ['Transaction date', 'Is declined', 'isForeignTransaction', 'isHighRiskCountry', 'isFradulent']
imputer = Imputer(strategy="median")
transaction_num = transaction_data_prepared.drop(cat_attribs, axis=1)
print(transaction_data_num.head())
print("------------------------------Imputer After Fit------------------------------")
imputer.fit(transaction_data_num)
print(imputer.statistics_)
print("------------------------------Transaction num - median, to compare to imputer------------------------------")
print(transaction_num.median().values)

transformed = imputer.transform(transaction_num)
transaction_tr = pd.DataFrame(transformed, columns=transaction_num.columns,
                          index = list(transaction_data_prepared.index.values))

# correlations of attributes
print("------------------------------Correlations------------------------------")
corr_transaction = transaction_data_prepared.corr()
print(corr_transaction)

# taking care of missing values
# optional, our data set does not have any missing values, TODO

# plot to determine best regression model
print("------------------------------Plots------------------------------")
print(list(transaction_data_prepared))
transaction_data_prepared.plot(kind="scatter", x="isHighRiskCountry", y="isFradulent", alpha=.1)
transaction_data_prepared.plot(kind="scatter", x="isForeignTransaction", y="isFradulent", alpha=.1)
transaction_data_prepared.plot(kind="scatter", x="Transaction_amount", y="isFradulent", alpha=.1)
transaction_data_prepared.plot(kind="scatter", x="Total Number of declines/day", y="isFradulent", alpha=.1)

transaction_data_prepared.hist(bins=50, figsize=(15,10))
plt.show()  

# sampling
print("------------------------------Sampling------------------------------")
split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42) 
for train_index, test_index in split.split(transaction_data_prepared, transaction_data_prepared["isHighRiskCountry"]):
        strat_train_set = transaction_data_prepared.loc[train_index]
        strat_test_set = transaction_data_prepared.loc[test_index]

print("------------------------------Stratified Sampling - Training Set------------------------------")
print(strat_train_set.head())
print("------------------------------Stratified Sampling - Test Set------------------------------")
print(strat_test_set.head())
transaction_labels_fraud_train = strat_train_set["isFradulent"].copy()
transaction_labels_fraud_test = strat_test_set["isFradulent"].copy()

# SGD Classifier model
# fit model
sgd_clf = SGDClassifier(random_state=42)
sgd_clf.fit(strat_train_set, transaction_labels_fraud_train)
print("------------------------------Transaction Labels Fraud------------------------------")
print(transaction_labels_fraud_train)

# mean squared error/rmse
sgd_mse = mean_squared_error(transaction_labels_fraud_test, sgd_clf.predict(strat_test_set))
sgd_rmse = np.sqrt(sgd_mse)
print("------------------------------Stochastic Gradient Descent Classifier MSE------------------------------")
print(sgd_mse)
print("------------------------------Stochastic Gradient Descent Classifier RMSE------------------------------")
print(sgd_rmse)

# cross validation

scores = cross_val_score(sgd_clf, strat_train_set, transaction_labels_fraud_train,
                             scoring="accuracy", cv=10)
rmse_scores = np.sqrt(scores)
print("------------------------------Cross Validation Score------------------------------")
print(scores)
print("------------------------------RMSE Scores------------------------------")
print(rmse_scores)





