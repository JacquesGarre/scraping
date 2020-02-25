import requests
import bs4 as BeautifulSoup
import json



# EX1
response = requests.get('https://fr.wikipedia.org/robots.txt')
robots_txt_content = response.text

#EX2
html = requests.get('https://www.data.gov/').text
soup = BeautifulSoup.BeautifulSoup(html, 'html.parser')
nb_datasets = soup.find('div', {'class': 'text-center getstarted'}).find('a').get_text()

#EX3
html = requests.get('https://www.linkedin.com/').text
soup = BeautifulSoup.BeautifulSoup(html, 'html.parser')
h1_tag =  soup.find('h1', {'class': 'hero__headline hero__headline--basic'})

#EX4
html = requests.get('https://en.wikipedia.org/wiki/Main_Page').text
soup = BeautifulSoup.BeautifulSoup(html, 'html.parser')
tags = ['h'+str(i) for i in range(1,7)]
headers = soup.find_all(tags)

#EX5
html = requests.get('https://fr.wikipedia.org/wiki/%C3%89lisabeth_II').text
soup = BeautifulSoup.BeautifulSoup(html, 'html.parser')
img_tags = soup.find_all('img')
img_urls = []
for img_tag in img_tags:
    img_urls.append(img_tag['src'])

#EX6
def get_followers_count(twitter_account):
    url = 'https://twitter.com/' + twitter_account
    html = requests.get(url).text
    soup = BeautifulSoup.BeautifulSoup(html, 'html.parser')
    followers_count = soup.find('a', {'href': '/'  + twitter_account + '/followers'})['title']
    return followers_count

get_followers_count('U_lookme')

#EX7
def to_celsius(kelvin):
    return round(kelvin - 273.15, 1)

def get_weather(city):
    API_KEY = 'de92b6127070e97064ae1271c2aed8d2'
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(city, API_KEY)
    json = requests.get(url).json()
    print('\n')
    print('======== Météo de ' + city + ' ========')
    print('\n')
    print('---- TEMPERATURE ----')
    print('température : ', to_celsius(json['main']['temp']), '°C')
    print('température ressentie : ', to_celsius(json['main']['feels_like']), '°C')
    print('température minimum : ', to_celsius(json['main']['temp_min']), '°C')
    print('température maximum: ', to_celsius(json['main']['temp_max']), '°C')
    print('\n')
    print('---- VENT ----')
    print('vitesse: ', json['wind']['speed'], 'km/h')
    print('\n')
    print('---- TEMPS ----')
    print('principal: ', json['weather'][0]['main'])
    print('description: ', json['weather'][0]['description'])
    print('\n')

# get_weather('Marseille')




