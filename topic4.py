'''
ex
python topic4.py -t 20 -c Afghanistan
python topic4.py --top=20 --country=Afghanistan
'''

import getopt
import json
import sys

import requests
from bs4 import BeautifulSoup


def crawler(number, country):
    url = 'https://www.alexa.com/topsites'
    if country:
        try:
            with open('country.json', 'r') as f:
                country_dict = json.load(f)
        except FileNotFoundError:
            save_country_json()
            with open('country.json', 'r') as f:
                country_dict = json.load(f)

        url += f'/countries/{country_dict[country]}'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    for s in soup.select('.td.DescriptionCell')[:number]:
        print(s.text.strip())

def save_country_json():
    url = 'https://www.alexa.com/topsites/countries'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    with open('country.json', 'w') as f:
        f.write(json.dumps({li.text.strip(): li('a')[0]['href'].split('/')[-1] for s in soup.select('.countries.span3') for li in s.select('li')}))

def main(argv):
    number = 20
    country = ''
    try:
        opts, args = getopt.getopt(argv, '-c:-t:', ['country=', 'top='])
    except getopt.GetoptError:
        print('topic4.py -top <number> -country <country>')
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-top', '--top'):
            number = arg
        elif opt in ('-c', '--country'):
            country = arg
    crawler(int(number), country)

if __name__ == '__main__':
    main(sys.argv[1:])
