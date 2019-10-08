import flask

from pypi_org.infrastructure.view_modifiers import response

blueprint = flask.Blueprint('package', __name__, template_folder='templates')


@blueprint.route('project/<package_name>')
@response(template_file='packages/details.html')
def package_details(package_name: str):
    return f'Package details for {package_name}'
