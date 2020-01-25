#Dane do uruchomienia:
# py Scraper.py Fiat Tipo 2018 Warszawa 50000 65000 2020 10000 100000

import json
import bs4
import requests
import sys
import base64

#Dane wejściowe:
brand = sys.argv[1]
model = sys.argv[2]
startYear = sys.argv[3]
location = sys.argv[4]
priceFrom = sys.argv[5]
priceTo = sys.argv[6]
endYear = sys.argv[7]
mileageFrom = sys.argv[8]
mileageTo = sys.argv[9]

paramList = ['year',
             'mileage',
             'engine_capacity',
             'fuel_type']

priceList = []
titleList = []
yearList = []
mileageList = []
engineCapacityList = []
fuelTypeList = []
imageList = []

path = 'https://www.otomoto.pl/osobowe/' + brand + '/' + \
       model + '/od-' + \
       startYear + '/' + \
       location + '/?search%5Bfilter_float_price%3Afrom%5D=' + \
       priceFrom + '&search%5Bfilter_float_price%3Ato%5D=' + \
       priceTo + '&search%5Bfilter_float_year%3Ato%5D=' + \
       endYear + '&search%5Bfilter_float_mileage%3Afrom%5D=' + \
       mileageFrom + '&search%5Bfilter_float_mileage%3Ato%5D=' + \
       mileageTo
print(path)


class Base64Encoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, bytes):
            return base64.b64encode(o).decode()
        return json.JSONEncoder.default(self, o)


def get_as_base64(url):
    return base64.b64encode(requests.get(url).content)


def separate_data(car_list, param_list):
    for car in carList:
        price = car.find('span', class_='offer-price__number').text.strip().replace(' ', '').replace('\n', ' ')
        priceList.append(price)
        title = car.find('a', class_='offer-title__link').text.strip()
        titleList.append(title)
        image = car.find('img').get('data-src')
        imageList.append(image)

        for param in paramList:
            current_parameter = car.find('li', {'data-code': param})
            if current_parameter:
                if param == 'year':
                    yearList.append(current_parameter.text.strip())
                elif param == 'mileage':
                    mileageList.append(current_parameter.text.strip())
                elif param == 'engine_capacity':
                    engineCapacityList.append(current_parameter.text.strip())
                else:
                    fuelTypeList.append(current_parameter.text.strip())
            else:
                continue


res = requests.get(path)
res.raise_for_status()
carSoup = bs4.BeautifulSoup(res.text, features='lxml')
pagers = carSoup.find(class_='pager')
page_count = 1

if pagers:
    page_count = int(pagers.select('a')[-2].text)

for i in range(1, page_count + 1):
    res=requests.get(path + '?page' + str(i))
    res.raise_for_status()
    currentPage = bs4.BeautifulSoup(res.text, features='lxml')
    carList = currentPage.select('article.offer-item')

    separate_data(car_list=carList, param_list=paramList)

fileDisplay = [{'Price': price,
                'Title': title,
                'Year': year,
                'Mileage': mileage,
                'Engine_Capacity': engine_capacity,
                'Fuel_Type': fuel_type,
                'Image': get_as_base64(image)} for
               price,
               title,
               year,
               mileage,
               engine_capacity,
               fuel_type,
               image in zip(priceList,
                            titleList,
                            yearList,
                            mileageList,
                            engineCapacityList,
                            fuelTypeList,
                            imageList)]

with open('ListaSamochodow.json', 'w', encoding='utf-8') as file:
    json.dump(fileDisplay, file, ensure_ascii=False, indent=4, cls=Base64Encoder)