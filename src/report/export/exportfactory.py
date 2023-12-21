from .console import *
from .json import *

class ExportFactory:
    @staticmethod
    def create_export(method):
        method = method.lower()

        if method == "console":
            return Console()
        elif method == "json":
            return Json()
        else:
            return Console()

