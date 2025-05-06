from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/multiplicator', methods=['POST'])
def multiplicator():
    data = request.get_json()
    nombre1 = data.get("nombre1")
    nombre2 = data.get("nombre2")
    if nombre1 is None or nombre2 is None:
        return jsonify({'error: ': 'verifiez les numeros! '}), 400
    try:
        nombre1 = int(nombre1)
        nombre2 = int(nombre2)
        resultat = nombre1 * nombre2
    except ValueError:
        return jsonify({'error ':'nombre1 et nombre2 doivent etre des numeros! '})
    except Exception as e:
        return jsonify({'error ': str(e)}), 500
    response = f'le resultat de {nombre1} * {nombre2} est {resultat}'
    return jsonify({'resultat ': response})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
    #mult = a*b
    #return mult