from prettyconf import config as pconf
from pyramid.config import Configurator

from thales import models # flake8: noqa


def main(global_config, **settings):
    settings['sqlalchemy.url'] = pconf('DATABASE_URL')
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.include('.routes')
    config.include('.db')
    config.scan()
    return config.make_wsgi_app()
