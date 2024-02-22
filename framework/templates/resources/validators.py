"""Request | Resource validators for this resource"""

from app.base.validators import RequestValidator


class POSTValidator(RequestValidator):
    """Validates a POST request for this resource"""


class GETValidator(RequestValidator):
    """Validates a GET request for this resource"""


class GETALLValidator(RequestValidator):
    """Validates a GET ALL request for this resource"""


class PUTValidator(RequestValidator):
    """Validates a PUT request for this resource"""


class OPTIONSValidator(RequestValidator):
    """Validates a OPTIONS request for this resource"""


class DELETEValidator(RequestValidator):
    """Validates a DELETE request for this resource"""
