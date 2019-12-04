import pytest
from abc import ABC
from collections import deque


class Animal(ABC):
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return self.noise


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.noise = "woof!"


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.noise = "weow"


class AnimalQueue:
    """
    A data structure for queueing two types of animals. It is strictly FIFO, and has
    the ability to choose which type of animal is wanted.
    """
    def __init__(self):
        self.counter = 0
        self.dog_queue = deque()
        self.cat_queue = deque()

    def enqueue(self, animal):
        if isinstance(animal, Dog):
            self.dog_queue.appendleft((animal, self.counter))
            self.counter += 1
        elif isinstance(animal, Cat):
            self.cat_queue.appendleft((animal, self.counter))
            self.counter += 1
        else:
            raise TypeError("Unknown animal")

    def dequeue_any(self):
        if not self.dog_queue:
            return self.dequeue_cat()

        if not self.cat_queue:
            return self.dequeue_dog()

        if self.dog_queue[-1][1] < self.cat_queue[-1][1]:
            return self.dequeue_dog()
        else:
            return self.dequeue_cat()

    def dequeue_cat(self):
        return self.cat_queue.pop()[0]

    def dequeue_dog(self):
        return self.dog_queue.pop()[0]


def test_animalshelter():
    queue = AnimalQueue()
    queue.enqueue(Cat("Fluffy"))
    queue.enqueue(Dog("Fido"))
    queue.enqueue(Dog("Rex"))
    queue.enqueue(Cat("Tinkerbell"))
    queue.enqueue(Dog("Snoopy"))
    queue.enqueue(Cat("Garfield"))

    animal = queue.dequeue_any()
    assert isinstance(animal, Cat)
    assert animal.name == "Fluffy"

    animal = queue.dequeue_any()
    assert isinstance(animal, Dog)
    assert animal.name == "Fido"

    animal = queue.dequeue_cat()
    assert isinstance(animal, Cat)
    assert animal.name == "Tinkerbell"

    queue.enqueue(Dog("Superdog"))

    animal = queue.dequeue_any()
    assert isinstance(animal, Dog)
    assert animal.name == "Rex"

    animal = queue.dequeue_dog()
    assert isinstance(animal, Dog)
    assert animal.name == "Snoopy"

    animal = queue.dequeue_any()
    assert isinstance(animal, Cat)
    assert animal.name == "Garfield"

    with pytest.raises(IndexError):
        queue.dequeue_cat()

    animal = queue.dequeue_any()
    assert isinstance(animal, Dog)
    assert animal.name == "Superdog"
    assert animal.make_sound() == "woof!"

    with pytest.raises(IndexError):
        queue.dequeue_any()


if __name__ == '__main__':
    pytest.main(args=[__file__])
