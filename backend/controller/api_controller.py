from objects.trng import Trng
from flask import Flask, request
from objects.lcg import LcgPRNG
from controller.test_controller import TestController

# @app.route("/getTestData")


def getTestData():
    mode = request.query_string
    trng = Trng()
    trng.setUp()
    trng.start_trng()
    prng = LcgPRNG(mode.decode("utf-8"), trng)
    controller = TestController(prng)
    output = controller.runAllTests()
    trng.stop()
    return output
