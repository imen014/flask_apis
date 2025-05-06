from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/pow', methods=['POST'])
def pow_api():
    data = request.get_json()
    number1 = data.get('number1')
    puissance = data.get('puissance')
    try:
        resultat = number1**puissance
        #return jsonify({'response ':response})
        if number1 is None or puissance is None:
            return jsonify({'error':'Number1 or pow is None'}), 400
    except ValueError:
        return jsonify({'error':'Value Error'}), 400
    except Exception as e:
        return jsonify({'error':str(e)}), 500
    
    #resultat = number1**puissance
    response = f'{number1} puissance {puissance} est égal à {resultat}'
    return jsonify({'response':response}), 200
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5000)

