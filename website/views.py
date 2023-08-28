from datetime import datetime
import pytz, json
from flask import Blueprint, render_template, request
from requests.models import default_hooks
from website.LoLEsportsAPI import get_live_games, get_schedule, get_game_details, get_live_window_game, get_live_details_game, remover_segundos

views = Blueprint('views', __name__)

data_atual = datetime.now(pytz.timezone('America/Manaus')).strftime('%Y-%m-%d')


@views.route("/")
def live():
    live_games_response = get_live_games()
    live_games_data = json.loads(live_games_response.text)
    events = live_games_data['data']['schedule']['events']
    if not events:
        nogames= True
    else:
        nogames = False

    return render_template('home.html', events=events, nogames=nogames)

@views.route("/schedule")
def schedule():
    schedule_response = get_schedule()
    schedule_data = json.loads(schedule_response.text)
    agenda = schedule_data['data']['schedule']['events']

    events = [event for event in agenda if remover_segundos(event.get('startTime'))[:10] == data_atual]

    if not events:
        nogames = True
    else:
        nogames = False

    return render_template('schedule.html', events=events, nogames=nogames)




@views.route('/game_details', methods=['GET'])
def get_game_details_route():
    game_id = request.args.get('game_id')

    if not game_id:
        return "ID inválido"
    else:
        game_details_response = get_game_details(game_id)
        game_details_data = json.loads(game_details_response.text)


        eventId = int(game_id) + 1
        getDetails = get_live_window_game(eventId)
        resposta = json.loads(getDetails.text)
        print(resposta)

        return render_template('game_details.html', game_details_data=game_details_data, resposta=resposta)
