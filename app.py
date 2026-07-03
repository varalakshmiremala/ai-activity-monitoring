import streamlit as st

st.title("AI Activity Monitoring")

app = Flask(__name__)

# Mee model file ni load cheskuntunnam
with open('heart_model.pkl','rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html', prediction="No Prediction Yet")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Ikkada JSON format asalu vaadoddu! 
        # Mee model ki kaavalsina direct inputs ni pampali.
        # Example ga mee model ki 3 features unte dummy values ila pampali:
        dummy_input = np.array([[0, 0, 0,0,0,0,0,0,0,0,0,0,0]]) 
        
        # Model prediction calculation
        prediction_code = model.predict(dummy_input)[0]
        
        # Model numbers isthe (0, 1) text ga maarchu
        if prediction_code == 0:
            result = "Walking"
        elif prediction_code == 1:
            result = "Running"
        else:
            result = "Standing"
            
    except Exception as e:
        print("Error details:", e)  # Terminal lo em error undo kanipisthundhi
        result = "Error in Prediction"

    # Thirigi andhamaina HTML screen ke result ni pampisthunnam
    return render_template('index.html', prediction=result)

if __name__ == '__main__':
    app.run(port=5000, debug=True)