import pyramid.testing
import pytest
from webtest import TestApp


@pytest.fixture
def pyramid_request():
    return pyramid.testing.DummyRequest()


@pytest.yield_fixture
def pyramid_config(pyramid_request):
    with pyramid.testing.testConfig(request=pyramid_request) as config:
        yield config


@pytest.fixture
def config():
    return {
        'jinja2.directories': 'templates',
    }


@pytest.fixture
def testapp(config):
    from thales import main
    return TestApp(main(None, **config))
