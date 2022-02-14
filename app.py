
from flask import Flask, jsonify,abort, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import delete

app = Flask(__name__)
paswd = '135790'
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:{}@localhost:5432/Bibliotheque'.format(paswd)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)

class Categorie(db.Model):
    __tablename__='categories'
    id = db.Column(db.Integer, primary_key=True)
    libelle_categorie = db.Column(db.String(150), nullable=False)
    v = db.relationship('Livre', backref='Categorie', lazy=True)

    def __init__(self, libelle_categorie):
        self.libelle_categorie = libelle_categorie,

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def format(self):
        return{
            'libelle_categorie':self.libelle_categorie,
        }   

class Livre(db.Model):
    __tablename__ = "livres"
    idlivre = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(100), nullable=False)
    titre = db.Column(db.String(50), nullable=False) 
    date_publication = db.Column(db.Date, nullable=False)
    auteur = db.Column(db.String(50), nullable=False)
    editeur = db.Column(db.String(50), nullable=False)
    id = db.Column(db.Integer, db.ForeignKey('categories.id'))

    def __init__(self, isbn, titre, date_publication, auteur, editeur, id):
        self.isbn = isbn,
        self.titre = titre,
        self.date_publication = date_publication,
        self.auteur = auteur,
        self.editeur = editeur,
        self.id = id,
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def format(self):
        return {
            'idlivre':self.idlivre, 
            'isbn':self.isbn,
            'titre':self.titre,
            'date_publication':self.date_publication,
            'auteur':self.auteur,
            'editeur':self.editeur,
        }
  
db.create_all()


##################################################################
#               LISTER TOUS LES LIVRES
##################################################################
@app.route('/livres')
def get_liv1():
   livres = Livre.query.all()
   livres = [p.format() for p in livres]
   return jsonify(livres)
##################################################################
# 
#               LISTER TOUTES LES CATEGORIES
# 
##################################################################
@app.route('/categories')
def get_cat1():
    categories = Categorie.query.all() 
    categories = [a.format() for a in categories]
    return jsonify(categories)
    
##################################################################
# 
#               RECHERCHER UN LIVRE EN PARTICULER PAR ID
# 
##################################################################
@app.route('/livres/<int:idlivre>')
def recherche_id(idlivre):
    liv2 = Livre.query.get(idlivre)  
    if liv2 is None:
        abort(404)
    else:
        return liv2.format()      
##################################################################
# 
#                 LISTE DES LIVRES D'UNE CATEGORIE
# 
###################################################################
@app.route('/categories/<int:id>/livres')
def categ(id):
    cat3 = Categorie.query.all()
    cat3.Livre = [z.format() for z in Categorie]
    return jsonify(cat3.Categorie)
###################################################################
# 
#                LISTE D'UNE CATEGORIE 
# 
###################################################################
@app.route('/categories/<int:id>/livres')
def categ2(id):
    cat3 = Categorie.query.all()
    cat3.Livre = [z.format() for z in Categorie]
    return jsonify(cat3.Categorie)
    
###################################################################
# 
#                 RECHERCHER UNE CATEGORIE PAR ID
# 
##################################################################    
@app.route('/categories/<int:id>')
def idcats(id):
    cat9 = Categorie.query.get(id)  
    if cat9 is None:
        abort(404)
    else:
        return cat9.format()
##################################################################
# 
#                  SUPPRIMER UN LIVRE
# 
##################################################################
@app.route('/livres/<int:idlivre>')
def suplivre(idlivre):    
    cont=Livre.query.get(idlivre) 
    db.session.delete(cont)
    db.session.commit()
##################################################################
# 
#                  SUPPRIMER UN CATEGORIE
# 
##################################################################
@app.route('/categorie/<int:id>')
def supcat(id):
    v=Categorie.query.get(id)
    db.session.delete(v)
    db.session.commit()
##################################################################
# 
#                  MODIFIER LES INFOS D'UN LIVRE
# 
##################################################################
@app.route('/livres<int:idlivre>', methods=['PATCH'])
def modinf(idlivre):
    body = request.get_json()
    infliv = Livre.query.get(idlivre)  
    if 'isbn' in body and 'titre' in body and 'date' in body and 'auteur' in body and 'editeur' in body:
        Livre.isbn = body['isbn'] 
        Livre.titre = body['titre']
        Livre.date = body['date']
        Livre.auteur = body['auteur']
        Livre.editeur = body['editeur']
    db.session.update() 
    return jsonify({
        'success modify': True,
        'livres': infliv.format(),
    })
##################################################################
# 
#                  MODIFIER LE LIBELLE D'UNE CATEGORIE
# 
##################################################################
@app.route('/categories<int:id>', methods=['PATCH'])
def modcat(id):
    body = request.get_json()
    libcat = Categorie.query.get(id)  
    if 'libelle_categorie' in body:
        Categorie.libelle_categorie = body['libelle_categorie'] 
    db.session.update() 
    return jsonify({
        'success modify': True,
        'categorie': libcat.format(),
    })
  
