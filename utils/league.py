import requests
import json
r = requests.get('https://esports-api.lolesports.com/persisted/gw/getSchedule?hl=pt-BR', headers={'x-api-key': '0TvQnueqKa5mxJntVWt0w4LpLfEkrV1Ta8rQBb9Z'})
resp_dict = r.json()
pretty = json.dumps(resp_dict, indent=4)
print(pretty)
save_file = open('json_data.json', 'w')
json.dump(resp_dict, save_file, indent=4)
