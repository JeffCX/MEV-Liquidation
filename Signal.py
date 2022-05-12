import requests
import json

def get_alpha_account(
    network='kovan', 
    page_size=50,
    health=1
):
    url = f'https://api.compound.finance/api/v2/account?max_health[value]={health}&network={network}&page_size={50}'
    resp = requests.get(url).json()
    return resp

def select_token_to_liquidate_by_account(entry):
    

if __name__ == "__main__":
    resp = get_alpha_account()['accounts']
    print(resp[0][0])
    # print(json.dumps(resp, indent=4))