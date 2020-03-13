import bcrypt


class User(object):
    def __init__(self, name):

        self._username = name
        #self.recent = datetime.fromtimestamp(datetime.timestamp(timezone.utc))

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, text):
        self._username = text.lower()


    def checkpw(self, pwd):
        #if type(pwd) == str:
        #    pwd = pwd.encode("utf-8")
        return bcrypt.checkpw(bytes(pwd.encode('utf-8')), self._hashpw)


    def hashpw(self, pw):
        self._hashpw = bcrypt.hashpw(bytes(pw.encode('utf-8')), bcrypt.gensalt())
        return True
