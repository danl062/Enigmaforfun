from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('enigma.html')


@app.route('/enigme', methods=['POST'])
def enigme():
    reponse = request.form['reponse']
    if reponse == "11":
        return redirect(url_for('enigme2'))
    else:
        return redirect(url_for('index'))


@app.route('/enigme2')
def enigme2():
    return render_template('enigme2.html')


@app.route('/enigme2', methods=['POST'])
def enigme2_submit():
    reponse = request.form['reponse']
    if reponse.lower() == "יצחק":
        return redirect(url_for('enigme3'))
    else:
        return redirect(url_for('enigme2'))


@app.route('/enigme3')
def enigme3():
    return render_template('enigme3.html')


@app.route('/enigme3', methods=['POST'])
def enigme3_submit():
    reponse = request.form['reponse']
    if reponse.lower() == "אלחנן":
        return "מזל טוב! פתרת את כל החידות וגילית את הכתובת: יצחק אלחנן 11, תל אביב."
    else:
        return redirect(url_for('enigme3'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
