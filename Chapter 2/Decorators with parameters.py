import functools

user = {"username": "jose", "access_level": "guest"}


def get_admin_password():
    return "1234"

def decorator(acees_level):
    def make_secure(func):
        @functools.wraps(func)
        def secure_function(*args, **kwargs):
            if user["access_level"] == "admin":
                return func(*args, **kwargs)
            else:
                return f"No admin permissions for {user['username']}."

        return secure_function

    return decorator

@make_secure("admin")
def get_admin_password():
        return "admin:  1234"


@make_secure9("user")
def get_dashboard_password():
    return "user: user_password"

print(get_admin_password())
print(get_dashboard_password())