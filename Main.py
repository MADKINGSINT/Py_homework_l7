
que = int(input('Выберите действие: \n1-импорт\n2-экспорт\n'))
print(que)
if (que == 1):
    from os.path import exists
    from CSV_creating import create_files
    from File_writing import write_csv
    from File_writing import write_file
    
    path = 'hw7.2/Phonebook.csv'
    valid = exists(path)
    if not valid:
        create_files()

    write_csv()
    write_file()
elif(que == 2):
    from export import export
    export()
