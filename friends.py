users = [
    { "id": 0, "name": "Rob" },
    { "id": 1, "name": "Matt" },
    { "id": 2, "name": "Kevin" },
    { "id": 3, "name": "Pinto" },
    { "id": 4, "name": "John" },
    { "id": 5, "name": "Steve" },
    { "id": 6, "name": "Anna" },
    { "id": 7, "name": "Peter" },
    { "id": 8, "name": "Mathew" },
    { "id": 9, "name": "Allan" }
]

#(0,1) refers that id 0 is friends with id 1 and 
# (1,2) refers id 1 is friends with id 2
friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
               (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

for user in users:
    user["friends"] = []
for i,j in friendships:
    users[i]["friends"].append(users[j]) #add i as friend of j
    users[j]["friends"].append(users[i]) #add j as friend of i

def num_of_friends(user):
    return len(user['friends'])

total_connections = sum(num_of_friends(user) for user in users)
num_of_users = len(users)
print(total_connections)
print(num_of_users)
average_connections = total_connections/num_of_users
print(average_connections)