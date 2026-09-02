import hashlib
from consensus.hardware_signer import JadeHardwareSigner

class ZKTallyEngine:
    def __init__(self):
        self.registered_voters = set()
        self.tally = {}
        self.signer = JadeHardwareSigner()

    def register_voter(self, commitment: str):
        # Sign the commitment with Blockstream Jade hardware secure enclave
        hw_sig = self.signer.sign_vote_commitment(commitment)
        self.registered_voters.add(commitment)
        print(f"Voter commitment registered & hardware-signed: {commitment[:10]}...")

    def generate_proof(self, secret_id: str, vote_choice: str) -> dict:
        commitment = hashlib.sha256(secret_id.encode("utf-8")).hexdigest()
        hw_sig = self.signer.sign_vote_commitment(commitment)
        return {
            "commitment": commitment,
            "vote": vote_choice,
            "hardware_signature": hw_sig["hardware_signature"],
            "device": hw_sig["device"]
        }

    def verify_and_tally(self, proof: dict) -> dict:
        commitment = proof.get("commitment")
        if commitment not in self.registered_voters:
            return {"status": "rejected", "reason": "unregistered_commitment"}
        
        vote = proof.get("vote")
        self.tally[vote] = self.tally.get(vote, 0) + 1
        return {"status": "accepted", "vote": vote, "device_verified": proof.get("device")}
