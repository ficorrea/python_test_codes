const _ = require('underscore');

class Populacao{

    constructor(individuos, cromossomos){
        this.individuos = individuos;
        this.cromossomos = cromossomos;
        this.populacao = [];
    };

    geraPopulacao(){
        for (var j=0; j < this.individuos; j++){
            this.populacao[j] = [];
            for(var i=0; i < 3; i++){
                this.populacao[j][i] = _.times(this.cromossomos, function aleatorio(){ return _.random(0, 1)});
            }                  
        }
        return this.populacao;
    };
}

module.exports = Populacao;