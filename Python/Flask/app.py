from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)

tasks = []
task_id_control = 1

@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_control
    data = request.get_json()
    
    if not data or "title" not in data:
        return jsonify({"message": "O campo 'title' é obrigatório!"}), 400
    
    new_task = Task(id=task_id_control, title=data.get("title"), description=data.get("description", ""))
    task_id_control += 1
    tasks.append(new_task)
    print(tasks)
    
    return jsonify({"message": "Nova tarefa criada com sucesso!", "task": new_task.to_dict()}), 201

@app.route('/tasks', methods=['GET'])
def get_all_tasks():
    task_list = [task.to_dict() for task in tasks]
    output = {
        "tasks": task_list,
        "total_tasks": len(task_list)
    }
    return jsonify(output)

@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict())
    return jsonify({"message": "Não foi possível encontrar a atividade"}), 404

@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
    print(task)
    if task == None:
        return jsonify({"message": "Não foi possível encontrar a atividade."})
    
    data = request.get_json()
    task.title = data['title']
    task.description = data['description']
    task.completed = data['completed']
    print(task)
    return jsonify({"message": "Tarefa atualizda com sucesso."}), 200

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t

    if not task:
        return jsonify({"message": "Não foi possivel encontrar a atividade."}), 404

    tasks.remove(task)
    return jsonify({"message": "Tarefa deletada com sucesso!"}), 200

if __name__ == "__main__":
    app.run(debug=True)
