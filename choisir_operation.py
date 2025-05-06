from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/choisir_operation', methods=['POST'])
def choisir_operation():
    data = request.get_json()
    number1 = int(data.get('number1'))
    number2 = int(data.get('number2'))
    operation = data.get('operation')
    if number1 is None or number2 is None or operation is None:
        return jsonify({'error':'number1 or number2 or operation is invalid'}), 400
    try:
        if operation == "addition":
            resultat = number1 + number2
        elif operation == "soustraction":
            resultat = number1 - number2
        elif operation == "multiplication":
            resultat = number1 * number2
        elif operation == "division":
            if number2 == 0:
                resultat = "division by is not required"
                return jsonify({'error':'division by zero is not required! '})
            else:
                resultat = number1 / number2
        else:
            resultat = "invalid operation introduced"
    except ValueError:
        return jsonify({'error':'Value error'}), 400
    except Exception as e:
        return jsonify({'error':str(e)}), 500
    
    response = f'le resulat de {number1} {operation} {number2} est: {resultat}'
    return jsonify({'response':response}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5000)
