"""
Descriere: Utilizatorul poate sorta taskurile după următoarele criterii:
▪ 1: Sortare ascendentă task
▪ 2: Sortare descendentă task
▪ 3:Sortare ascendentă dată
▪ 4:Sortare descendentă dată
▪ 5:Sortare ascendentă persoană responsabilă
▪ 6: Sortare descendentă persoană responsabilă
▪ 7: Sortare ascendentă categorie
▪ 8: Sortare descendentă categorie
o Fișier implicat: taskuri.txt
o Funcționalitate: Sortare și afișare taskuri în funcție de criteriile selectate.
"""

import pandas as pd


def sort_task(file, sort_type):
    df = pd.read_csv(file)
    if sort_type == 1:
        sdf = df.sort_values(by=['name'])
    elif sort_type == 2:
        sdf = df.sort_values(by=['name'], ascending=False)
    elif sort_type == 3:
        df['max_date'] = pd.to_datetime(df['max_date'], format='%d.%m.%Y %H:%M', errors='coerce')
        sdf = df.sort_values(by=['max_date'])
    elif sort_type == 4:
        df['max_date'] = pd.to_datetime(df['max_date'], format='%d.%m.%Y %H:%M', errors='coerce')
        sdf = df.sort_values(by=['max_date'], ascending=False)
    elif sort_type == 5:
        sdf = df.sort_values(by=['assignee'])
    elif sort_type == 6:
        sdf = df.sort_values(by=['assignee'], ascending=False)
    elif sort_type == 7:
        sdf = df.sort_values(by=['category'])
    elif sort_type == 8:
        sdf = df.sort_values(by=['category'], ascending=False)
    return sdf


print(sort_task("taskuri.csv", 4))
