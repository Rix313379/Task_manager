'''Adăugare task nou
o Descriere: Utilizatorul introduce un nou task. Detalii necesare:
▪ Task (un text unic care nu poate fi duplicat)
▪ Dată limită (format specific, ex. 22.01.2022 21:30)
▪ Persoana responsabilă
▪ Categoria (trebuie să existe deja în lista de categorii)
'''


import pandas as pd
from datetime import datetime

def category_exists(category, file = 'categorii.csv'):
    df = pd.read_csv(file)
    return category in df['category'].values
    
def task_exists(task, file = 'taskuri.csv'):
    df = pd.read_csv(file)
    return task in df['name'].values

def get_new_id(file='taskuri.csv'):
    df = pd.read_csv(file)
    return df['id'].max() + 1

def add_new_tasks():

    task = input("Please insert your task: ")
    category = input("Please insert your category: ")
    
    if not category_exists(category):
        print("This category is not in the database")
        return # Ieșim din funcție dacă formatul nu este valid
    
    deadline = input("Please insert the deadline (format: dd.mm.yyyy hh:mm): ")
    person_responsible = input("Please insert the person responsible for this task: ")
    
    try:
        deadline_dt = datetime.strptime(deadline, "%d.%m.%Y %H:%M")
    except ValueError:
        print("Incorrect date format, please retry! ")
        return  
        
    if task_exists(task):
        print(f'"{task}" already exists')
    else:
        df = pd.read_csv('taskuri.csv')
        
        new_task = {
            'id': get_new_id(),
            'name': task.strip(),
            'max_date': deadline_dt.strftime('%Y-%m-%d'),  # Salvăm data în format YYYY-MM-DD
            'assignee': person_responsible.strip(),
            'category': category.strip()
        }
        
        df = df.append(new_task, ignore_index=True)
        
        print(f' "{task}" in "{category}" has been added for "{person_responsible}", the date limit is: "{deadline}". ') 
        
add_new_tasks()