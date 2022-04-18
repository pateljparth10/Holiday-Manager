import datetime
from datetime import timedelta
from datetime import datetime
import json
from bs4 import BeautifulSoup as soup
from numpy import datetime_as_string
import requests
from dataclasses import dataclass
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager


class Holiday:
      
    def __init__(self,name, date):
        #Your Code Here 
        self._name = name
        self._date = date       
    
    def __str__ (self):
        # String output
        return (f"{self._name} ({self._date})")
        # Holiday output when printed.
class HolidayList:
    def __init__(self):
       self.innerHolidays = {}
    def __str__(self):
        return self.innerHolidays
   
    def addHoliday(self,holidayObj):
        # Make sure holidayObj is an Holiday Object by checking the type
        # Use innerHolidays.append(holidayObj) to add holiday
        self.innerHolidays[holidayObj._date] = holidayObj._name
        print("Sucess: ")
        print(f"{holidayObj._name} ({holidayObj._date}) has been added to the holiday list.")
        # print to the user that you added a holiday
    def findHoliday(self,HolidayName):
        # Find Holiday in innerHolidays
        for i in range(len(self.innerHolidays)):
            if list(self.innerHolidays.values())[i] == HolidayName:
                return HolidayName
    
    def findDate(self,Date):
        # Find Holiday in innerHolidays
        for i in range(len(self.innerHolidays)):
            if list(self.innerHolidays.keys())[i] == Date:
                return Date

    def removeDate(self,date, holiday):
        legnth = len(self.innerHolidays)
        # Find Holiday in innerHolidays by searching the name and date combination.
        for i in range(legnth):
            if list(self.innerHolidays)[i] == date:
                position = date
        del self.innerHolidays[position]
        print(f"You have removed the Holiday and date:{holiday}({date})")     
        # remove the Holiday from innerHolidays
        # inform user you deleted the holiday
    def read_json(self,filelocation):
        # Read in things from json file location
        f= open(filelocation)
        data = json.load(f)
        for i in range(len(data["holidays"])):
            name = data["holidays"][i]["name"]
            date = data["holidays"][i]["date"]
            holiday = Holiday(name,date)
            global add_test
            add_test.addHoliday(holiday)
        # Use addHoliday function to add holidays to inner list.
    def numHolidays(self):
        # Return the total number of holidays in innerHolidays
        return len(self.innerHolidays)
    def save_to_json(self, filelocation):
        # Write out json file to selected file.
        with open(filelocation, "w") as f:
            f.write(str(self.innerHolidays))
            print("Success:")
            print("Your changes have been saved.")
    def scrapeHolidays(self):
        # Scrape Holidays from https://www.timeanddate.com/holidays/us/ 
        url_2022 = "https://www.timeanddate.com/holidays/us/?hol=1"
        executable_path = {'executable_path': ChromeDriverManager().install()}
        browser = Browser('chrome', **executable_path, headless=True)
        browser.visit(url_2022)
        html = browser.html
        html_soup = soup(html, "html.parser")
        TextDisplayObject = html_soup.find_all("tr",{"class": "showrow"},"th")
        for tags in TextDisplayObject:
            website_content = tags.get_text("|").split("|")
            date = "2022 " + website_content[0] 
            date_time_date = datetime.strptime(date, "%Y %b %d")
            date_string = datetime.strftime(date_time_date, "%Y-%m-%d")
            website_holiday = Holiday(website_content[2], date_string)
            global add_test
            add_test.addHoliday(website_holiday)
        
        url_2021 = "https://www.timeanddate.com/holidays/us/2021?hol=1"
        executable_path = {'executable_path': ChromeDriverManager().install()}
        browser = Browser('chrome', **executable_path, headless=True)
        browser.visit(url_2021)
        html = browser.html
        html_soup = soup(html, "html.parser")
        TextDisplayObject = html_soup.find_all("tr",{"class": "showrow"},"th")
        for tags in TextDisplayObject:
            website_content = tags.get_text("|").split("|")
            date = "2021 " + website_content[0] 
            date_time_date = datetime.strptime(date, "%Y %b %d")
            date_string = datetime.strftime(date_time_date, "%Y-%m-%d")
            website_holiday = Holiday(website_content[2], date_string)
            add_test.addHoliday(website_holiday)
        url_2020 = "https://www.timeanddate.com/holidays/us/2020?hol=1"
        executable_path = {'executable_path': ChromeDriverManager().install()}
        browser = Browser('chrome', **executable_path, headless=True)
        browser.visit(url_2020)
        html = browser.html
        html_soup = soup(html, "html.parser")
        TextDisplayObject = html_soup.find_all("tr",{"class": "showrow"},"th")
        for tags in TextDisplayObject:
            website_content = tags.get_text("|").split("|")
            date = "2020 " + website_content[0] 
            date_time_date = datetime.strptime(date, "%Y %b %d")
            date_string = datetime.strftime(date_time_date, "%Y-%m-%d")
            website_holiday = Holiday(website_content[2], date_string)
            add_test.addHoliday(website_holiday)
        url_2023 = "https://www.timeanddate.com/holidays/us/2023?hol=1"
        executable_path = {'executable_path': ChromeDriverManager().install()}
        browser = Browser('chrome', **executable_path, headless=True)
        browser.visit(url_2023)
        html = browser.html
        html_soup = soup(html, "html.parser")
        TextDisplayObject = html_soup.find_all("tr",{"class": "showrow"},"th")
        for tags in TextDisplayObject:
            website_content = tags.get_text("|").split("|")
            date = "2023 " + website_content[0] 
            date_time_date = datetime.strptime(date, "%Y %b %d")
            date_string = datetime.strftime(date_time_date, "%Y-%m-%d")
            website_holiday = Holiday(website_content[2], date_string)
            add_test.addHoliday(website_holiday)
        url_2024 = "https://www.timeanddate.com/holidays/us/2024?hol=1"
        executable_path = {'executable_path': ChromeDriverManager().install()}
        browser = Browser('chrome', **executable_path, headless=True)
        browser.visit(url_2024)
        html = browser.html
        html_soup = soup(html, "html.parser")
        TextDisplayObject = html_soup.find_all("tr",{"class": "showrow"},"th")
        for tags in TextDisplayObject:
            website_content = tags.get_text("|").split("|")
            date = "2024 " + website_content[0] 
            date_time_date = datetime.strptime(date, "%Y %b %d")
            date_string = datetime.strftime(date_time_date, "%Y-%m-%d")
            website_holiday = Holiday(website_content[2], date_string) 
            add_test.addHoliday(website_holiday)
        # Remember, 2 previous years, current year, and 2  years into the future. You can scrape multiple years by adding year to the timeanddate URL. For example https://www.timeanddate.com/holidays/us/2022
        # Check to see if name and date of holiday is in innerHolidays array
        # Add non-duplicates to innerHolidays
        # Handle any exceptions.
    def filter_holidays_by_week(self, year_request, week_number):
        list_date = holiday_dict.keys()
        list_name = list(holiday_dict.values())
        holiday_list = []
        dateObjList = list(map(lambda x: (datetime.strptime(x,"%Y-%m-%d")), list_date))
        list_date_list = list(list_date)
        
        for i in range(len(dateObjList)):
            if dateObjList[i].isocalendar().week == int(week_number) and dateObjList[i].year == int(year_request):
                date = list_date_list[i]
                holiday_name = list_name[i]
                entry = holiday_name + " (" + date + ")"
                holiday_list.append(entry)
        for i in range (len(holiday_list)):
            print(holiday_list[i])
        # Use a Lambda function to filter by week number and save this as holidays, use the filter on innerHolidays

        # Week number is part of the the Datetime object
        # Cast filter results as list
        # return your holidays
        

