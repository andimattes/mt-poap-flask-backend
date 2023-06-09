from flask import Flask, request, jsonify
from modules.poap import authorization, event_hashes, claims

app = Flask(__name__)


@app.route("/create_subscription", methods=["POST"])
def createSubscription():
    address = request.json["address"]

    if not authorization.validateAccessToken():
        authorization.generateAccessToken()

    hashes = event_hashes.getEventHashes()
    claim_hash = event_hashes.getUnclaimedHash(hashes=hashes)

    if not claim_hash:
        event_hashes.requestEventHashes(numberOfHashes=5, rtype="qr_code")
        return "No unclaimed hashes, new hashes have been requested", 200

    claim_data = claims.getClaimSecret(qr_hash=claim_hash)

    if claim_data["claimed"]:
        return (
            f"Hash {claim_hash} already claimed "
            + f"on {claim_data['claimed_date']} "
            + f"by {claim_data['beneficiary']}",
            200,
        )

    claim_secret = claim_data["secret"]

    claim_response = claims.claimPOAP(address=address, qr_hash=claim_hash, secret=claim_secret)

    data = {'status': "POAP Distributed", 'hash': claim_hash, 'address': address, 'event_id': claim_data['event_id']}

    response = jsonify(data)
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response, 200


@app.route("/update_subscription", methods=["POST"])
def updateSubscription():
    pass


@app.route("/cancel_subscription", methods=["POST"])
def cancelSubscription():
    pass


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000, threaded=True)
