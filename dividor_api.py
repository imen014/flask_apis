from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/dividor', methods=['POST'])
def dividor():
    data = request.get_json()
    nombre1 = int(data.get('nombre1'))
    nombre2 = int(data.get('nombre2'))
    if nombre1 is None or nombre2 is None or nombre2 == 0:
        return jsonify({'error ':'verify entered numbers!'})
    try:
        resultat = nombre1 / nombre2
    except ValueError:
        return jsonify({'error ':'value error! '}), 400
    except Exception as e:
        return jsonify({'error: ': str(e)}), 500
    response = f'le resultat de {nombre1} / {nombre2} est: {resultat}'
    return jsonify({'response ': response})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


