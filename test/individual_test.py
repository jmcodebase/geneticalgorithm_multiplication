import os, sys
import unittest
from random import seed,random, randrange
from unittest.mock import patch
sys.path.append(os.getcwd() + '/../src/mtable')
from individual import *


class IndividualTest(unittest.TestCase):
    def test_flipbit_index0(self):
        i = Individual()
        string_test="0000"
        index=0

        ret = i.flip_bit(string_test,index)
         
        self.assertTrue(ret == "1000")

    def test_flipbit_index3(self):
        i = Individual()
        string_test="0000"
        index=3

        ret = i.flip_bit(string_test,index)
         
        self.assertTrue(ret == "0001")


    def test_flipbit_index2(self):
        i = Individual()
        string_test="0000"
        index=2

        ret = i.flip_bit(string_test,index)
         
        self.assertTrue(ret == "0010")
   
    @patch('individual.Individual.random_wrapper')
    def test_mutate(self, mock_random):
        #100 is an arbitrary number that i know is higher than the mutation rate
        mock_random.return_value=100 
        i = Individual()

        ret = i.mutate("1111")
        
        self.assertTrue(ret == "1111")

    def binary(n):
        return format(n,'04b')

    @patch('individual.Individual.mutate')
    def test_crossover(self, mock_obj):
        two =   IndividualTest.binary(2)
        five =  IndividualTest.binary(5)
        four =  IndividualTest.binary(4)
        three = IndividualTest.binary(3)

        mock_obj.side_effect = [two,five,four,three]

        ind_one = Individual(2,3)
        #'other' individual below
        ind_two = Individual(4,5)

        ind_one.mutate = mock_obj
        mutated_one, mutated_two = ind_one.crossover(ind_two)
        
        mutated_one_crossedover = mutated_one.get_number1_as_int() == 2 and mutated_one.get_number2_as_int() == 5
        mutated_two_crossedover = mutated_two.get_number1_as_int() == 4 and mutated_two.get_number2_as_int() == 3
            
        print(mutated_one_crossedover)
        print(mutated_two.get_number1_as_int())
        mutates_are_correct = mutated_one_crossedover and mutated_two_crossedover

        self.assertTrue(mutates_are_correct)

    def test_generate_score_correct_answer(self):
        ind = Individual(2,5)
        expected_score = 0.5

        ind.generate_score(10,1,1.5)
        actual_score = ind.Score
        self.assertEqual(expected_score,actual_score)

    def test_generate_score_is_wrong_flag_correct_answer(self):
        ind = Individual(2,5)
        expected_score = 0.5

        ind.generate_score(10,1,1.5)
        actual_score = ind.Score
        self.assertFalse(ind.Is_wrong)

    def test_generate_score_incorrect_answer(self):
        ind = Individual(2,5)

        ind.generate_score(11,1,1.5)
        actual_score = ind.Score
        self.assertEqual(2.05,actual_score)

    def test_generate_score_is_wrong_flag_incorrect_answer(self):
        ind = Individual(2,5)
        ind.generate_score(11,1,1.5)
        actual_score = ind.Score
        self.assertTrue(ind.Is_wrong)
        

if __name__ == '__main__':
    unittest.main()
