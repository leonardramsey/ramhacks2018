var express = require('express');
var router = express.Router();
var cors = require('cors');
var Web3 = require('../web3_modules/initiateWeb3');
var coin = require('../web3_modules/coin_abi');
 var web3 = Web3.initiateWeb3();



router.post('/', cors(), function(req, res) {
	console.log("in txStatus");
    console.log("body::::::::::::: ",req.body);
    var receipt = web3.eth.getTransaction(req.body.txhash);
	console.log("in txStatus{",receipt);
    res.status(200).json({"result":receipt});
});




module.exports = router;
