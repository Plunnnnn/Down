from flask import Blueprint, render_template, request
from app.game import *
from app.scrape import *
import threading

routes = Blueprint('routes', __name__)

games = []
last_query = ""

def create_game(info, idx):
    game = Game(info, idx)
    games.append(game)

@routes.route('/game/<int:idx>')
def game_detail(idx):
    if idx < len(games):
        game = games[idx]
        return render_template('game_detail.html', game=game, details=game.details)
    else:
        return "Game not found", 404

@routes.route('/', methods=['GET', 'POST'])
def index():
    global last_query, info  
    if request.method == 'POST':
        search_query = request.form.get('search_query')
        if search_query and search_query != last_query:
            last_query = search_query
            thread = []
            info = Info(search_query)
            games.clear()
            for idx in range(len(info.links)):
                t = threading.Thread(target=create_game, args=(info, idx))
                thread.append(t)
                t.start()
            for t in thread:
                t.join()
            return render_template('index.html', games=games)
    
    return render_template('index.html', games=games)