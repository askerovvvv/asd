import csv
from abc import ABC, abstractmethod

class AddGet:
    def add(self, new_element):
        raise NotImplementedError()

    def get(self):
        raise NotImplementedError()


class CrudService(AddGet):
    def remove(self, element):
        raise NotImplementedError()

    def get_by_id(self, id):
        raise NotImplementedError()

class SaveService(CrudService):
    def save(self):
        raise NotImplementedError()


class Group(CrudService):
    group_list = ['MAR-20', 'Sca-20', 'Des-20']
    
    @classmethod
    def add(cls, new_group):
        cls.group_list.append(new_group)

    @classmethod
    def get(cls):
        return cls.group_list

    @classmethod
    def remove(cls, element):
        cls.group_list.remove(element)

    @classmethod
    def get_by_id(cls, id):
        return cls.group_list[id]

aco = Group()
aco.add('Aco-20')
csc = Group()
csc.add('Csc-20')

print(csc.get())


class Student(Group, AddGet):
    def __init__(self, name, age, gender):
        super().__init__()
        Student.student_groups = {}
        self.name = name
        self.age = age
        self.gender = gender

    def add(self, group,):
        if not group in self.group_list:
            raise Exception('No such group exists!')
        Student.student_groups[group] = self.name
    
    @classmethod
    def get(cls):
        return cls.student_groups


std1 = Student('Tom', 18, 'male')
std2 = Student('Gerald', 18, 'male')
std3 = Student('John', 19, 'female')
std4 = Student('Kane', 19, 'female')

std1.add('Sca-20')
std2.add('Des-20')
std3.add('MAR-20')

print(std2.get())


class Save(SaveService):
    def save(self, data, group):
        with open("data.csv", "a") as file:
            writer = csv.writer(file, delimiter=",")
            writer.writerow((data[group])) 

saver = Save()
saver.save(Student.get(), 'Sca-20')

class Specification:
    def is_satisfied(self, student):
        pass

class Filter:
    def filter(self, students, spec):
        pass

class AgeSpecification(Specification):
    def __init__(self, age):
        self.age = age
    
    def is_satisfied(self, student):
        return student.age == self.age
        
class GenderSpecification(Specification):
    def __init__(self, gender):
        self.gender = gender
    
    def is_satisfied(self, student):
        return student.gender == self.gender

class FilterStudent(Filter):
    def filter(self, students, spec):
        for student in students:
            if spec.is_satisfied(student):
                yield student
        
# std1 = Student('Tom', 18, 'male')
# std2 = Student('Gerald', 18, 'male')
# std3 = Student('John', 19, 'female')
# students = [std1, std2, std3]

# male = GenderSpecification('male')
# fs = FilterStudent()
# for p in fs.filter(students, male):
#     print(p.name)

