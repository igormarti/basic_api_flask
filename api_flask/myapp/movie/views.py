
from flask import Blueprint,request,jsonify
from myapp.movie.models import Movie
from myapp import app,db

movie_bp = Blueprint('movie',__name__)

@movie_bp.route('/',methods=['GET'])
def home():
    return jsonify({'great':'Welcome to api'})


@movie_bp.route('/movies',methods=['GET'])
def moviesAll():

    movies = Movie.query.all()
    if not movies:
        return jsonify({'status':False,'msg':'Movies empty'})
    
    res = {}
    for m in movies:
        res[m.id] = {'name':m.name,'year':m.year}
        
    return jsonify({'status':True,'movies':res})  


@movie_bp.route('/movie/<id>',methods=['GET'])
def getMovie(id):

    movie = Movie.query.filter_by(id=id).first()
    
    if not movie:
        return jsonify({'status':False,'msg':'Movie not exists'})
        
    return jsonify({'status':True,'id':movie.id,'name':movie.name,'year':movie.year})  


@movie_bp.route('/movie/create',methods=['POST'])
def createMovie():
    
    movie = Movie(name=request.form.get('name'),year=request.form.get('year'))

    if not movie:
        return jsonify({'status':False,'msg':'Error'})
    
    db.session.add(movie)
    db.session.commit()
    
    return jsonify({'id':movie.id,'name':movie.name,'year':movie.year})

@movie_bp.route('/movie/update/<id>',methods=['PUT'])
def updateMovie(id):
    
    movie = Movie.query.filter_by(id=id).first()
    
    if not movie:
         return jsonify({'status':False,'msg':'Not found movie'})
     
    movie.name = request.form.get('name') 
    movie.year = request.form.get('year') 
    db.session.commit()
    
    return jsonify({'status':True,'msg':'Movie updated with success'}) 
    
@movie_bp.route('/movie/delete/<id>',methods=['DELETE'])    
def deleteMovie(id):
    
    movie = Movie.query.filter_by(id=id).first()  
    
    if not movie:
         return jsonify({'status':False,'msg':'Not found movie'})
     
    db.session.delete(movie) 
    db.session.commit()
    
    return jsonify({'status':True,'msg':'Movie deleted with success'})  