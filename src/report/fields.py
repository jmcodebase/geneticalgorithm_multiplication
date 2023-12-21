import sys
import os
sys.path.append(os.getcwd() + '/mtable/')
import individual

class Fields:
    def __init__(self, ind: individual):
        self.__times_wrong=1 if ind.Is_wrong == True else 0
        self.__avg_time=ind.Time_score
        self.__count = 1
    def __add__(self,other):
        self.Times_wrong = self.Times_wrong + other.Times_wrong
        self.Count = self.Count + other.Count
        self.Avg_time=(self.Avg_time + other.Avg_time)/(self.Count)
        return self

    @property
    def Count(self):
        return self.__count
    
    @Count.setter
    def Count(self, value):
        self.__count=value

    @property
    def Times_wrong(self)->int:
        return self.__times_wrong

    @Times_wrong.setter
    def Times_wrong(self, value: int):
        self.__times_wrong = value

    @property
    def Avg_time(self)->float:
        return self.__avg_time
    
    @Avg_time.setter
    def Avg_time(self,value: float):
        self.__avg_time=value

    def __str__(self):
        return f"Times Wrong {self.Times_wrong}, Average time: {self.Avg_time}"


    
