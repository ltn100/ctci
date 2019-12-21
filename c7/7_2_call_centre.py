import pytest
from queue import PriorityQueue


class Employee:
    def __init__(self):
        self.priority = -1
        self.title = "Employee"
        self.call = None
        self.queue = None

    def start_call(self, call, queue=None):
        self.call = call
        self.queue = queue
        return "{} starting call {}".format(self.title, self.call)

    def end_call(self):
        if self.queue:
            self.queue.put(self)
            self.call = None
        self.queue = None

    def __lt__(self, other):
        """
        For PriorityQueue comparison
        """
        return self.priority < other.priority


class Respondent(Employee):
    def __init__(self):
        super().__init__()
        self.priority = 1
        self.title = "Respondent"


class Manager(Employee):
    def __init__(self):
        super().__init__()
        self.priority = 2
        self.title = "Manager"


class Director(Employee):
    def __init__(self):
        super().__init__()
        self.priority = 3
        self.title = "Director"


class CallCentre:
    def __init__(self, num_respondends=0, num_managers=0, num_directors=0):
        self.employees = PriorityQueue()

        for _ in range(num_respondends):
            self.employees.put(Respondent())

        for _ in range(num_managers):
            self.employees.put(Manager())

        for _ in range(num_directors):
            self.employees.put(Director())

    def dispatch_call(self, call):
        employee = self.employees.get()
        response = employee.start_call(call, self.employees)
        return response, employee


def test_solution():
    cs = CallCentre(2, 2, 2)
    r, e1 = cs.dispatch_call(1)
    assert r == "Respondent starting call 1"
    r, e2 = cs.dispatch_call(2)
    assert r == "Respondent starting call 2"
    r, e3 = cs.dispatch_call(3)
    assert r == "Manager starting call 3"
    e2.end_call()
    r, e4 = cs.dispatch_call(4)
    assert r == "Respondent starting call 4"
    r, e5 = cs.dispatch_call(5)
    assert r == "Manager starting call 5"
    r, e6 = cs.dispatch_call(6)
    assert r == "Director starting call 6"
    e4.end_call()
    r, e7 = cs.dispatch_call(7)
    assert r == "Respondent starting call 7"


if __name__ == '__main__':
    pytest.main(args=[__file__])