add_test = HolidayList()
holiday_dict = add_test.__str__()


def startup():
    print("Holiday Managment")
    print("====================")
    global add_test
    add_test.read_json("holidays.json")
def add_holiday():
    print("Add a Holiday")
    print("===============")
    add_holiday_loop = True
    while add_holiday_loop:
        user_holiday = input("Holiday: ")
        user_date = input("Date (yyyy-mm-dd): ")
        user_date_strip = user_date.split("-")
        if len(user_date_strip[0]) != 4:
            print("Error:")
            print("Invalid Date. Please try again.")
        elif len(user_date_strip[1]) != 2:
            print("Error:")
            print("Invalid Date. Please try again.")
        elif len(user_date_strip[2]) != 2:
            print("Error:")
            print("Invalid Date. Please try again.")
        else:
            add_holiday_obj = Holiday(user_holiday, user_date)
            add_test.addHoliday(add_holiday_obj)
            add_holiday_loop = False
def remove_holiday():
    remove_holiday_loop = True
    print("Remove a Holiday")
    print("===================")
    while remove_holiday_loop:
        user_holiday = input("Holiday Name: ")
        user_date = input("Date: ")
        global add_test
        find_holiday = add_test.findHoliday(user_holiday)
        if find_holiday == None:
            print("Error:")
            print(f"{user_holiday} was not found.")
            remove_holiday_loop = False
        else:
            add_test.removeDate(user_date, user_holiday)
            remove_holiday_loop = False
def save_holiday():
    print("Save Holiday List")
    print("=====================")
    global saved
    saved = False
    decision = input("Are you sure you want to save your changes? [y/n]: ")
    if decision == "n":
        print("Canceled:")
        print("Holiday list file saved canceled.")
    elif decision == "y":
        saved = True
        global add_test
        add_test.save_to_json("SaveFile.json")

def view_holidays():
    print("View Holidays")
    print("===============")
    user_year = input("Which year: ")
    user_week = input("Which week? #[1-52, Leave blank for the current week]: ")
    current_day = datetime.today()
    current_week = current_day.isocalendar().week
    global add_test
    if user_week == "":
        add_test.filter_holidays_by_week(user_year,current_week)
    else:
        add_test.filter_holidays_by_week(user_year,user_week)

def exit():
    print("Exit")
    print("=====")
    exit_loop = True
    global saved 
    while exit_loop:
        if saved == False:
            user_choice = input("Are you sure you want to exit? \nYour changes will be lost.\n[y/n]: ")
            if user_choice =="y":
                exit_loop = False
                return False
            elif user_choice == "n":
                exit_loop = False
                return True
            else:
                print("That is not a valid entry. Please try again.")
        else:
            user_choice = input("Are you sure you want to exit? [y/n]: ")
            if user_choice =="y":
                exit_loop = False
                return False
            elif user_choice == "n":
                exit_loop = False
                return True
            else:
                print("That is not a valid entry. Please try again.")

startup()
saved = False
add_test.scrapeHolidays()
loop_menu = True
while loop_menu:
    print("Holiday Menu")
    print("===============")
    print("1. Add a Holiday")
    print("2. Remove a Holiday")
    print("3. Save Holiday List")
    print("4. View Holidays")
    print("5. Exit")
    menu_choice = input("\nWhat would you like to do?")
    if menu_choice == "1":
        add_holiday()
    elif menu_choice == "2":
        remove_holiday()
    elif menu_choice == "3":
        save_holiday()
    elif menu_choice == "4":
        view_holidays()
    elif menu_choice == "5":
        loop_menu = exit()
    else: 
        print("That is not a valid entry. Please try again.")

print("Goodbye!")