# -*- coding: utf-8 -*-
import github_api

api = github_api.Api(access_token='977903c5f22e1a1b4a8398512a885ccfc5f950c6')


response = api.users.set('vir-mir').get()
print(response.json())
