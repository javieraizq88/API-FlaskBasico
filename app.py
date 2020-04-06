from flask import Flask, jsonify, request, render_template
# jsonify devuelve en formato JSON la informacion
# request para usar GET, POST, PUT, DELETE
# render_template : crea una salida en html del archivo q yo le diga
from flask_script import Manager # generar los comando para q corra la app
from flask_migrate import Migrate, MigrateCommand # libreria para q genera los comandos para hacer las migraciones (script de las tablas) y crearlas en el gestor de BBDD
from flask_cors import CORS #protege la app y evita el error de cors al ejecutar un fetch
from models import db #comunar la app con el gestor de migraciones 

app = Flask(__name__) # atributo obligatorio
app.url_map.strict_slaches = False # para q si falta un / no de error
app.config['DEBUG'] = True # para ver los errores de la app
app.config['ENV'] = 'development' # entorno de la app o se puede usar 'production' cuando ya se publique
# para desarrollo usando sqlite
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, "db.sqlite3") # para decir q tipo de BBDD va a ser (sqlite)
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # muestra los tracking de la BBDD
# para produccion usando MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = '' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db.init_app(app)
Migrate(app, db)
CORS(app) #para proteger la app

manager = Manager(app)
manager.add_command ('db', MigrateCommand) # init (carpeta de migraciones la primera vez), migrate (crea las migraciones), upgrade (envia las migraciones a la BBDD)

@app.route('/') #por defecto es method: ['GET']
def root():
    return render_template('index.html')

if __name__ == '__main__':
    manager.run()
