var express = require('express');
const Web3 = require('../web3_modules/initiateWeb3');
var router = express.Router();
var cors = require('cors');
var router = express.Router();

router.post('/', cors(), function(req, res) {
	console.log("in blockNumber");
    var web3 = Web3.initiateWeb3();
    console.log("body::::::::::::: ");
    var receipt =  web3.eth.blockNumber;
    console.log("receipt  ",receipt);

    res.status(200).json({"result":receipt});
});

module.exports = router;
