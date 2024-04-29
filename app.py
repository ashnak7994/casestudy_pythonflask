from flask import Flask,render_template, request

import pickle

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        model = pickle.load(open('model.pkl', 'rb'))
        age = int(request.form['age'])
        salary = int(request.form['salary'])
        prediction = model.predict([[age, salary]])
        result = "Will Purchase" if prediction[0] == 1 else "Will Not Purchase"
        return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run()
