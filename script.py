from flask import Flask

from Blueprint.blueprint import blueprint as blueprint

app = Flask(__name__)

app.config['RESTPLUS_VALIDATE'] = True
app.config.SWAGGER_UI_REQUEST_DURATION = True

app.register_blueprint(blueprint)

app.run(debug=True, host='0.0.0.0')
