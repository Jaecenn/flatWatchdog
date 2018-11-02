import watchdog_scraper as scraper
import google_directions as maps
import time
from locationsList import locationsList

locList = locationsList()

locList.addNewLocation('Siemensova 1, Praha', 8)
locList.addNewLocation('Husinecká, Praha 3',2)
locList.addNewLocation('Sovova 503/3, Praha 8', 2)


important_locations = [['Siemensova 1, Praha', 70],
                       ['Husinecká, Praha 3',15],
                       ['Sovova 503/3, Praha 8', 15]]

# testAddr = ['Praha 2', 'Mládí, Praha 5 - Stodůlky', 'Augustinova, Praha 4 - Chodov', 'Koněvova, Praha 3 - Žižkov', 'Sinkulova, Praha 4 - Podolí', 'Bulovka, Praha 8 - Libeň', 'Libeňský ostrov, Praha 8 - Libeň', 'Bulovka, Praha 8 - Libeň', 'Káranská, Praha 10 - Malešice', 'Stejskalova, Praha 8 - Libeň', 'Dlážděná, Praha 1 - Nové Město', 'Praha 7 - Troja', 'Lihovarská, Praha 9 - Libeň', 'Fryčovická, Praha 9 - Letňany', 'Na Břehu, Praha - Vysočany', 'náměstí Jiřího z Lobkovic, Praha 3 - Vinohrady', 'Petrské náměstí, Praha 1 - Nové Město', 'Jana Masaryka, Praha 2 - Vinohrady', 'Pražského, Praha 5 - Hlubočepy', 'ulice Hanusova, Praha - Michle', 'ulice Prosluněná, Praha 5 - Hlubočepy']


# resultAddr = ('Dlážděná, Praha 1 - Nové Město', 'Petrské náměstí, Praha 1 - Nové Město', 'Mládí, Praha 5 - Stodůlky', 'Koněvova, Praha 3 - Žižkov', 'Sinkulova, Praha 4 - Podolí', 'Praha 2', 'Lihovarská, Praha 9 - Libeň', 'Pražského, Praha 5 - Hlubočepy', 'Na Břehu, Praha - Vysočany', 'Libeňský ostrov, Praha 8 - Libeň', 'Stejskalova, Praha 8 - Libeň', 'Jana Masaryka, Praha 2 - Vinohrady', 'náměstí Jiřího z Lobkovic, Praha 3 - Vinohrady', 'ulice Hanusova, Praha - Michle', 'Káranská, Praha 10 - Malešice', 'Bulovka, Praha 8 - Libeň', 'Bulovka, Praha 8 - Libeň', 'Augustinova, Praha 4 - Chodov', 'Praha 7 - Troja', 'Fryčovická, Praha 9 - Letňany')
# resultScore = (28.134444444444444, 31.76, 31.86111111111111, 39.07888888888889, 40.35111111111111, 42.138888888888886, 44.766666666666666, 45.56111111111111, 46.5, 47.20444444444445, 47.233333333333334, 49.27, 50.730000000000004, 55.12555555555556, 57.02111111111111, 59.48222222222223, 63.68222222222222, 65.66777777777777, 67.35666666666667, 69.30444444444444)

page_source = scraper.getHTML('https://www.sreality.cz/hledani/prodej/byty/praha?velikost=2%2B1,3%2Bkk,3%2B1&bez-aukce=1', True, 'page-layout')
flatList = scraper.getItemsList(page_source, 'span', 'locality ng-binding')


scoreboard = []
#maps.getTravelTime(True, flatList[0], important_locations[0])

timeTravel_max = 4500

for flatId in range(0, len(flatList) - 1):
    scoreboard.append(0)
    #scoreboard[flatId][0] = flatList[flatId]
#for flat in range(0,10):
    for loc in important_locations:
        time.sleep(1)
        coefficient = loc[1] / timeTravel_max
        # value = maps.getTravelTime(True, flatList[flatId], loc[0])
        value = 40
        if (value > timeTravel_max):
            score = 0
        else:
            score = value * coefficient
        print(score)
        scoreboard[flatId] = scoreboard[flatId] + score
        #scoreboard[flatId][1] = scoreboard[flatId][1] + score
#maps.getTravelTime(False, flatList[0], important_locations[0])
list1, list2 = zip(*sorted(zip(scoreboard, flatList)))
print(list1)
print(list2)

