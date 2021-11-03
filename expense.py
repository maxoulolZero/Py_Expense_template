from PyInquirer import prompt
import csv

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
        "type":"input",
        "name":"spender",
        "message":"New Expense - Spender: ",
    },

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
        spamwriter.writerow([expense["amount"], expense["label"], expense["spender"]])

def new_expense(*args):
    infos = prompt(expense_questions)
    print("Expense Added !")
    write_expense(infos)
    return True


