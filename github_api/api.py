# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests


class GitHubExcept(Exception):
    pass


class GitHubMethodExcept(GitHubExcept):
    pass


class Api(object):
    def __init__(self, access_token=None, api_version='v3'):
        self.access_token = access_token
        self.api_version = api_version
        self.session = requests.Session()

    def valid_token(self):
        response = self.send_method()

        if response.status_code == 200:
            return True
        else:
            return False

    def send_method(self, url='', method='head', **kwargs):
        url = 'https://api.github.com%s' % url

        headers = {
            'Authorization': 'token %s' % self.access_token,
            'Content-Type': 'application/json',
            'Accept': 'application/vnd.github.%s+json' % self.api_version,
        }

        if 'headers' in kwargs:
            headers.update(kwargs['headers'])

        kwargs['headers'] = headers

        if method == 'head':
            method = self.session.head
        elif method == 'post':
            method = self.session.post
        elif method == 'get':
            method = self.session.get
        elif method == 'put':
            method = self.session.put
        elif method == 'delete':
            method = self.session.delete
        elif method == 'patch':
            method = self.session.delete
        else:
            raise GitHubMethodExcept('not method %s' % method)

        return method(url, **kwargs)

    def set(self, method_name):
        return self.__getattr__(method_name)

    def __call__(self, method_name, **kwargs):
        method = method_name.pop()
        url = '/%s' % '/'.join(method_name)
        return self.send_method(url=url, method=method, **kwargs)

    def __getattr__(self, method_name):
        return APIMethod(self, [method_name])


class APIMethod(object):

    _method_name = []

    def __init__(self, api_session, method_name):
        self._api_session = api_session
        self._method_name = method_name

    def set(self, method_name):
        return self.__getattr__(method_name)

    def __getattr__(self, method_name):
        return APIMethod(self._api_session, self._method_name + [method_name])

    def __call__(self, **method_kwargs):
        return self._api_session(self._method_name, **method_kwargs)