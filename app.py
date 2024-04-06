from flask import Flask,render_template, request
import pickle

app = Flask(__name__)

#load the model
model = pickle.load(open('model.pkl','rb'))

@app.route('/')
def home():
    result = ''
    return render_template('index.html',**locals())

@app.route('/predict',methods=['POST','GET'])
def predict():
    N = float(request.form['N'])
    P = float(request.form['P'])
    K = float(request.form['K'])
    temperature = float(request.form['temperature'])
    humidity = float(request.form['humidity'])
    ph = float(request.form['ph'])
    result = model.predict([[N,P,K,temperature,humidity,ph]])[0]
    return render_template('index.html',**locals())

if __name__ == '__main__':
    app.run(debug=True)
    
    
