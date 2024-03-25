class Animal:
    id = 0

    @classmethod
    def create(cls,  name, age):
        cls.id += 1
        return cls(name, age)

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("ИД", self.id)
        print("Имя", self.name)
        print("Возраст", self.age)


class Worker:
    count = 0

    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
        Worker.count += 1

    def display(self):
        print("Worker:")
        print("{} {}".format(self.name,self.surname))


w1 = Worker("Ivan", "Ivanov")
print("w1.count: ", w1.count)
w2 = Worker("Alexei", "Petrov")
print("w2.count: ", w2.count)
print("w1.count: ", w1.count)
print("Worker.count: {0} \n".format(Worker.count))
print("Worker.__name__: ", Worker.__name__)
print("Worker.__dict__: ", Worker.__dict__)
print("Worker.__doc__: ", Worker.__doc__)
print("Worker.__bases__: ", Worker.__bases__)

animal1 = Animal.create("Иван", 10)
animal2 = Animal.create("Иннокентий", 20)
animal3 = Animal.create("Афанасий", 30)

print(animal1.display())
print(animal2.display())
print(animal3.display())