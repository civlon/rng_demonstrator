# =====================================================
# main


import controller.api_controller as api
from controller.test_controller import TestController
from flask import Flask


def main():
    app = Flask(__name__)

    app.add_url_rule('/', view_func=api.getTestData)

    app.run(debug=True)


if __name__ == '__main__':
    main()

# =====================================================
