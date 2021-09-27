''' defines a new metaclass for use as a Singleton '''

class Singleton(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
            print('~~ Singleton class created ~~') # Demo purposes only
            return self.__instance
        else:
            print('~~ Singleton class already instantiated ~~') # Demo purposes only
            return self.__instance


class Manager(metaclass=Singleton):
    ''' single manager with full administrative privileges '''
    def __init__(self, username, admin):
        self.username = username
        self.admin = admin

# creating list of users
users = []

# creating 2 different instances of class Manager
administrator = Manager('robobob', True)
manager = Manager('tony montana', True)

users.append(administrator)


# ------------------------------ TEST CASE ----------------------------------- #

print('\nTest prints:')

print(administrator.username == manager.username)
print(administrator.username)   # Should print 'Robobob'
print(manager.username)         # Should print 'Robobob' despite someone trying
                                # to create a new instance of Manager() class.

for user in users:
    if user.admin == True:
        print(f"\nUser: {user.username}\t Privileges: Administrative access")
    else:
        print(f"\nUser: {user.username}\t Privileges: User access only")
