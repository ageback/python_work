print('输入两个数，用来做除法。')
print('输入 "q" 退出程序。')

while True:
    first_number = input("\n第一个数：")
    if first_number == 'q':
        break
    second_number = input("\n第二个数：")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print('0 不能作为被除数！')
    else:
        print(answer)