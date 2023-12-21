from random import randrange, shuffle, seed
from .individual import *
import time
import sys
import os
sys.path.append(os.getcwd() + '/../report/')
import report.report as r

class Mtable:
    def __init__(self):
        
        #Random number Range        
        self.__min=1
        self.__max=13
        
        #Iteration range
        self.__size = 10
        
        self.__crossover_rate = 9
        self.__list_of_individuals=self.__generate_individuals(self.__size)
        self.__results_rep = r.Report()

    @property
    def Report(self)->r.Report:
        return self.__results_rep
    
    @Report.setter
    def Report(self, value: r.Report):
        self.__results_rep = value

    @property
    def List_of_individuals(self)->list[Individual]:
        return self.__list_of_individuals
    
    @List_of_individuals.setter
    def List_of_individuals(self, value: list[Individual]):
        self.__list_of_individuals = value

    @property
    def Size(self)->int:
        return self.__size
    
    @Size.setter
    def Size(self,value: int):
        self.__size=value

    def __generate_individuals(self, size: int):
        ret=[]
        sd = int((time.time() % 1)) * 1000
        seed(sd)
        for x in range(size):
            y = Individual(randrange(self.__min,self.__max),randrange(self.__min,self.__max))
            ret.append(y)
        return ret
    
    def print_mult(one:int,two:int):
        print(f'{one} * {two}')

    def process(self, iterations: int):
        for i in range(iterations):
            print(f'    generation:{i}')

            self.process_generation()
            print([str(x) for x in self.List_of_individuals])
            # mate

            print("begin mate")
            list_of_individuals = list(set(sorted(filter(lambda x: x.get_score()>2, self.List_of_individuals),key=lambda y: y.get_score(), reverse=True)[:6]))
            list_of_children = []
            last = len(list_of_individuals)
            wrong=len([x for x in self.List_of_individuals if x.Is_wrong is True])
            print(f'you got {wrong} wrong, carrying over {len(list_of_individuals)}')

            for i,v in enumerate(list_of_individuals):
                index_copy=i
                if (i == last-1):
                    index_copy=0
                new_individuals = v.mate(list_of_individuals[index_copy],self.__crossover_rate)
                c1,c2 = new_individuals
                list_of_children.append(c1)
                list_of_children.append(c2)

            self.List_of_individuals = list_of_children[:10]

            print("begin fill")

            # fill with randomly generated individuals
            if len(self.List_of_individuals)<self.Size:
                self.__generate_individuals(self.Size()-len(self.List_of_individuals))
        self.Report.export("test")

    def __accept_input(self):
        while True:
                try:
                    ret = int(input("Enter answer:"))
                    return ret
                except ValueError:
                    print("Please enter an integer (1,2,3,4,5 etc) only")

    def __seed_random(self):
        if self.__is_seeded == False:
            return int((time.time() % 1) * 100)
    def process_generation(self):
            shuffle(self.List_of_individuals)
            #print([str(x) for x in self.List_of_individuals])
            for x in self.List_of_individuals:
                x.print_mult()
                start = time.perf_counter()
                y = self.__accept_input()
                end = time.perf_counter()
                x.generate_score(int(y),start,end)
                self.Report.add_individual(x)
