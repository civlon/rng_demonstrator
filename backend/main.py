import os
import controller.api_controller
from flask import Flask


def main():
    api = controller.api_controller.ApiController()

    app = Flask(__name__)

    app.add_url_rule('/roll', view_func=api.roll)

    app.add_url_rule('/run', view_func=api.runTest)

    port = int(os.environ.get('PORT', 5000))

    app.run(debug=False, host='0.0.0.0', port=port, use_reloader=False)


if __name__ == '__main__':
    main()
