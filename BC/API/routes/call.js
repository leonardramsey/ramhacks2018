var express = require('express');
var router = express.Router();
var cors = require('cors');
var Web3 = require('../web3_modules/initiateWeb3');
var coin = require('../web3_modules/coin_abi');
 var web3 = Web3.initiateWeb3();




router.post('/', cors(), function(req, res) {
	var receipt = web3.eth.call({to:req.body.to,data:req.body.data});
    console.log("receipt  ",receipt);
	const decodedLogs = web3.toAscii(req.body.data);
console.log(decodedLogs);
	console.log("heelloo",decodedLogs);
    res.status(200).json({"jsonrpc":"2.0","id":req.body.id,"result":receipt});
	
});



module.exports = router;
