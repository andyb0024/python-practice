class Name:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def my_name(self):
        print("bonjour ",self.name, "your age is ", self.age)
new_name=Name("andy",500)
Name.my_name(new_name)
# new_name.my_name()

# class Second:
#     x=new_name.name
#     print(x)
