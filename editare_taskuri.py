import pandas as pd
  #  editare taskuri
"""
df = pd.read_csv('taskuri.csv')
print(df)
"""

def edit_task(file_name):
    # Citim taskurile din fișierul CSV
    tasks_df = pd.read_csv(file_name)

    # Cerem utilizatorului să introducă ID-ul taskului pe care dorește să îl editeze
    value_to_edit = int(input('Id-ul task-ului de editat: '))

    # Găsim taskul cu ID-ul respectiv
    row_to_edit = tasks_df[tasks_df['id'] == value_to_edit]

    if row_to_edit.empty:
        print(f"\n*******************\nNu există task-ul cu id-ul introdus! \n*******************\n")
    else:
        print(
            f"\n********************************\nTask-ul pe care vrei să îl editezi este: \n{row_to_edit} \n********************************\n")

        # Afișăm meniul pentru editare și oferim opțiunea de a edita câmpurile
        print("Ce câmp dorești să editezi?")
        print("1. Nume task")
        print("2. Dată limită")
        print("3. Persoană responsabilă")
        print("4. Categorie")
        print("5. Ieșire fără modificări")

        optiune = input("Alege o opțiune (1-5): ")

        if optiune == "1":
            # Edităm numele taskului
            new_name = input("Introdu noul nume pentru task: ")
            tasks_df.loc[tasks_df['id'] == value_to_edit, 'name'] = new_name.strip()
            print(f'Numele taskului a fost schimbat în: "{new_name}".')

        elif optiune == "2":
            # Edităm data limită
            new_deadline = input("Introdu noua dată limită (format: dd.mm.yyyy hh:mm): ")
            try:
                new_deadline_dt = dt.datetime.strptime(new_deadline, "%d.%m.%Y %H:%M")
                tasks_df.loc[tasks_df['id'] == value_to_edit, 'max_date'] = new_deadline_dt.strftime('%d.%m.%Y %H:%M')
                print(f'Data limită a fost schimbată în: "{new_deadline}".')
            except ValueError:
                print("Formatul datei este incorect. Modificarea a fost anulată.")

        elif optiune == "3":
            # Edităm persoana responsabilă
            new_assignee = input("Introdu noua persoană responsabilă: ")
            tasks_df.loc[tasks_df['id'] == value_to_edit, 'assignee'] = new_assignee.strip()
            print(f'Persoana responsabilă a fost schimbată în: "{new_assignee}".')

        elif optiune == "4":
            # Edităm categoria
            new_category = input("Introdu noua categorie: ")
            if category_exists(new_category):  # Verificăm dacă există categoria
                tasks_df.loc[tasks_df['id'] == value_to_edit, 'category'] = new_category.strip()
                print(f'Categoria a fost schimbată în: "{new_category}".')
            else:
                print("Categoria introdusă nu există. Modificarea a fost anulată.")

        elif optiune == "5":
            print("Ieșire fără modificări.")
            return

        # Salvăm modificările în fișierul CSV
        tasks_df.to_csv(file_name, index=False)
        print(f'Task-ul cu id-ul {value_to_edit} a fost actualizat.')
