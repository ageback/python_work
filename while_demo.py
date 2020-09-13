current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
message = ""
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")


# 用字典存储用户输入
responses = {}
polling_active = True
while polling_active:
    name = input("\n您的姓名 ？")
    response = input("您想爬哪座山？")
    responses[name] = response

    repeat = input("您想让另一个人回答吗？(yes/ no)")
    if repeat == 'no':
        polling_active = False
    
    print('\n--- 投票结果 ---')
    for name, response in responses.items():
        print(f"{name} 想爬 {response}。")