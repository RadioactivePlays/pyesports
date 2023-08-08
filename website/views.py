from datetime import datetime
from flask import Blueprint, json, render_template, request
from website.LoLEsportsAPI import get_live_games, get_schedule, get_game_details, remove_seconds, remove_seconds

views = Blueprint('views', __name__)

current_time = datetime.now().strftime('%Y-%m-%d')

@views.route("/")
def live():
    live_games_response = get_live_games()
    live_games_data = json.loads(live_games_response.text)
    events = live_games_data['data']['schedule']['events']
    if events == []:
        return render_template('home.html', nogames=True)
    else:
        return render_template('home.html', events=events, nogames=False)

@views.route("/schedule")
def schedule():
    schedule_response = get_schedule()
    schedule_data = json.loads(schedule_response.text)
    agenda = schedule_data['data']['schedule']['events']
    
    events = [event for event in agenda if remove_seconds(event.get('startTime'))[:10] == current_time]

    if not events:
        return render_template('schedule.html', nogames=True)
    else:
        print(events)
        return render_template('schedule.html', events=events, nogames=False)




@views.route('/game_details', methods=['GET'])
def get_game_details_route():
    game_id = request.args.get('game_id')

    if game_id is not None:
        game_details_response = get_game_details(game_id)
        game_details_data = json.loads(game_details_response.text)

        return render_template('game_details.html', game_details_data=game_details_data)
    else:
        return "ID inválido"
