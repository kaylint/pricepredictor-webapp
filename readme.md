# Flask Web App of a Sale Price Prediction model

This is a simple flask web application that allows the user to key in some paramters and the website will give a predicted sale price. This web application has been hosted on the for free on the Python server called pythonanywhere. [Click here](http://ameshousingpp.pythonanywhere.com/) to visit the website.

## Data set and Modelling - Jupyter Notebook: model.ipynb

Please check **model.ipynb**
- Data set used: Ames Housing Dataset
- For more information on data set please [click here](http://jse.amstat.org/v19n3/decock/DataDocumentation.txt)
- Model was created using 5 features with the highest correlation to sale price
- Model created using sklearn package with elasticnet penalty
- Model will give Sale Price prediction when user keys in these 5 features

For more details on this, check out other github repository: Ames housing Model

## Flask App

App has 2 html pages, one py file and a joblib file of the saved model. 
- **index.html**: landing page with html form
- **result.html**: page which returns the predicted sale price
- **app.py**: flask application that takes input from index.html, converts html form into a dataframe, calls the presentation_model.joblib to run and returns the predicted sale price on result.html.
- **presentation_model.joblib**: Model created using sklearn

## Python script: application.py

When user visits the website, it will show the main landing page. After user submits the form, flask will take the user input and run the model, it will return the result on the result.html page. Logic is the same as what was tested in the jupyter notebook earlier.

## HTML Pages: index.html and result.html

**index.html**: Consists of basic information and html form. html form is here for user to input the values for the 5 features of their property. Predicted price will be based on user input. There are limits set on what the user can input so that it suits the model.

**result.html**: Page displays predicted price

## Limitations of the model

- Model is being trained with only 5 features to make it easy for user to input. The RSME is around 30,000.
- This model is only usable for houses built from 1950 to 2000 and for square feet of 2000 to 4500. This is because of the data the model was trained on. Other houses are outliers and will cause the model to give unrealiable sale price prediction.

## Credits

- Free html based template from w3schools was used and modified to suit this web app. [template](https://www.w3schools.com/w3css/w3css_templates.asp).
- Free CSS style file used can be found here: [css file](https://www.w3schools.com/w3css/4/w3.css). 
- Google font 'Poppins' was used, free font google API: [font](https://fonts.googleapis.com/css?family=Poppins)