bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title()+", that was a great trick!")
    print("I can't wait to see your next trick, "+magician.title()+".\n")

print("Thank you, everyone. That was a great magic show!")


# range()
for value in range(5):
    print(value)
print(list(range(2, 11)))    
print(list(range(2, 11, 2)))    

squares=[]
for value in range(1, 11):
    squares.append(value ** 2)
print(squares)

# 列表解析
squares=[value**2 for value in range(1,11)]
print(squares)

print("# 练习")
print([value for value in range(1,21)])
# print([value for value in range(1,1000001)])
list1 = range(1, 1000001)
print(min(list1))
print(max(list1))
print(sum(list1))
print([value for value in range(1, 20 ,2)])
print('3到30能被3整除的数:')
print([value for value in range(3, 31 ,3)])
print('立方:')
print([value**3 for value in range(1,11)])
print('\n')
print('列表切片：')
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-2:])
print(players[-3:-1])
print('\n')
print('循环列表切片')
for player in players[:3]:
    print(player.title())


# 复制列表
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print('\n复制列表')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

print('\n练习 4-10 ~ 4-12')
print('The first three items in the list are:')
print(players[:3])
print('Three items from the middle of the list are:')
print(players[1:4])
print('The last three items in the list are:')
print(players[-3:])

# 元组(tuples)
print('\n元组：')
dimensions=(200,50)
print(dimensions[0])
print(dimensions[1])
#尝试修改元组的元素，会出错
#dimensions[1]=250
print('\n遍历元组')
for d in dimensions:
    print(d)

#修改元组变量，不会出错
dimensions=(400,100)
for d in dimensions:
    print(d)

foods=('面条','馄饨', '白菜','酸辣汤', '小笼包')
for f in foods:
    print(f)
#foods[0]='小馄饨'
foods = ('面条', '鱼', '猪肉', '酸辣汤', '小笼包')
for f in foods:
    if f == '鱼' or f=='猪肉':
        print('吃了一条鱼')
    print(f)
print('钱' in foods)
print('鱼' in foods)
