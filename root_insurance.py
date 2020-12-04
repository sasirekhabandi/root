#read the input file
from collections import defaultdict
from datetime import datetime
import math


class root_insurance:
    
    def __init__(self,name):

        # class variables name, total_miles,total_time
        self.name = name
        self.total_miles = 0
        self.total_time = 0
    
    #adding a trip for the respective driver
    def add_trip(self,start_time,end_time,miles):

        # time format
        time_format = '%H:%M'
    
        
        #calculate time diff
        tdelta = datetime.strptime(end_time, time_format) - datetime.strptime(start_time, time_format)
        diff_time = tdelta.total_seconds()/3600;
                
        # total miles
        speed = miles/diff_time

        #discarding speed less than 5 and greater than 100
        if speed >= 5 and speed <=100:
            
            self.total_miles =miles + self.total_miles
            self.total_time = diff_time + self.total_time

    # calculating speed
    def calculate_speed(self):
        
        try :
            avg_speed =  math.ceil(self.total_miles/ self.total_time)
            
        except ZeroDivisionError:

            avg_speed = 0
            
        return avg_speed

    #get total miles
    def get_total_miles(self):
        
        return int(self.total_miles)
    
