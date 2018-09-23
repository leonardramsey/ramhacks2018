var express = require('express');
const Web3 = require('../web3_modules/initiateWeb3');
const contract = require('../web3_modules/coin_abi');
var router = express.Router();
var cors = require('cors');
var router = express.Router();


router.post('/', cors(), function(req, res) {


		web3.eth.getGasPrice(function(err,result){
			var balance =""+result;
		let temp = parseInt(balance);
		let hex = temp.toString(16);
		console.log("hex:",hex)
				  res.status(200).json({"jsonrpc":"2.0","id":"277506dc58d82254e8952f63a652db8b","result":"0x"+hex});


		});

});

module.exports = router;
