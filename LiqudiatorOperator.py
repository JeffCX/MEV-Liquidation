from web3 import Web3, HTTPProvider
from config import *
import time
import json
import binascii
import traceback
from web3.middleware import geth_poa_middleware

class Liquidator:

    def __init__(self):

        print(NODE_URL)
        self.w3 = Web3(HTTPProvider(NODE_URL))
        address = Web3.toChecksumAddress(config[KOVAN_NETWORK]['cETH'])
        self.ctoken_contract = self.w3.eth.contract(address=address, abi=CETH_ABI)
        controller_contract_address = self.ctoken_contract.functions.comptroller.call()
        self.controller_contract = self.w3.eth.contract(
            address=controller_contract_address,
            abi=COMP_CONTROLLER_ABI 
        )

    def get_risk_factor(self):
        return self.controller_contract_address.closeFactorMantissa()

    def liqudate(self, account, token, amount):

        try:

            checksum_address = Web3.toChecksumAddress(ACCOUNT_ADDRESS)
            nonce = self.w3.eth.getTransactionCount(checksum_address)
            cToken_address = config[kovan][token]

            func = getattr(self.contract.functions, '')
            token_txn = func(account, amount, cToken_address).buildTransaction({
                'gas': 140000,
                'gasPrice': self.w3.eth.gasPrice,
                'nonce': nonce,
            })

            signed_txn = self.w3.eth.account.signTransaction(token_txn, private_key=ACCOUNT_PRIVATE_KEY)

            raw_hash = self.w3.eth.sendRawTransaction(signed_txn.rawTransaction)
            tx_hash = '0x' + binascii.hexlify(raw_hash).decode()
            return tx_hash

        except:

            error = traceback.format_exc()
            print(error)
            return None
    

if __name__ == "__main__":
    # operator = Liquidator()
    # risk_factor = operator.get_risk_factor
    # resp = get_alpha_account()['accounts']
    # result = select_token_to_liquidate_by_account(
    #     resp,
    #     token_filter='cETH',
    #     balance_threshold=2
    # )
    # account = resp.keys()[0]
    # amount = resp[account] * 10 ** 18
    # amount_replay = int(amount * risk_factor)
    # operator.liqudate(account, 'cETH', amount_replay)
    pass