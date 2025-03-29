from flask import Flask
from flask_mysqldb import MySQL # biblioteca mysql flask
from controllers.produto_controller import produto_bp
import config

app = Flask(__name__) #instaciar o Flask
app.config.from_object(config) # configura variaveis


mysql = MySQL(app)


# passa a conexao para os controlers
app.mysql = mysql

app.register_blueprint(produto_bp)


if __name__ == '__main__':
    app.run(debug=True)
    
    
    
    


