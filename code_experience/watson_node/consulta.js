/* Consulta modelo versão js */

const btoa    = require("btoa");
const axios = require("axios");
const XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;

/* Variáveis de acesso */
const APIKEY = "8uCS7iFWdfm-Ft3WpZWXn7AeY52UCRjYNiWH173hSpCV";
const INSTANCEID = "4dc9cbe9-0160-4b3c-91cb-450387605b52";
const URLMODELO = "https://us-south.ml.cloud.ibm.com/v4/deployments/e652076d-738a-4784-980e-d48d24549ce9/predictions";

/* Funções para número aleatório */
function aleatorioDecimal() {
    return Math.random();
};

function aleatorioInteiro(){
    return Math.ceil(Math.random()*100);
};

/* Cria array de valores */
function criaArrayValues(x){
    var valores = [x]
    for (var i = 0; i < x - 1; i++){
        valores[i] = aleatorioDecimal();
    }
    valores[x - 1] = aleatorioInteiro();
    return valores;
};

/* Cria payload */
function criaPayload(x){
    const payload = '{"input_data": [{"fields": ["length", "diameter", "height", "whole_h", "shucked_w", "viscera_w", "shell_w", "rings"], "values": [' + '[' + criaArrayValues(x) + ']' + ']}]}';
    return payload;
};

/* Função para gerar token */
async function geraToken(apikey){
    var IBM_Cloud_IAM_uid = "bx";
    var IBM_Cloud_IAM_pwd = "bx";
    
    var options = { url     : "https://iam.bluemix.net/oidc/token",
                    headers : {"Content-Type"  : "application/x-www-form-urlencoded",
                                "Authorization" : "Basic " + btoa( IBM_Cloud_IAM_uid + ":" + IBM_Cloud_IAM_pwd )},
                    body    : "apikey=" + apikey + "&grant_type=urn:ibm:params:oauth:grant-type:apikey"};           
    
   
    let token = await axios({method: 'POST', 
                             url: options.url, 
                             headers: {Authorization: options.headers["Authorization"],
                                       'Content-Type': options.headers["Content-Type"]},
                             data: options.body});
    return token.data["access_token"];
}

/* Executa a consulta */
function consultaModelo(urlModelo, tokenId, instanceId, payload, loadCallback, errorCallback){
	const oReq = new XMLHttpRequest();
	oReq.addEventListener("load", loadCallback);
	oReq.addEventListener("error", errorCallback);
	oReq.open("POST", urlModelo);
	oReq.setRequestHeader("Accept", "application/json");
	oReq.setRequestHeader("Authorization", tokenId);
	oReq.setRequestHeader("ML-Instance-ID", instanceId);
	oReq.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
	oReq.send(payload);
}

/* Função principal */
async function main(){
    let token = await geraToken(APIKEY);
    
    const AuthHeader = "Bearer " + token;
    
    var payload = criaPayload(8);

    consultaModelo(URLMODELO, AuthHeader, INSTANCEID, payload, function (resp) {
        let parsedPostResponse;
        try {
            parsedPostResponse = JSON.parse(this.responseText);
        } catch (ex) {
        }
        console.log("Scoring response");
        console.log(parsedPostResponse);
    }, function (error) {
        console.log(error);
    });
}

main();