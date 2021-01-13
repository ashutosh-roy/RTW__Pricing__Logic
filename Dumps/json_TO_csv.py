# -----------------------------
# SOURCE CODE 1
# -----------------------------

# import csv, json, sys
# #if you are not using utf-8 files, remove the next line
# # sys.setdefaultencoding("UTF-8") #set the encode to utf8
# #check if you pass the input file and output file
# if sys.argv[1] is not None and sys.argv[2] is not None:
#     fileInput = sys.argv[1]
#     fileOutput = sys.argv[2]
#     inputFile = open(fileInput) #open json file
#     outputFile = open(fileOutput, 'w') #load csv file
#     data = json.load(inputFile) #load json content
#     inputFile.close() #close the input file
#     output = csv.writer(outputFile) #create a csv.write
#     output.writerow(data[0].keys())  # header row
#     for row in data:
#         output.writerow(row.values()) #values row



# -----------------------------
# SOURCE CODE 2
# -----------------------------

# import json 
# import csv 
  
  
# Opening JSON file and loading the data 
# into the variable data 
# with open('data.json') as json_file: 
#     data = json.load(json_file) 

# import pandas as pd
# df = pd.read_json (r'JSON_Data_v.5.json',lines=True)
# df.to_csv (r'RTW.csv', index = None)

# -----------------------------
# SOURCE CODE 3
# -----------------------------

import json 
import csv 
  
  
# Opening JSON file and loading the data 
# into the variable data 
with open('v.5.json') as json_file: 
    data = json.load(json_file) 
johordata = data[0]["JOHOR"]

print(johordata)
# now we will open a file for writing 
data_file = open('RTW.csv', 'w') 
  
# create the csv writer object 
csv_writer = csv.writer(data_file) 
  
# Counter variable used for writing  
# headers to the CSV file 
count = 0

for i in johordata:
    for key,value in i.items(): 
        print("KEY = {}".format(key))
        print("Value = {}".format(value))
    # if count == 0: 
    #     print("----------------------------------")
    #     print("COUNT = {}".format(emp))

    #     print("----------------------------------")
    #     # Writing headers of CSV file 
    #     header = emp['JOHOR'].keys() 
    #     csv_writer.writerow(header) 
    #     count += 1
  
    # Writing data of CSV file 
    csv_writer.writerow(i.values()) 
  
data_file.close() 
