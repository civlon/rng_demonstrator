from flask import Flask, g

from controller.test_controller import TestController

app = Flask(__name__)
output = {}


@app.route("/getTestData")
def get_test_data():
    controller = TestController()
    print('test')
    controller.runDieharderTest(0)
    output = controller.summerizeTestResults().toJSON()
    return output
