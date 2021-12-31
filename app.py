from flask import Flask
from flask import jsonify

app = Flask(__name__)

def change(amount):
    """Calculate amount (dollars) change and store the result"""
    res = [] # Result
    coins = [1, 5, 10, 25] # Pennies, Nickels, Dimes, Quarters
    coin_lookup = {25: "Quarters",
                   10: "Dimes",
                   5: "Nickels",
                   1: "Pennies"}

    # Divide the amount in cents by the biggest coin value, record the number
    # of coins that evenly divides and the remainder.
    coin = coins.pop() # Biggest coin value
    num, rem = divmod(int(amount*100), coin)

    # Append coin type and number that had no remainder
    res.append({num:coin_lookup[coin]})

    # While there is still remainder, continue adding coins to the result
    while rem > 0:
        coin = coins.pop()
        num, rem = divmod(rem, coin)
        if num:
            if coin in coin_lookup:
                res.append({num:coin_lookup[coin]})

    return res

@app.route('/')
def hello():
    """Return a HTTP greeting"""
    print("I am inside hello")
    return 'Greetings! I can make change at route: /change'

@app.route('/change/<dollar>/<cents>')
def changeroute(dollar, cents):
    print(f"Change for ${dollar}.{cents}")
    amount = f"{dollar}.{cents}"
    result = change(float(amount))
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
