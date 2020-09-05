# 大小写相关函数
name="ada lovelace"
print('# 大小写相关函数')
print(name.title())
print(name.upper())
print(name.lower())
print("\n")

# 在字符串中使用变量
# f字符串是 python 3.6引入的，3.5或更早版本需要使用format()方法
first_name="ada"
last_name="lovelace"
full_name=f"{first_name} {last_name}"
print('# 在字符串中使用变量')
print(full_name)
print(f"Hello, {full_name.title()}!")
# format
print("{} {}".format(first_name, last_name))
print("\n")

# 制表符和换行符
print('# 制表符和换行符')
print('Languages:\n\tPython\n\tC\n\tJavascript')

# 删除空白
print('# 删除空白')
fav_lang="python "
fav_lang=fav_lang.rstrip()
print(fav_lang)

# 练习 2-3
print('# 练习 2-3')
person_name="Eric"
print(f"Hello {person_name}, would you like to learn some Python today?")

#练习2-5
print('#练习2-5')
print('Albert Einstein once said, "A person who never made a mistake never tried anything new."')

#练习2-6
print('#练习2-6')
famous_person="Albert Einstein"
message=f'{famous_person} once said, "A person who never made a mistake never tried anything new."'
print(message)

#练习2-7
print('#练习2-7')
person_name="\n\t  Michael Lu  \t\n"
print(person_name)
print(person_name.lstrip())
print(person_name.rstrip())
print(person_name.strip())