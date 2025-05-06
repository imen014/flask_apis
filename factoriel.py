from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/factoriel', methods=['POST'])
def factoriel():
    data = request.get_json()
    nombre1 = int(data.get('nombre1'))
    i = int(data.get('i'))
    if nombre1 is None or i is None:
        return jsonify({'error ': 'nombre1 or nombre2 is None! '})
    try:
        for i in range(nombre1):
            resulat = nombre1 * nombre1
    except ValueError:
        return jsonify({'error ': 'There is a value error! '})
    except Exception as e:
        return jsonify({'error ': str(e)}), 500
    response = f'le resultat de factoriel de {nombre1} - {i} fois est égal à : {resulat}'
    return jsonify({'response ': response})

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)
