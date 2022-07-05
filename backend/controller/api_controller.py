from flask import Flask, request
import multiprocessing

from controller.test_controller import TestController

# app = Flask(__name__)


# @app.route("/getTestData")
def getTestData():
    mode = request.query_string
    controller = TestController(mode.decode("utf-8"))
    # jobs = []
    # process1 = multiprocessing.Process(target=controller.runDieharderTest(3))
    # jobs.append(process1)
    # process1.start()
    # process2 = multiprocessing.Process(target=controller.runDieharderTest(4))
    # jobs.append(process2)
    # process2.start()
    # process3 = multiprocessing.Process(target=controller.runDieharderTest(5))
    # jobs.append(process3)
    # process3.start()
    # for p in jobs:
    #     p.join()
    controller.runDieharderTest(3)
    controller.runDieharderTest(4)
    controller.runDieharderTest(5)
    output = controller.summerizeTestResults().toJSON()
    return output
