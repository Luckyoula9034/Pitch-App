from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    message = 'Pitch App'
    return render_template('index.html',message = message)

@app.route('/pitch/<int:pitch_id>')
def pitch(pitch_id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    return render_template('pitch.html',id = pitch_id)