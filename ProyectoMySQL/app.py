from flask import Flask, render_template, request, redirect, url_for
import os
import database as db

template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir, 'src', 'templates')
app = Flask(__name__, template_folder=template_dir)

# Rutas de la aplicación
@app.route('/')
def home():
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM songs")
    myresult = cursor.fetchall()
    # Convertir los datos a diccionario
    songs = []
    columnNames = [column[0] for column in cursor.description]
    for record in myresult:
        songs.append(dict(zip(columnNames, record)))
    cursor.close()
    return render_template('index.html', songs=songs)

# Ruta para guardar canciones en la base de datos
@app.route('/song', methods=['POST'])
def addSong():
    titulo = request.form['titulo']
    artista = request.form['artista']
    genero = request.form['genero']
    reproducciones = request.form['reproducciones']
    album = request.form['album']
    if titulo and artista and genero and reproducciones and album:
        cursor = db.database.cursor()
        sql = "INSERT INTO songs (titulo, artista, genero, reproducciones, album) VALUES (%s, %s, %s, %s, %s)"
        data = (titulo, artista, genero, reproducciones, album)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('home'))

@app.route('/delete/<string:id>')
def delete(id):
    cursor = db.database.cursor()
    sql = "DELETE FROM songs WHERE id=%s"
    data = (id,)
    cursor.execute(sql, data)
    db.database.commit()
    return redirect(url_for('home'))

@app.route('/edit/<string:id>', methods=['POST'])
def edit(id):
    titulo = request.form['titulo']
    artista = request.form['artista']
    genero = request.form['genero']
    reproducciones = request.form['reproducciones']
    album = request.form['album']
    if titulo and artista and genero and reproducciones and album:
        cursor = db.database.cursor()
        sql = "UPDATE songs SET titulo = %s, artista = %s, genero = %s, reproducciones = %s, album = %s WHERE id = %s"
        data = (titulo, artista, genero, reproducciones, album, id)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, port=4000)