import time
from string import capwords
import matplotlib.pyplot as plt
import numpy as np
from termcolor import colored
def convertTuple(tup):
    'functions converts tuple to string'
    # initialize an empty string
    str = ''
    for item in tup:
        str = str + item # add item to str
    return str;
def firstnamelist(file_name):
    'functions creates a list of first names'
    first_name=[]# create list
    with open (file_name,"r") as f:# open file as f
        for line in f:
            list_of_words=line.split(",")# split line where , is
            collum = list_of_words[0]  # name_from_the_list is equal to collom 3 of the file
            first_name.append(collum)#add collum to list
    return first_name
def lastnamelist(file_name):
    'functions creates a list of last names'
    last_name=[]# create list
    with open (file_name,"r") as f:# open file as f
        for line in f:
            list_of_words=line.split(",")# split line where , is
            collum = list_of_words[2]  # name_from_the_list is equal to collom 3 of the file
            last_name.append(collum)#add collum to list
    return last_name
def cities():
    'functions creates a cites with out the duplicates '
    res = []
    with open(file_name, "r") as f:# set f to open file in read mode
        for line in f:
            list_of_words = line.split(",")  # split the file into were the , is
            collum = list_of_words[7]  # name_from_the_list is equal to collum 3 of the file
            res.append(collum)#add collum to list
    cities___ = []
    for i in res:# for item in res
        if i not in cities___:# if item not in cites
            cities___.append(i)# then append it to the list
    cities___.pop(0)#pop the first line in the file

    return cities___
def cities_with_out_dup(file_name):
    'functions creates a cites with the duplicates '
    res = []
    with open(file_name, "r") as f:# set f to open file in read mode
        for line in f:
            list_of_words = line.split(",")  # split the file into were the , is
            collum = list_of_words[7]  # name_from_the_list is equal to collum 3 of the file
            res.append(collum)#add collum to list
    cities___ = []
    for i in res:# for item in res
        if i not in cities___:# if item not in cites
            cities___.append(i)# then append it to the list
    cities___.pop(0)#pop the first line in the file

    return cities___
def state_list(file_name):
    'functions creates a list of states '
    state=[]# create list
    with open (file_name,"r") as f:# open file as f
        for line in f:
            list_of_words=line.split(",")# split line where , is
            collum = list_of_words[8]  # name_from_the_list is equal to collom 3 of the file
            state.append(collum)#add collum to list
    return state
def zip_list(file_name):
    'functions creates a list of zip codes'
    zip=[]# create list
    with open (file_name,"r") as f:# open file as f
        for line in f:
            list_of_words=line.split(",")# split line where , is
            collum = list_of_words[9]  # name_from_the_list is equal to collom 3 of the file
            print(collum)
            zip.append(collum)#add collum to list
    return zip
def amount_of_first_name(file_name):
    'functions tells user how many times a name appears in the file'
    'does this by asking the user for a name and then looking each line in the file for the name'
    file_in = open(file_name,"r")#open the file
    first_name= input("what name")#asks user what name they want to seacrch for
    first_name = capwords(first_name)
    while first_name not in firstnamelist(file_name):
        first_name = input("none of the students at gcds are named this\ntry again\n")
        first_name = capwords(first_name)
    name_counter = 0#counter for how many people with name user searcher for
    first_name=capwords(first_name)#uper cases the first letter of the string
    for line in file_in:#fo r each line in the file=
        list_of_words = line.split(",")#split the file into were the , is
        name_from_the_list=list_of_words[0] # name_from_the_list is equal to collum 3 of the file
        if name_from_the_list==first_name:
            name_counter= name_counter +1
    file_in.close()
    return name_counter;
def info_on_student(file_name):
    'functions tells user information on specific student'
    file_in = open(file_name)
    print("what student")
    student=input("type first_name")#asks user what student they want to search
    student = capwords(student)
    while student not in firstnamelist(file_name):
        student = input("none of the students at gcds are named this\ntry again\n")
        student = capwords(student)
    info_line=("")#string where the info for the student will go
    for line in file_in:#fo r each line in the file

        collum= line.split(",")#split the file into were the , is
        first_name_=collum[0]#first name in the list
        if first_name_ == student:
            info_line=info_line+(line)

    file_in.close()
    return info_line;
