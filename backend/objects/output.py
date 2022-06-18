import json


class Output:
    def __init__(self,
                 numberOfTests,
                 allTestNames,
                 numberOfPassedTests,
                 numberOfFailedTests,
                 averagePValue):

        self.numberOfTests = numberOfTests
        self.allTestNames = allTestNames
        self.numberOfPassedTests = numberOfPassedTests
        self.numberOfFailedTests = numberOfFailedTests
        self.averagePValue = averagePValue

    def toJSON(self):
        return json.dumps(self.__dict__)
