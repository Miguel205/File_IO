import time
from string import capwords
import matplotlib.pyplot as plt
import numpy as np
from termcolor import colored
def convertTuple(tup):
    # initialize an empty string
    str = ''
    for item in tup:
        str = str + item # add item to str
    return str;

def firstnamelist(file_name):
    first_name=[]# create list
    with open (file_name,"r") as f:# open file as f
        for line in f:
            list_of_words=line.split(",")# split line where , is
            collum = list_of_words[0]  # name_from_the_list is equal to collom 3 of the file
            first_name.append(collum)#add collum to list
    return first_name

def lastnamelist(file_name):
    first_name=[]# create list
    with open (file_name,"r") as f:# open file as f
        for line in f:
            list_of_words=line.split(",")# split line where , is
            collum = list_of_words[0]  # name_from_the_list is equal to collom 3 of the file
            first_name.append(collum)#add collum to list
    return first_name

def first_name(file_name):
    file_in = open(file_name,"r")#open the file
    first_name= input("what name")#asks user what name they want to seacrch for
    first_name = capwords(first_name)
    while first_name not in firstnamelist(file_name):
        first_name = input("none of the students at gcds are named this\ntry again\n")
        first_name = capwords(first_name)
    name_counter = 0#counter for how many peopel with name user seacher for
    first_name=capwords(first_name)#uper cases the first letter of the string
    for line in file_in:#fo r each line in the file=
        list_of_words = line.split(",")#split the file into were the , is
        name_from_the_list=list_of_words[0] # name_from_the_list is equal to collom 3 of the file
        if name_from_the_list==first_name:
            name_counter= name_counter +1
    file_in.close()
    return name_counter;

def info_on_student(file_name):
    file_in = open(file_name)
    print("what student")
    student=input("type frist_name")#asks user what student they want to search
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

def cities():
    res = []
    with open(file_name, "r") as f:# set f to open file in read mode
        for line in f:
            list_of_words = line.split(",")  # split the file into were the , is
            collum = list_of_words[7]  # name_from_the_list is equal to collom 3 of the file
            res.append(collum)#add collum to list
    cities___ = []
    for i in res:# for item in res
        if i not in cities___:# if item not in cites
            cities___.append(i)# then appened it to the list
    cities___.pop(0)#pop the first line in the file

    return cities___

def percent_students_city(file_name):
    city_choice = input("what city\n")
    city_choice = capwords(city_choice)
    while city_choice not in cities():
        city_choice = input("none of the students at gcds live in this city\ntry again\n")
        city_choice = capwords(city_choice)
    file_in = open(file_name)  # open the file
    all_ppl = -1  # all of the popele in the file /-1 to get rid of the first line
    num_ppl = 0  # number of poeple in a city
    for line in file_in:  # fo r each line in the file=
        list_of_words = line.split(",")  # split the file into were the , is
        city = list_of_words[7]  # city is equal to collom 9 of the file
        all_ppl = all_ppl + 1
        if city == city_choice:  # if the city is = to stamford
            num_ppl = num_ppl + 1  # add one to the counter
    dec_ppl = (num_ppl / all_ppl)  # divides the number of poeple who live in stamford by the number of poeple in the school
    precent_of = str(dec_ppl)# turns int into a str
    rounded=[]#this is were the rounded of percent will go
    if precent_of [1]==("."):
        rounded= precent_of[2] +precent_of[3]+("%")# rouned = precent of[3] and %
    if precent_of [2] ==("0"):# if the number in precent_of[2] is a 0
        rounded= precent_of[3] +("%")# rouned = precent of[3] and %
    if precent_of [2] ==("0") and precent_of[3] ==("0"):
        rounded= (".")+precent_of[4]+("%")
    if precent_of [2] ==("0") and precent_of[3] ==("0") and precent_of[4]==("0"):
        rounded=(".")+precent_of[4]+precent_of[5]+("%")
    return rounded, city_choice;