def percent_students_city(file_name):
    'functions tells user percent of city'
    city_choice = input("what city\n")
    city_choice = capwords(city_choice)
    while city_choice not in cities():
        city_choice = input("none of the students at gcds live in this city\ntry again\n")
        city_choice = capwords(city_choice)
    file_in = open(file_name)  # open the file
    all_ppl = -1  # all of the people in the file /-1 to get rid of the first line
    num_ppl = 0  # number of people in a city
    for line in file_in:  # fo r each line in the file=
        list_of_words = line.split(",")  # split the file into were the , is
        city = list_of_words[7]  # city is equal to collum 9 of the file
        all_ppl = all_ppl + 1
        if city == city_choice:  # if the city is = to stamford
            num_ppl = num_ppl + 1  # add one to the counter
    dec_ppl = (num_ppl / all_ppl)  # divides the number of people who live in stamford by the number of poeple in the school
    precent_of = str(dec_ppl)# turns int into a str
    rounded=[]#this is were the rounded of percent will go
    'changes decimal into percent'
    if precent_of [1]==("."):
        rounded= precent_of[2] +precent_of[3]+("%")# rounded = present of[3] and %
    if precent_of [2] ==("0"):# if the number in present_of[2] is a 0
        rounded= precent_of[3] +("%")# rounded = present of[3] and %
    if precent_of [2] ==("0") and precent_of[3] ==("0"):
        rounded= (".")+precent_of[4]+("%")
    if precent_of [2] ==("0") and precent_of[3] ==("0") and precent_of[4]==("0"):
        rounded=(".")+precent_of[4]+precent_of[5]+("%")
    return rounded, city_choice;
def pie(file_name):
    'functions gives user graph'
    cities___=cities()
    pos = 0
    all_percent = []
    while pos < len(cities___):
        city_choice = (cities___[pos])
        city_choice = capwords(city_choice)
        file_in = open(file_name)  # open the file
        all_ppl = -1  # all of the people in the file /-1 to get rid of the first line
        num_ppl = 0  # number of people in a city
        for line in file_in:  # fo r each line in the file=
            list_of_words = line.split(",")  # split the file into were the , is
            city = list_of_words[7]  # city is equal to collum 9 of the file
            all_ppl = all_ppl + 1
            if city == city_choice:  # if the city is = to stamford
                num_ppl = num_ppl + 1  # add one to the counter
        dec_ppl = (num_ppl / all_ppl)  # divides the number of people who live in stamford by the number of poeple in the school

        pos += 1
        all_percent.append(str(dec_ppl) + ("filler") + city_choice)#add filler to know where to split the file
    all_percent.sort(reverse=True)# sort the list and reverse it because sort puts it least to greatest
    '''
    the next part is to remove all the cites less then .1% as they take up to much space in the graph
    '''
    pos = 0
    to_small = 0  # were the cites small then %1 will go
    while pos < len(all_percent):
        wrd_in = all_percent[pos]  # a letter in
        if wrd_in[2] == "0" and wrd_in[3] == "0":
            all_percent.remove(wrd_in)# remove wrd in from list
            pos -= 1#delet 1 from pos as a vaule of all percent was deleted so the len decreases
            just_num = wrd_in.split("filler")
            to_small = to_small + (float(just_num[0]))
        if wrd_in[2] == "0" and wrd_in[3] == "f":# becuae one of the line in the csv file is missing a vuale CT sometimes shows up as 0.0filerCT so this piece of code is just to get rid of that value
            all_percent.remove(wrd_in)# remove wrd in from list
            pos -= 1#delet 1 from pos as a vaule of all percent was deleted so the len decreases
        pos += 1# add one to pos
    mylabels = []#lables from chart
    num = []#numbers for chart
    for item in all_percent:
        t = item.split("filler")# item in all precent were the filler is
        mylabels.append(t[1])# add the city to my labels
        num.append(t[0])# add the number to num
    mylabels.append("Other")# add the label other to the list
    num.append(to_small)# add the number of all the precent of cites that were to smal to the list

    y = np.array(num)# numbers for chart
    plt.pie(y, labels=mylabels)#label for graph
    plt.legend(title="Cites:")# tile of graph
    plt.show()#show the graph
