from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#iniciando framework
app = Flask(__name__)
#iniciando o banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.sqlite3'
#instanciando o banco
db = SQLAlchemy(app)

from myapp.movie.views import movie_bp

app.register_blueprint(movie_bp)

db.create_all()

