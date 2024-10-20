# filtrare_task-uri
import pandas as pd
import numpy as np
import datetime as dt


def main():
    filtring_option = input('Alegeti o filtrare: ')
    print(f"\n********************************\nRESULT: \n{filter_tasks(filtring_option)} \n********************************\n")

def filter_tasks(opt):
    filter_by = {1: 'name', 2: 'max_date', 3: 'assignee', 4: 'category'}
    opt = int(opt)
    selected_col = filter_by[opt]

    tasks_df = pd.read_csv('taskuri.csv')

    # DELETE on merge
    print(tasks_df)
    print('================================')
    # /
    tasks_df_filtered = None

    if opt == 2:
        tasks_df_filtered = filter_datetype_data(selected_col, tasks_df)
    else:
        tasks_df_filtered = filter_texttype_data(selected_col, tasks_df)

    # DELETE on merge
    # convert the data in the selected column to date type
    # tasks_df['max_date'] = pd.to_datetime(tasks_df['max_date'], errors='coerce')

    # get the column name based on column index
    # col_name = tasks_df.columns[opt]
    # /

    return tasks_df_filtered

def filter_texttype_data(col_name, data):
    searched_term = input('Introdu termenul cautat: ')
    return data[data[col_name].str.contains(searched_term, case=False)]

def filter_datetype_data(col_name, data):
    from_date = input('De la data (apasa enter daca nu vrei sa setezi nici o data de inceput): ')
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
    print('================================')

    # return the filtered result between the given dates
    return data[(data[col_name] >= from_date_64) & (data[col_name] <= to_date_64)]

main()