import flask

from infrastructure.view_modifiers import response

import pypi_org.services.package_service as package_service

app = flask.Flask(__name__)


if __name__ == '__main__':
    app.run(debug=True)
