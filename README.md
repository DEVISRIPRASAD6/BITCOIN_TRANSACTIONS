Team Members
Kari Sai Babu - 230001036
Budireddy Devi Sri Prasad - 230001015
Bukya Gnanika - 230041007

Bitcoin Transactions (Legacy and SegWit) on Regtest Network
This guide documents the successful setup and execution of Bitcoin transactions using Legacy and SegWit addresses on the regtest network. All transactions were completed without errors, and the Bitcoin Core node successfully processed both the Legacy and SegWit transactions.

Prerequisites
Ensure that you have the following:

Bitcoin Core installed (bitcoind or bitcoin-qt).

Bitcoin CLI installed (bitcoin-cli).

A Bitcoin Core node running in regtest mode.

Steps Taken
1. Generating Bitcoin Addresses
We generated Legacy and SegWit Bitcoin addresses for use in transactions. These addresses were used in the transactions below.

Legacy Address A': 2MyrX22ozYhuwZ9TPgP8gtcQ5xLWW8bHbG5

Legacy Address B': 2NEtCEpmCQ3nqr7ma3aPiuaXbBEjBG8Nck3

SegWit Address C': 2N4YWJdPasaJAsckKaAy28Kx7JY3rVUeM19

2. Funding Address A'
We funded Legacy Address A' with 1 BTC. The transaction was confirmed successfully.

TXID (Funding A'): 451d615b051b5205be4b382b0c6457edae09a773b79f692bffa7d3504b88c0c1

This transaction was confirmed by mining a block.

3. Creating Legacy Transactions (A' → B' and B' → C')
We created two Legacy transactions as follows:

Legacy Transaction A' → B':

TXID A' → B': 52e6d24664f4728865d3fe71736cc166997a5ddd1af16393b1aa665ba5fb35b9

This Legacy transaction was successfully broadcasted and mined.

Legacy Transaction B' → C':

TXID B' → C': 54838e7493801d7cd045187fd177dc6c746bcefe2d3c18e93906050bc462311c

This Legacy transaction was also successfully broadcasted and mined in the regtest network.

4. Creating Separate SegWit Transaction (B' → C')
We then created a SegWit transaction from B' to C':

SegWit Transaction B' → C':

TXID B' → C': 3f2eab16c98ab709a17f49b9a2e5f9fe3b9844fdeddf4f879bcbe3c1a07b6d90

This SegWit transaction was successfully broadcasted and mined in a separate block on the regtest network.

5. Verifying Transactions
We successfully queried all transactions using bitcoin-cli without encountering any errors.

Commands used:
Get Transaction:
The gettransaction command was successfully used to verify that all transactions were correctly recorded in the wallet.

Get Raw Transaction:
The getrawtransaction command was successfully used to retrieve detailed transaction data, including inputs and outputs.

6. Transaction Confirmation
All transactions were confirmed by mining blocks in the regtest network. We verified the successful confirmation of the following transactions:

Legacy Transaction A' → B': Successfully confirmed with the block hash 626d8f15bf1d8f5fe1b0464d79028281d88f6630d51ed8e40115f9ab10841594.

Legacy Transaction B' → C': Successfully confirmed with the block hash 626d8f15bf1d8f5fe1b0464d79028281d88f6630d51ed8e40115f9ab10841594.

SegWit Transaction B' → C': Successfully confirmed in a separate block.

Results
Legacy Transactions: Successfully completed A' → B' and B' → C' transactions using Legacy addresses.

SegWit Transaction: Successfully completed a SegWit transaction from B' → C'.

Both transaction types were handled successfully without any errors, and the transactions were included in mined blocks.

Troubleshooting and Tips
No Errors Found: Throughout the process, no errors were encountered with the Bitcoin Core node, and all transactions were successfully processed.

Bitcoin Core Node Running: The node was successfully running in regtest mode with no issues.

Helpful Commands
Get Blockchain Info:

bash
Copy
Edit
bitcoin-cli -regtest getblockchaininfo
Get Block Information:

bash
Copy
Edit
bitcoin-cli -regtest getblock <blockhash>
Get Raw Transaction:

bash
Copy
Edit
bitcoin-cli -regtest getrawtransaction <txid> true
Get Transaction Details:

bash
Copy
Edit
bitcoin-cli -regtest gettransaction <txid>
Conclusion
Both Legacy and SegWit transactions were successfully executed on the regtest network. The Bitcoin Core node processed these transactions without encountering any errors, and the transactions were mined and confirmed in the blockchain.

