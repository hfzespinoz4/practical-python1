import os
from flask import Flask

# Instacia de flask asignada a la variable app
# Si se utiliza un solo módulo se puede utilizar __name__,
# sino deberá especificarse
app = Flask(__name__)

# decorator, @ es conocido como "pie notation"


@app.route('/')
def hello():
    return "Hello, World"


# si __name__ es principal ejecutar:
if __name__ == "__main__":

    # __main__ es el nmbre del módulo por defecto en Python
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
