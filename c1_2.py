# Unpacking elements from iterables of Arbitrary Length
record1 = ('Dave', 'dave@example.com', '02-22-19', '289-283-3231', '898-564-9876')
name, email, dob,  *phone_num = record1
print(name, email, dob, phone_num)

record2 = ('289-283-3231', '898-564-9876', 'Dave')
*phone_num2, name2 = record2
print(*phone_num2, name2)
print(phone_num2)

