from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

# Connexion à la base de données MongoDB
client = MongoClient('mongodb://root:pass12345@localhost:27017/')
db = client['dblp']  # Remplacez 'dblp' par le nom de votre base de données
sub_collection = db['publis']  # Remplacez 'publis' par le nom de votre sous-collection

# Page d'accueil
@app.route('/')
def index():
    # Récupération de toutes les publications et de leurs auteurs
    publications = list(sub_collection.find())
    authors = set(author for publication in publications for author in publication.get('authors', []))
    return render_template('index.html', publications=publications, authors=authors)

# Page de filtrage par auteur
@app.route('/filter_by_author', methods=['GET', 'POST'])
def filter_by_author():
    if request.method == 'POST':
        author = request.form['authors']
        publications = list(sub_collection.find({'authors': author}))
        authors = set(author for publication in publications for author in publication.get('authors', []))
        return render_template('filter_by_author.html', filtered_publications=publications, author=author)

# Page de détails d'une publication
@app.route('/publication/<publication_id>')
def publication_detail(publication_id):
    # Remplacez ce code par la logique pour récupérer les détails de la publication par son ID
    publication = {}  # Remplacez par la publication spécifique
    return render_template('publication_details.html', publication=publication)

# Ajouter une nouvelle publication
@app.route('/add_publication', methods=['POST'])
def add_publication():
    # Remplacez ce code par la logique pour ajouter une nouvelle publication à la base de données
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
