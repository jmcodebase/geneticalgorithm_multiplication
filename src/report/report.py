import report.fields as f
import sys
import os
from report.export.exportfactory import ExportFactory as ef
sys.path.append(os.getcwd() + '/../mtable/')
import individual

class Report:
    def __init__(self):
        self.__items={}

    @property
    def Items(self):
        return self.__items

    @Items.setter
    def Items(self, value):
        self.__items = value

    #dictionary lookup always follows as biggernumber * smallernumber
    def create_lookup(self, individual):
        n1=individual.get_number1_as_int()
        n2=individual.get_number2_as_int()

        if (n1 > n2):
            return f"{str(n1)} x {str(n2)}"
        return f"{str(n2)} x {str(n1)}"

    def add_individual(self, i: individual):
        new_field = f.Fields(i)
        lookup = self.create_lookup(i)
        
        if (lookup in self.Items):
            new_field = new_field + self.Items[lookup]
            
        self.Items[self.create_lookup(i)]=new_field

    def add_individuals(self,i: list[individual]):
        for x in i:
            self.add_individual(x)
    """
    Add multiple types of exports, like csv, json etc
    Default to console output
    """
    def export(self, method):
        x = ef.create_export(method)
        x.Load(self.Items)
        x.Export()
        #for k,v in self.Items.items():
         #   print(f"key: {k}    -   value: {v}")

