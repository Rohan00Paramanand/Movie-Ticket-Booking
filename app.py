from flask import Flask, render_template, request
from random import sample

app = Flask(__name__, template_folder='templates')

Cities = ['Delhi', 'Mumbai', 'Chennai', 'Kolkata', 'Chandigarh', 'Shimla']
Theatres = ['PVR', 'INOX', 'US Cinemas', 'JAM']
Movies_by_theatre = {
    'PVR': ['Bahubali 1', 'Bahubali 2', 'RRR', 'The Kashmir Files'],
    'INOX': ['RRR', 'Bhool Bhulaiyaa', 'Singham'],
    'US Cinemas': ['Bahubali 2', 'Dabangg', 'Bajarangi Bhaijaan'],
    'JAM': ['URI: The Surgical Strike', 'RRR', 'Life of Pi', 'English Medium'],
}

# Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Pick City
@app.route('/choose_city')
def choose_city():
    return render_template('choose_city.html', cities = Cities)

# Pick Theatre
@app.route('/City', methods = ['POST'])
def choose_theatre():
    return render_template('choose_theatre.html', theatres = Theatres)

# Pick Movie
@app.route('/Theatre', methods = ['POST'])
def choose_movie():
    theatre = request.form.get('choose_theatre')
    available_movies = sample(Movies_by_theatre[theatre], k=min(3, len(Movies_by_theatre[theatre])))
    return render_template('choose_movie.html', movies = available_movies)

# Book Tickets
@app.route('/Book', methods = ['POST'])
def book_tickets():
    global Movie
    Movie = request.form.get('choose_movie')
    return render_template('book_tickets.html', movie = Movie)

# Success Page
@app.route('/Tickets', methods = ['POST'])
def success():
    Tickets = request.form.get('no_tickets')
    return render_template('success.html', tickets = Tickets, movie = Movie)


if __name__ == "__main__":
    app.run(debug=True)