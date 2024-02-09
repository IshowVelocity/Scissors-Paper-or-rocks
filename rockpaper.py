import random

options={1:"rock",2:"paper",3:"scissors"}
list_options=[]
for key,value in options.items():
    list_options.append(value)
user_input=''
input_message="Pick an option between\n"
print("*Please write rock, paper or scissors with correct spelling*\n")
for index,option in options.items():
    input_message +=f"{index}) {option}\n"
input_message+= "Your choice: "

while user_input.lower() not in options.values():
    user_input=input(input_message)

print(f"You picked: {user_input}")

pc_input=random.choice(list_options)
print(f"Computer picked: {pc_input}")

if(user_input.lower()==pc_input):
    print("It's a draw.")
elif(user_input.lower()=="rock" and pc_input=="scissors"):
    print("You win")
elif(user_input.lower()=="paper" and pc_input=="rock"):
    print("You win")  
elif(user_input.lower()=="scissors" and pc_input=="paper"):
    print("You win")
else:
    print("You lost")

