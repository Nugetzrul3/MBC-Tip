Tip MBC
====
Forked from Sugarchain's [Tip Bot](https://github.com/sugarchain-project/Tip-Sugar)

A discord Tip-bot for Microbitcoin

## Demo

![Demo](https://user-images.githubusercontent.com/43717671/57532105-fa58c400-7375-11e9-8730-6d7d4c32399c.gif)

## Usage

Command prefix : `//`

|Command                         |Description                                  |Example                                            |
|--------------------------------|---------------------------------------------|---------------------------------------------------|
|`//info`                        |Show information of MBC.                    |                                                   |
|`//help`                        |Show help message.                           |                                                   |
|`//balance`                     |Show your balances.                          |                                                   |
|`//deposit`                     |Show your deposit address.                   |                                                   |
|`//tip (@mention) (amount)`     |Tip specified amount to specified user.      |`//tip @Nugetzrul3 3.939`                          |
|`//withdraw (address) (amount)` |Send specified amount to specified address.  |`//withdraw 9NAnjoh31HTFGzQXRh1XN226ebsv79vikL 10` |
|`//withdrawall (address)`       |Send your all balances to specified address. |`//withdrawall 9NAnjoh31HTFGzQXRh1XN226ebsv79vikL` |

### Tips

withdraw-fee is 0.001 MBC.

Number of Confirmations is 6 blocks.

Address type is `bech32` (native segwit).

In `withdraw`, amount must be at least 0.5 MBC.

You can use Tip MBC on DM.

You can donate by tip to Tip MBC. (example : /tip @MBC-Tip 3.939)

The address changes with each deposit, but you can use the previous one. However, it is recommended to use the latest address.

Please do not use Tip MBC addresses as a receiving address for mining rewards to prevent the increase of load due to the increase of UTXO.

## Licence

[MIT](https://github.com/sugarchain-project/Tip-Sugar/blob/master/LICENSE)

## Requirement

* Python 3.5.3 or higher
* [discord.py](https://github.com/Rapptz/discord.py) (rewrite)
* [python-bitcoinrpc](https://github.com/jgarzik/python-bitcoinrpc)

```
python3 -m pip install -U discord.py
```

```
python3 -m pip install python-bitcoinrpc
```

## How to run

1. Edit `config.py`

2. Edit configuration file of coind (bitcoin.conf etc.)

```
daemon=1
server=1
rpcuser={same as config.py}
rpcpassword={same as config.py}
```

3. Run `tipmagi.py`

```
python3 tipmagi.py
```
