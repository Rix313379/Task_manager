import pandas as pd
import numpy as np
import datetime as dt

def afisare_meniu():
    print("\n--- Meniu Principal ---")
    print("1. Adăugare categorii")
    print("2. Listare taskuri")
    print("3. Sortare taskuri")
    print("4. Filtrare taskuri")
    print("5. Adăugare task nou")
    print("6. Editare task")
    print("7. Ștergere task")
    print("8. Ieșire")


def afisare_meniu_sortare():
    print("\n--- Sortare Taskuri ---")
    print("1. Sortare ascendentă după task")
    print("2. Sortare descendentă după task")
    print("3. Sortare ascendentă după dată")
    print("4. Sortare descendentă după dată")
    print("5. Sortare ascendentă după persoana responsabilă")
    print("6. Sortare descendentă după persoana responsabilă")
    print("7. Sortare ascendentă după categorie")
    print("8. Sortare descendentă după categorie")


def afisare_meniu_filtrare():
    print("\n--- Filtrare Taskuri ---")
    print("1. Filtrare după task")
    print("2. Filtrare după dată")
    print("3. Filtrare după persoana responsabilă")
    print("4. Filtrare după categorie")

# ##### 1. Adaugare categorii ####################################################
def adaugare_categorii():
    categorie_noua = input("\nIntroduceti o categorie noua:\n")

    with open('categorii.csv', newline='') as file_obj:
        categories_list = file_obj.read()
        print(categories_list.lower())

    if categorie_noua.lower() in categories_list.lower():
        print(
            f"\n********************************\nExista deja aceasta categorie \n********************************\n")
    else:
        with open('categorii.csv', 'a', newline='') as file_obj:
            file_obj.write(categorie_noua.lower() + '\n')

# ###### 2. Listare task-uri ####################################################
def listare_taskuri(file):
    try:
        df = pd.read_csv(file)
        df_sorted = df.sort_values(by='category')
        print(
            f"\n********************************\n{df_sorted} \n********************************\n")
    except Exception as e:
        print(f"An error has occurred: {e}")

# ###### 4. Filtrare task-uri ####################################################
def filter_tasks(opt: int, file_name):
    tasks_df = pd.read_csv(file_name, index_col=False)

    selected_col = tasks_df.columns[opt]
    date_cols = get_datetype_columns(tasks_df)
    tasks_df_filtered = (
        filter_datetype_data(selected_col, tasks_df)
        if selected_col in date_cols
        else filter_texttype_data(selected_col, tasks_df)
    )

    return (
        "Nu s-a gasit nici un rezultat"
        if tasks_df_filtered.empty
        else tasks_df_filtered
    )


def get_datetype_columns(data):
    headers = data.columns.tolist()
    date_cols = []

    for col in headers:
        if pd.to_datetime(data[col], format="%Y-%m-%d", errors='coerce').notna().any():
            date_cols.append(col)

    return date_cols


def filter_texttype_data(col_name, data):
    searched_term = input('\nIntrodu termenul cautat: ')
    return data[data[col_name].str.contains(searched_term, case=False)]


def filter_datetype_data(col_name, data):
    from_date = input('\nDe la data (apasa enter daca nu vrei sa setezi nici o data de inceput): ')
    to_date = input('Pana la data (apasa enter daca nu vrei sa setezi nici o data de sfarsit): ')

    # set the default date in case the from and to date are not provided
    if from_date == '':
        from_date = '1900-01-01'

    if to_date == '':
        to_date = dt.datetime.today()

    # convert the dates in format necessary for DataFrame operations
    from_date_64 = np.datetime64(from_date)
    to_date_64 = np.datetime64(to_date)

    # convert the data in the selected column to date type
    data[col_name] = pd.to_datetime(data[col_name], errors='coerce')

    # return the filtered result between the given dates
    return data[(data[col_name] >= from_date_64) & (data[col_name] <= to_date_64)]


# ###### 7. Stergere task-uri ####################################################
def remove_task(file_name):
    tasks_df = pd.read_csv(file_name)
    value_to_remove = int(input('Id-ul task-ului de sters: '))
    row_to_remove = tasks_df[tasks_df['id'] == value_to_remove]

    if row_to_remove.empty:
        print(
            f"\n*******************\nNu exista task-ul cu id-ul introdus! \n*******************\n")
    else:
        print(
            f"\n********************************\nTask-ul pe care vrei sa il stergi este: \n{row_to_remove} \n********************************\n")
        delete_agreed = confirm_delete()

        if delete_agreed:
            tasks_df_updated = tasks_df[tasks_df['id'] != value_to_remove]
            tasks_df_updated.to_csv(file_name, index=False)
            print(f'Task-ul cu id-ul {value_to_remove} a fost sters.')


def confirm_delete():
    while True:
        confirmation = input('Confirma stergerea acestui task (y/n): ')

        if confirmation.upper() == 'Y':
            return True

        if confirmation.upper() == 'N':
            return False


# ##### Main ####################################################
def main():
    tasks_file = 'taskuri.csv'
    while True:
        afisare_meniu()
        optiune = input("Alegeți o opțiune (1-8): ")

        if optiune == "1":
            # Adăugare categorii
            adaugare_categorii()
        elif optiune == "2":
            # Listare taskuri
            print("Listarea taskurilor...")
            # Aici se va apela o funcție de listare a taskurilor
            listare_taskuri(tasks_file)
        elif optiune == "3":
            afisare_meniu_sortare()
            opt_sortare = input("Alegeți o opțiune de sortare (1-8): ")
            # Apelați funcțiile de sortare pe baza opțiunii
        elif optiune == "4":
            afisare_meniu_filtrare()
            opt_filtrare = input("Alegeți o opțiune de filtrare (1-4): ")
            # Apelați funcțiile de filtrare pe baza opțiunii

            rezultat_filtrare = filter_tasks(int(opt_filtrare), tasks_file)
            print(
                f"\n********************************\nRESULT: \n{rezultat_filtrare} \n********************************\n")

        elif optiune == "5":
            # Adăugare task nou
            print("Adăugare task nou...")
            # Aici se va apela o funcție de adăugare task
        elif optiune == "6":
            # Editare task
            print("Editare task...")
            # Aici se va apela o funcție de editare task
        elif optiune == "7":
            # Ștergere task
            # Aici se va apela o funcție de ștergere task
            remove_task(tasks_file)
        elif optiune == "8":
            print("Ieșire din program.")
            break
        else:
            print("Opțiune invalidă, vă rugăm să alegeți din nou.")


main()