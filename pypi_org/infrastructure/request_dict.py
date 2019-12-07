import flask


class RequestDictionary(dict):
    def __init__(self, *args, default_val=None, **kwargs):
        self.default_val = default_val
        super().__init__(*args, **kwargs)

    def __getattr__(self, key):
        return self.get(key, self.default_val)


def create(default_val=None, **route_args) -> RequestDictionary:
    """Unifies where all the data comes from."""
    request = flask.request
    data = {
        **request.args,  # The key/value pairs in the URL query string
        **request.headers,  # Header values
        **request.form,  # The key/value pairs in body, from a HTML post form
        **route_args,  # Add additional args that the method accesses,
        # if they want them merged
    }

    return RequestDictionary(data, default_val=default_val)
