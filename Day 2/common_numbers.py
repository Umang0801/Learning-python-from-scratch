list1 = input('Enter the first list of elements: ').split(',')
list2 = input('Enter the second list of elememts: ').split(',')

user_list1 =[]
for num in list1:
    user_list1.append(int(num.strip()))

user_list2 = []
for num in list2:
    user_list2.append(int(num.strip()))

common_elements = list(set(user_list1) & set(user_list2))

if common_elements:
    print(f'Common elements between the two lists: {common_elements}')
else:
    print('No common elements found between the two lists.')
