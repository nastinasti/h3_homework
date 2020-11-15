'''
-----User Class-----
'''

import uuid


class User:
    def __init__(self, username, userpass, email):
        self.id = uuid.uuid4()
        self._username = username
        self._userpass = userpass
        self._email = email

    @property
    def username(self):
        return self._username

    @property
    def userpass(self):
        return '*' * len(self._userpass)