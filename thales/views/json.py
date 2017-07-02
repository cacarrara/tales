from pyramid.view import view_config


@view_config(route_name='home', accept='application/json', renderer='json')
def home(request):
    return {'name': 'Thales Library Management System'}
