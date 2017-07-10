'''
Created on 5 Jul 2017

@author: jdrumgoole
'''

'''
Derived from https://data.gov.uk/dataset/anonymised_mot_test/resource/1d4236e8-92a4-4449-8711-213b40b6353b
'''

Vehicle_Class = {
    "motor_cycle"            : "1",
    "motor_bicycle"          : "2",
    "three_wheeled_vehicles" : "3",
    "cars"                   : "4",
    "cars_special"           : "4A",
    "buses"                  : "5",
    "buses_special"          :"5A",
    "trucks"                 : "7,"
    }

Test_Outcomes = {
    "Pass"                    : "P",
    "Fail"                    : "F",
    "Pass_with_rectification" : "PRS",
    "Abandon"                 : "ABA",
    "Abort"                   : "ABR",
    "refusal"                 : "R",
    }

Test_Types = {
    "Normal"                : "N",
    "Full_retest"           : "F",
    "Partial_retest_minor"  : "PM",
    "Partial_retest_repair" : "PR",
    "Refusal"               : "RF",
    "Partial_retest_left"   : "PL",
    }

Fuel_Type = {
    "Petrol"     : "P",
    "Diesel"     : "D",
    "Electric"   : "E",
    "Steam"      : "S",
    "LPG"        : "L", #liquified pertroleum gas
    "CNG"        : "C", #Compress natural gas
    "LNG"        : "N",  #liquifed natural gas
    "Fuel_cells" : "F",
    "Other"      : "O"
    }

#reasons for rejection
RFR_Types = {
    "Fail"            : "F",
    "PRS"             : "P", #pass with rectification at station
    "Advisory"        : "A",
    "Abandon"         : "ABA",
    "Abort"           : "ABR",
    "Refusal_to_test" : "R",
    }

Test_Result = {
    "Test_ID"        : "int",
    "Vehicle_ID"     : "int",
    "Test_date"      : "date",
    "Test_class_ID"  : "str",
    "Test_type"      : "str",
    "Test_result"    : "str",
    "Test_mileage"   : "int",
    "Postcode_area"  : "str",
    "make"           : "str",
    "model"          : "str",
    "colour"         : "str",
    "Fuel_type"      : "str",
    "CC"             : "str",
    "First_use_date" : "date",
    }

Test_item = {
    "TEST_ID"          : "int",
    "RFR_ID"           : "int",
    "RFR_TYPE"         : "str",
    "Lat_location_ID"  : "str",
    "Lon_location_ID"  : "str",
    "Vert_location_ID" : "str",
    "D_mark"           : "str",
    
    
    }
    
    
    }
