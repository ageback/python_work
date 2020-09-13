filename = 'text_files/pi_million_digits.txt'
# 一次性读取文件
# with open(filename) as file_object:
#     contents = file_object.read()
# print(contents)
# print('\n')

# 逐行读取文件，
# with open(filename) as file_object:
#     for line in file_object:
#         print("@@@"+line)
    
# 保存到列表中
with open(filename) as file_object:
    lines = file_object.readlines()
pi_str = ''    
for line in lines:
    pi_str += line.rstrip()
# print(pi_str)
# print(len(pi_str))

birthday=input('输入你的生日，格式为 mmddyy: ')
if birthday in pi_str:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")