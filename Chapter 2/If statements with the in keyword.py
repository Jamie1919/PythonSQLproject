movies_watched = {"The Matrix", "Green Book", "Her"}
user_movie = input("Enter something you've watched recently")

if user_movie in movies_watched:
    print(f"I have watched {user_movie} too!" )
else:
    print("I haaven't watched that yet.")

#Magic number app
number = 19
user_input = input("Enter 'y' if you would like to play:").lower()

if user_input == "y":
    user_number = int(input("Guess our number:"))
    if user_number == number:
        print("You guessed correclty!")
    elif abs(number - user_number) == 1:
        print("You were off by one")
    else:
        print("Sorry, it's wrong!")