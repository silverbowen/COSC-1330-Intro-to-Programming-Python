# Student class holds: name, student ID #, GPA, expected grade for course, and full/part-time

class Student:
    
    # __init__  accepts arguments for all five attributes
    # and assigns them to an instance of the student object
    def __init__(self, name, ID, GPA, grade,  time):
        self.__name = name
        self.__ID = ID
        self.__GPA = GPA
        self.__grade = grade
        self.__time = time
        
    # set_name accepts an argument for the student's name
    def set_name(self, name):
        self.__name = name

    # set_ID accepts an argument for the student's ID
    def set_ID(self, ID):
        self.__ID = ID

    # set_GPA accepts an argument for the student's GPA
    def set_GPA(self, GPA):
        self.__GPA = GPA

    # set_grade accepts an argument for the student's grade
    def set_grade(self, grade):
        self.__grade = grade

    # set_time accepts an argument for the student's time
    def set_time(self, time):
        self.__time = time

    # get_name returns the student's name
    def get_name(self):
        return self.__name

    # get_ID returns the student's ID
    def get_ID(self):
        return self.__ID

    # get_GPA returns the student's GPA
    def get_GPA(self):
        return self.__GPA

    # get_grade returns the student's grade
    def get_grade(self):
        return self.__grade

    # get_time returns the student's time
    def get_time(self):
        return self.__time
