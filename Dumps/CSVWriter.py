# import csv

# with open('names.csv', 'w', newline='') as csvfile:
#     # fieldnames = ['first_name', 'last_name']
#     writer = csv.DictWriter(csvfile)

#     writer.writeheader()
#     writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
#     writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
#     writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
import csv

nms = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]]

f = open('numbers2.csv', 'w')

with f:

    writer = csv.writer(f)
    
    for row in nms:
        writer.writerow(row)