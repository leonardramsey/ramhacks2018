var express = require('express');
const Web3 = require('../web3_modules/initiateWeb3');
const contract = require('../web3_modules/coin_abi');
var router = express.Router();
var cors = require('cors');
var router = express.Router();
var decToHex = require("dec-to-hex");
var bigInt = require("big-integer");
var BigNumber = require('bignumber.js');

router.post('/', cors(), function(req, res) {
	var web3 = Web3.initiateWeb3();
	var coin = contract.getCoinInstance();
	var result = coin.balanceOf(req.body.address);
    res.status(200).json({status:1,message:"OK",result:result});
}); 

module.exports = router;
