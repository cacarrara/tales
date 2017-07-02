from pyramid.view import view_config


@view_config(route_name='home', accept='text/html', renderer='home.jinja2')
def home(request):
    return {'name': 'Thales Library Management System'}
