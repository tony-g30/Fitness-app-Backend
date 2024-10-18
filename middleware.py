from flask_jwt_extended import jwt_required

def requires_auth(f):
    @jwt_required()
    def decorated_function(*args, **kwargs):
        return f(*args, **kwargs)
    return decorated_function