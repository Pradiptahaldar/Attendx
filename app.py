from flask import Flask
from routes.auth import auth
from routes.home import home
from routes.register import register 

app = Flask(__name__)

app.register_blueprint(auth)
app.register_blueprint(home)
app.register_blueprint(register)
    

if __name__ == "__main__":
    app.run(debug=True)