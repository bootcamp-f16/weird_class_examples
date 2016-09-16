class Language():
    def __init__(self, name, user):
        self.name = name
        self.user = user
        self.user.add_language(self) ### Only runs once during the init

