airdrops = [
    {"id": 1, "name": "Airdrop Card 1", "amount": "1 PolkaDot", "claimed": False},
    {"id": 2, "name": "Airdrop Card 2", "amount": "1 PolkaDot", "claimed": False},
    {"id": 3, "name": "Airdrop Card 3", "amount": "1 PolkaDot", "claimed": False},
    {"id": 4, "name": "Airdrop Card 4", "amount": "1 PolkaDot", "claimed": False},
    {"id": 5, "name": "Airdrop Card 5", "amount": "1 PolkaDot", "claimed": False},
]

def airdrop(card_id):
    card = next((card for card in airdrops if card["id"] == card_id), None)
    if card and not card["claimed"]:
        card["claimed"] = True
        return {"message": f"{card['name']} claimed successfully!", "amount": card["amount"]}
    else:
        return {"message": "This card has already been claimed or does not exist."}
