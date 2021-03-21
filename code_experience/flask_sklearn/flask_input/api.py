from flask import Flask, request, render_template
from sklearn.externals import joblib
import numpy as np

# Carrega modelo e OneHotEncoder
clf = joblib.load('class.pkl')
ohe = joblib.load('ohe.pkl')

app = Flask(__name__)

# Carrega página para imputar dados
@app.route('/dados')
def dados():
    return render_template('data.html')

# Carrega resultado
@app.route('/resultado', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':

        # Salva dados dos atributos
        atributos = request.form

        # Salva individualmente os dados de atributos
        sl = float(request.form['sl'])
        sw = float(request.form['sw'])
        pl = float(request.form['pl'])
        pw = float(request.form['pw'])
        var = [sl, sw, pl, pw]

        # Executa predição e transformação do resultado em nome
        predict = clf.predict([var])
        predict = np.insert(predict, 0, float(0))
        result = ohe.inverse_transform([predict])[0][0]

        if np.sum(predict) == 0:
            result = 'iris-setosa'

        # Retorna resultado
        return render_template('result.html', atributos=atributos, result=result)

if __name__ == '__main__':
    app.run(debug=True)