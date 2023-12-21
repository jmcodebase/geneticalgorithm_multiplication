from random import random,randrange,seed
import time

class Individual:
    """
    Any interger works for num1 and num2
    If -1 is passed in, it will skip the automatic conversion to binary
    The reason for this is, some parts of the code want to make a new individual from random numbers
    others want to mate two already existing individuals
    
    n>0     is for making new individual
    n==-1   is for mating two individuals
    """
    def __init__(self, num1=-1, num2=-1):
        self.__mutation_rate=float(.125)
        self.__score=0
        self.__is_wrong = False
        self.__time_score = 0

        if num1 != -1:
            self.number1=self.__int_to_binary(num1)
        if num2 != -1:
            self.number2=self.__int_to_binary(num2)

    def __int_to_binary(self,integer: int):
        return format(integer, '04b')

    # to make unit testing easier, issues with mocking random.random. figure it out later.
    def random_wrapper(self):
        return random()

    @property
    def Time_score(self) -> bool:
        return self.__time_score
    
    @Time_score.setter
    def Time_score(self, value: bool):
        self.__time_score = value
   
    @property
    def Is_wrong(self) -> bool:
        return self.__is_wrong
    
    @Is_wrong.setter
    def Is_wrong(self, value: bool):
        self.__is_wrong = value

    @property
    def Score(self)->int:
        return self.__score

    @Score.setter
    def Score(self, value: int):
        self.__score=value

    def mult_as_str(self) -> str:
        return f'{self.get_number1_as_int()} * {self.get_number2_as_int()}'

    def print_mult(self):
        #self.create_random_numbers()
        print(self.mult_as_str())

    def set_number1_from_binary(self, binary: str):
        self.number1=binary

    def set_number2_from_binary(self, binary: str):
        self.number2=binary

    def __number_as_int(self,n) -> int:
        return int(n,2)
    
    def get_number1_as_int(self) -> int:
        return self.__number_as_int(self.number1)
    
    def get_number2_as_int(self) -> int:
        return self.__number_as_int(self.number2)

    def noncrossover(self,other_individual):
        return (self,other_individual)

    def crossover(self, other_individual):
        child1_number1=self.mutate(self.number1)
        child1_number2=self.mutate(other_individual.number2)

        child2_number1=self.mutate(other_individual.number1)
        child2_number2=self.mutate(self.number2)
        child1 = Individual()
        child1.set_number1_from_binary(child1_number1)
        child1.set_number2_from_binary(child1_number2)

        child2 = Individual()
        child2.set_number1_from_binary(child2_number1)
        child2.set_number2_from_binary(child2_number2)
        
        return (child1,child2)

    def mate(self,other_individual,crossover_rate):
        if (random() > crossover_rate):
            return self.noncrossover(other_individual)
        return self.crossover(other_individual)

    def generate_score(self, answer_given: int, start_time: float, end_time: float):
        # 0 is a perfect score. The higher the number the more "wrong" the user is.
        expected_answer = self.get_number1_as_int() * self.get_number2_as_int()
        self.Time_score = (end_time - start_time)
        self.__expected_answer=expected_answer
        self.__answer_given=answer_given

        time_mult = 1
        offby = abs(expected_answer - answer_given) 
        #change the weight of time when they're right to punish looking up answers or counting fingers etc
        if (offby == 0):
            if (self.Time_score >= 1.5):
                time_mult=1.5
        else:
            self.Is_wrong=True
            time_mult=1.1

        self.__offby_penalty=offby*3*self.Time_score
        self.__time_penalty=self.Time_score*time_mult
        #penalize getting the answer wrong more
        self.Score = self.__offby_penalty+self.__time_penalty
         
    def get_score(self) -> int:
        return self.Score

    def flip_bit(self,number_as_string,index) -> str:
        if (number_as_string[index]) == "0":
            replacement = "1"
        else:
            replacement = "0"

        new_string = number_as_string[:index] + replacement + number_as_string[index+1:]
        return new_string

    def mutate(self,number_as_binary: str) -> str:
        for i in range(len(number_as_binary)):
            a = self.random_wrapper()
            if a < self.__mutation_rate:
                number_as_binary = self.flip_bit(number_as_binary,i)
        return number_as_binary
    
    def __lt__(self, other):
        return self.Score < other.score

    def __eq__(self, other):
        return self.Score == other.Score

    def __gt__(self, other):
        return self.Score > other.score

    def __hash__(self):
        return hash(self.mult_as_str())

    def __str__(self):
        print(f'score: {self.Score} \n eq: {self.mult_as_str()} \n is wrong: {self.Is_wrong} offby penalty: {self.__offby_penalty} time penalty:{self.__time_penalty} given answer: {self.__answer_given} right answer: {self.__expected_answer}')
        return str(self.Score)

