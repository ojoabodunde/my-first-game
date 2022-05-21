print ("hello world!")
print("you are welcome to my first game!!")
name = input("what is your name ")
age = input("what is your age ")
print ("Hello", name, "you are", age, "years old")
if age >= '18':
    print("you are old enough to play!")

    if age <= '18':
        print("you are not old enough to play!")

    health = 10
    print("you are starting with", health, "health")

    want_to_play = input("do you want to play? ").lower()
    if want_to_play == "yes":
        print("lets play! ")

    else:
        print('have a nice day')

        print("you are starting with", health, "health")


    left_or_right = input("first choice...left or right (left/right)? ")
    if left_or_right == "left":
        ans = input("Nice, you follow a path and reach a lake... do you swim across or go around (across/around)? ")

    if left_or_right == "right":
        ans = input("sorry you lost")

    if ans == "around":
        print("you went around and reached the other side of the lake")

    elif ans == "across":
        print("you managed to get across and got bit by a shark and lost 5 health.")
        health -= 5

    ans = input("you noticed a house and a river, which do you go to (river/house)? ")
    if ans == "house":
        print("got to the house and greet the owner. After greeting him, he hit you so hard and you lose 5 health")
    health -= 5

    if health <= 0:
        print("you now have 0 health and you lost the game...")
    else:
        print("you have survived...")
        print("Wow congratulations, you win ")



else:
    print("you are not old enough to play...")
    print('you would need a supervision to play...')



'''
this for you to just take note for the different types of data
string "hello" "hi" "ojo"
integer 8.-8,54,-1
float 2.4,-5.0,7.4
bool True, False
not when you enter right theres an error fix it
'''



