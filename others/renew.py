# def find_odd_and_ever(list):
#     odd = []
#     even = []
#     for num in list:
#         if num%2 == 0:
#             even.append(num)
#         else:
#             odd.append(num)

#     print(odd)
#     print(even)

# find_odd_and_ever([2,3,4,6,6])




word = "abccba"
length = len(word)

is_it = False
for i in range(len(word)):
    if word[i] != word[-i-1]:
        is_it = False
        break
    else:
        is_it = True

print(is_it)


