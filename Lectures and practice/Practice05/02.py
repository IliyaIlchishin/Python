# with open("text.txt", "r", encoding= 'utf_8') as file:
#     list = list(file.readline().split())
#     print(list)
#     stop_list = 'абв'
#     filtered_list =' '.join(filter(lambda x: stop_list not in x, list))
#     print ('Фильтр: ', filtered_list)

# # #         # Вывод: Привет приабев


with open('text.txt', 'r') as f:
    text = list(f.readline().split())
    print(text)
    for i in text:
        if not 'абв'in i:
            print(i)


