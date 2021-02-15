#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# AZhong, 2021-Feb-14, Modifyied the script fro using lists to dictionaries
#------------------------------------------#

# Declare variabls

strChoice = '' # User input
lstTbl = []  # list of lists to hold data
dicRow = {} # dictionary of data
lstRow = []  # list of data row 
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] Load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] Delete CD from Inventory\n[s] Save Inventory to file\n[x] Exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # x: Exit the program if the user chooses so
        print('Thank you for using the Magic CD Inventory')
        break
    if strChoice == 'l':
        # l: Add the functionality of loading existing data
        lstTbl.clear()
        objFile = open(strFileName, 'r')
        for row in objFile: 
            lstRow = row.strip().split(',')
            dicRow = {'ID': int(lstRow[0]), 'Title': lstRow[1], 'Artist': lstRow[2]}
            lstTbl.append(dicRow)
        objFile.close()
        print('Inventory has been loaded from file.\n')
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # a: Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        dicRow = {'ID': intID, 'Title': strTitle, 'Artist': strArtist}
        lstTbl.append(dicRow)
        print()
        print(strTitle, 'by', strArtist, 'has been added to the Inventory.\n')
    elif strChoice == 'i':
        # i: Display the current data to the user each time the user wants to display the data
        print('CURRENT INVENTORY')
        print('ID, CD Title, Artist')
        for row in lstTbl:
            print(*row.values(), sep = ', ')
        print()
    elif strChoice == 'd':
        # d: Add functionality of deleting an entry
        print('CURRENT INVENTORY')
        print('ID, CD Title, Arist')
        for row in lstTbl: 
            print(*row.values(), sep = ', ')
        deleteID = int(input('Enter the ID you wish to remove: '))
        foundIt = False
        rowNumber = -1
        for row in lstTbl:
            rowNumber += 1
            if row['ID'] == deleteID:
               del lstTbl[rowNumber]
               foundIt = True
               break
        if foundIt:
            print('ID:', deleteID,  'has been removed.\n')
        else: 
            print('ID:', deleteID, 'cannot be found. Please try again.\n')
    elif strChoice == 's':
        # s: Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'w')
        for row in lstTbl:
            strRow = ''
            for item in row.values():
                strRow += str(item) + ','
            strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
        objFile.close()
        print('New entries have been saved to the text file.\n')
    else:
        # catch all 
        print('Please choose either l, a, i, d, s or x!')

