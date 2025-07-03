from flask import Flask, request, render_template
import pandas as pd
import pickle

app = Flask(__name__)
model = pickle.load(open('xgboost_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generic')
def generic():
    return render_template('generic.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
    return render_template('result.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Only these features will be passed to the model, in this order
    model_features = [
        'blood_glucose_random', 'blood_urea', 'packed_cell_volume', 'red_blood_cell_count',
        'serum_creatinine', 'albumin', 'white_blood_cell_count', 'hemoglobin', 'age', 'sugar'
    ]
    input_data = []
    for feat in model_features:
        value = request.form.get(feat)
        try:
            input_data.append(float(value))
        except:
            input_data.append(0.0)
    df = pd.DataFrame([input_data], columns=model_features)
    output = model.predict(df)[0]
    if output in [1, 'ckd', 'CKD', 'yes']:
        prediction_text = "The patient is likely to have Chronic Kidney Disease."
    else:
        prediction_text = "The patient is not likely to have Chronic Kidney Disease."
    return render_template('prediction.html', prediction_text=prediction_text)

if __name__ == '__main__':
    app.run(debug=True)
