from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('search5.html')

@app.route('/search', methods = ['POST'])
def search():
    import pandas as pd
    genere = request.form.getlist('option1')
    dati_film = pd.read_csv('https://raw.githubusercontent.com/wtitze/3E/main/2010.csv', sep=';')
    risultato = dati_film[dati_film['Genres']==genere[0]]
    if len(risultato) == 0:
        table = 'film non trovato'
    else:
        table = risultato.to_html()
    return render_template('table5.html', tabella = table)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)