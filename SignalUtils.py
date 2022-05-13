import requests
import json
from config import config

def get_alpha_account(
    network='kovan', 
    page_size=50,
    health=1
):
    url = f'https://api.compound.finance/api/v2/account?max_health[value]={health}&network={network}&page_size={50}'
    resp = requests.get(url).json()
    return resp

def select_token_to_liquidate_by_account(
    entry,
    token_filter='cETH',
    heatlh_threshold=0.8,
    balance_threshold=2
):

    result = {}
    for account_info in entry:
        health_score = account_info['health']['value']
        if float(health_score) > heatlh_threshold:
            continue
        address = account_info['address']
        for token_info in account_info['tokens']:
            if(token_info['symbol'] == token_filter):
                borrow_balance_underlying = float(token_info['borrow_balance_underlying']['value'])
                if borrow_balance_underlying > 0 and borrow_balance_underlying <= balance_threshold:
                    result[address] = borrow_balance_underlying
    return result

if __name__ == "__main__":
    resp = get_alpha_account()['accounts']
    result = select_token_to_liquidate_by_account(
        resp,
        token_filter='cETH',
        balance_threshold=2
    )
    print(json.dumps(result, indent=4))