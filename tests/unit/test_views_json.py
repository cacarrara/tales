def test_home_request(pyramid_request):
    from thales.views.json import home
    response = home(pyramid_request)
    assert 'name' in response
