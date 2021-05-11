#use flask to create application
#flask python web app framework

from flask import Flask, render_template, request
app = Flask(__name__)


#this is the landing page
#calling index.html page
@app.route('/')
def index():
    return render_template('index.html')

#result page will be shown when user press 'submit'
@app.route('/result', methods=['POST'])
def response():

    #same logic as jupyter notebook model.ipynb
    import numpy as np
    import pandas as pd

    form = dict(request.form.items())
    df = pd.DataFrame.from_dict([form])

    from sklearn.preprocessing import StandardScaler,PolynomialFeatures
    poly_convert = PolynomialFeatures(include_bias=False)
    poly = poly_convert.fit_transform(df)

    from joblib import load
    model = load('presentation_model.joblib')
    
    predict = model.predict(poly)
    result = np.round(predict[0],2)

    return render_template('result.html', price=result)
