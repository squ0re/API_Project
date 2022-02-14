# API_Project

## Getting Started

### Installation des Dépendances

#### Python 3.10.2
#### pip 21.2.4 from C:\Users\Samuel\AppData\Local\Programs\Python\Python310\lib\site-packages\pip (python 3.10)

Suivez les instructions suivantes pour installer l'ancienne version de python sur la plateforme [python docs](https://www.python.org/downloads/windows/#getting-and-installing-the-latest-version-of-python)

#### Dépendances de PIP

Pour installer les dépendances, ouvrez le dossier `/Documentation` et exécuter la commande suivante:

```bash ou powershell ou cmd
pip install -r requirements.txt
or
pip3 install -r requirements.txt
```

Nous passons donc à l'installation de tous les packages se trouvant dans le fichier `requirements.txt`.

##### clé de Dépendances

- [Flask](http://flask.pocoo.org/)  est un petit framework web Python léger, qui fournit des outils et des fonctionnalités utiles qui facilitent la création d’applications web en Python.

- [SQLAlchemy](https://www.sqlalchemy.org/) est un toolkit open source SQL et un mapping objet-relationnel écrit en Python et publié sous licence MIT. SQLAlchemy a opté pour l'utilisation du pattern Data Mapper plutôt que l'active record utilisés par de nombreux autres ORM

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Démarrer le serveur

Pour démarrer le serveur sur Linux ou Mac, executez:

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```
Pour le démarrer sur Windows, executez:

```bash
set FLASK_APP=app.py
set FLASK_ENV=development
flask run
``` 

## API REFERENCE

Getting starter

Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, http://localhost:5000; which is set as a proxy in frontend configuration.

## Type d'erreur
Les erreurs sont renvoyées sou forme d'objet au format Json:
{
    "success":False
    "error": 400
    "message":"Ressource non disponible"
}

L'API vous renvoie 4 types d'erreur:
. 400: Bad request ou ressource non disponible
. 500: Internal server error
. 422: Unprocessable
. 404: Not found

## Endpoints
. ## GET/livres

    GENERAL:
        Cet endpoint retourne la liste des objets livres, la valeur du succès    
        
    EXEMPLE: curl http://localhost:5000/livres
```
        {
    "livres": [
        {
    "auteur": "PABLO", 
    "date_publication": "Mon, 11 Oct 1999 00:00:00 GMT", 
    "editeur": "ED", 
    "idlivre": 4, 
    "isbn": "l2b", 
    "titre": "Durandeau"
  }, 
  {
    "auteur": "PABLO", 
    "date_publication": "Mon, 11 Oct 1999 00:00:00 GMT", 
    "editeur": "ED", 
    "idlivre": 5, 
    "isbn": "l2b", 
    "titre": "durandeau"
  }, 
  {
    "auteur": "PABLO", 
    "date_publication": "Mon, 01 Jan 2001 00:00:00 GMT", 
    "editeur": "ED", 
    "idlivre": 6, 
    "isbn": "lcb", 
    "titre": "ddeau"
  }, 
  {
    "auteur": "PABLO", 
    "date_publication": "Sun, 19 Sep 1999 00:00:00 GMT", 
    "editeur": "ED", 
    "idlivre": 8, 
    "isbn": "l1d", 
    "titre": "dundeau"
  }, 
  {
    "auteur": "PABLO", 
    "date_publication": "Mon, 11 Oct 1999 00:00:00 GMT", 
    "editeur": "ED", 
    "idlivre": 9, 
    "isbn": "md", 
    "titre": "duradeau"
  }, 
  {
    "auteur": "PABLO", 
    "date_publication": "Wed, 11 Mar 2009 00:00:00 GMT", 
    "editeur": "ED", 
    "idlivre": 10, 
    "isbn": "lm", 
    "titre": "durdeau"
  }, 
  {
    "auteur": "PABLO", 
    "date_publication": "Wed, 11 Mar 2009 00:00:00 GMT", 
    "editeur": "ED", 
    "idlivre": 11, 
    "isbn": "lm", 
    "titre": "durdeau"
  }, 
  {
    "auteur": "PABLO", 
    "date_publication": "Tue, 11 Feb 2003 00:00:00 GMT", 
    "editeur": "ED", 
    "idlivre": 12, 
    "isbn": "l2b", 
    "titre": "durandeau"
  }, 
  {
    "auteur": "PABLO", 
    "date_publication": "Mon, 11 Nov 1799 00:00:00 GMT", 
    "editeur": "ED", 
    "idlivre": 13, 
    "isbn": "l2b", 
    "titre": "durand"
  }, 
  {
    "auteur": "PABLO", 
    "date_publication": "Fri, 11 Dec 1699 00:00:00 GMT", 
    "editeur": "ED", 
    "idlivre": 14, 
    "isbn": "ru", 
    "titre": "durande"
  }, 
  {
    "auteur": "PABLO", 
    "date_publication": "Sat, 13 Nov 1599 00:00:00 GMT", 
    "editeur": "ED", 
    "idlivre": 15, 
    "isbn": "i2b", 
    "titre": "randeau"
  }, 
  {
    "auteur": "PABLO", 
    "date_publication": "Sun, 01 Oct 1499 00:00:00 GMT", 
    "editeur": "ED", 
    "idlivre": 16, 
    "isbn": "pl2b", 
    "titre": "dudeau"
  }, 
  {
    "auteur": "PABLO", 
    "date_publication": "Fri, 11 Oct 1399 00:00:00 GMT", 
    "editeur": "ED", 
    "idlivre": 17, 
    "isbn": "l", 
    "titre": "deau"
  }, 
  {
    "auteur": "PABLO", 
    "date_publication": "Sun, 11 Oct 1299 00:00:00 GMT", 
    "editeur": "ED", 
    "idlivre": 18, 
    "isbn": "l2C", 
    "titre": "durandeau"
  }, 
  {
    "auteur": "PABLO", 
    "date_publication": "Mon, 11 Oct 1199 00:00:00 GMT", 
    "editeur": "ED", 
    "idlivre": 19, 
    "isbn": "l12b", 
    "titre": "drandeu"
  }, 
  {
    "auteur": "PABLO", 
    "date_publication": "Wed, 11 Oct 1099 00:00:00 GMT", 
    "editeur": "ED", 
    "idlivre": 20, 
    "isbn": "lb", 
    "titre": "dur"
  }, 
  {
    "auteur": "ESCOBAR", 
    "date_publication": "Sun, 11 Oct 1998 00:00:00 GMT", 
    "editeur": "ED", 
    "idlivre": 21, 
    "isbn": "l2C", 
    "titre": "KIOSK"
  }, 
  {
    "auteur": "ESCOBAR", 
    "date_publication": "Wed, 11 Oct 1893 00:00:00 GMT", 
    "editeur": "ED", 
    "idlivre": 22, 
    "isbn": "l12b", 
    "titre": "FEU"
  }, 
  {
    "auteur": "ESCOBAR", 
    "date_publication": "Sun, 11 Oct 1699 00:00:00 GMT", 
    "editeur": "ED", 
    "idlivre": 23, 
    "isbn": "lb", 
    "titre": "DRAMATURE"
  }
    ],
    "status_code": 200,
    "success": true,
  }
```

.##GET/books(book_id)
  GENERAL:
  Cet endpoint permet de récupérer les informations d'un livre particulier s'il existe par le biais de l'ID.

    EXEMPLE: http://localhost:5000/books/3
```
    {
        "auteur": "Louis Saulnier, Théodore Gringoire",
        "code_ISBN": "978-2-0802",
        "date_publication": "26-02-2022",
        "editeur": "Flammarion",
        "id": 3,
        "titre": "Le répertoire de la cuisine"
    }
```


. ## DELETE/books (book_id)

    GENERAL:
        Supprimer un element si l'ID existe. Retourne l'ID du livre supprimé, la valeur du succès et le nouveau total.

        EXEMPLE: curl -X DELETE http://localhost:5000/books/4
```
    {
        "id_book": 4,
        "new_total": 3,
        "success": true
    }
```

. ##PATCH/books(book_id)
  GENERAL:
  Cet endpoint permet de mettre à jour, le titre, l'auteur, et l'éditeur du livre.
  Il retourne un livre mis à jour.

  EXEMPLE.....Avec Patch
  ``` curl -X PATCH http://localhost:5000/books/1 -H "Content-Type:application/json" -d '{"auteur": "Azychika, Takumi Fukui","editeur": "Ki-oon","titre": "Jujutsu Kaisen"}'
  ```
  ```
    {
        "auteur": "Azychika, Takumi Fukui",
        "code_ISBN": "979-1-0327",
        "date_publication": "03-02-2022",
        "editeur": "Ki-oon",
        "id": 1,
        "titre": "Jujutsu Kaisen"
    }
    ```

. ## GET/categories

    GENERAL:
        Cet endpoint retourne la liste des categories de livres, la valeur du succès et le total des categories disponibles. 
    
        
    EXEMPLE: curl http://localhost:5000/categories

        {
    "categories": [
        {
    "libelle_categorie": "Linux"
  }, 
  {
    "libelle_categorie": "livre_fantastique"
  }, 
  {
    "libelle_categorie": "livre_policier"
  }, 
  {
    "libelle_categorie": "livre_horreur"
  }, 
  {
    "libelle_categorie": "livre_drame"
  }
    ],
    "status_code": 200,
    "success": true,
    "total": 12
}
```

.##GET/categories(categorie_id)
  GENERAL:
  Cet endpoint permet de récupérer les informations d'une categorie si elle existe par le biais de l'ID.

    EXEMPLE: http://localhost:5000/categories/6
```
    {
        "categorie": "Cuisine",
        "id": 6
    }
```

. ## DELETE/categories (categories_id)

    GENERAL:
        Supprimer un element si l'ID existe. Retourne l'ID da la catégorie supprimé, la valeur du succès et le nouveau total.

        EXEMPLE: curl -X DELETE http://localhost:5000/categories/11
```
    {
        "id_cat": 11,
        "new_total": 10,
        "status": 200,
        "success": true
    }
```

. ##PATCH/categories(categorie_id)
  GENERAL:
  Cet endpoint permet de mettre à jour le libelle ou le nom de la categorie.
  Il retourne une nouvelle categorie avec la nouvelle valeur.

  EXEMPLE.....Avec Patch
  ``` curl -X PATCH 'http://localhost:5000/categories/4' -H "Content-Type:application/json" -d '{"categorie": "Bandes Dessinées"}'
  ```
  ```
    {
        "categorie": "Bandes Dessinées",
        "id": 4
    }

.##GET/books/categories(categorie_id)
  GENERAL:
  Cet endpoint permet de lister les livres appartenant à une categorie donnée.
  Il renvoie la classe de la categorie et les livres l'appartenant.

    EXEMPLE: http://localhost:5000/books/categories/4
```
    {
    "Status_code": 200,
    "Success": true,
    "books": [
        {
            "auteur": "Gege Atakumi",
            "code_ISBN": "979-1-0328",
            "date_publication": "03-02-2022",
            "editeur": "Ki-oon",
            "id": 2,
            "titre": "Jujutsu Kaisen T13"
        },
        {
            "auteur": "Azychika, Takumi Fukui",
            "code_ISBN": "979-1-0327",
            "date_publication": "03-02-2022",
            "editeur": "Ki-oon",
            "id": 1,
            "titre": "Jujutsu Kaisen"
        }
    ],
    "classe": {
        "categorie": "Bandes Dessinées",
        "id": 4
    }
}
'''
