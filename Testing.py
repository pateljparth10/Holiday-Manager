import datetime
import json
from bs4 import BeautifulSoup
import requests
from dataclasses import dataclass


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

    def removeDate(self,date):
        legnth = len(self.innerHolidays)
        # Find Holiday in innerHolidays by searching the name and date combination.
        for i in range(legnth):
            if list(self.innerHolidays)[i] == date:
                position = date
        del self.innerHolidays[position]
        print(f"You have removed the date: {date}")     
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
   
        

test = Holiday("Birthday", "1995-10-29")

print(test.__str__())

add_test = HolidayList()
add_test.addHoliday(test)
test = Holiday("Halloween", "1995-10-31")
add_test.addHoliday(test)
holiday_dict = add_test.__str__()
print (holiday_dict.keys(), holiday_dict.values())

holiday = add_test.findHoliday("Halloween")
print(holiday)
date = add_test.findDate("1995-10-31")

print(list(holiday_dict))
add_test.removeDate(date)
print (list(holiday_dict.keys()), list(holiday_dict.values()))

add_test.read_json("holidays.json") 
total_holidays = add_test.numHolidays()
print(total_holidays)
 
print (holiday_dict.keys(), holiday_dict.values())
add_test.save_to_json("SaveFile.json")

