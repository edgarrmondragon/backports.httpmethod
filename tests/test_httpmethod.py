from backports.httpmethod import HTTPMethod


def test_equals_string():
    assert HTTPMethod.GET == "GET"


def test_value():
    assert HTTPMethod.GET.value == "GET"


def test_description():
    assert HTTPMethod.GET.description == "Retrieve the target."


def test_available_methods():
    assert list(HTTPMethod) == [
        HTTPMethod.CONNECT,
        HTTPMethod.DELETE,
        HTTPMethod.GET,
        HTTPMethod.HEAD,
        HTTPMethod.OPTIONS,
        HTTPMethod.PATCH,
        HTTPMethod.POST,
        HTTPMethod.PUT,
        HTTPMethod.TRACE,
    ]
