def test_home_html(testapp):
    content_type = 'text/html'
    response = testapp.get('/', headers={'Accept': content_type})
    assert content_type == response.content_type
    assert b'<h1>Hello' in response.body


def test_home_json(testapp):
    content_type = 'application/json'
    response = testapp.get('/', headers={'Accept': content_type})
    assert content_type == response.content_type
    assert b'{"name":' in response.body
