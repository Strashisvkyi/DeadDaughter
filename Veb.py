from abc import ABC, abstractmethod


class AbstractParent(ABC):
    @abstractmethod
    def hello_friend():
        raise NotImplementedError

    def __del__(self):
        print('deleted ' + self.__class__.__name__)
        return

    def die(self):
        self.__del__()
        print("I died")

class Friend:
    pass

class Mother(AbstractParent):
    def init(self, age=0):
        self.age = age
        print('Mother constructor!')

    def do_work(self):
        print("I'm working")

    def do_housework(self):
        print("i do hoovering")

    def hello_friend(self):
        print('hello friend')


class Father(AbstractParent):
    def init(self):
        print('Father constructor!')

    def play_guitar(self):
        print('play guitar')

    def do_house_work(self):
        print("i do nothing")

class Daughter(Mother, Father):

    def init(self, age=0):
        Mother.init(self, age=age)
        Father.init(self)

    def do_work(self):
        print("I'm working like a horse!")

    def hello_friend(self):
        print("hi!!!!!!!")

    def __del__(self):
        print('deleted ' + self.__class__.__name__)
        return


def greet_mother(mother: Mother):
    print("Hello mom!!!!!!")
    mother.do_work()


def greet_father(father: Father):
    print('BEER!!!!!')
    father.play_guitar()

if __name__ == '__main__':
    daughter = Daughter()
    greet_mother(daughter)
    greet_father(daughter)
    daughter.hello_friend()

    for x in [daughter]:
        x.do_housework()

    #daughter.__class__ = Friend

    # tuple
    vasian = ('11 years', 12, 3.14, daughter)
    # set
    my_set = {23, 11, 10, 10, 'call'}
    print(my_set)
    # list
    povtorka_list = ['mathan_2', 'programming_2', 'superprise']
    print(povtorka_list)
    # frozen set
    another_set = frozenset(['let', 'it', 'go'])
    print(another_set)
    # dictionary
    my_dict = {1: "first", "2": 123, (1, 2, 3): "tuple_as_a_key"}
    print(my_dict)

    daughter.die()
    daughter.hello_friend()








