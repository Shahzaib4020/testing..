from flask import Flask, request, render_template
from wallet import create_wallet, import_wallet
from features import airdrop

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/create_wallet', methods=['GET'])
def create_wallet_route():
    wallet = create_wallet()
    return render_template('wallet_created.html', wallet=wallet)

@app.route('/import_wallet', methods=['GET', 'POST'])
def import_wallet_route():
    if request.method == 'POST':
        data = request.form['key_or_phrase']
        wallet = import_wallet(data)
        return render_template('wallet_imported.html', wallet=wallet)
    return render_template('import_wallet.html')

@app.route('/nft_marketplace', methods=['GET'])
def nft_marketplace_route():
    # Placeholder for NFT marketplace logic
    return render_template('nft_marketplace.html')

@app.route('/airdrop', methods=['GET', 'POST'])
def airdrop_route():
    if request.method == 'POST':
        card_id = int(request.form['card_id'])
        result = airdrop(card_id)
        return render_template('airdrop_result.html', result=result)
    return render_template('airdrop.html')

@app.route('/confirm_payment', methods=['GET', 'POST'])
def confirm_payment_route():
    # Placeholder for payment confirmation logic
    return render_template('confirm_payment.html')

if __name__ == '__main__':
    app.run(debug=True)
