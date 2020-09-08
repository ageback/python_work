alien_0 = {'color':'green', 'points':5}
print(alien_0.get('color2', '无颜色'))
print(alien_0['points'])
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# 循环
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
for key, value in user_0.items():
    print(f'\nKey: {key}')
    print(f'Value: {value}')

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        language = favorite_languages[name].title()
        print(f'\t{name.title()}, I see you love {language}')
    if 'erin' not in favorite_languages.keys():
        print('Erin, please take our poll!')

# 字典排序
for name in sorted(favorite_languages.keys()):
    print(f'\n{name.title()}, thank you for taking th poll.')

# 循环值，不排除重复项
for language in favorite_languages.values():
    print(language.title())
# 循环值，排除重复项
for language in set(favorite_languages.values()):
    print(language.title())

# 定义一个set
languages = {'python', 'ruby', 'python', 'c'}
print(languages)