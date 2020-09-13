class Dog:
    """一次模拟小狗的简单尝试"""
    def __init__(self, name, age):
        """初始化名字和年龄属性"""
        self.name = name
        self.age = age
    
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f'{self.name} is now sitting.')

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6)
my_dog.sit()
my_dog.roll_over()
print(f"我的狗的名字是 {my_dog.name}")
print(f"我的狗 {my_dog.age} 岁了。")