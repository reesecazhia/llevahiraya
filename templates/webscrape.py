from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime
import time


def earthquake_today(): 
	url = 'https://monitoring-dashboard.ndrrmc.gov.ph/page/earthquake_reports/'
	page= requests.get(url, verify = False)
	soup= BeautifulSoup(page.text, 'lxml')

	active_earthquakes = soup.find('table', class_= 'table table-bordered')

	headers = []
	for i in active_earthquakes.find_all('th'):
		title = i.text
		headers.append(title)


	mydata = pd.DataFrame(columns = headers)

	for j in active_earthquakes.find_all('tr') [1:]:
		row_data = j.find_all('td')
		row = [i.text for i in row_data]
		length = len(mydata)
		mydata.loc[length] = row
		# mydata['DATE OF OCCURRENCE'] = pd.to_datetime(mydata['DATE OF OCCURRENCE']) #make string data to datetime format
		# mydata['TIME OF OCCURRENCE'] = pd.to_datetime(mydata['TIME OF OCCURRENCE'])
		# data_today = mydata.loc[mydata['DATE OF OCCURRENCE'] == pd.to_datetime('today').normalize()]

	mydata.to_json('earthquake.json', orient="index")
		
	# print (data_today)

def rainfall_today():
	url = 'https://monitoring-dashboard.ndrrmc.gov.ph/page/rainfall_reports/'
	page= requests.get(url, verify = False)
	soup= BeautifulSoup(page.text, 'lxml')

	active_rainfall = soup.find('table', class_= 'table table-bordered')

	rainfall_headers = []
	for c in active_rainfall.find_all('th'):
		title = c.text
		rainfall_headers.append(title)


	rain_data = pd.DataFrame(columns = rainfall_headers)

	for j in active_rainfall.find_all('tr') [1:]:
		row_data = j.find_all('td')
		row = [i.text for i in row_data]
		length = len(rain_data)
		rain_data.loc[length] = row
		# rain_data['DATE'] = pd.to_datetime(rain_data['DATE']) #make string data to datetime format
		# rain_data_today = rain_data.loc[rain_data['DATE'] == pd.to_datetime('today').normalize()] #find data for today's date
		# rain_data_today = rain_data[(rain_data['DATE'] == '2022-05-03')]
	rain_data.to_json('rain.json', orient="index")
	# print (rain_data)


def typhoon_today():
	url = 'https://monitoring-dashboard.ndrrmc.gov.ph/page/weather_reports/'
	page= requests.get(url, verify = False)
	soup= BeautifulSoup(page.text, 'lxml')

	active_typhoon = soup.find('table', class_= 'table table-bordered')

	typhoon_headers = []
	for l in active_typhoon.find_all('th'):
		title = l.text
		typhoon_headers.append(title)


	typ_data = pd.DataFrame(columns = typhoon_headers)

	for j in active_typhoon.find_all('tr') [1:]:
		row_data = j.find_all('td')
		row = [i.text for i in row_data]
		length = len(typ_data)
		typ_data.loc[length] = row
		# typ_data['DATE'] = pd.to_datetime(typ_data['DATE']) #make string data to datetime format
		# typ_data_today = typ_data.loc[typ_data['DATE'] == pd.to_datetime('today').normalize()] #find data for today's date
		# typ_data_today = typ_data[(typ_data['DATE'] == '2022-04-09')]
	typ_data.to_json('typhoon.json', orient="index")
	# print (typ_data)

def flood_today():
	url = 'https://monitoring-dashboard.ndrrmc.gov.ph/page/flood_advisory_reports/'
	page= requests.get(url, verify = False)
	soup= BeautifulSoup(page.text, 'lxml')

	active_flood = soup.find('table', class_= 'table table-bordered')

	flood_headers = []
	for m in active_flood.find_all('th'):
		title = m.text
		flood_headers.append(title)


	fl_data = pd.DataFrame(columns = flood_headers)

	for j in active_flood.find_all('tr') [1:]:
		row_data = j.find_all('td')
		row = [i.text for i in row_data]
		length = len(fl_data)
		fl_data.loc[length] = row
		# fl_data['DATE'] = pd.to_datetime(fl_data['DATE']) #make string data to datetime format
		# fl_data_today = fl_data.loc[fl_data['DATE'] == pd.to_datetime('today').normalize()] #find data for today's date
		# fl_data_today = fl_data[(fl_data['DATE'] == '2022-04-28')]
	fl_data.to_json('flood.json', orient="index")
	# print (fl_data)

def volcano_today(): #TAAL ONLY
	url = 'https://monitoring-dashboard.ndrrmc.gov.ph/page/volcanos_reports'
	page= requests.get(url, verify = False)
	soup= BeautifulSoup(page.text, 'lxml')

	active_volcano = soup.find('table', class_= 'table table-bordered')

	volcano_headers = []
	for b in active_volcano.find_all('th'):
		title = b.text
		volcano_headers.append(title)


	vc_data = pd.DataFrame(columns = volcano_headers)

	for j in active_volcano.find_all('tr') [1:]:
		row_data = j.find_all('td')
		row = [i.text for i in row_data]
		length = len(vc_data)
		vc_data.loc[length] = row
		vc_data['DATE'] = pd.to_datetime(vc_data['DATE']) #make string data to datetime format
		vc_data_today = vc_data.loc[vc_data['DATE'] == pd.to_datetime('today').normalize()] #find data for today's date
		# vc_data_today = vc_data[(vc_data['DATE'] <= '2022-05-01')]
		# vc_data_today['DATE'].dt.strftime('%Y-%m-%d')

	vc_data_today.assign(
		**vc_data_today.select_dtypes(['datetime']).astype(str).to_dict('list')
		).to_json('volcano.json', orient="index", date_format = 'iso')
	print (vc_data_today)

if __name__ == '__main__':
	while True:
		earthquake_today()
		rainfall_today()
		typhoon_today ()
		flood_today()
		volcano_today()
		# time_wait = 60
		# time.sleep(time_wait* 60)

