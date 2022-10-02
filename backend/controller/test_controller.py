import multiprocessing
from multiprocessing.dummy import Process
import multiprocessing.popen_fork
from objects.prng import PRNG
from objects.test_results_output import TestResultsOutput
from objects.dieharder_test import DieharderTest
import multiprocessing.popen_fork

class TestController:
    def __init__(self, prng):
        self.prng = prng

    def startTest(self, testNumber, prng: PRNG, testsQueue: multiprocessing.Queue):
        dieharderTest = DieharderTest(testNumber, prng.mode)
        res = dieharderTest.runSubprocess(prng)
        dieharderTest.stripOutputIntoVariables(res)
        testsQueue.put(dieharderTest)

    def createProcess(self, testNumber, prng: PRNG, testsQueue, processes):
        processStatic = multiprocessing.Process(
        target=self.startTest, args=(testNumber, prng, testsQueue))
        processStatic.daemon = True
        processStatic.start()
        processes.append(processStatic)

    def getTestResults(self, testNumber, changingPRNG, staticPRNG, testsQueue: multiprocessing.Queue):
        processes = []
        self.createProcess(testNumber, staticPRNG, testsQueue, processes)
        self.createProcess(testNumber, changingPRNG, testsQueue, processes)

        for p in processes:
            p.join()

        output = TestResultsOutput(testsQueue.get(), testsQueue.get()).toJSON()

        testsQueue.close()

        return output

