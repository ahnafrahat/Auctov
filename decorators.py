from flask import session, redirect, url_for
from functools import wraps


def is_loggedIn(f):

    @wraps(f)
    def wrapper(*args, **kwds):
        if 'UserName' not  in session:
            return redirect(url_for('auth.getLogin'))
           
        
        return f(*args, **kwds)
    return wrapper