def dictories():
    'functions give user dictionary on information they choose'
    print("what do you want to look for\nmost common\ntype",colored('1', 'blue'),"for First name\ntype",colored('2', 'blue'),"for Cities")
    user_data=input()
    while user_data not in ['1','2']:
        print("not an acceptable answer\n type either1 or 2")
        user_data=input()
    if user_data == "1": # if user data = first name
        list_cat=firstnamelist(file_name)# list_cat= first name list
    if user_data == "2":
        list_cat=cities_with_out_dup(file_name)
    f = open("dictionary.csv", "w+")  # opening the file with w+ mode truncates the file
    f.close()  # close file
    counts = {}  # creats emty dictionary
    for line in list_cat:
        for word in line.split():
            if word not in counts.keys():  # if word had nor yet appeared in counts.keys
                counts[word] = 1  # give that word a key of 1
            else:
                counts[word] += 1  # add one to that key
    sorted_counts = []  # creates list
    for key, val in list(counts.items()):  # for key and val in list that is counts
        sorted_counts.append((val, key))  # add keys and vals to soured counts
    sorted_counts.sort(reverse=True)  # sorts the keys and vals in order greats to lest
    dicti_names = ()  # creats string
    with open("dictionary.csv", "a") as f:  # open dictionary frist.csv in apened mode
        for tuple in sorted_counts[:10]:  # for tuple in the top 10 of the sorted_counts
            list_kids = list(tuple)  # adds tuple to list
            f.write(list_kids[1] + "," + str(list_kids[0]) + "\n")  # writes list in .csv
    # ==========================================================
def most_common_graph():
    'functions gives user graph of dictionaries '
    # graph stuff
    heights = []  # how tall the values on the graph are
    bar_labels = []  # labels for values
    left_coordinates = []  # number of values
    counter = 1  # counter for number of values
    with open("dictionary.csv", "r") as r:  # open file and set that to r
        for line in r:  # for line in r
            collums = line.split(",")  # split line at ,
            numb = collums[1].split("\n")  # split line at \n
            bar_labels.append(collums[0])  # add stuff to list
            heights.append(int(numb[0]))  # add stuff to list
            left_coordinates.append(int(counter))  # add stuff to list
            counter += 1  # add 1 counter
    plt.bar(left_coordinates, heights, tick_label=bar_labels, width=0.6, color=['orange', 'black', ])  # info for bar
    plt.xlabel('info')# x axis
    plt.ylabel('Number of time info shows up') #y axis
    plt.title("Most common info at GCDS")# tile of graph
    plt.show()# show graph
def delete(file_name):
    'deletes line in file by checking if the name that the user puts in is the same of name that is on the line'
    print("who do you want to remove from the file")
    line_delte_1st_name=input("type first name")# input for first name
    line_delte_last_name=input("type last name")# input for last name
    line_delte_1st_name = capwords(line_delte_1st_name)# capitalize
    line_delte_last_name=capwords(line_delte_last_name)#caputlize
    while line_delte_1st_name not in firstnamelist(file_name) or line_delte_last_name not in lastnamelist(file_name):# the code is coped and changed to or becuase of a bug were the user would put one correct answer
        print("none of the students at gcds are named this\ntry again\n")
        line_delte_1st_name = input("type first name")#input
        line_delte_last_name = input("type last name")#input
        line_delte_1st_name = capwords(line_delte_1st_name)# capitalize
        line_delte_last_name=capwords(line_delte_last_name)#caputlize
    line_delte_1st_name = capwords(line_delte_1st_name)#capitlize
    line_delte_last_name=capwords(line_delte_last_name)#capitlize
    list_file = []  # where the file stuff goes
    with open(file_name, "r") as f:# set f to open file in read mode
        for line in f:  # fo r each line in the file=
            collum = line.split(",")  # split the file into were the , is
            if collum[0] != line_delte_1st_name and collum[1] != line_delte_last_name[1]:# if collum 0 (first name on line) not equal to first name of user and if collum 1 (last name on line) not equal to last name of user choice
                list_file.append(line)# add line
    with open(file_name, "w") as f:#open file nae in write mode this truncates the file
        for i in list_file:# for item in the list with the file stuff
            f.write(i)# write team
    print("deleted")
def update(file_name):
    'updates the file'
    "does this by checking if the name that the user puts in is the same name that is on the line"
    "if it is add the list of new data"
    print("who do you want to update from the file")
    'this is code copied from the function above and it just fool proofs it '
    line_delte_1st_name=input("type first name")# input for first name
    line_delte_last_name=input("type last name")# input for last name
    line_delte_1st_name = capwords(line_delte_1st_name)# capitlize
    line_delte_last_name=capwords(line_delte_last_name)#caputlize
    while line_delte_1st_name not in firstnamelist(file_name) or line_delte_last_name not in lastnamelist(file_name):# while the first name input not in a the list of first names and while the last name is not in the list of last names
        print("none of the students at gcds are named this\ntry again\n")
        line_delte_1st_name = input("type first name")#input
        line_delte_last_name = input("type last name")#input
        line_delte_1st_name = capwords(line_delte_1st_name)# capitalize
        line_delte_last_name=capwords(line_delte_last_name)#caputlize
    print("type data if not applicable press enter ")
    name = input("First Name\n")
    name=capwords(name)
    middle = input("Middle name(s)\n")
    middle= capwords(middle)
    last = input("Last name(s)\n")
    last=capwords(last)
    grade = input("Grade\n values accepted N PK K 1-12\n")
    while grade not in ["N","n","PK","pk","K","k","1","2","3","4","5","6","7","8","9","10","11","12"]:
        print("not acceptable answer please type either\nN PK K 1-12")
        grade= input()
    gen = input("Gender\n values accepted M or F")
    advisor = input("advisor name\n last name first first name last separated by coma")
    citiey = input("city\n")
    state = input("sate abbreviation\n")
    zip = input("zip code\n")
    advisor = ('"') + advisor + ('"')
    new_data = (
    name, (","), middle, (","), last, (","), grade, (","), gen, (","), advisor, (","), citiey, (","), state, (","), zip,
    ("\n"))
    new_data = convertTuple(new_data)

    list_file = []  # where the file stuff goes
    with open(file_name, "r") as f:
        for line in f:  # fo r each line in the file=
            collum = line.split(",")  # split the file into were the , is
            if collum[0] == line_delte_1st_name and collum[2] == line_delte_last_name:  # if name is not eequal to users anem choice
                list_file.append((new_data))

            else:
                list_file.append(line)  # append the line to the list
    with open(file_name, "w") as f:
        for i in list_file:
            f.write(i)
    print(colored("updated",'green'))


#========================================================================================================================================================================================================================
'allows the user to input name of file'
print(("would you like to type the name of the file\ntype"),(colored('Yes', 'green')),("or"),(colored('No', 'red')))# asks the user if they want to put  the name of the file
n_choice=str(input())# users input
n_choice=capwords(n_choice)# captilize
if n_choice=="Yes": # if user choice = yes
    print("if the file you put in is not present the functions will print nothing")
    file_name=str(input("type file name exactly how it is called"))# user input for name of file
    try:# try running
        with open(file_name,"r") as f:# set f to open file
            h=1# a filler statement
    except:# if error
        print(colored("the file you entered is not prestent please download file and run the program again","red"))
        quit()  # quit the program
if n_choice =="No":# if user answer =no
    file_name=str("gcds.csv") # the file is set to gcds.csv
    try:# try running
        with open(file_name,"r") as f:# set f to open file
            h=1# a filler statement
    except:# if error
        print(colored("gcds.csv is not prestent please rename file or download file and run the program again","red"))
        quit()  # quit at this point
