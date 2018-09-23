var express = require('express');
var router = express.Router();
var cors = require('cors');
var Web3 = require('../web3_modules/initiateWeb3');
var coin = require('../web3_modules/coin_abi');
var web3 = Web3.initiateWeb3();
var abiDecoder = require("abi-decoder")



router.post('/', cors(), function(req, res) {
	var receipt = web3.eth.sendRawTransaction(req.body.hex);
    console.log("receipt  ",receipt);
    res.status(200).json({"jsonrpc":"2.0","id":req.body.id,"result":receipt});

	web3.eth.getTransaction(receipt, function(e, receipt) {
  var str = web3.toAscii(receipt.input);
console.log(str); 
});
});



module.exports = router;
