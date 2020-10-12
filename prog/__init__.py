from flask import Flask

application = app = Flask(__name__)
# app = Flask(__name__)
# application = Flask(__name__)
from prog import views
# application.run()