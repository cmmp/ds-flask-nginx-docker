from sklearn.externals import joblib
import numpy as np
from flask import Flask, request
from flasgger import Swagger

clf = joblib.load('models/svm.pkl')

app = Flask(__name__)

template = {
  "info": {
    "title": "Iris prediction API",
    "version": "1.0"
  }
}
swagger = Swagger(app, template=template)

@app.route('/predict')
def predict_iris():
    """Endpoint for iris prediction
    ---    
    parameters:
        - name: sepal_length
          in: query
          type: number
          required: true
        - name: sepal_width
          in: query
          type: number
          required: true
        - name: petal_width
          in: query
          type: number
          required: true
        - name: petal_length
          in: query
          type: number
          required: true
    responses:
        200:
            description: Value of prediction
            type: number
    """
    s_len = request.args.get('sepal_length')
    s_wid = request.args.get('sepal_width')
    p_len = request.args.get('petal_length')
    p_wid = request.args.get('petal_width')
    pred = clf.predict(np.array([[s_len, s_wid, p_len, p_wid]]))
    return str(pred[0])

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
