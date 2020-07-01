
import datetime
import time
import json
import requests

data_link = "http://tfe-opendata.com/api/v1/live_bus_times/36298678"

while True:
    now = datetime.datetime.now()
    time_now = now.strftime("%H:%M")
    date = now.strftime("%d/%m/%Y")

    response = requests.get(data_link)
    bus_data = json.loads(response.text)
    #print(bus_data)  uncomment to see the json data

    if not bus_data:
        departures = []
    else:
        bus_dict = bus_data[0]
        dict_len = len(bus_dict['departures'])
        #print(dict_len) uncomment to see number of entries in json data

        non_terms = []
        for n in range(dict_len):
            if bus_dict['departures'][n]['isTerminatingHere'] != True:
                non_terms.append(n)
            else:
                non_terms = non_terms

        #print(non_terms) uncomment to see a check that we're ony pulling through non-terminating buses

        departures = []

        for x in non_terms:
            route = bus_dict['departures'][x]['routeName']
            dest = bus_dict['departures'][x]['destination']
            dep = bus_dict['departures'][x]['departureTimeUnix']
            dep = datetime.datetime.utcfromtimestamp(dep)
            delta1 = dep - now
            leaves = str(int(round(((delta1.seconds)/60 - 60),0)))
            data = [route,dest,leaves]
            # print(data) uncomment if you want to see the data for each departure
            departures.append(data)

        # print(departures) uncomment if you want to see the list of lists combined above

        if not non_terms:
            message = "There are no more buses today."
        elif len(departures[1]) == 0:
            message = "The next bus, the no. " + departures[0][0] + " to " + departures[0][1] + ", is in " + departures[0][2] + " minutes./nThere are no further departures."
        else:
            message = "The next bus, the no. " + departures[0][0] + " to " + departures[0][1] + ", is in " + departures[0][2] + " minutes.\nThe bus after that, the no. " + departures[1][0] + " to " + departures[1][1] + ", is in " + departures[1][2] + " minutes."
    print("The time is " + time_now + " on " + date + ".")
    print(message)
    time.sleep(10)
