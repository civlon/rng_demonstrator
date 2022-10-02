import multiprocessing
from objects.trng import Trng
from flask import Flask, request
from objects.prng import PRNG
from controller.test_controller import TestController
import multiprocessing.queues
import multiprocessing.synchronize

class ApiController():
    def __init__(self):
        self.trng = Trng()
        self.changingRng = PRNG('changing', self.trng)
        self.staticRng = PRNG('static', self.trng)
        self.trng.setUp()
        self.trng.start_trng()

    def runTest(self):
        testNumber = request.query_string.decode("utf-8")
        controller = TestController(self.changingRng)
        try:
            testsQueue = multiprocessing.Queue()
        except:
            testsQueue = multiprocessing.Queue()
            testsQueue.close()
        finally:
            testsQueue = multiprocessing.Queue()
        return controller.getTestResults(testNumber, self.changingRng, self.staticRng, testsQueue)

    def roll(self):
        mode = request.query_string.decode("utf-8")
        if(mode == 'changing'):
            return self.changingRng.rollDice()
        if(mode == 'static'):
            return self.staticRng.rollDice()