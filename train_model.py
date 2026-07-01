from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Ikkada malli original model.pkl file ni load chesthunnam
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html', prediction="No Prediction Yet")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # User screen meedha type chese 3 input values ni ikkada capture chesthunnam
        val1 = float(request.form.get('input1', 0))
        val2 = float(request.form.get('input2', 0))
        val3 = float(request.form.get('input3', 0))
        
        # User ichina real inputs ni model ki pampisthunnam
        user_input = np.array([[val1, val2, val3]]) 
        
        # Model prediction logic (Direct ga Walking, Running, Sitting text ichesthundhi)
        result = model.predict(user_input)[0]
            
    except Exception as e:
        print("Error details:", e)
        result = "Error in Prediction"

    return render_template('index.html', prediction=result)

if __name__ == '__main__':
    app.run(port=5000, debug=True)