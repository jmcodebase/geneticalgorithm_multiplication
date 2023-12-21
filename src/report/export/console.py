from report.export.export import Export

class Console(Export):
    def Load(self, i):
        self.__kvp = i
    def Export(self):
        for k,v in self.__kvp.items():
            print(f"key: {k}    -   value: {v}")
