from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/soustract', methods=['POST'])
def soustract():
    data = request.get_json()
    nombre1 = data.get('nombre1')
    nombre2 = data.get('nombre2')
    if nombre1 is None or nombre2 is None:
        return jsonify({'error': 'Les champs "nombre1" et "nombre2" sont requis dans le corps de la requête JSON.'}), 400
    try:
        nombre1 = int(nombre1)
        nombre2 = int(nombre2)
        resultat_soustract = nombre1 - nombre2
    except ValueError:
        return jsonify({'error': 'Les valeurs de "nombre1" et "nombre2" doivent être des nombres.'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    #sous = a-b
    #return sous
    reponse = f"Le résultat de {nombre1} - {nombre2} est : {resultat_soustract}"
    #return jsonify({'resultat': reponse}), 200
    
    return jsonify({'resultat': reponse}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)