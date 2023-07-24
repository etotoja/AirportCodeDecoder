# Importing neccesary Python modules
import json
from requests import get
from datetime import datetime, timedelta

# Setting headers for opening the URL
headers = {
        "accept-encoding": "gzip, br",
        "accept-language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
        "cache-control": "max-age=0",
        "origin": "https://www.flightradar24.com",
        "referer": "https://www.flightradar24.com/",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    }


while True:
    try:
        
        input_apt = input("Enter 3-letter IATA code or 4-letter ICAO code for chosen airport: ")
        apt_selected = input_apt


        url = f"https://www.flightradar24.com/airports/traffic-stats/?airport={apt_selected}"
        response = get(url, headers=headers)
        selected_apt_data = json.loads(response.text)

        apt_name = selected_apt_data['details']['name']
        apt_iata = selected_apt_data['details']['code']['iata']
        apt_icao = selected_apt_data['details']['code']['icao']
        apt_country = selected_apt_data['details']['position']['country']['name']
        apt_city = selected_apt_data['details']['position']['region']['city']
        apt_time = selected_apt_data['details']['timezone']['offsetHours'] 
 
        def calculate_timezone(move):
            # Getting current date and time in UTC
            currenttime = datetime.utcnow() 

            # Calculating time split in other using "hours:minutes"
            hours, minutes = map(int, move.split(':'))

            # Creating timedelta using timesplitting
            delta = timedelta(hours=hours, minutes=minutes)

            # Calculating new time based on local's user time and offset hours
            new_time_and_date = currenttime + delta

            # Returning new time and date in "HH:MM" format, erasing the date, seconds and miliseconds
            return str(new_time_and_date)[11:16]

        # Function call for selected offset
        apt_localtime = calculate_timezone(apt_time)


        apt_timezone = selected_apt_data['details']['timezone']['abbr']

        print(f"{apt_name}, also known byt its IATA code {apt_iata} or ICAO code {apt_icao}, lays in {apt_city}, {apt_country}. Local time is {apt_localtime} {apt_timezone}")
        break
    except TypeError:
        print(f"Selected code: '{apt_selected}' does not exist as IATA or ICAO code!")
        print("Rerunning program...")
        print(" ")
        