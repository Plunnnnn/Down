from flask import Blueprint, render_template, request
from app.game import *
from app.scrape import *
import re

routes = Blueprint('routes', __name__)

games = []  # This should be populated elsewhere

@routes.route('/game/<int:idx>')
def game_detail(idx):
	if idx < len(games):
		game = games[idx]
		
		#print("TESTR __________________\n\n\n", " OF TYPE =", type(details), "\n\n\n". game.details ,"\n\n\n")
		return render_template('game_detail.html', game=game, details=game.details)
	else:
		return "Game not found", 404

@routes.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		search_query = request.form.get('search_query')
		if search_query:
			global info
			info = Info(search_query)
			game = []
			for idx in range(len(info.links)):
				game = Game(info, idx)
				games.append(game)
			return render_template('index.html', games=games)
	
	return render_template('index.html', games=games)
