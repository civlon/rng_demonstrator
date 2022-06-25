import os
import controller.api_controller as api
from controller.test_controller import TestController
from flask import Flask


def main():
    app = Flask(__name__)

    app.add_url_rule('/getTestData', view_func=api.getTestData)

    port = int(os.environ.get('PORT', 5000))

    app.run(debug=True, host='0.0.0.0', port=port)


if __name__ == '__main__':
    main()
