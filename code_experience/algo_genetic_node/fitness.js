const utils = require('./utils');

class Fitness{

    constructor(){
        this.utils = new utils();
    };  
    
    calculaFitness(variaveis){
        var total = variaveis.reduce(this.utils.reducer);
        console.log(total);
        var totalEquacao = 1 / (1 + Math.log(total));
        return totalEquacao;
    };
}

module.exports = Fitness;