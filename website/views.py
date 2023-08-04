from flask import Blueprint, blueprints, json, render_template
from website.LoLEsportsAPI import get_live_games

views = Blueprint('views', __name__)

@views.route("/")
def home():
    live_games_response = get_live_games()
    live_games_data = json.loads(live_games_response.text)
    events = live_games_data['data']['schedule']['events']
    if not events:
        return render_template('table.html', nogames=True)

    if len(events) >= 1:
        return render_template('table.html', events=events)
    else:
        return None
