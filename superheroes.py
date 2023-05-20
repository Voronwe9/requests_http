import requests

def _getting_file():
    file_path = url + command
    response = requests.get(file_path).json()
    if requests.get(file_path).status_code != 200:
        print(f'Ошибка {requests.get(file_path).status_code}')
    return response

def int_superheroes(name_list):
    superheroes = []
    name = ''
    for items in _getting_file():
        if items['name'] in name_list:
            superheroes.append({'name': items['name'], 'intelligence': items['powerstats']['intelligence']})

    int_hero = 0
    for intel_hero in superheroes:
        if int_hero < int(intel_hero['intelligence']):
            int_hero = int(intel_hero['intelligence'])
            name = intel_hero['name']
    return f"Самый умный супергерой -  {name}, интеллект: {int_hero}"

if __name__ == '__main__':
    url = 'https://akabab.github.io/superhero-api/api'
    command = '/all.json'
    super_need = ['Hulk', 'Captain America', 'Thanos']
    print(int_superheroes(super_need))