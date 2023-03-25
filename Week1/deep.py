#Getting input from the user
question = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower()

#Comparing answers to get yes
if question.strip() == "42":
    print("Yes")
elif question.lower().strip() == "forty-two":
    print("Yes")
elif question.lower().strip() == "forty two":
    print("Yes")

#Comparing answers for the no
else:
    print("No")