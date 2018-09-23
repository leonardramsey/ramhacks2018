var express = require('express');
var router = express.Router();
var cors = require('cors');
var Web3 = require('../web3_modules/initiateWeb3');
var coin = require('../web3_modules/coin_abi');
 var web3 = Web3.initiateWeb3();
 var decToHex = require("dec-to-hex")




router.post('/', cors(), function(req, res) {
	    console.log("receiptdf ",req.body.to,req.body.value);
	var receipt = web3.eth.estimateGas({to:req.body.to,data:req.body.data});
	console.log("hey",receipt);
	var balance =""+receipt;
		let temp = parseInt(balance);
		let hex = temp.toString(16);

    res.status(200).json({"jsonrpc":"2.0","id":req.body.id,"result":"0x"+hex});//+hex
	

});


module.exports = router;