if n_choice != "Yes" and n_choice != "No":
    print(colored("not a valid answer default file (gcds.csv) will be used","red"))
    file_name=str("gcds.csv")
    try:# try running
        with open(file_name,"r") as f:# set f to open file
            h=1
    except:# if error
        print(colored("gcds.csv is not present please rename file or download file","red"))
        quit()  # quit at this point
    time.sleep(.5)# pause for .5 sec
#====================================================================================================================
'user picks what program they want '
print("what do you want from the file")
print(("type"), (colored('1', 'blue')), " for how many times a name shows up")
time.sleep(.25)
print(("type"), (colored('2', 'blue')), " for specific information on a student")
time.sleep(.25)
print(("type"), colored('3', 'blue'), " for the percent of people in a city")
time.sleep(.25)
print(("type"), colored('4', 'blue'), "to make a dictionary of the most common frist name")
time.sleep(.25)
print(("type"), colored('5', 'blue'), " for delete a line in file")
time.sleep(.25)
print(("type"), colored('6', 'blue'), "to update a file")
choice=input()
#====================================================================================================================
'users choices '
while choice not in ["1","2","3","4","5","6"]:# while the users choice is not 1 2 3 4 5 or 6
    print("not a vaild answer\ntype either",colored('1,2,3,4,5 or 6','blue'))
    choice = input()# ask again for input
if choice== "1":
    print(amount_of_first_name(file_name))
if choice=="2":
    print(info_on_student(file_name))
if choice=="3":

    city = ""
    data,city = percent_students_city(file_name)
    print( data + " of the students live in " + city)
    print("would you like a pie cart of the students\n",colored('Yes', 'green'),("or"),colored('No', 'red'))# asks user if they want pie chart
    pie_question= input()
    pie_question=capwords(pie_question) # capitalize
    while pie_question not in ["Yes","No"]:#while the users answer is not yes or no
        print("not valid answer type ether yes or no")
        pie_question=input()# ask again for user input
        pie_question=capwords(pie_question)# capitalize
    if pie_question== "Yes":# if user answer yes
        print(colored('close chart when you want to continue using the program','red'))
        time.sleep(.75)
        pie(file_name)# run pie chart function
if choice == "4":
    dictories()
    print("check file dictory csv")
    time.sleep(1)
    print("would you like a graph of the data",colored('Yes', 'green'),("or"),colored('No', 'red'))
    oth_choice=input()
    oth_choice=capwords(oth_choice)
    while oth_choice not in ["Yes","No"]:#while the users answer is not yes or no
        print("not valid answer type ether yes or no")
        oth_choice=input()# ask again for user input
        oth_choice=capwords(oth_choice)
    if oth_choice== "Yes":# if user answer yes
        print(colored('close graph when you want to continue using the program','red'))
        time.sleep(.75)
        most_common_graph()# run graph function
if choice=="5":
    delete(file_name)
if choice=="6":
    update(file_name)

"runs program again"
print("would you like to run the program again",colored('Yes', 'green'),("or"),colored('No', 'red')) #
user_in=input()
user_in=capwords(user_in)# capitalize
while user_in not in ["Yes", "No"]:# while the users answers is not yes or no
    print("not valid answer type ether yes or no",colored('Yes', 'green'),("or"),colored('No', 'red')) # print not valid answer
    user_in= input()# users input
    user_in = capwords(user_in)#captilize
