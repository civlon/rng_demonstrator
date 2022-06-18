# =====================================================
# main


from controller.api_controller import ApiController
from controller.test_controller import TestController


def main():
    testController = TestController()
    testController.runDieharderTest(0)
    # controller.runDieharderTest(1)
    # controller.runDieharderTest(10)
    # controller.runDieharderTest(11)
    output = testController.summerizeTestResults().toJSON()
    print(output)
    apiController = ApiController(output)
    apiController.run()


if __name__ == '__main__':
    main()

# =====================================================