def pie(file_name):
    res = []
    with open(file_name, "r") as f:
        for line in f:
            list_of_words = line.split(",")  # split the file into were the , is
            collum = list_of_words[7]  # name_from_the_list is equal to collom 3 of the file
            res.append(collum)

    cities___ = []
    for i in res:
        if i not in cities___:
            cities___.append(i)
    cities___.pop(0)
    pos = 0
    all_percent = []
    while pos < len(cities___):
        city_choice = (cities___[pos])
        city_choice = capwords(city_choice)
        file_in = open(file_name)  # open the file
        all_ppl = -1  # all of the popele in the file /-1 to get rid of the first line
        num_ppl = 0  # number of poeple in a city
        for line in file_in:  # fo r each line in the file=
            list_of_words = line.split(",")  # split the file into were the , is
            city = list_of_words[7]  # city is equal to collom 9 of the file
            all_ppl = all_ppl + 1
            if city == city_choice:  # if the city is = to stamford
                num_ppl = num_ppl + 1  # add one to the counter
        dec_ppl = (num_ppl / all_ppl)  # divides the number of poeple who live in stamford by the number of poeple in the school

        pos += 1
        all_percent.append(str(dec_ppl) + ("filler") + city_choice)#add filler to know where to split the file
    all_percent.sort(reverse=True)# sort the list and reverse it becuase sort puts it least to greatest
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
    f = open("dictionary.csv", "w+")  # opening the file with w+ mode truncates the file
    f.close()  # close file
    with open("first came.csv", "r") as fhand:  # set varible fand to open file first came.csv
        lines = fhand.readlines()  # sets varible lines to the lines in first came.csv
    counts = {}  # creats emty dictionary
    for line in lines:
        for word in line.split():
            if word not in counts.keys():  # if word had nor yet appered in counts.keys
                counts[word] = 1  # give that word a key of 1
            else:
                counts[word] += 1  # add one to that key
    sorted_counts = []  # creates list
    for key, val in list(counts.items()):  # for key and val in list that is counts
        sorted_counts.append((val, key))  # add keys and vals to soured counts
    sorted_counts.sort(reverse=True)  # sorts the keys and vals in order greats to lest
    dicti_names = ()  # creats string
    with open("dictionary.csv", "a") as f:  # open dcitionary frist.csv in apened mode
        for tuple in sorted_counts[:10]:  # for tuple in the top 10 of the sorted_counts
            list_kids = list(tuple)  # adds tuple to list
            f.write(list_kids[1] + "," + str(list_kids[0]) + "\n")  # writes list in .csv
    # ==========================================================


def most_common_graph():
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
    plt.xlabel('Students')# x axis
    plt.ylabel('Number of time name shows up') #y axis
    plt.title("Most common names at GCDS")# tile of graph
    plt.show()# show graph

def delete(file_name):
    print("who do you want to remove from the file")
    line_delte_1st_name=input("type first name")# input for first name
    line_delte_last_name=input("type last name")# input for last name
    line_delte_1st_name = capwords(line_delte_1st_name)# capitlize
    line_delte_last_name=capwords(line_delte_last_name)#caputlize
    while line_delte_1st_name not in firstnamelist(file_name) and line_delte_last_name not in lastnamelist(file_name):# while the first name input not in a the list of first names and while the last name is not in the list of last names
        print("none of the students at gcds are named this\ntry again\n")
        line_delte_1st_name = input("type first name")#input
        line_delte_last_name = input("type last name")#input
        line_delte_1st_name = capwords(line_delte_1st_name)# capitlize
        line_delte_last_name=capwords(line_delte_last_name)#caputlize
    line_delte_1st_name = capwords(line_delte_1st_name)
    line_delte_last_name=capwords(line_delte_last_name)
    list_file = []  # where the file stuff goes
    with open(file_name, "r") as f:
        for line in f:  # fo r each line in the file=
            collum = line.split(",")  # split the file into were the , is
            if collum[0] != line_delte_1st_name and collum[1] != line_delte_last_name[1]:
                list_file.append(line)
    with open(file_name, "w") as f:
        for i in list_file:
            f.write(i)
    print("delted")
def update(file_name):
    print("who do you want to update from the file")
    'this is code copyied from the funtion above and it just fool proofs it '
    line_delte_1st_name=input("type first name")# input for first name
    line_delte_last_name=input("type last name")# input for last name
    line_delte_1st_name = capwords(line_delte_1st_name)# capitlize
    line_delte_last_name=capwords(line_delte_last_name)#caputlize
    while line_delte_1st_name not in firstnamelist(file_name) and line_delte_last_name not in lastnamelist(file_name):# while the first name input not in a the list of first names and while the last name is not in the list of last names
        print("none of the students at gcds are named this\ntry again\n")
        line_delte_1st_name = input("type first name")#input
        line_delte_last_name = input("type last name")#input
        line_delte_1st_name = capwords(line_delte_1st_name)# capitlize
        line_delte_last_name=capwords(line_delte_last_name)#caputlize
    print("type data if not applicatble press enter ")
    name = input("Frist Name\n")
    middle = input("Middle name(s)\n")
    last = input("Last name(s)\n")
    grade = input("Grade\n vaules accpeted 12-1,M,PK,N\n")
    gen = input("Gender\n vaules accpeted M or F")
    advisor = input("advisor name\n last name first frist name last seperated by coma")
    citiey = input("city\n")
    state = input("sate abrviasionts\n")
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
    print("updated")