while user_in=="Yes":#while user anwser continues to be yes run program

    # ========================================================================================================================================================================================================================
    'allows the user to input name of file'
    print(("would you like to type the name of the file\ntype"), (colored('Yes', 'green')), ("or"),
          (colored('No', 'red')))  # asks the user if they want to put  the name of the file
    n_choice = str(input())  # users input
    n_choice = capwords(n_choice)  # captilize
    if n_choice == "Yes":  # if user choice = yes
        print("if the file you put in is not present the functions will print nothing")
        file_name = str(input("type file name exactly how it is called"))  # user input for name of file
        try:  # try running
            with open(file_name, "r") as f:  # set f to open file
                h = 1  # a filler statement
        except:  # if error
            print(colored("the file you entered is not prestent please download file and run the program again", "red"))
            quit()  # quit the program
    if n_choice == "No":  # if user answer =no
        file_name = str("gcds.csv")  # the file is set to gcds.csv
        try:  # try running
            with open(file_name, "r") as f:  # set f to open file
                h = 1  # a filler statement
        except:  # if error
            print(colored("gcds.csv is not prestent please rename file or download file and run the program again",
                          "red"))
            quit()  # quit at this point
    if n_choice != "Yes" and n_choice != "No":
        print(colored("not a valid answer default file (gcds.csv) will be used", "red"))
        file_name = str("gcds.csv")
        try:  # try running
            with open(file_name, "r") as f:  # set f to open file
                h = 1
        except:  # if error
            print(colored("gcds.csv is not present please rename file or download file", "red"))
            quit()  # quit at this point
        time.sleep(.5)  # pause for .5 sec
    # ====================================================================================================================
    'user picks what program they want '
    print("what do you want from the file")
    print(("type"), (colored('1', 'blue')), " for how many times a name shows up")
    time.sleep(.25)
    print(("type"), (colored('2', 'blue')), " for specific information on a student")
    time.sleep(.25)
    print(("type"), colored('3', 'blue'), " for the percent of people in a city")
    time.sleep(.25)
    print(("type"), colored('4', 'blue'), "to make a dictionary of the most common frist name")
    time.sleep(.25)
    print(("type"), colored('5', 'blue'), " for delete a line in file")
    time.sleep(.25)
    print(("type"), colored('6', 'blue'), "to update a file")
    choice = input()
    # ====================================================================================================================
    'users choices '
    while choice not in ["1", "2", "3", "4", "5", "6"]:  # while the users choice is not 1 2 3 4 5 or 6
        print("not a vaild answer\ntype either", colored('1,2,3,4,5 or 6', 'blue'))
        choice = input()  # ask again for input
    if choice == "1":
        print(amount_of_first_name(file_name))
    if choice == "2":
        print(info_on_student(file_name))
    if choice == "3":

        city = ""
        data, city = percent_students_city(file_name)
        print(data + " of the students live in " + city)
        print("would you like a pie cart of the students\n", colored('Yes', 'green'), ("or"),
              colored('No', 'red'))  # asks user if they want pie chart
        pie_question = input()
        pie_question = capwords(pie_question)  # capitalize
        while pie_question not in ["Yes", "No"]:  # while the users answer is not yes or no
            print("not valid answer type ether yes or no")
            pie_question = input()  # ask again for user input
            pie_question = capwords(pie_question)  # capitalize
        if pie_question == "Yes":  # if user answer yes
            print(colored('close chart when you want to continue using the program', 'red'))
            time.sleep(.75)
            pie(file_name)  # run pie chart function
    if choice == "4":
        dictories()
        print("check file dictory csv")
        time.sleep(1)
        print("would you like a graph of the data", colored('Yes', 'green'), ("or"), colored('No', 'red'))
        oth_choice = input()
        oth_choice = capwords(oth_choice)
        while oth_choice not in ["Yes", "No"]:  # while the users answer is not yes or no
            print("not valid answer type ether yes or no")
            oth_choice = input()  # ask again for user input
            oth_choice = capwords(oth_choice)
        if oth_choice == "Yes":  # if user answer yes
            print(colored('close graph when you want to continue using the program', 'red'))
            time.sleep(.75)
            most_common_graph()  # run graph function
    if choice == "5":
        delete(file_name)
    if choice == "6":
        update(file_name)

    print("would you like to run the program again", colored('Yes', 'green'), ("or"), colored('No', 'red'))
    user_in = input()
    user_in = capwords(user_in)
    while user_in not in ["Yes", "No"]:
        print("not valid answer type ether yes or no", colored('Yes', 'green'), ("or"), colored('No', 'red'))
        user_in = input()
        user_in = capwords(user_in)
