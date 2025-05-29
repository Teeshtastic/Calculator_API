#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, request, jsonify

app = Flask(__name__)

def get_numbers():
    # Extract numbers from query parameters or JSON body
    if request.is_json:
        data = request.get_json()
        num1 = data.get('num1')
        num2 = data.get('num2')
    else:
        num1 = request.args.get('num1', type=float)
        num2 = request.args.get('num2', type=float)
    return num1, num2

@app.route('/add', methods=['GET', 'POST'])
def add():
    num1, num2 = get_numbers()
    if num1 is None or num2 is None:
        return jsonify({"error": "Please provide num1 and num2"}), 400
    return jsonify({"result": num1 + num2})

@app.route('/subtract', methods=['GET', 'POST'])
def subtract():
    num1, num2 = get_numbers()
    if num1 is None or num2 is None:
        return jsonify({"error": "Please provide num1 and num2"}), 400
    return jsonify({"result": num1 - num2})

@app.route('/multiply', methods=['GET', 'POST'])
def multiply():
    num1, num2 = get_numbers()
    if num1 is None or num2 is None:
        return jsonify({"error": "Please provide num1 and num2"}), 400
    return jsonify({"result": num1 * num2})

@app.route('/divide', methods=['GET', 'POST'])
def divide():
    num1, num2 = get_numbers()
    if num1 is None or num2 is None:
        return jsonify({"error": "Please provide num1 and num2"}), 400
    if num2 == 0:
        return jsonify({"error": "Cannot divide by zero"}), 400
    return jsonify({"result": num1 / num2})

if __name__ == '__main__':
    app.run(debug=True)


# In[ ]:




