
# No other modules apart from 'socket', 'BeautifulSoup', 'requests' and 'datetime'
# need to be imported as they aren't required to solve the assignment

# Import required module/s
import socket
from bs4 import BeautifulSoup
import requests
import datetime
# Define constants for IP and Port address of Server
# NOTE: DO NOT modify the values of these two constants
HOST = '127.0.0.1'
PORT = 24680
def fetchWebsiteData(url_website):
	"""Fetches rows of tabular data from given URL of a website with data excluding table headers.

	Parameters
	----------
	url_website : str
		URL of a website

	Returns
	-------
	bs4.element.ResultSet
		All rows of Tabular data fetched from a website excluding the table headers
	"""
	
	web_page_data = ''

	##############	ADD YOUR CODE HERE	##############
	
	req = requests.get(url_website)
	soup = BeautifulSoup(req.text , 'xml')

	for i in soup.find_all('tbody'):
		web_page_data = i.find_all('tr')



	##################################################
	return web_page_data
def fetchVaccineDoses(web_page_data):
	"""Fetch the Vaccine Doses available from the Web-page data and provide Options to select the respective Dose.

	Parameters
	----------
	web_page_data : bs4.element.ResultSet
		All rows of Tabular data fetched from a website excluding the table headers

	Returns
	-------
	dict
		Dictionary with the Doses available and Options to select, with Key as 'Option' and Value as 'Command'
	
	Example
	-------
	>>> url_website = "https://www.mooc.e-yantra.org/task-spec/fetch-mock-covidpage"
	>>> web_page_data = fetchWebsiteData(url_website)
	>>> print(fetchVaccineDoses(web_page_data))
	{'1': 'Dose 1', '2': 'Dose 2'}
	"""

	vaccine_doses_dict = {}

	##############	ADD YOUR CODE HERE	##############
	doses = []
	for td in web_page_data :
		doses.append(td.find_all("td", {"class": "dose_num"})[0].text)
	doses = sorted(list(set(doses)))
	vaccine_doses_dict = {str(i+1): "Dose {}".format(doses[i]) for i in range(len(doses))}
	
	##################################################
	return vaccine_doses_dict
def fetchAgeGroup(web_page_data, dose):
	"""Fetch the Age Groups for whom Vaccination is available from the Web-page data for a given Dose
	and provide Options to select the respective Age Group.

	Parameters
	----------
	web_page_data : bs4.element.ResultSet
		All rows of Tabular data fetched from a website excluding the table headers
	dose : str
		Dose available for Vaccination and its availability for the Age Groups

	Returns
	-------
	dict
		Dictionary with the Age Groups (for whom Vaccination is available for a given Dose) and Options to select,
		with Key as 'Option' and Value as 'Command'
	
	Example
	-------
	>>> url_website = "https://www.mooc.e-yantra.org/task-spec/fetch-mock-covidpage"
	>>> web_page_data = fetchWebsiteData(url_website)
	>>> print(fetchAgeGroup(web_page_data, '1'))
	{'1': '18+', '2': '45+'}
	>>> print(fetchAgeGroup(web_page_data, '2'))
	{'1': '18+', '2': '45+'}
	"""

	age_group_dict = {}

	##############	ADD YOUR CODE HERE	##############
	age_group = []
	for td in web_page_data:
		if (td.find_all("td", {"class": "dose_num"})[0].text == dose):
			age_group.append(td.find_all("td", {"class": "age" })[0].text)
	age_group = sorted(list(set(age_group)))
	age_group_dict = {str(i+1): "{}".format(age_group[i]) for i in range(len(age_group))}
	
	##################################################
	return age_group_dict
def fetchStates(web_page_data, age_group, dose):
	"""Fetch the States where Vaccination is available from the Web-page data for a given Dose and Age Group
	and provide Options to select the respective State.

	Parameters
	----------
	web_page_data : bs4.element.ResultSet
		All rows of Tabular data fetched from a website excluding the table headers
	age_group : str
		Age Group available for Vaccination and its availability in the States
	dose : str
		Dose available for Vaccination and its availability for the Age Groups

	Returns
	-------
	dict
		Dictionary with the States (where the Vaccination is available for a given Dose, Age Group) and Options to select,
		with Key as 'Option' and Value as 'Command'
	
	Example
	-------
	>>> url_website = "https://www.mooc.e-yantra.org/task-spec/fetch-mock-covidpage"
	>>> web_page_data = fetchWebsiteData(url_website)
	>>> print(fetchStates(web_page_data, '18+', '1'))
	{
		'1': 'Andhra Pradesh', '2': 'Arunachal Pradesh', '3': 'Bihar', '4': 'Chandigarh', '5': 'Delhi', '6': 'Goa',
		'7': 'Gujarat', '8': 'Harayana', '9': 'Himachal Pradesh', '10': 'Jammu and Kashmir', '11': 'Kerala', '12': 'Telangana'
	}
	"""

	states_dict = {}

	##############	ADD YOUR CODE HERE	##############
	states = []
	for td in web_page_data:
		if (td.find_all("td", {"class": "dose_num"})[0].text == dose and td.find_all("td", {"class": "age"})[0].text == age_group):
			states.append(td.find_all("td", {"class": "state_name" })[0].text)
	states = sorted(list(set(states)))
	states_dict = {str(i+1): "{}".format(states[i]) for i in range(len(states))}
	
	
	##################################################
	return states_dict
def fetchDistricts(web_page_data, state, age_group, dose):
	"""Fetch the District where Vaccination is available from the Web-page data for a given State, Dose and Age Group
	and provide Options to select the respective District.

	Parameters
	----------
	web_page_data : bs4.element.ResultSet
		All rows of Tabular data fetched from a website excluding the table headers
	state : str
		State where Vaccination is available for a given Dose and Age Group
	age_group : str
		Age Group available for Vaccination and its availability in the States
	dose : str
		Dose available for Vaccination and its availability for the Age Groups

	Returns
	-------
	dict
		Dictionary with the Districts (where the Vaccination is available for a given State, Dose, Age Group) and Options to select,
		with Key as 'Option' and Value as 'Command'
	
	Example
	-------
	>>> url_website = "https://www.mooc.e-yantra.org/task-spec/fetch-mock-covidpage"
	>>> web_page_data = fetchWebsiteData(url_website)
	>>> print(fetchDistricts(web_page_data, 'Ladakh', '18+', '2'))
	{
		'1': 'Kargil', '2': 'Leh'
	}
	"""

	districts_dict = {}

	##############	ADD YOUR CODE HERE	##############
	districts = []
	for td in web_page_data:
		if (td.find_all("td", {"class": "dose_num"})[0].text == dose and td.find_all("td", {"class": "age"})[0].text == age_group and td.find_all("td", {"class": "state_name"})[0].text == state):
			districts.append(td.find_all("td", {"class": "district_name" })[0].text)
	districts = sorted(list(set(districts)))
	districts_dict = {str(i+1): "{}".format(districts[i]) for i in range(len(districts))}
	
	##################################################
	return districts_dict
def fetchHospitalVaccineNames(web_page_data, district, state, age_group, dose):
	"""Fetch the Hospital and the Vaccine Names from the Web-page data available for a given District, State, Dose and Age Group
	and provide Options to select the respective Hospital and Vaccine Name.

	Parameters
	----------
	web_page_data : bs4.element.ResultSet
		All rows of Tabular data fetched from a website excluding the table headers
	district : str
		District where Vaccination is available for a given State, Dose and Age Group
	state : str
		State where Vaccination is available for a given Dose and Age Group
	age_group : str
		Age Group available for Vaccination and its availability in the States
	dose : str
		Dose available for Vaccination and its availability for the Age Groups

	Returns
	-------
	dict
		Dictionary with the Hosptial and Vaccine Names (where the Vaccination is available for a given District, State, Dose, Age Group)
		and Options to select, with Key as 'Option' and Value as another dictionary having Key as 'Hospital Name' and Value as 'Vaccine Name'
	
	Example
	-------
	>>> url_website = "https://www.mooc.e-yantra.org/task-spec/fetch-mock-covidpage"
	>>> web_page_data = fetchWebsiteData(url_website)
	>>> print(fetchHospitalVaccineNames(web_page_data, 'Kargil', 'Ladakh', '18+', '2'))
	{
		'1': {
				'MedStar Hospital Center': 'Covaxin'
			}
	}
	>>> print(fetchHospitalVaccineNames(web_page_data, 'South Goa', 'Goa', '45+', '2'))
	{
		'1': {
				'Eden Clinic': 'Covishield'
			}
	}
	"""
	
	hospital_vaccine_names_dict = {}

	##############	ADD YOUR CODE HERE	##############
	hospitals = []
	vaccine = []
	for td in web_page_data:
		if (td.find_all("td", {"class": "dose_num"})[0].text == dose and td.find_all("td", {"class": "age"})[0].text == age_group and td.find_all("td", {"class": "state_name"})[0].text == state and td.find_all("td", {"class": "district_name"})[0].text == district):
			hospitals.append(td.find_all("td", {"class": "hospital_name" })[0].text)
			vaccine.append(td.find_all("td", {"class": "vaccine_name" })[0].text)
	hospitals = sorted(list(set(hospitals)))

	hospital_vaccine_names_dict = {str(i+1): {hospitals[i]: "{}".format(vaccine[i])} for i in range(len(hospitals))}
	
	
	##################################################
	return hospital_vaccine_names_dict
def fetchVaccineSlots(web_page_data, hospital_name, district, state, age_group, dose):
	"""Fetch the Dates and Slots available on those dates from the Web-page data available for a given Hospital Name, District, State, Dose and Age Group
	and provide Options to select the respective Date and available Slots.

	Parameters
	----------
	web_page_data : bs4.element.ResultSet
		All rows of Tabular data fetched from a website excluding the table headers
	hospital_name : str
		Name of Hospital where Vaccination is available for given District, State, Dose and Age Group
	district : str
		District where Vaccination is available for a given State, Dose and Age Group
	state : str
		State where Vaccination is available for a given Dose and Age Group
	age_group : str
		Age Group available for Vaccination and its availability in the States
	dose : str
		Dose available for Vaccination and its availability for the Age Groups

	Returns
	-------
	dict
		Dictionary with the Dates and Slots available on those dates (where the Vaccination is available for a given Hospital Name,
		District, State, Dose, Age Group) and Options to select, with Key as 'Option' and Value as another dictionary having
		Key as 'Date' and Value as 'Available Slots'
	
	Example
	-------
	>>> url_website = "https://www.mooc.e-yantra.org/task-spec/fetch-mock-covidpage"
	>>> web_page_data = fetchWebsiteData(url_website)
	>>> print(fetchVaccineSlots(web_page_data, 'MedStar Hospital Center', 'Kargil', 'Ladakh', '18+', '2'))
	{
		'1': {'May 15': '0'}, '2': {'May 16': '81'}, '3': {'May 17': '109'}, '4': {'May 18': '78'},
		'5': {'May 19': '89'}, '6': {'May 20': '57'}, '7': {'May 21': '77'}
	}
	>>> print(fetchVaccineSlots(web_page_data, 'Eden Clinic', 'South Goa', 'Goa', '45+', '2'))
	{
		'1': {'May 15': '0'}, '2': {'May 16': '137'}, '3': {'May 17': '50'}, '4': {'May 18': '78'},
		'5': {'May 19': '145'}, '6': {'May 20': '64'}, '7': {'May 21': '57'}
	}
	"""

	vaccine_slots = {}

	##############	ADD YOUR CODE HERE	##############
	Slots = []

	for td in web_page_data:
		for j in range(15,22):
			if (td.find_all("td", {"class": "dose_num"})[0].text == dose and td.find_all("td", {"class": "hospital_name"})[0].text == hospital_name and td.find_all("td", {"class": "age"})[0].text == age_group and td.find_all("td", {"class": "state_name"})[0].text == state and td.find_all("td", {"class": "district_name"})[0].text == district):
				Slots.append(td.find_all("td", {"class": "may_"+str(j) })[0].text)

	vaccine_slots = {str(i+1): {"May "+str(i+15): "{}".format(Slots[i])} for i in range(len(Slots))}
	##################################################

	return vaccine_slots


