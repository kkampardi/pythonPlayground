import bs4
import requests


def main():
    # print the header
    print_header()
    # get zipcode from user
    code = input('What zipcode do you want the weather for(26335)? ')

    # get html data from web
    html_data = get_data_from_web(code)

    # parse the html
    get_data_from_html(html_data)

    # display for the forecast


def print_header():
    print("----------------------------")
    print("----------Wheather----------")
    print("----------------------------")
    print()


def get_data_from_web(zipcode):
    url = 'https://www.wunderground.com/weather-forecast/{}'.format(zipcode)
    print("DEBUG: %", url)
    response = requests.get(url)
    #print(response.text[0:250])

    return response.text


def get_data_from_html(html):
    html = bs4.BeautifulSoup(html, 'html.parser')
    location = html.find(id='region-content-header').find('h1')
    print("DEBUG:")
    print(location)


if __name__ == '__main__':
    main()