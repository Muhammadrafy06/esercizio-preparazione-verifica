from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('search2.html')

@app.route('/search', methods = ['GET'])
def search():
    import pandas as pd
    genere = request.args['genere']
    dati_film = pd.read_csv('https://raw.githubusercontent.com/wtitze/3E/main/2010.csv', sep=';')
    risultato = dati_film[dati_film['Genres']==genere.capitalize()]
    if len(risultato) == 0:
        table = 'film non trovato'
    else:
        table = risultato.to_html()
    return render_template('table2.html', tabella = table)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)