from flask import Flask, request,render_template
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)
with open('coffee_quality_prediction(rfc).pkl','rb') as file:
    model = pickle.load(file)
    
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/details")
def predict():
    return render_template("details.html")
@app.route("/about")
def about():
    return render_template("about.html")
@app.route('/submit',methods=["POST","GET"])
def submit():
    #reading the inputs given by user
    input_feature=[float(x) for x in request.form.values()]
    #input_features = np.transpose(input_feature)
    x=[np.array(input_feature)]
    print(input_feature)
    names = ['Aroma','Flavor','Aftertaste','Acidity','Body','Balance','Uniformity','Quakers','Color_Encoded']
    data = pd.DataFrame(x,columns=names)
    print(data)
    pred = model.predict(data)
    if(pred == 1):
        return render_template('result.html',predict="Unhealthy")
    else:
        return render_template('result.html',predict="Healthy")
@app.route('/result')
def result():
    return render_template('result.html')
if __name__ == "__main__":
    app.run(debug = True,port = 5555)