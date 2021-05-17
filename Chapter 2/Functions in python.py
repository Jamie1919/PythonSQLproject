#Function 1
def hello():
    print("Hello!")

hello()

#Function 2
print("Welcome to the age in secounds program")

def user_age_in_secounds():
    user_age = int(input("Enter your age"))
    age_secounds = user_age * 365 * 24 * 60 * 60
    print(f"Your age is in secounds is {age_secounds}.")

user_age_in_secounds()

print("Goodbye")

#Function 3
friends = []


def add_friend():
    friends.append("Rolf")


add_friend()
add_friend()
add_friend()

print(friends) # [Rolf]