numbers = [1, 3, 5]
doubled = [x * 2 for x in numbers]
 
#Friend list
friends = ["Rolf", "Sam", "John", "Jen", "Sarah", "Samantha"]
starts_s = [friend for friend in friends if friend.startswith("S")]

print(friends)
print(starts_s)
print("friends:", id(friends), "starts_s:", id(starts_s))

#False
print(friends is start_s)

#True
print(friends[0] is starts_s[0])
