from flask import Flask, render_template, request, jsonify  

app = Flask(__name__)  

@app.route('/')  
def index():  
    return render_template('index.html')  

@app.route('/show_alert', methods=['POST'])  
def show_alert():  
    input_text = request.form.get('inputText')  
    return jsonify({'input_text': input_text})  

if __name__ == '__main__':  
    app.run(debug=True)  