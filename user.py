from PyInquirer import prompt
import csv 
import json


user_questions = [
    {
        "type":"input",
        "name":"Name",
        "message":"New User - Name: ",
    }
]
my_file = "./users.csv"

def get_user_list():
    L = []
    with open(my_file, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ')
        for row in spamreader:
            for i in range(len(row)):
                L.append(str(row[i])) 
    return L

def get_user_list_no_spender():
    L = []
    with open(my_file, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ')
        for row in spamreader:
            for i in range(len(row)):
                data = {}
                data['name'] = row[i]
                L.append(json.dumps(data)) 
    print(L)
    return L



def read_user():
    with open(my_file, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ')
        for row in spamreader:
            print(', '.join(row))

def write_user(user):    
    with open(my_file, 'a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')
        spamwriter.writerow([user["Name"]])

def add_user():
    infos = prompt(user_questions)
    print("User Added")
    write_user(infos)
    return True