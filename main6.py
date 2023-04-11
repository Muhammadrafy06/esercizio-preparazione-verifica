from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    import pandas as pd
    dati_film = pd.read_csv('https://raw.githubusercontent.com/wtitze/3E/main/2010.csv', sep=';')
    risultato = dati_film[dati_film['Budget'].isnull()][['Title']]
    table = risultato.to_html()
    return render_template('search6.html', tabella = table)


   
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)