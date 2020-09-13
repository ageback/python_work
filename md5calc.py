import hashlib

def get_md5(str):
    m = hashlib.md5()
    m.update(str)
    return m.hexdigest()



calc_md5_flag = True
while calc_md5_flag:
    userInput = input("请输入要计算MD5值的字符串：")
    print(get_md5(userInput.encode("utf-8")))
    print(get_md5(userInput.encode("utf-8")).upper())
    repeat = input("您想继续计算下一个字符串的md5值吗？(y/n)")
    if repeat == 'n' or repeat == 'no':
        calc_md5_flag = False