from sanic import Blueprint
from sanic import response

import ujson

from jinja2 import Environment, PackageLoader, select_autoescape

from .views import BooksView
from .db import init_db

import sys
# Enabling async template execution which allows you to take advantage
# of newer Python features requires Python 3.6 or later.
enable_async = sys.version_info >= (3, 6)

blueprint = Blueprint('myapp')

# Load the template environment with async support
template_env = Environment(
    loader=PackageLoader('apps.myapp'),
    autoescape=select_autoescape(['html', 'xml']),
    enable_async=enable_async
)

# Load the template from file
kitty_template = template_env.get_template('kitty.html')

@blueprint.listener('before_server_start')
def init(sanic, loop):
    init_db(sanic, loop)

@blueprint.route('/', methods=['GET'])
async def handle_main(request):
    return response.json({
        'name': 'mehdi',
    })

@blueprint.route('/echo', methods=['PUT'])
async def handle_echo(request):
    return response.json(ujson.loads(request.body))

@blueprint.route('/name/<name>', methods=['GET'])
async def handle_name(request, name):
    return response.json({
        'name': name,
    })

@blueprint.route('/kitties', methods=['GET'])
async def handle_kitties(request):
    rendered_kitty_template = await kitty_template.render_async(
        kitties=['mooli', 'makhmal', 'kopol'],
    )
    return response.html(rendered_kitty_template)

blueprint.add_route(BooksView.as_view(), '/books/')
