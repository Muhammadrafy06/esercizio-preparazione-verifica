from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


#-------------------esercizio 1--------------------
@app.route('/es1')
def es1():
    return render_template('search.html')


@app.route('/es1search', methods = ['GET'])
def search():
    import pandas as pd
    genere = request.args['film']
    dati_film = pd.read_csv('https://raw.githubusercontent.com/wtitze/3E/main/2010.csv', sep=';')
    risultato = dati_film[dati_film['Genres']==genere.capitalize()]
    if len(risultato) == 0:
        table = 'film non trovato'
    else:
        table = risultato.to_html()
    return render_template('table2.html', tabella = table)
#-------------------esercizio 2--------------------
@app.route('/es2')
def es2():
    return render_template('search2.html')

@app.route('/es2search', methods = ['GET'])
def search2():
    import pandas as pd
    genere = request.args['genere']
    dati_film = pd.read_csv('https://raw.githubusercontent.com/wtitze/3E/main/2010.csv', sep=';')
    risultato = dati_film[dati_film['Genres']==genere.capitalize()]
    if len(risultato) == 0:
        table = 'film non trovato'
    else:
        table = risultato.to_html()
    return render_template('table2.html', tabella = table)

#-------------------esercizio 3--------------------
@app.route('/es3')
def es3():
    return render_template('search3.html')

@app.route('/search_tendina', methods = ['GET'])
def search3():
    film=request.args["genere"]
    genere=df[df["Genres"].str.lower().str.contains(film.strip().lower())]
    dfhtm=genere.to_html()
    return render_template('risultato.html', tabella = dfhtm)

#-------------------esercizio 4--------------------
@app.route('/es4')
def es4():
    return render_template('search4.html')

@app.route('/es4search', methods = ['POST'])
def search4():
    import pandas as pd
    genere = request.form['option1']
    dati_film = pd.read_csv('https://raw.githubusercontent.com/wtitze/3E/main/2010.csv', sep=';')
    risultato = dati_film[dati_film['Genres']==genere.capitalize()]
    if len(risultato) == 0:
        table = 'film non trovato'
    else:
        table = risultato.to_html()
    return render_template('table4.html', tabella = table)


#-------------------esercizio 5--------------------
@app.route('/es5')
def es5():
    return render_template('search5.html')

@app.route('/es5search', methods = ['POST'])
def search5():
    import pandas as pd
    genere = request.form.getlist('option1')
    dati_film = pd.read_csv('https://raw.githubusercontent.com/wtitze/3E/main/2010.csv', sep=';')
    risultato = dati_film[dati_film['Genres']==genere[0]]
    if len(risultato) == 0:
        table = 'film non trovato'
    else:
        table = risultato.to_html()
    return render_template('table5.html', tabella = table)


#-------------------esercizio 6--------------------
@app.route('/es6')
def es6():
    import pandas as pd
    dati_film = pd.read_csv('https://raw.githubusercontent.com/wtitze/3E/main/2010.csv', sep=';')
    risultato = dati_film[dati_film['Budget'].isnull()][['Title']]
    table = risultato.to_html()
    return render_template('search6.html', tabella = table)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)