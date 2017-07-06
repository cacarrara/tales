import pyramid.httpexceptions as exc
from pyramid.view import view_config

from thales.models import Author


@view_config(route_name='home', accept='text/html', renderer='home.jinja2')
@view_config(route_name='home', accept='application/json', renderer='json')
def home(request):
    return {'name': 'Thales Library Management System'}


@view_config(route_name='authors', accept='text/html', renderer='authors.jinja2')
@view_config(route_name='authors', accept='application/json', renderer='json')
def authors(request):
    authors = request.db.query(Author).order_by(Author.name).all()
    return {'authors': authors}


@view_config(route_name='author', request_method="GET", accept='text/html', renderer='author_form.jinja2')
def author_form(request):
    return {}


@view_config(route_name='author', request_method="POST", accept='text/html', renderer='author_form.jinja2')
@view_config(route_name='author', request_method="POST", accept='application/json', renderer='json')
def author_submit(request):
    author = Author(name=request.POST.get('name'))
    request.db.add(author)
    return exc.HTTPFound(request.route_url('authors'))
