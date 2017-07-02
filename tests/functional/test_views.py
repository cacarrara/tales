def test_home(testapp):
    response = testapp.get('/', status=200)
    assert b'<h1>Hello' in response.body
