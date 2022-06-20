from flask import Flask

from controller.test_controller import TestController

# app = Flask(__name__)


# @app.route("/getTestData")
def getTestData():
    controller = TestController()
    controller.runDieharderTest(0)
    output = controller.summerizeTestResults().toJSON()
    return output
