# Flask Web App of a Sale Price Prediction model

This is a simple flask web application that allows the user to key in some paramters and the website will give a predicted sale price.

## Data set and Modelling

Please check **model.ipynb**
- Data set used: Ames Housing Dataset
- For more information on data set please [click here](http://jse.amstat.org/v19n3/decock/DataDocumentation.txt)
- Model was created using top 5 features found in earlier studies
- Model created using sklearn package with elasticnet penalty
- Model will give Sale Price prediction when user keys in these 5 features

For more details on this, check out other github repository: Ames housing Model

## Flask App

Flask app has 2 html pages, one py file and a joblib file of the saved model. 
- **index.html**: landing page with html form
- **result.html**: page which returns the predicted sale price
- **app.py**: flask application that takes input from index.html, converts html form into a dataframe, calls the presentation_model.joblib to run and returns the predicted sale price on result.html.