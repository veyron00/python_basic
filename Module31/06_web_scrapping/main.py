import requests
import json
import re


def parse(domain: str, tag: str = 'h3') -> list:
    """
    Находит содержимое указанное в тегах html разметки.

    :param domain: Адрес сайта
    :param tag: Название тега (по умолчанию h3)
    :return: None
    """
    pattern = r'<{0}.*?>(.*?)</{0}>'.format(tag)
    site_page = requests.get(domain)
    site_page_to_json = json.dumps(site_page.text)

    result = re.findall(pattern, site_page_to_json)
    return result


site_address = 'http://www.columbia.edu/~fdc/sample.html'
print(parse(site_address))

site_address2 = 'https://habr.com/ru/post/349860/#Regulyarki/videolesson'
data = parse(site_address2, 'h2')
for i_text in data:
    print(i_text.encode().decode('unicode-escape'))  # Декодируем полученный текст