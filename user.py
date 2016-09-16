from languages import Language

class User():
    def __init__(self, first_name, last_name, health=10):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.health = health
        self.set_full_name()
        self.languages = []

    def set_full_name(self):
        self.full_name = "{} {}".format(self.first_name, self.last_name)

    def add_health(self, num=2):
        self.health += num

    def remove_health(self, num=1):
        self.health -= num

    def add_language(self, language):
        self.languages.append(language)


############# OUTSIDE THE CLASS ##################

bob = User('bob', 'johnson', 20)
nancy = User('nancy', 'smith')

bob.first_name # => 'Bob'
nancy.last_name # => 'Smith'

bob.add_health(5)
bob.health # => 25

nancy.full_name # => 'Nancy Smith'

ruby = Language('Ruby', bob)
bob.languages # => [<languages.Language object at 0x10218c710>]
######## WTF IS THAT? ########
bob.languages[0].name # => 'Ruby'
ruby.user.full_name # => 'Bob Johnson'

python = Language('Python', bob)

bob.languages # => [<languages.Language object at 0x10295d710>, <languages.Language object at 0x10295d748>]

for language in bob.languages:
    print("{} knows {}".format(bob.full_name, language.name))
