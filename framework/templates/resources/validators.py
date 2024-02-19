"""Request | Resource validators for this resource"""

from app.core.validators import ReqValidator


class POSTValidator(ReqValidator):
    """Validates a POST request for this resource"""


class GETValidator(ReqValidator):
    """Validates a GET request for this resource"""


class GETALLValidator(ReqValidator):
    """Validates a GET ALL request for this resource"""


class OPTIONSValidator(ReqValidator):
    """Validates a OPTIONS request for this resource"""


class DELETEValidator(ReqValidator):
    """Validates a DELETE request for this resource"""
