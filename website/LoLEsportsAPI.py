import requests
from pprint import pprint
from datetime import datetime, timedelta

date = datetime.now()

API_URL_PERSISTED = "https://esports-api.lolesports.com/persisted/gw"
API_URL_LIVE = "https://feed.lolesports.com/livestats/v1"
API_KEY = "0TvQnueqKa5mxJntVWt0w4LpLfEkrV1Ta8rQBb9Z"


def get_live_games():
    return requests.get(f"{API_URL_PERSISTED}/getLive?hl=pt-BR", 
                        headers = {
                        "x-api-key": API_KEY,
                        })

def get_schedule():
    return requests.get(f"{API_URL_PERSISTED}/getSchedule?hl=pt-BR",
                        headers = {
                        "x-api-key": API_KEY,
                            })

def get_live_window_game(gameId:dict, date:dict):
    return requests.get(f"{API_URL_LIVE}/window/{gameId}",
                        params = {
                        "hl": "pt-BR",
                        "startingTime": date,
                        "gameId": gameId,
                        },
                        headers = {
                        "x-api-key": API_KEY,
                        }
                        )

def get_live_datails_game(gameId:dict, date:dict):
    return requests.get(f"{API_URL_PERSISTED}/details/window/{gameId}",
                        params = {
                        "hl": "pt_BR",
                        "startingTime": date,
                        },
                        headers = {
                        "x-api-key": API_KEY,
                        })

def get_game_details(gameId:str):
    return requests.get(f"{API_URL_PERSISTED}/getEventDetails",
                        params = {
                        "hl": "pt-BR",
                        "id": "gameId",
                        },
                        headers = {
                        "x-api-key": API_KEY,
                        })

def get_iso_date_multiply_of_10():
    date = datetime.now().replace(microsecond=0)
    if date.second % 10 != 0:
        date = date.replace(second=date.second - (date.second % 10))
  
    date = date - timedelta(seconds=60)
  
    return date.isoformat()
resultado = get_iso_date_multiply_of_10()
print(type(resultado))




response = get_live_window_game("110418013824164864", str("2023-07-31T16:00:00Z")).json()
#response = get_live_games().json()
#pprint(date)
