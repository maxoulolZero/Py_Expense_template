from PyInquirer import prompt, Separator
import csv
from user import get_user_list, get_user_list_no_spender, read_user

expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"list",
        "name":"spender_choice",
        "message":"New Expense - choose a Spender: ",
        "choices": get_user_list()
    },
    {
        'type': 'checkbox',
        'qmark': '😃',
        'message': 'Select users to share with',
        'name': 'Users',
        'choices': get_user_list_no_spender() 
        
    }
]


my_file = "./expense_report.csv"


def read_expense():
    with open(my_file, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ')
        for row in spamreader:
            print(', '.join(row))

def write_expense(expense):    
    with open(my_file, 'a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')
        spamwriter.writerow([expense["amount"], expense["label"], expense["spender_choice"]])

def new_expense(*args):
    infos = prompt(expense_questions)
    print(infos)
    print("Expense Added !")
    write_expense(infos)
    read_expense()
    return True


