from flask import render_template
from app import app

@app.route('/',methods=['GET','POST'])
@app.route('/index',methods=['GET','POST'])
def index():
    return render_template('index.html',title="pooptitle")

@app.route('/game',methods=['GET','POST'])
def game():
    return render_template('game.html')

@app.route('/match',methods=['GET','POST'])
def match():
    return render_template('match.html')

@app.route('/choice',methods=['GET','POST'])
def choice():
    return render_template('choice.html')

@app.route('/definition',methods=['GET','POST'])
def definition():
    return render_template('definition.html')