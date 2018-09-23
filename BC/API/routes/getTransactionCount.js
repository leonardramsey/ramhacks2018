var express = require('express');
var router = express.Router();
var cors = require('cors');
var Web3 = require('../web3_modules/initiateWeb3');
var coin = require('../web3_modules/coin_abi');
 var web3 = Web3.initiateWeb3();


router.post('/', cors(), function(req, res) {
	
	var receipt = web3.eth.getTransactionCount(req.body.address);
	    console.log("receipt  ",receipt);

		var balance =""+receipt;
		let temp = parseInt(balance);
		let hex = temp.toString(16);


    res.status(200).json({"jsonrpc":"2.0","id":req.body.id,"result":"0x"+hex});
});






module.exports = router;
