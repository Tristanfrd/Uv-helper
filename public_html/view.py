from flask import Flask, render_template

app = Flask(__name__)

# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')
# To get one variable, tape app.config['MY_VARIABLE']


@app.route('/index/')
def index():
    return render_template('index.html')


@app.route('/connexion/')
def connexion():
    return render_template('pageConnexion.html')

@app.route('/listesPatient/')
def listesPatient():
    return render_template('listePatients.html')
