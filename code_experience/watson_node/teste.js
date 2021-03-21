var sleep = require("sleep");
// const util = require('util');
// const requestPromise = util.promisify(sleep.sleep);

async function main() {
    var um = await funcaoUm();
    var dois = await funcaoDois();

    return await Promise.resolve(um);
}

async function funcaoUm() {
    await sleep.sleep(2);
    return "Um";
}

async function funcaoDois() {
    await sleep.sleep(2);
    return "Dois";
}

async function mama(){
    return await main();
}

x = main().then(um => {var y = um; return y});
console.log(x);