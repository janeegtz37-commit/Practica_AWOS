from flask import Flask, render_template, request, justify, make_response,session
app = Flask(__name__)

@app.route('/productos')
def productos():
 import mysql.connector
 mydb = mysql.connector.connect(
  host="46.28.42.226",
  user="u760464709_24005242_usr",
  password="u7?Jpkt>Y*E7",
  database="u760464709_24005242_bd"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM productos")
myresult = mycursor.fetchall()
return make_response(jsonify(myresult))

mycursor = mydb.cursor()
sql = "INSERT INTO productos (titulo, descripcion, precio, talla, estado, disponible) VALUES (%s, %s, %s, %s, %s, %s)"
val = (request.form['txtTitulo'], request.form['txtDescripcion'], request.form['txtPrecio'], request.form['txtTalla'], request.form['txtEstado'], request.form['txtDisponible'])
mycursor.execute(sql, val)

mydb.commit()
