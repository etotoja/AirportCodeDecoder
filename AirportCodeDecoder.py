from FlightRadar24.api import FlightRadar24API
import requests
import json
from datetime import datetime, timedelta

fr_api = FlightRadar24API()

while True:
    try:
        input_apt = input("Enter 3-letter IATA code or 4-letter ICAO code for chosen airport: ")

        selected_apt = input_apt
        selected_apt_data = fr_api.get_airport(selected_apt)


        apt_name = selected_apt_data['name']
        apt_iata = selected_apt_data['code']['iata']
        apt_icao = selected_apt_data['code']['icao']
        apt_country = selected_apt_data['position']['country']['name']
        apt_city = selected_apt_data['position']['region']['city']

        apt_time = selected_apt_data['timezone']['offsetHours'] 
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


        apt_timezone = selected_apt_data['timezone']['abbrName']

        print(f"{apt_name}, also known byt its IATA code {apt_iata} or ICAO code {apt_icao}, lays in {apt_city}, {apt_country}. Local time is {apt_localtime} ")
        
        break
    except TypeError:
        print(f"Selected code: '{selected_apt}' does not exist as IATA or ICAO code!")
        print("Rerunning program...")
        print(" ")
        