lst = ["Apple, Banana, Cherry, Date, Blueberry"]
print("Length of list:", len(lst))
print('First Element:', lst[0])
print('Last Element:', lst[-1])

lst.append("Elderberry")
print('Updated list:',lst)
lst.remove('Banana')
print('List after removing Banana:', lst)
lst.sort()
print('Sorted list:', lst)
lst.pop(1)
print('List after popping index 1:', lst)
lst=lst[:4]
print('List after slicing to first 4 elements:', lst)
lst.clear()
print('List after clearing all elements:', lst)