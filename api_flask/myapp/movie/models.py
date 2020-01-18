from myapp import db

class Movie(db.Model):
    
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(255))
    year = db.Column(db.Integer)
    
    def __init__(self,name,year):
        self.name = name
        self.year = year