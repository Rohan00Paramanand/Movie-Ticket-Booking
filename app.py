from flask import Flask, render_template, request
from random import sample

app = Flask(__name__, template_folder='templates')

global theatre
Cities = ['Delhi', 'Mumbai', 'Chennai', 'Kolkata', 'Chandigarh', 'Shimla']
Theatres = ['PVR', 'INOX', 'US Cinemas', 'JAM']
Movies_by_theatre = {
    'PVR': ['Bahubali 1', 'Bahubali 2', 'RRR', 'The Kashmir Files'],
    'INOX': ['RRR', 'Bhool Bhulaiyaa', 'Singham'],
    'US Cinemas': ['Bahubali 2', 'Dabangg', 'Bajarangi Bhaijaan'],
    'JAM': ['URI: The Surgical Strike', 'RRR', 'Life of Pi', 'English Medium'],
}

@app.route('/')
def home():
    return render_template('index.html', cities = Cities)

@app.route('/City', methods = ['POST'])
def choose_theatre():
    theatre = request.form
    return render_template('choose_theatre.html', theatres = Theatres)

@app.route('/Theatre', methods = ['POST'])
def choose_movie():
    available_movies = sample(Movies_by_theatre[theatre], k=min(3, len(Movies_by_theatre[theatre])))
    return render_template('choose_movie', movies = available_movies)

if __name__ == "__main__":
    app.run(debug=True)