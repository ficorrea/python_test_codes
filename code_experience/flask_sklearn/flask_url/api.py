from flask import Flask, jsonify, request
from sklearn.externals import joblib
import numpy as np

# Carrega modelo e OneHotEncoder
clf = joblib.load('class.pkl')
ohe = joblib.load('ohe.pkl')

app = Flask(__name__)

@app.route('/classificador')
def kind_classificador():
	# Carrega dados da URL
	# sepal_length=valor&sepal_width=valor...
    sepal_length = float(request.args.get('sepal_length'))
    sepal_width = float(request.args.get('sepal_width'))
    petal_length = float(request.args.get('petal_length'))
    petal_width = float(request.args.get('petal_width'))

    event = [sepal_length, sepal_width, petal_length, petal_width]

    result = {}
	
	# Resultado da predição
    predict = clf.predict([event])

    predict = np.insert(predict, 0, float(0))
    flower = ohe.inverse_transform([predict])
    
    if np.sum(predict) == 0:
        flower = [['iris-setosa']]
        predict = np.delete(predict, 0)
        predict = np.insert(predict, 0, float(1))
	
	# Gera json
    result['flower'] = flower[0][0]
    result['predict'] = str(predict)
	
	# Retorna json com os dados
    return jsonify(result), 200

app.debug = True
app.run()