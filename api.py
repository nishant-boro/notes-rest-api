from model import *

@app.route('/notes', methods=['GET'])
def get_notes():
    return jsonify({'Notes': Note.get_all_notes()})


@app.route('/notes/<int:id>', methods=['GET'])
def get_note_by_id(id):
    return_value = Note.get_note(id)
    return jsonify(return_value)


@app.route('/notes', methods=['POST'])
def add_note():
    request_data = request.get_json()
    Note.add_note(request_data["note"])
    return Response("Note added", 201, mimetype='application/json')

@app.route('/notes/<int:id>', methods=['PUT'])
def update_note(id):
    request_data = request.get_json()
    Note.update_note(id, request_data['note'])
    return Response("Note Updated", status=200, mimetype='application/json')

@app.route('/notes/<int:id>', methods=['DELETE'])
def remove_note(id):
    Note.delete_note(id)
    return Response("Note Deleted", status=200, mimetype='application/json')

if __name__ == "__main__":
    app.run(port=1234, debug=True)