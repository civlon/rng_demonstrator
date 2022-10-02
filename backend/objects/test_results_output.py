import json

from objects.dieharder_test import DieharderTest


class TestResultsOutput:
    def __init__(self,
                 firstTest: DieharderTest,
                 secondTest: DieharderTest,
                 ):
        
        self.testName = firstTest.name
        if(firstTest.mode == 'changing'):
            self.dieharderTestChangingMode = firstTest.asDict()
            self.dieharderTestStaticMode = secondTest.asDict()
            return
        self.dieharderTestChangingMode = secondTest.asDict()
        self.dieharderTestStaticMode = firstTest.asDict()

    def toJSON(self):
        return json.dumps(self.__dict__)