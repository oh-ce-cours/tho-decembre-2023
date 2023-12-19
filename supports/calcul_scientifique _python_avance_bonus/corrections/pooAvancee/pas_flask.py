# source : https://ains.co/blog/things-which-arent-magic-flask-part-1.html


class PasFlask:
    def __init__(self):
        self.routes = {}

    def route(self, route_str):
        """Ce décorateur agit comme une
        sorte de pattern observer
        """

        def decorator(f):
            self.routes[route_str] = f
            return f

        return decorator

    def serve(self, path):
        view_function = self.routes.get(path)
        if view_function:
            return view_function()
        else:
            raise ValueError("La route '{}' n'a pas été enregistrée".format(path))


app = PasFlask()


@app.route("/")
def hello():
    return "Hello World!"


print(app.serve("/"))
print(app.serve("/index"))
