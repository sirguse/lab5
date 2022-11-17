int_numbers = [10, 20, 33]

str_numbers = ["ten", "twenty", "thirty"]

dictionary = dict(zip(str_numbers, int_numbers))

print(dictionary)


dict_1 = {}

for i in range(len(int_numbers)):
    dict_1[str_numbers[i]] = int_numbers[i]
print(dict_1)



dict_2 = dict(thirty=30, fourty= 40, fifty= 50)
dict_3 = dict_1.copy()
dict_3.update(dict_2)
print(dict_3)