print(("would you like to type the name of the file\ntype"),(colored('Yes', 'green')),("or"),(colored('No', 'red')))
n_choice=str(input())
n_choice=capwords(n_choice)
file_name=()
if n_choice=="Yes":
    print("if the file you put in is not present the functions will print nothing")
    file_name=str(input("type file name exactly how it is called"))
    try:
        with open(file_name,"r") as f:
            h=1
    except:
        print(colored("the file you entered is not prestent please download file and run the program again","red"))
        quit()  # quit at this point
if n_choice =="No":
    file_name=str("gcds.csv")
    try:
        with open(file_name,"r") as f:
            h=1
    except:
        print(colored("gcds.csv is not prestent please rename file or download file and run the program again","red"))
        quit()  # quit at this point
if n_choice != "Yes" and n_choice != "No":
    print("not a valid answer defualt file (gcds.csv) will be used")
    file_name=str("gcds.csv")
    try:
        with open(file_name,"r") as f:
            h=1
    except:
        print(colored("gcds.csv is not prestent please rename file or download file","red"))
        quit()  # quit at this point
    time.sleep(.5)



print("what do you want from the file\n")
print(("type"),(colored('1', 'blue')),(" for how many times a name shows up"))
time.sleep(.25)
print(("type"),(colored('2', 'blue')),(" for speacific infromation on a student"))
time.sleep(.25)
print(("type"),colored('3', 'blue'),(" for the percent of poeple in a city"))
time.sleep(.25)
print(("type"),colored('4', 'blue'),("to make a dictory of the most common frist name"))
time.sleep(.25)
print(("type"),colored('5', 'blue'),(" for delete a line in file"))
time.sleep(.25)
print(("type"),colored('6', 'blue'),("to update a file"))
choice=input()
while choice not in ["1","2","3","4","5","6"]:
    print("not a vaild answer\ntype either",colored('1,2,3,4,5 or 6','blue'))
    choice = input()
#=======================================================================================================================


if choice== "1":
    print(first_name(file_name))

if choice=="2":
    print(info_on_student(file_name))

if choice=="3":

    city = ""
    data,city = percent_students_city(file_name)
    print( data + " of the students live in " + city)
    pie_question = input("would you like a pie cart of the students\n")
    pie_question=capwords(pie_question)
    if pie_question== "Yes":
        pie(file_name)

if choice=="4":
    dictories()
    print("check file dictory csv")
if choice=="5":
    delete(file_name)

if choice=="6":
    update(file_name)

user_in=input("would you like to run the program again")
user_in=capwords(user_in)
if user_in=="Yes":

    n_choice = str(input("would you like to type the name of the file\ntype yes or no"))
    n_choice = capwords(n_choice)
    file_name = ()
    if n_choice == "Yes":
        print("if the file you put in is not present the functions will print nothing")
        file_name = str(input("type file name exactly how it is called"))
    if n_choice == "No":
        file_name = str("gcds.csv")
    else:
        print("not a valid answer defualt file (gcds.csv) will be used")
        file_name = str("gcds.csv")
        time.sleep(.5)

    print("what do you want from the file\n")
    print(("type"), (colored('1', 'blue')), (" for how many times a name shows up"))
    time.sleep(.25)
    print(("type"), (colored('2', 'blue')), (" for speacific infromation on a student"))
    time.sleep(.25)
    print(("type"), colored('3', 'blue'), (" for the percent of poeple in a city"))
    time.sleep(.25)
    print(("type"), colored('4', 'blue'), ("for a graph of the most common names"))
    time.sleep(.25)
    print(("type"), colored('5', 'blue'), (" for delete a line in file"))
    time.sleep(.25)
    print(("type"), colored('6', 'blue'), ("to update a file"))
    choice = input()
    while choice not in ["1", "2", "3", "4", "5", "6"]:
        print("not a vaild answer\ntype either", colored('1,2,3,4,5 or 6', 'blue'))
        choice = input()
    # =======================================================================================================================

    if choice == "1":
        print(first_name(file_name))

    if choice == "2":
        print(info_on_student(file_name))

    if choice == "3":

        city = ""
        data, city = percent_students_city(file_name)
        print(data + " of the students live in " + city)
        pie_question = input("would you like a pie cart of the students\n")
        pie_question = capwords(pie_question)
        if pie_question == "Yes":
            pie(file_name)

    if choice == "4":
        dictories()
        print("check file dictory csv")

    if choice == "5":
        delete(file_name)

    if choice == "6":
        update(file_name)
