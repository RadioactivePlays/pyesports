from flask import Blueprint, blueprints, json, render_template
from datetime import datetime
from website.LoLEsportsAPI import get_live_games

views = Blueprint('views', __name__)

response = get_live_games()
live_games_data = json.loads(response.text)

print(type(live_games_data))
print(live_games_data)


@views.route('/')
def home():
    filtered_data = [event for event in live_games_data['data']['schedule']['events'] if event['state'] == 'inProgress']
    filtered_games = filtered_data
    print(filtered_games)
    return render_template('table.html', live=filtered_games)
