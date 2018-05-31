class Dog:
    species='mammal'
    color='black'
    hair="long"
    def __init__(self, name, age):
        self.name=name
        self.age=age
        self.is_sent=False
    def description(self):
        return"{} is {} years old".format(self.name, self.age)
    def speak(self, sound):
        return"{} says {}".format(self.name, sound)
    def send_Email(self):
        self.is_sent=True
    

class poodle(Dog):
    species='not a dog'
    color='Pink'
    def run(self,speed):
        
        return"{} runs {}".format(self.name, speed)

if __name__=="__main__":
    d=Dog("maltise",8)
    e=Dog("german shepard",10)
    print(type(d))

    print("{0} is {1} and {2} is {3}".format(d.name,d.age,e.name,e.age))

    if d.species=="mammal":
        print("{0} is a {1}!".format(d.name, d.species))
    print(d.description())
    print(d.speak("wuff wuff"))

    print(d.is_sent)
    print(d.send_Email())
    print(d.is_sent)
    p=poodle("poo",2)
    print(p.run('fast'))
    print(p.description())
    print(isinstance(p,poodle))
    print(isinstance(p,Dog))
    print(isinstance(poodle,Dog))
    print(p.species)
    print(p.color)


