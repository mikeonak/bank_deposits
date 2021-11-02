
import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
import pickle

from xgboost.training import train


df = pd.read_csv('bank-additional-full.csv',sep=';')

# data preparation

del df['duration']
df.y = df.y.eq('yes').mul(1)


df_full_train, df_test = train_test_split(df,test_size = 0.2, random_state=1,stratify=df.y)


dv = DictVectorizer(sparse=False)
train_dicts = df_full_train.to_dict(orient='records')
X_full_train = dv.fit_transform(train_dicts)
y_test = df_test.y.values
y_full_train = df_full_train.y.values

features = dv.get_feature_names()

# Training the final model

dtrain = xgb.DMatrix(X_full_train, label=y_full_train, feature_names=features)


xgb_params = {
    'eta': 0.1, 
    'max_depth': 3,
    'min_child_weight': 20,
    'colsample_bytree': 0.5,
    'subsample': 1,

    'objective': 'binary:logistic',
    'eval_metric': 'auc',
    'nthread': 4,

    'seed': 1,
    'verbosity': 1,
}

model = xgb.train(xgb_params, dtrain, num_boost_round=150)
y_pred = model.predict(dtrain)

with open('model_deposits.bin', 'wb') as f_out:
    pickle.dump((dv,model), f_out)
