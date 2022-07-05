from objects.dieharder_test import DieharderTest
from objects.output import Output


class TestController:
    def __init__(self, mode):
        self.mode = mode
        self.dieharderTestList = []
        self.numberOfPassedTests = 0
        self.numberOfFailedTests = 0
        self.allPValues = []

    def runDieharderTest(self, testNumber):
        dieharderTest = DieharderTest(testNumber, self.mode)
        self.dieharderTestList.append(dieharderTest)
        self.allPValues.append(float(dieharderTest.pvalue))
        if(dieharderTest.result == 'PASSED'):
            self.numberOfPassedTests = self.numberOfPassedTests + 1
        elif(dieharderTest.result == 'WEAK'):
            self.numberOfPassedTests = self.numberOfPassedTests + 1
        else:
            self.numberOfFailedTests = self.numberOfFailedTests + 1
        print(dieharderTest)

    def summerizeTestResults(self):
        allTestNames = []
        averagePValue = sum(self.allPValues) / len(self.allPValues)
        for test in self.dieharderTestList:
            allTestNames.append(test.name)
        return Output(len(self.dieharderTestList), allTestNames, self.numberOfPassedTests, self.numberOfFailedTests, averagePValue)
