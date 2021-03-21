const population = require('./population');
const utils = require('./utils');
const fitness = require('./fitness');

var populacao = new population(3, 10);
var pops = populacao.geraPopulacao();
// console.log(pops);
// console.log(pops[0].length);

var tt = new utils();
var dd = tt.converteBinarioDecimal(pops[0]);
console.log(dd.reduce(tt.reducer));

var ff = new fitness();
console.log(ff.calculaFitness(dd));