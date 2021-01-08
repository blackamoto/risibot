# risibot
bot du FF 

packages à installer avec pip au préalable : ccxt, pandas, requests_html ("pip install XXX")

Utilisation :

- Stop Post Limit : 

Récupérer votre cookie de connexion grâce aux instructions du topic du khey https://www.jeuxvideo.com/forums/42-51-63087978-1-0-1-0-officiel-jvc-py-api-jvc-pour-poster-etc-opensource-github.htm

Le coller dans stop_post.py dans la variable c.
ajouter le lien de vos topic favoris en variable dans stop_post.py, par exemple : 

```
alerte_btc = "http://www.jeuxvideo.com/forums/42-3011927-61017614-1-0-1-0-blabla-alerte-btc.htm"
ethereum = "https://www.jeuxvideo.com/forums/42-3011927-62269929-373-0-1-0-eth-ethereum-2-0.htm"
ripple = https://www.jeuxvideo.com/forums/42-3011927-54909192-1-0-1-0-xrp-ripple.htm
```
Puis 

codez ce que vous voulez avec la fonction .add_stop_post() : 

``` python
client.add_stop_post(topic_url=alerte_btc, message="AYAAAAAAAA", paire="BTC/USDT", condition=">100000")
client.add_stop_post(topic_url=ethereum, message="To the moon", paire="ETH/USDT", condition= ">1400") 
cliet.add_stop_post(topic_url=ripple, message="On vous avait prévenu pourtant", paire="XRP/USDT", condition="<0.10")
client.run()
```


Pour finir lancez le fichier python dans un terminal avec la commande :

```
python stop_post.py
```


Autres fonctions à venir : 

- le Stop Stop Loss (SSL) : poser un stop loss seulement une fois un prix de validation atteint, (ex achat de bas de range, stop si sortie du range par le haut, stop placé au milieu du range initial)

- le Stop Market Multi (SMM) : enclencher une action de trade sur une paire seulement si l'autre paire a réuni une condition (ex acheter du Litecoin peu importe son prix lorsque le Bitcoin atteint 30000$).
- le Whatever Trade First (WTF) : multiplier votre liquidité en postant plusieurs ordres limit sur plusieurs paires

- le Panic Sell Market (PSM) : TP un certain pourcentage de votre wallet d'un seul coup sur toutes vos paires le plus rapidement possible, selon une condition ou manuellement. Un script executable à garder sur votre bureau en cas de panique totale pour éviter d'ouvrir 10 onglets d'un coup

