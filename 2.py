# Дан список, вывести отдельно буквы и цифры, пользуясь filter.
# [12,'sadf',5643] ---> ['sadf'] ,[12,5643]

new_list = [12,'sadf',5643]
list2 = []
list2.append(list(filter(lambda x: type(x) == int, new_list)))
list2.append(list(filter(lambda x: type(x) == str, new_list)))
print('Числа в списке:', *list2[0], '\nСтроки в списке:', *list2[1])