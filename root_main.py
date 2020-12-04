# importing the class root_insurance
from root_insurance import*
import sys

def main(path_file):

    #dictionary to store driver name and class objects
    driver = {}

    #opening  the file
    with open(path_file) as fp:

        #Read each line 
        line = fp.readline()
        
        while line:
            
            # splitting the input and case-sensitive for driver and trip
            instr = line.split()
            first_ele = instr[0].lower()
            
            if first_ele == 'driver':

                #creating new driver and object
                if instr[1] not in driver:
                    driver[instr[1]] = root_insurance(instr[1])
            #
            elif first_ele == 'trip':
                 if instr[1] not in driver:
                     driver[instr[1]] = root_insurance(instr[1])
                     
                 #adding trips
                 driver[instr[1]].add_trip(instr[2],instr[3],float(instr[4]))
            
            line = fp.readline()
    #closing the file        
    fp.close()

    # displaying based on the highest miles
    for drivers, obj in sorted(driver.items(), key=lambda item: item[1].get_total_miles(),reverse = True):

        if obj.get_total_miles() != 0:
            print("{0}: {1} miles @ {2} mph ".format(drivers,obj.get_total_miles(),obj.calculate_speed()))
        else:
            print("{0}: {1} miles".format(drivers,obj.get_total_miles()))

    


if __name__ == "__main__":

    main(sys.argv[1])

    
    

