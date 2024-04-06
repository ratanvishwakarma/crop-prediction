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

 <table>
        <tr>
          <th>Label</th>
          <th>N</th>
          <th>P</th>
          <th>K</th>
          <th>Temperature</th>
          <th>Humidity</th>
          <th>pH</th>
        </tr>
        <tr>
          <td>Apple</td>
          <td>0 - 40</td>
          <td>120 - 145</td>
          <td>195 - 205</td>
          <td>21 - 24</td>
          <td>90 - 95</td>
          <td>5 - 6.5</td>
        </tr>
         <tr>
          <td>Banana</td>
          <td>80 - 120</td>
          <td>70 - 95</td>
          <td>45 - 55</td>
          <td>25 - 30</td>
          <td>75 - 85</td>
          <td>5 - 6.5</td>
        </tr>
      </table>

if __name__ == '__main__':
    app.run(debug=True)
    
    
