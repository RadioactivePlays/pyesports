from flask import Blueprint, blueprints, json, render_template
from datetime import datetime
from website.LoLEsportsAPI import get_live_games, print_game

views = Blueprint('views', __name__)

#response = get_live_games()
#live_games_data = json.loads(response.text)

#print(type(live_games_data))
#print(live_games_data)

#time_a = live_games_data['data']['schedule']['events'][0]['match']['teams'][0]['name']
#time_b = live_games_data['data']['schedule']['events'][0]['match']['teams'][1]['name']


@views.route('/')
def home():
    response = get_live_games()
    live_games_data = json.loads(response.text)

#    filtered_data = [event for event in live_games_data['data']['schedule']['events'] if event['state'] == 'inProgress']
#    filtered_games = filtered_data
#    print(filtered_games)
    events = live_games_data['data']['schedule']['events']
    if not events:
        return render_template('table.html', nogames=True)

    if len(events) >= 1:
        time_a = events[0]['match']['teams'][0]['name']
        time_b = events[0]['match']['teams'][1]['name']
        return render_template('table.html', time_a=time_a, time_b=time_b, events=events)

    else:
        time_a = None
        time_b = None
#    return render_template('table.html', events=events, timea=time_a, timeb=time_b)
