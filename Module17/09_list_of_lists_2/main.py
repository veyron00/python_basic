nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]


list1 = [unpacking_3 for unpacking_1 in nice_list
         for unpacking_2 in unpacking_1
         for unpacking_3 in unpacking_2
]


print(list1)
