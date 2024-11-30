from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/City')
def choose_city():
    pass

if __name__ == "__main__":
    app.run(debug=True)