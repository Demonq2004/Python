
import mysql.connector

from flask import Flask, render_template
app = Flask(__name__)

polaczenie = mysql.connector.connect(user='dejw', password='Programista2021!', host='127.0.0.1', database='3atp', auth_plugin='mysql_native_password')

zapytanie = "SELECT imie,nazwisko,stanowisko,wiek from uczniowie"

cursor = polaczenie.cursor()
cursor.execute(zapytanie)


    

@app.route('/')
def index():
    lista = []
    for (imie,nazwisko,stanowisko,wiek) in cursor:
        lista.append(imie)
        lista.append(nazwisko)
        
    return render_template('index.html', tekst = tekst)
    
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 

polaczenie.close()