from flask import Flask, render_template, session, redirect,request

app = Flask(__name__)

app.secret_key="!LoveBo0kk$sS735"

@app.route('/')
def index():
    return render_template("survey.html")


@app.route('/intake', methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect('/received')

@app.route('/received')
def success():
    return render_template('display_info.html')
    
if __name__=="__main__":
    app.run(debug=True)