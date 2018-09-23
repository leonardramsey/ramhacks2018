var express = require('express');
const Web3 = require('../web3_modules/initiateWeb3');
const contract = require('../web3_modules/coin_abi');
var router = express.Router();
var cors = require('cors');
var router = express.Router();
var decToHex = require("dec-to-hex")
var web3 = Web3.initiateWeb3();




router.post('/', cors(), function(req, res) {
		var coin = contract.getCoinInstance();
		var result = coin.balanceOf(req.body[0].params[0]);
		var balance =""+result.c[0]+result.c[1];
		let temp = parseInt(balance);
		let hex = temp.toString(16);
		
		var Count = web3.eth.getTransactionCount(req.body[2].params[0]);
		web3.eth.getGasPrice(function(err,result){
		res.status(200).json([{"jsonrpc":"2.0","id":req.body.id,"result":"0x"+hex},{"jsonrpc":"2.0","id":req.body.id,"result":result.c[0]},{"jsonrpc":"2.0","id":req.body.id,"result":Count}]);
		});

});

module.exports = router;


