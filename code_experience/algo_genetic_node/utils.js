class Utils{

    constructor(){};

    converteBinarioDecimal(array){
        const digitos = array[0].length - 1;
        var numeros = [];
        for (var i = 0; i < array.length; i++){
            var total = 0;
            for (var j = digitos; j >= 0; j--){
                total = total + array[i][j] * Math.pow(2, j);
            }
            numeros[i] = total;
        }
        return numeros;
    };

    reducer(acumulador, valorAtual){
        return acumulador + valorAtual;
    }; 

}

module.exports = Utils;