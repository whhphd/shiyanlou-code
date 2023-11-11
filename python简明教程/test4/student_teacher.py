#!/usr/bin/env python3
from collections import Counter
import sys


class Person(object):
    """
    返回具有给定名称的 Person 对象
    """

    def __init__(self, name):
        self.name = name

    def get_details(self):
        """
        返回包含人名的字符串
        """
        return self.name

    def get_grade(self):
        return None


class Student(Person):
    """
    返回 Student 对象，采用 name, branch, year 3 个参数
    """

    def __init__(self, name, branch, year, grade):
        Person.__init__(self, name)
        self.branch = branch
        self.year = year
        self.grade = grade

    def get_details(self):
        """
        返回包含学生具体信息的字符串
        """
        return "{} studies {} and is in {} year.".format(self.name, self.branch, self.year)

    def get_grade(self):
        fail_count = str(self.grade).count('D')
        pass_count = len(self.grade) - fail_count
        print('Pass: {}, Fail: {}'.format(pass_count, fail_count))


class Professor(Person):
    """
    返回 Professor 对象，采用 name, papers 2 个参数
    """

    def __init__(self, name, papers, grade):
        Person.__init__(self, name)
        self.papers = papers
        self.grade = grade

    def get_details(self):
        """
        返回包含教授具体信息的字符串
        """
        return "{} teaches {}".format(self.name, ','.join(self.papers))


class Teacher(Person):
    """
    返回 Teacher 对象，采用字符串列表作为参数
    """

    def __init__(self, name, papers, grade):
        Person.__init__(self, name)
        self.papers = papers
        self.grade = grade

    def get_details(self):
        return "{} teaches {}".format(self.name, ','.join(self.papers))

    def get_grade(self):
        res = []
        for i, j in Counter(self.grade).most_common():
            res.append("{}: {}".format(i, j))
        print(",".join(res))


# person1 = Person('Sachin')
if sys.argv[1] == 'teacher':
    teacher1 = Teacher('Prashad', ['C', 'C++'], sys.argv[2])
    teacher1.get_grade()
else:
    student1 = Student('Kushal', 'CSE', 2005, sys.argv[2])
    student1.get_grade()

# print(person1.get_details())
# print(student1.get_details())
# print(teacher1.get_details())
