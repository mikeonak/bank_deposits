import pickle
from flask import Flask
from flask import request
from flask import jsonify
import xgboost as xgb


with open('model_deposits.bin','rb') as f_in:
    dv, model = pickle.load(f_in)


app = Flask('churn')
@app.route('/predict', methods=['POST'])

def predict():
    customer = request.get_json()
    X = dv.transform([customer])
    features = dv.get_feature_names()
    dtest = xgb.DMatrix(X,  feature_names=features)
    y_pred = model.predict(dtest)[0]
    success = y_pred >= 0.5
    result={
        'succes_proba':str(y_pred),
        'Call the client':bool(success)
    }

    return jsonify(result)





if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0.', port=9696)