def openConnection():
	"""Opens a socket connection on the HOST with the PORT address.

	Returns
	-------
	socket
		Object of socket class for the Client connected to Server and communicate further with it
	tuple
		IP and Port address of the Client connected to Server
	"""

	client_socket = None
	client_addr = None

	##############	ADD YOUR CODE HERE	##############
	with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as soc:
		soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		soc.bind((HOST,PORT))
		soc.listen()
		client_socket , client_addr = soc.accept()
		print("Client is connected at:  ('{}', {})".format(HOST,PORT))

	##################################################
	
	return client_socket, client_addr
def startCommunication(client_conn, client_addr, web_page_data):
	"""Starts the communication channel with the connected Client for scheduling an Appointment for Vaccination.

	Parameters
	----------
	client_conn : socket
		Object of socket class for the Client connected to Server and communicate further with it
	client_addr : tuple
		IP and Port address of the Client connected to Server
	web_page_data : bs4.element.ResultSet
		All rows of Tabular data fetched from a website excluding the table headers
	"""

	##############	ADD YOUR CODE HERE	##############
	welcome = "============================\n# Welcome to CoWIN ChatBot #\n============================\n\nSchedule an Appointment for Vaccination:\n"
	client_conn.send(welcome.encode("utf-8"))
	# if Flag is 0 : Successfully got the Value
	# 			 1 : get back to last function 
	#			 2 : close the connection		
	Flag = 0
	func_no = 0

	while func_no < 6:

		if func_no == 0:
			selected_dose, Flag = doses(client_conn, web_page_data)
			if Flag == 0 : 
				func_no = func_no+1
				continue
			elif Flag == 1:
				func_no = 0
				continue
			elif Flag == 2:
				break

		if func_no == 1:
			selected_age_group, Flag = age_group(client_conn, web_page_data,selected_dose)
			if Flag == 0 : 
				func_no = func_no+1
				continue
			elif Flag == 1:
				func_no = func_no - 1
				continue
			elif Flag == 2:
				break

		if func_no == 2:
			selected_state, Flag = states(client_conn, web_page_data,selected_dose,selected_age_group)
			if Flag == 0 : 
				func_no = func_no+1
				continue
			elif Flag == 1:
				func_no = func_no - 1
				continue
			elif Flag == 2:
				break

		if func_no == 3:
			selected_district, Flag = district(client_conn, web_page_data,selected_dose,selected_age_group,selected_state)
			if Flag == 0 : 
				func_no = func_no+1
				continue
			elif Flag == 1:
				func_no = func_no - 1
				continue
			elif Flag == 2:
				break

		if func_no == 4:
			selected_vaccine_centre, Flag = vaccine_centre(client_conn, web_page_data,selected_dose,selected_age_group,selected_state,selected_district)
			if Flag == 0 : 
				func_no = func_no+1
				continue
			elif Flag == 1:
				func_no = func_no - 1
				continue
			elif Flag == 2:
				break

		if func_no == 5:
			selected_slot , selected_slots_available_vaccines, Flag = slots(client_conn, web_page_data,selected_dose,selected_age_group,selected_state,selected_district,selected_vaccine_centre)
			if Flag == 0 : 
				func_no = func_no+1
				continue
			elif Flag == 1:
				func_no = func_no - 1
				continue
			elif Flag == 2:
				break
				

	client_conn.send("\n<<< See ya! Visit again :)".encode("utf-8"))
	stopCommunication(client_conn)

	##################################################
def stopCommunication(client_conn):
	"""Stops or Closes the communication channel of the Client with a message.

	Parameters
	----------
	client_conn : socket
		Object of socket class for the Client connected to Server and communicate further with it
	"""

	##############	ADD YOUR CODE HERE	##############
	client_conn.close()
	

	##################################################


################# ADD UTILITY FUNCTIONS HERE #################
## You can define any utility functions for your code.      ##
## Please add proper comments to ensure that your code is   ##
## readable and easy to understand.                         ##
##############################################################

def available_vaccines(slots, input_string ):
	Flag,selected_slots = input_check(client_conn,slots , input_string)
	selected_date = 0
	if Flag == 0:
		
		selected_slots = slots[selected_slots]
		for key,value in selected_slots.items():
			selected_date = key
			selected_slots = value

		print("Vaccination Date selected: " + selected_date)
		print("Available Slots on that date: " + selected_slots)
		client_conn.send("\n<<< Selected Vaccination Appointment Date: {}".format(selected_date).encode("utf-8"))
		client_conn.send("\n<<< Available Slots on the selected Date: {}".format(selected_slots).encode("utf-8"))
	return Flag, selected_date,selected_slots
