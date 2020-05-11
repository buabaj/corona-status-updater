import requests
import json
from win10toast import ToastNotifier
from time import sleep

country = input('What country do you want notifications on: ')

base_api = 'https://corona.lmao.ninja/v2/countries/'
complete_api = base_api + country
apiData_get = requests.get(complete_api)

apiData_toJSON = apiData_get.json()
text = f'Confirmed Cases : {apiData_toJSON["cases"]} \nTotal Deaths : {apiData_toJSON["deaths"]} \nNumber of Recoveries : {apiData_toJSON["recovered"]} \nCases Today : {apiData_toJSON["todayCases"]} \nDeaths Today : {apiData_toJSON["todayDeaths"]} \nActive cases : {apiData_toJSON["active"]} \nCritical Cases : {apiData_toJSON["critical"]} '
		
while True:
	toast = ToastNotifier()
	toast.show_toast(country+" Covid-19 Status Notification",text ,duration=30, icon_path= "virus.ico")
	sleep(3600)