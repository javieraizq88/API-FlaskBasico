                            API REACT FLASK

1) crear archivo $ Pipfile


2) en terminal

$$$$ pipenv shell 
o
$ pipenv --python=3.7.7 (la version de python)


3) crear app.py (seria como el index.js)

4) instalar flask

$$$ pipenv install flask
$ pipenv install flask-script
$ pipenv install flask-cors
$ pipenv install flask-migrate
$ pipenv install flask-cors
$ pipenv install flask-sqlalchemy

flask: libreria ppal
flask-script y flask-migrate: para configurar el entorno de ejecucion de la app 
flask-cors: quien puede ver la pagina
flask-sqalchemy: conecta con el gestor de BBDD

genera un Pipfile.lock q es como el Package.json

5) hacer los from xxxxxx import xxxxx en app.py

6) $ python app.py runserver

###############################################################################################################
                                            opcion 1: SQlite
6) en el terminal

$ python app.py db init

se ejevuta la primera vez q estoy config mi aplicacion
crea una carpeta Migrations q guarda las migraciones de los modelos def en el archivo models

7) terminal
$ python app.py db migrate

se va a crear un archivo bd.sqlite3


8) terminal
$ python app.py db upgrade

para actualizar la migraciones al archivo bd.sqlite3 y los lleva a la BBDD

9) instalar plug-in SQLite 0.8.1
permite ver la BBDD

10) en la app principal, hacer click en cualquier parte y ejecutar ctrl + E
escribir:
    >SQLite Open database

seleccionar archivo:
    db.sqlite3

abre a mano derecha abajo, en el explorador de archivos una BBDD db.sqlite3 con la info

#########################################################################################################
                                
                                opcion 2: MySQL
1) en cmd administrador, buscar el archivo donde estoy trabajando (cd OneDrive....)

pip install --only-binary :all: mysqlclient


2) en terminal 
    $ pipenv install PyMySQL


3) para ver si esta funcionando en terminal

$ python app.py db init
$ python app.py db migrate
$ python app.py db upgrade


4) en terminal 
$ pipenv install


6) para crear la BBDD
abrir MySQL 8.0 Command Line Client
    escribir el password
    $ create databse testapi;

