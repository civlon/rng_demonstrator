import cProfile
import multiprocessing
from objects.dieharder_test import DieharderTest
from objects.output import Output

ALL_TEST_NUMBERS = [11, 12, 10, 0, 8, 204, 15, 100, 206, 4]


class TestController:
    def __init__(self, prng):
        self.prng = prng

    # same as runDieharderTest() just with profiling
    def runDieharderTestProfiler(self, testNumber):
        cProfile.runctx('self.runDieharderTest(testNumber)',
                        globals(), locals(), 'profFiles/profTestNumber%s.prof' % (testNumber))

    def runDieharderTest(self, testNumber, allTests):
        dieharderTest = DieharderTest(testNumber, self.prng)
        # result od process needs to be put into a managed list, because a multiprocess does not return the current instance of a class
        allTests.append(dieharderTest)

    # same as runAllTests() just with profiling
    def runAllTestsProfiler(self):
        cProfile.runctx('self.runAllTests()',
                        globals(), locals(), 'profFiles/profAllTests.prof')

    def runAllTests(self):
        # create managed list to later summerize all test results
        manager = multiprocessing.Manager()
        allTests = manager.list()
        processes = []
        for i in ALL_TEST_NUMBERS:
            process = multiprocessing.Process(
                target=self.runDieharderTest, args=(i, allTests))
            process.daemon = True
            process.start()
            processes.append(process)

        for p in processes:
            p.join()

        return self.summerizeTestResults(allTests).toJSON()

    def summerizeTestResults(self, allTests):
        testList = allTests
        print(testList)
        numberOfPassedTests = 0
        numberOfFailedTests = 0
        allTestNames = []
        allPValues = []
        for test in testList:
            allPValues.append(float(test.pvalue))
            allTestNames.append(test.name)
            if(test.result == 'PASSED'):
                numberOfPassedTests += 1
            else:
                numberOfFailedTests += 1
        averagePValue = sum(allPValues) / len(allPValues)
        return Output(len(testList), allTestNames, numberOfPassedTests, numberOfFailedTests, averagePValue)
