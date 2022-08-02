from flask import Flask, request
from objects.lcg import LcgPRNG
from controller.test_controller import TestController

# @app.route("/getTestData")


def getTestData():
    mode = request.query_string
    prng = LcgPRNG(mode.decode("utf-8"))
    controller = TestController(prng)
    output = controller.runAllTests()
    return output
