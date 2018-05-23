import bs4
import requests
import collections


WeatherReport = collections.namedtuple('WeatherReport', 'cond, temp, scale, loc')

def main():
    # print the header
    print_header()
    # get zipcode from user
    code = input('What zipcode do you want the weather for(26335)? ')

    # get html data from web
    html_data = get_data_from_web(code)

    # parse the html
    report = get_data_from_html(html_data)
    print('The temp in {} is {} {} and {}'.format(
        report.loc,
        report.temp,
        report.scale,
        report.cond
    ))

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
    soup = bs4.BeautifulSoup(html, 'html.parser')
    location = soup.find(class_='region-content-header').find('h1').get_text()
    condition = soup.find(class_='condition-icon').get_text()
    temp = soup.find(class_='wu-unit-temperature').find(class_='wu-value').get_text()
    scale = soup.find(class_='wu-unit-temperature').find(class_='wu-label').get_text()

    #location = cleanup_text(location)
    location = find_city_and_state_from_location(location)
    condition = cleanup_text(condition)
    temp = cleanup_text(temp)
    scale = cleanup_text(scale)

    report = WeatherReport(cond=condition, temp=temp, scale=scale, loc=location)
    return report


def cleanup_text(text):
    """ cleans up text from white spaces"""

    if not text:
        return text

    text = text.strip()

    return text


def find_city_and_state_from_location(loc: str):
    parts = loc.split('\n')
    return parts[0].strip()


if __name__ == '__main__':
    main()