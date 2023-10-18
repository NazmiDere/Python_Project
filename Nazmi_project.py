employees = {'Daniel Ricciardo':(34,2011),'Charles Leclerc':(26,2018),'Lando Norris':(23,2019)} #creating a new dictionary with two instances

                                       
while True:
    inp = str(input("Type 'show', 'add', 'delete' or 'quit':")).lower().strip() #getting input from user as lowercase and getting rid of extra spaces   
    filtered_inp = filter(str.isalpha,inp)                              #filtering the input from unnecessary characters
    inp_new = ''.join(filtered_inp)                                     #getting together the whole input 

    while inp_new not in ['add','show','delete','quit']:                    #checking if the user enters a valid option
        inp = str(input("You have only 4 options 'show', 'add', 'delete' or 'quit':")).lower().strip() #getting a new input from user
        filtered_inp = filter(str.isalpha,inp)                              #filtering the input from unnecessary characters
        inp_new = ''.join(filtered_inp)                                     #getting together the whole input 
        
    if inp_new == 'show':                                               
        for a in employees.keys():
            print('\nName:',a,'\nAge:',employees[a][0],'\nStarting year:',#if user types 'show', showing all dictionary with for loop
               employees[a][1],'\n')

    if inp_new == 'add':
        while True:
            name = str(input('Please enter a name and surname:'))           #if user types add, asking for a name
            raw_name = ''.join(name.split())                                #clearing spaces between words
            if not raw_name.isalpha():                                      #checking if it is alphabetic 
                print('You can enter only letters') 
                continue
            if len(name.split()) < 2:                                       #checking if user enters at least 2 words
                print('Please enter both name and surname')
                continue
            break
        while True:
            age = input('Please enter an age:')                     #asking for a age
            if not age.isdigit():                                   #checking if it is numeric
                print('You can enter only numbers')                                                              
                continue
            age = int(age)
            if age < 18 or age > 67:                                #checking if it is between 18 and 67
                print('Please enter an age between 18 and 67')
                continue
            break
        
        while True:
            year = input('Please enter a starting year:')               #asking for a starting year
            if not year.isdigit():                                      #checking if it is numeric
                print('You can enter only numbers')
                continue
            year = int(year)
            if year < 1950 or year > 2023:                              #checking if it is between 1950 and 2023
                print('Please enter a starting year between 1950 and 2023')
                continue
            break
    
        employees[' '.join(name.split()).title()] = (age, year)     #adding a new pair in the dictionary

    if inp_new == 'delete':
        while True:
            delname = str(input('Please enter the name you want to delete:'))   #if user types delete, getting the user name to delete 
            raw_delname = ''.join(delname.split())                              #deleting spaces and creating raw text
            new_delname = ' '.join(delname.split())                             #creating a new name with a space between each other
            if not raw_delname.isalpha():                                       #checking if it is alphabetic 
                print('You can enter only letters') 
                continue
            if len(delname.split()) < 2:                                        #checking if user enters at least 2 words
                print('Please enter both name and surname to delete')
                continue
            break
        del employees[new_delname.title()]                                      #deleting the pair which user wants to delete
        print(f'{new_delname.title()} has been deleted')
        
    if inp_new == 'quit':
        quit()


        
        

