from pyramid.view import view_config


@view_config(route_name='home', accept='text/html', renderer='home.jinja2')
def home(request):
    return {'name': 'Thales Library Management System'}


@view_config(route_name='home', accept='application/json', renderer='json')
def home_json(request):
    return {'name': 'Thales Library Management System'}
