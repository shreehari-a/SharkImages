from flask_login import UserMixin

from imageup import app
#class for user 
class User(UserMixin):
    def __init__(self, username_in):
        self.id = username_in

#@login_manager.user_loader
#def load_user(username_in):
    ''' 
    user obect will be returned in this function
    '''
#    return User(username_in)

def login_required(test):
    @wraps(test)
    def wrap( *args, **kwargs):
        if 'username_in' in session:
            return test(*args,**kwargs)
        else:
            return render_template('login.html')
    return wrap


