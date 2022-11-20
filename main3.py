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
    group_ = []
    
    def __init__(self):
        self.group_list = {}
        
    
    def add(self, new_group, faculty):
        self.group_list = {'Group': new_group, 'faculty': faculty}
        Group.group_.append(self.group_list)

    
    def get(self):
        return self.group_list

    @classmethod
    def remove(cls, id):
        cls.group_.pop(id)

    @classmethod
    def get_by_id(cls, id):
        return cls.group_[id]
        


class ITGroup(Group):
    def __init__(self):
        self.group_list = {}


class Student(AddGet):
    def __init__(self, name, age, gender):
        Student.student_groups = {}
        self.name = name
        self.age = age
        self.gender = gender

    def add(self, group,):
        for i in Group.group_:
            if group in i.values():
                Student.student_groups[group] = self.name
    
            # else:
            #     raise Exception('No such group exists!', group)
    
    @classmethod
    def get(cls):
        return cls.student_groups


class Save(SaveService):
    def save(self, data, group):
        with open("data.csv", "a") as file:
            writer = csv.writer(file, delimiter=",")
            writer.writerow((data[group])) 


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
        

def controller():
    aco = Group()
    csc = Group()
    it = ITGroup()

    it.add('Sca-20', 'IT')
    aco.add('Aco-20', 'economy')
    csc.add('Csc-20', 'IT')
    csc.remove(1)

    print(csc.get_by_id(0))
    print(it.get())
    print(Group.group_)


    std1 = Student('Tom', 18, 'male')
    std2 = Student('Gerald', 18, 'male')
    std3 = Student('John', 19, 'female')
    std4 = Student('Kane', 19, 'female')

    std1.add('Sca-20')
    std2.add('Aco-20')
    std3.add('MAR-20')
    students = [std1, std2, std3]
    print(Student.get())

    saver = Save()
    saver.save(Student.get(), 'Sca-20')

    male = GenderSpecification('male')
    fs = FilterStudent()
    for p in fs.filter(students, male):
        print(p.name)

controller()

