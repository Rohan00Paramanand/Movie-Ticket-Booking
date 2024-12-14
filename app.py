from flask import Flask, render_template, request, g
from database import get_db, close_db, get_Cities, get_Movies, get_Theatres, book, get_Tickets, ticket_info

app = Flask(__name__, template_folder='templates')

@app.teardown_appcontext
def teardown_db(exception):
    close_db(exception)

# Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Check ticket availability
@app.route('/check_tickets')
def check_tickets():
    Available_Tickets = get_Tickets()
    return render_template('check_tickets.html', A_Tickets = Available_Tickets)

# Pick City
@app.route('/choose_city')
def choose_city():
    Cities = get_Cities()
    return render_template('choose_city.html', cities = Cities)

# Pick Theatre
@app.route('/City', methods = ['POST', 'GET'])
def choose_theatre():
    Theatres = get_Theatres()
    return render_template('choose_theatre.html', theatres = Theatres)

# Pick Movie
@app.route('/Theatre', methods = ['POST', 'GET'])
def choose_movie():
    Movies = get_Movies()
    theatre = request.form.get('choose_theatre')
    return render_template('choose_movie.html', movies = Movies)

# Book Tickets
@app.route('/Book', methods = ['POST', 'GET'])
def book_tickets():
    global Movie
    Movie = request.form.get('choose_movie')
    Available_Tickets = ticket_info(Movie)
    if Available_Tickets == 0:
        return render_template('house_full.html', movie =  Movie)
    return render_template('book_tickets.html', movie = Movie, AT = Available_Tickets)

# Success Page
@app.route('/Tickets', methods = ['POST', 'GET'])
def success():
    Tickets = request.form.get('no_tickets')
    book(Movie, int(Tickets))
    return render_template('success.html', tickets = Tickets, movie = Movie)

if __name__ == "__main__":
    app.run(debug=True)