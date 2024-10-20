#  Listare taskuri
# o Descriere: Taskurile existente sunt listate. Sortarea implicită este după
# categorie.
# o Fișier implicat: taskuri.txt (care conține: task, dată limită, persoană
# responsabilă, categorie)
# o Funcționalitate: Citirea și afișarea taskurilor din fișier.

import pandas as pd

def listing(file):
     try:
        df = pd.read_csv(file)
        df_sorted = df.sort_values(by='categorie')
        print("\n--- List Tasks ---")
        print(df_sorted)
     except Exception as e:
        print(f"An error has occurred: {e}")

# ----Testing----
name_file='file.csv'
listing(name_file)

