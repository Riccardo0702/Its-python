def remove_duplicates(list1) -> list:
    list2 = []
    for i in list1:
        if i not in list2:
            list2.append(i)
    return list2

print(remove_duplicates([1, 2, 3, 2]))