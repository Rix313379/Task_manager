import pandas as pd

def remove_task(file_name):
    tasks_df = pd.read_csv(file_name)
    value_to_remove = int(input('Id-ul task-ului de sters: '))
    row_to_remove = tasks_df[tasks_df['id'] == value_to_remove]

    if row_to_remove.empty:
        print(
            f"\n*******************\nTask-ul introdus nu exista! \n*******************\n")
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


tasks_file = 'taskuri.csv'
remove_task(tasks_file)
