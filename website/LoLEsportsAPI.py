import requests
from datetime import datetime
from jinja2 import Environment, FileSystemLoader
from flask import render_template

date = datetime.now()


env = Environment(loader=FileSystemLoader('website/templates/'))


ITEMS_URL = "https://ddragon.bangingheads.net/cdn/latest/img/item/"
CHAMPIONS_URL = "https://ddragon.bangingheads.net/cdn/latest/img/champion/"

#template = env.get_template('game_details.html')
#output = render_template(CHAMPIONS_URL=CHAMPIONS_URL)


API_URL_PERSISTED = "https://esports-api.lolesports.com/persisted/gw"
API_URL_LIVE = "https://feed.lolesports.com/livestats/v1"
API_KEY = "0TvQnueqKa5mxJntVWt0w4LpLfEkrV1Ta8rQBb9Z"


'''Função para obter partidas ao vivo'''
def get_live_games():
    return requests.get(f"{API_URL_PERSISTED}/getLive?hl=pt-BR", 
                        headers = {
                        "x-api-key": API_KEY,
                        })


'''Função para obter a agenda de partidas, precisa filtrar pela data atual'''
def get_schedule():
    return requests.get(f"{API_URL_PERSISTED}/getSchedule?hl=pt-BR",
                        headers = {
                        "x-api-key": API_KEY,
                        })



def get_live_window_game(gameId):
    return requests.get(f"{API_URL_LIVE}/window/{gameId}",
                        params = {
                        "hl": "pt-BR",
                        },
                        headers = {
                        "x-api-key": API_KEY,
                        }
                        )



def get_live_details_game(gameId):
    return requests.get(f"{API_URL_LIVE}/details/{gameId}",
                        params = {
                        "hl": "pt_BR",
                        #                        "startingTime": date,
                        },
                        headers = {
                        "x-api-key": API_KEY,
                        })



def get_game_details(gameId):
    return requests.get(f"{API_URL_PERSISTED}/getEventDetails",
                        params = {
                        "hl": "pt-BR",
                        "id": gameId,
                        },
                        headers = {
                        "x-api-key": API_KEY,
                        })




'''Remover os segundos e adiconar Z'''
def remover_segundos(startTime):
    return startTime[:-6] + '00Z'

