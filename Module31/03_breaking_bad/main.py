import requests
import json

gen_info = requests.get('https://www.breakingbadapi.com/api/')
info_to_json = json.loads(gen_info.text)
print(info_to_json['deaths'])
gen_deaths_info = requests.get(info_to_json['deaths'])
info_to_json2 = json.loads(gen_deaths_info.text)
max_deaths_info = max(info_to_json2, key=lambda x: x['number_of_deaths'])
with open('max-death-info.json', 'w') as file:
    data = '1. ID эпизода {0}.\n' \
           '2. Номер сезона {1}.\n' \
           '3. Номер эпизода {2}.\n' \
           '4. Общее количество смертей {3}.\n' \
           '5. Список погибших {4}.'. \
        format(max_deaths_info['death_id'], max_deaths_info['season'],
               max_deaths_info['episode'], max_deaths_info['number_of_deaths'],
               max_deaths_info['death'])
    file.write(data)
print('Самое большое количество смертей произошло в {} серии {} сезона. '
      '\nКоличество смертей - {} жертв'.
      format(max_deaths_info['episode'], max_deaths_info['season'],
             max_deaths_info['number_of_deaths']))
