# 2023-24 ATU Data Prepresentation Topic04
# Lab04.1.9 Write a program in another file that works out the average book price 
# from all the books on the server
# by: Eva Czeyda-Pommersheim

from lab04_1 import readbooks

books = readbooks()
total = 0
count = 0
for book in books:
    total += book['Price']
    count += 1
print(f'The average book price of the', count, 'books is €', round(total/count))