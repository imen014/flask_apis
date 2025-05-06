from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/somme', methods=['POST'])
def addition_api():
    try:
        data = request.get_json()
        nombre1 = data.get('nombre1')
        nombre2 = data.get('nombre2')

        if nombre1 is None or nombre2 is None:
            return jsonify({'error': 'Les champs "nombre1" et "nombre2" sont requis dans le corps de la requête JSON.'}), 400

        try:
            nombre1 = int(nombre1)
            nombre2 = int(nombre2)
        except ValueError:
            return jsonify({'error': 'Les valeurs de "nombre1" et "nombre2" doivent être des nombres.'}), 400

        resultat_somme = nombre1 + nombre2
        reponse = f"Le résultat de {nombre1} + {nombre2} est : {resultat_somme}"
        return jsonify({'resultat': reponse}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4000)
"""
a=1
b=2
def somme(a,b):
    sum = a+b
    return sum

resultat= f"le resultat de {a} + {b} est:   {somme(1,2)}"
print(resultat)
"""