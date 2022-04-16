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
        legnth = len(self.innerHolidays) -1
        # Find Holiday in innerHolidays by searching the name and date combination.
        for i in range(legnth):
            if list(self.innerHolidays)[i] == date:
                del self.innerHolidays[date]
               
        # remove the Holiday from innerHolidays
        # inform user you deleted the holiday
   
        

test = Holiday("Birthday", "1995-10-29")
test1 = Holiday("Halloween", "1995-10-31")
print(test.__str__())
add_test = HolidayList()
add_test.addHoliday(test)
add_test.addHoliday(test1)
holiday_dict = add_test.__str__()
print (holiday_dict.keys(), holiday_dict.values())
holiday = add_test.findHoliday("Halloween")
print(holiday)
date = add_test.findDate("1995-10-29")

print(type(date))
print(list(holiday_dict))
add_test.removeDate(date)
print (list(holiday_dict.keys()), list(holiday_dict.values()))
     