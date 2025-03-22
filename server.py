
from flask import Flask, jsonify, request, render_template

#criando aplicação em Flask

app = Flask(__name__)

#get = buscar algo

@app.route('/')
def home():
        return render_template('index.html')
    


@app.route("/helloworld", methods=['GET'])
def helloworld():
    return jsonify({
        "msg":"ola mundo, como voces estao?"
    })
   
    
tarefas = [
    {"id":1, "titulo": "Estudar Python", "feito": False},
    {"id":2, "titulo": "Ler a DOc", "feito": True},
]

@app.route("/tarefas", methods=['GET'])
def get_tarefas():
    return jsonify(tarefas)

#POST - criar iuma nova tarefa

@app.route('/tarefas', methods=['POST'])
def add_tarefa():
    nova_tarefa = request.json #pega informação do body
    nova_tarefa['id'] = len(tarefas) + 1 #nov id
    tarefas.append(nova_tarefa) #adicionado nova tarefa na lista
    return jsonify(nova_tarefa), 201 #201 criado com sucesso
    """
    JavaScript (front)
    React (Front)
    Insomnia(aplicativo) - simula um front    
    Postman (Aplicativo) - Simula um front   
    BACKend - Modelo de API - FULL REST
    Full stack - Arquitetura MVC (model, view, controller)
    """
#Iniciar o srvidor
if __name__ == '__main__':
    app.run(debug=True)
    

