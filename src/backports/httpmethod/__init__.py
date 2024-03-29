import sys

if sys.version_info < (3, 11):
    from backports.strenum import StrEnum
else:
    from enum import StrEnum

__all__ = ["HTTPMethod"]


class HTTPMethod(StrEnum):
    """HTTP methods and descriptions

    Methods from the following RFCs are all observed:

        * RFC 7231: Hypertext Transfer Protocol (HTTP/1.1), obsoletes 2616
        * RFC 5789: PATCH Method for HTTP
    """

    def __new__(cls, value, description):
        obj = str.__new__(cls, value)
        obj._value_ = value
        obj.description = description
        return obj

    def __repr__(self):
        return f"<{self.__class__.__name__}.{self._name_}>"

    CONNECT = "CONNECT", "Establish a connection to the server."
    DELETE = "DELETE", "Remove the target."
    GET = "GET", "Retrieve the target."
    HEAD = "HEAD", "Same as GET, but only retrieve the status line and header section."
    OPTIONS = "OPTIONS", "Describe the communication options for the target."
    PATCH = "PATCH", "Apply partial modifications to a target."
    POST = "POST", "Perform target-specific processing with the request payload."
    PUT = "PUT", "Replace the target with the request payload."
    TRACE = "TRACE", "Perform a message loop-back test along the path to the target."
