categorie_noua = input("Introduceti o categorie noua:\n")

with open('categorii.csv', newline='') as file_obj:
    categories_list = file_obj.read()

if categorie_noua in categories_list:
    print("Eroare exista deja aceasta categorie")
else:
    with open('categorii.csv', 'a', newline='') as file_obj:
        file_obj.write(categorie_noua + '\n')





   



















