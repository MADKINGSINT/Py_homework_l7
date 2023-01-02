import csv

def export():
    with open('Phonebook.csv', mode ='r', encoding='utf-8') as file:
    # reading the CSV file
        csv_file = csv.DictReader(file)
    # displaying the contents of the CSV file
        for line in csv_file:
            print(line)


        