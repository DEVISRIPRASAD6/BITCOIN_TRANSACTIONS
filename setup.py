import json
from bitcoinrpc.authproxy import AuthServiceProxy

def connect_rpc():
    rpc_user = "SAIBABU"
    rpc_password = "12345"
    rpc_port = 18443
    return AuthServiceProxy(f"http://{rpc_user}:{rpc_password}@127.0.0.1:{rpc_port}")

def setup_wallet(rpc):
    wallet_name = "testwallet"

    # Check if wallet is already loaded
    loaded_wallets = rpc.listwallets()
    if wallet_name in loaded_wallets:
        print(f"Wallet '{wallet_name}' is already loaded.")
        return

    # Check if wallet exists
    wallets = rpc.listwalletdir()
    wallet_exists = any(w["name"] == wallet_name for w in wallets["wallets"])

    if wallet_exists:
        print(f"Loading existing wallet: {wallet_name}")
        rpc.loadwallet(wallet_name)
    else:
        print(f"Creating new wallet: {wallet_name}")
        rpc.createwallet(wallet_name)

    balance = rpc.getbalance()
    print(f"Wallet Balance: {balance} BTC")

if __name__ == "__main__":
    rpc = connect_rpc()
    setup_wallet(rpc)