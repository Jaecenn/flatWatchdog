import requests
import json

def getTravelTime(byPublic, origin, destination):

    if (byPublic == True):
        request_end = '&mode=transit&transit_mode=train&key='
    else:
        request_end = '&key='

    api_url = 'https://maps.googleapis.com/maps/api/distancematrix/json?'

    key = 'AIzaSyB_XAqno0WJ9EE5idCa0NK-P8LrdQkfaiY'
    origin_tag = 'origins='
    #origin = 'Siemensova 1, Praha'

    destination_tag = '&destinations='
    #destination = 'Kafkova 608/20, Praha 6'

    new_url = api_url + origin_tag + origin + destination_tag + destination + request_end + key
    print(new_url)
    headers = {'User-Agent': 'Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0;  rv:11.0) like Gecko'}

    page = requests.get(new_url, headers)
    page_json = json.loads(page.text)
    print(page_json)
    #print(page_json['origin_addresses'])

    duration = page_json['rows'][0]['elements'][0]['duration']['value']
    return duration
    #print(page.text)
    #url = 'https://maps.googleapis.com/maps/api/distancematrix/json?origins=Vancouver+BC|Seattle&destinations=San+Francisco|Victoria+BC&mode=transit&transit_mode=train&key='
