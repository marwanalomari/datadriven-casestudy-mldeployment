# Import libraries
import pickle
from flask import Flask, request, jsonify, render_template
from sklearn.feature_extraction.text import CountVectorizer

app = Flask(__name__)
@app.route('/')

def my_form():
    return render_template('form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    # Import trained model
    pickled_model = pickle.load(open('model_lr.pkl', 'rb')) 
    vectorizer=pickle.load(open("vectorizer.pickle", 'rb'))
    text = request.form['text']
    result = pickled_model.predict_proba(vectorizer.transform([text]))[0][1]
    if result > 0.5:
        label="True"
    else:
        label="False"
    data = [{'query':text,'is_posology':label}]
    return(render_template('form.html', variable=(json.dumps(data))))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4002)
