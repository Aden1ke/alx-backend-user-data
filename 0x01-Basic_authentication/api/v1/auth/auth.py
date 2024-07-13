#!/usr/bin/env python3
""" Auth class and API authentication """


from typing import List, TypeVar
from flask import request


class Auth:
    """ Authentication """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        if path is None or excluded_paths == [] or excluded_paths is None:
            return True
        if path[-1] != '/':
            path = path + '/'

        return not (path in excluded_paths)

    def authorization_header(self, request=None) -> str:
        """ Authorization method """
        if request is None or request.headers.get('Authorization') is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """ defines the current user """
        return None
