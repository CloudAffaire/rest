from flask import Flask, jsonify, abort, make_response, request

app = Flask(__name__)

employees = [
  {
    "id": 1,
    "firstName": "Debjeet",
    "lastName": "Bhowmik",
    "email": "debjeettoni@gmail.com",
    "phone": "9748239852"
  },
  {
    "id": 2,
    "firstName": "Chandrima",
    "lastName": "Koley",
    "email": "chandrima@gmail.com",
    "phone": "1111111111"
  }
]

@app.route('/')
def index():
    return jsonify({"Message": "Welcome to REST API Version 1"})

@app.route('/api/v1.0/employees', methods=['GET'])
def get_employees():
    return jsonify({"employees": employees})

@app.route('/api/v1.0/employees/<int:id>', methods=['GET'])
def get_employee(id):
    employee = [employee for employee in employees if employee['id'] == id]
    if len(employee) == 0:
        abort(400)
    return jsonify({"employee": employee[0]})

@app.route('/api/v1.0/employees', methods=['POST'])
def create_employee():
    if not request.json or not 'firstName' or not 'lastName' or not 'email' or not 'phone' in request.json:
        abort(400)
    employee = {
        "id": employees[-1]["id"] + 1,
        "firstName": request.json.get("firstName", ""),
        "lastName": request.json.get("lastName", ""),
        "email": request.json.get("email", ""),
        "phone": request.json.get("phone", "")
    }
    employees.append(employee)
    return jsonify({"employees": employees}), 201

@app.route('/api/v1.0/employees/<int:id>', methods=['PUT'])
def update_employee(id):
    employee = [employee for employee in employees if employee['id'] == id]
    if not request.json or not 'firstName' or not 'lastName' or not 'email' or not 'phone' in request.json:
        abort(400)
    employee[0]['firstName'] = request.json.get('firstName', employee[0]['firstName'])
    employee[0]['lastName'] = request.json.get('lastName', employee[0]['lastName'])
    employee[0]['email'] = request.json.get('email', employee[0]['email'])
    employee[0]['phone'] = request.json.get('phone', employee[0]['phone'])
    return jsonify({"employee": employee[0]})

@app.route('/api/v1.0/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):
    employee = [employee for employee in employees if employee['id'] == id]
    if len(employee) == 0:
        abort(400)
    employees.remove(employee[0])
    return jsonify({'result': True})

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'Error': 'Bad Request'}), 400)

if __name__ == '__main__':
    app.run(debug=True)
