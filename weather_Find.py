import requests
import time


def by_city():
    city = input("Please enter the city you want to know the weather:")
    print('-----------------------------------------------------------')
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=e10ca2a3ad4b1f2ebb06b0e3b99bb782&units=metric'.format(
        city)
    res = requests.get(url)
    data = res.json()
    show_data(data)


def by_location():
    res = requests.get('https://ipinfo.io')
    data = res.json()

    location = data['loc'].split(',')
    latitude = location[0]
    longitude = location[1]

    print('Weather in your location:')
    print('--------------------------')
    url = 'http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid=e10ca2a3ad4b1f2ebb06b0e3b99bb782&units=metric'.format(
        latitude, longitude)
    res = requests.get(url)
    data = res.json()
    show_data(data)


def show_data(data):
    temp = data['main']['temp']
    wind_speed = data['wind']['speed']
    pressure = data['main']['pressure']
    humidity = data['main']['humidity']
    description = data['weather'][0]['description']
    name = data['name']

    t = time.localtime()
    print("%s" % time.asctime(t))
    print('-----------')
    print('City: {}'.format(name))
    print('-----------')
    print('Temperature: {} Degree Celsius'.format(temp))
    print('-----------')
    print('Wind Speed: {} m/s'.format(wind_speed))
    print('-----------')
    print('Pressure: {}'.format(pressure))
    print('-----------')
    print('Humidity: {}'.format(humidity))
    print('-----------')
    print('Weather: {}'.format(description))


def fivedays():
    city = input("Please enter the city you want to know the weather:")
    print('-----------------------------------------------------------')
    url = (
        'http://api.openweathermap.org/data/2.5/forecast?q={}&appid=e10ca2a3ad4b1f2ebb06b0e3b99bb782&units=metric').format(
        city)
    res = requests.get(url)
    data = res.json()

    description = data['list'][1]['weather'][0]['description']
    description1 = data['list'][2]['weather'][0]['description']
    description2 = data['list'][3]['weather'][0]['description']
    description3 = data['list'][4]['weather'][0]['description']
    description4 = data['list'][4]['weather'][0]['description']
    t = time.localtime()
    print("%s" % time.asctime(t))
    print('Weather of the first day: {}'.format(description))
    print('Weather of the second day:{}'.format(description1))
    print('Weather of the third day:{}'.format(description2))
    print('Weather of the fourth day:{}'.format(description3))
    print('Weather of the fifth day:{}'.format(description4))


def main():
    print('1.Get by weather by city')
    print('2.Get by weather by location')
    print('3.Next five days weather')
    choice = input('Please enter your choice:')

    if choice == '1':
        by_city()
    elif choice == '2':
        by_location()
    elif choice == '3':
        fivedays()
    else:
        print("ERROR!!! PLEASE SELECT AGAIN!!!")


if __name__ == '__main__':
    main()