def get_date(client_conn,selected_dose,input_string_1):
	error = 0
	while True:
		client_conn.send(input_string_1.encode("utf-8"))
		date = client_conn.recv(1024).decode("utf-8")
		if (date == 'q') or (date == 'Q') :
			print("Client wants to quit!")
			print("Saying Bye to client and closing the connection!")
			return selected_dose,2
		if (date == 'b') or (date == 'B'):
			return selected_dose,1
		if (date.isalpha() or '/' not in date):
			error = error+1
			if error < 3:
				client_conn.send("<<< Invalid input provided {} time(s)! Try again.".format(error).encode("utf-8"))
				print("Invalid input detected {} time(s)!".format(error))
				continue
			else:
				client_conn.send("<<< Invalid input provided {} time(s)! Try again.".format(error).encode("utf-8"))
				print("Invalid input detected {} time(s)!".format(error))
				return selected_dose,2
		else:
			date_list = date.split('/')
			try :
				date = datetime.date(int(date_list[2]),int(date_list[1]),int(date_list[0]))	
			except:
				client_conn.send("\n<<< Invalid Date provided of First Vaccination Dose: {}".format(date).encode("utf-8"))
				
			today = datetime.date.today()
			if date>today:
				client_conn.send("\n<<< Invalid Date provided of First Vaccination Dose: {}/{}/{}".format(date.day,date.month,date.year).encode("utf-8"))
				continue
			else:
				client_conn.send("\n<<< Date of First Vaccination Dose provided: {}/{}/{}".format(date.day,date.month,date.year).encode("utf-8"))

				no_of_weeks = ((today - date).days//7)
				client_conn.send("\n<<< Number of weeks from today: {}".format(str(no_of_weeks)).encode("utf-8"))
				
				if no_of_weeks < 4:
					client_conn.send("\n<<< You are not eligible right now for 2nd Vaccination Dose! Try after {} weeks.".format(str(4-no_of_weeks)).encode("utf-8"))
					return (selected_dose,2)
				elif no_of_weeks > 8 :
					client_conn.send("\n<<< You have been late in scheduling your 2nd Vaccination Dose by {} weeks.".format(str(no_of_weeks - 8)).encode("utf-8"))
					
				else: 
					client_conn.send("\n<<< You are eligible for 2nd Vaccination Dose and are in the right time-frame to take it.".encode("utf-8"))
			break

	
	return selected_dose,0
def input_check(client_conn,valids , input_string):
	error = 0

	while True:
		if error == 3:
			input_Flag = 2
			print("Notifying the client and closing the connection!")
			break
		client_conn.send(input_string.encode("utf-8"))
		input_recieved = client_conn.recv(1024).decode("utf-8")
		if  input_recieved == 'q' or input_recieved == 'Q':
			input_Flag = 2
			print("Client wants to quit!")
			print("Saying Bye to client and closing the connection!")
			break
		elif input_recieved == 'b' or input_recieved == 'B':
			input_Flag = 1
			break
		elif (input_recieved.isalpha() or (not input_recieved.isalnum()) or (not input_recieved.isdigit())):
			error = error+1
			client_conn.send("\n<<< Invalid input provided {} time(s)! Try again.".format(error).encode("utf-8"))
			print("Invalid input detected {} time(s)!".format(error))
		elif int(input_recieved) > len(valids) or int(input_recieved) < 1:
			error = error+1
			client_conn.send("\n<<< Invalid input provided {} time(s)! Try again.".format(error).encode("utf-8"))
			print("Invalid input detected {} time(s)!".format(error))
		else:
			input_Flag = 0
			break
	return input_Flag, input_recieved
def doses(client_conn , web_page_data):
	dose = fetchVaccineDoses(web_page_data)
	error = 0
	input_string = "\n>>> Select the Dose of Vaccination: \n{}\n".format(dose)
	Flag ,selected_dose  = input_check(client_conn,dose,input_string)
	if Flag == 0:
		print("Dose selected: " + selected_dose)
		client_conn.send("\n<<< Dose selected: {}".format(selected_dose).encode("utf-8"))
		if selected_dose == '2':
			input_string_1 = "\n>>> Provide the date of First Vaccination Dose (DD/MM/YYYY), for e.g. 12/05/2021"
			return get_date(client_conn,selected_dose,input_string_1)
	return selected_dose,Flag
def age_group(client_conn,web_page_data,selected_dose):
	
	age_group = fetchAgeGroup(web_page_data,selected_dose)
	input_string = "\n>>> Select the Age Group:\n{}\n".format(age_group)
	Flag , selected_age_group = input_check(client_conn,age_group , input_string)
	if Flag == 0:
		selected_age_group = age_group[selected_age_group]
		client_conn.send("\n<<< Selected Age Group: {}".format(selected_age_group).encode("utf-8"))
		print("Age Group selected: {}".format(selected_age_group))
	return (selected_age_group,Flag)
def states(client_conn,web_page_data,selected_dose, selected_age_group):
	state = fetchStates(web_page_data,selected_age_group,selected_dose)
	input_string = "\n>>> Select the State:\n{}\n".format(state)
	Flag,selected_state = input_check(client_conn,state , input_string)
	if Flag == 0:
		selected_state = state[selected_state]
		client_conn.send("\n<<< Selected State: {}".format(selected_state).encode("utf-8"))
		print("State selected: " + selected_state)
	return (selected_state,Flag)
def district(client_conn,web_page_data,selected_dose, selected_age_group,selected_state):
	district = fetchDistricts(web_page_data,selected_state,selected_age_group,selected_dose)
	input_string = "\n>>> Select the District:\n{}\n".format(district)
	Flag,selected_district = input_check(client_conn,district,input_string)
	if Flag == 0:
		selected_district = district[selected_district]
		client_conn.send("\n<<< Selected District: {}".format(selected_district).encode("utf-8"))
		print("District selected: " + selected_district)
	return (selected_district,Flag)
def vaccine_centre(client_conn,web_page_data,selected_dose,selected_age_group,selected_state,selected_district):
	vaccine_centre = fetchHospitalVaccineNames(web_page_data,selected_district,selected_state,selected_age_group,selected_dose)
	input_string = "\n>>> Select the Vaccination Center Name:\n{}\n".format(vaccine_centre)
	Flag,selected_vaccine_centre = input_check(client_conn,vaccine_centre,input_string)
	if Flag == 0:
		selected_vaccine_centre = vaccine_centre[selected_vaccine_centre]
		for key, values in selected_vaccine_centre.items():
			selected_vaccine_centre = key

		client_conn.send("\n<<< Selected Vaccination Center: {}".format(selected_vaccine_centre).encode("utf-8"))
		print("Hospital selected: {}".format(selected_vaccine_centre))
	return (selected_vaccine_centre,Flag)
def slots(client_conn,web_page_data,selected_dose,selected_age_group,selected_state,selected_district,selected_vaccine_centre):
	slots = fetchVaccineSlots(web_page_data,selected_vaccine_centre,selected_district,selected_state,selected_age_group,selected_dose)
	input_string = "\n>>> Select one of the available slots to schedule the Appointment:\n{}\n".format(slots)
	Flag ,selected_date, selected_slots = available_vaccines(slots, input_string)
	
	if Flag == 0:
		while not (selected_slots > '0'):
				client_conn.send("\n<<< Selected Appointment Date has no available slots, select another date!\n".encode('utf-8'))
				Flag, selected_date, selected_slots = available_vaccines(slots, input_string)
		client_conn.send("\n<<< Your appointment is scheduled. Make sure to carry ID Proof while you visit Vaccination Center!".encode("utf-8"))
	return (selected_date,selected_slots,Flag)



##############################################################


if __name__ == '__main__':
	"""Main function, code begins here
	"""
	url_website = "https://www.mooc.e-yantra.org/task-spec/fetch-mock-covidpage"
	web_page_data = fetchWebsiteData(url_website)
	client_conn, client_addr = openConnection()

	startCommunication(client_conn, client_addr, web_page_data)
