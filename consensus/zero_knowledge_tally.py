# Zero-Knowledge Tallying Engine for E_Mance Governance
import hashlib
import json

class ZKTallyEngine:
    def __init__(self):
        self.registered_voters = set()

    def register_voter(self, voter_identity_commitment):
        self.registered_voters.add(voter_identity_commitment)
        print(f"Voter commitment registered: {voter_identity_commitment[:10]}...")

    def generate_proof(self, secret_voter_id, vote_choice):
        # Simulated ZK proof generation (proves membership and validity without revealing identity)
        identity_hash = hashlib.sha256(secret_voter_id.encode('utf-8')).hexdigest()
        proof_payload = {
            "commitment": identity_hash,
            "vote": vote_choice,
            "proof_signature": hashlib.sha256(f"{identity_hash}:{vote_choice}:zk-snark".encode('utf-8')).hexdigest()
        }
        return proof_payload

    def verify_and_tally(self, proof):
        commitment = proof.get("commitment")
        vote = proof.get("vote")
        signature = proof.get("proof_signature")

        # Verify commitment was previously registered
        if commitment not in self.registered_voters:
            return {"status": "rejected", "reason": "Unregistered voter commitment"}

        # Re-verify proof integrity
        expected_sig = hashlib.sha256(f"{commitment}:{vote}:zk-snark".encode('utf-8')).hexdigest()
        if signature != expected_sig:
            return {"status": "rejected", "reason": "Invalid ZK proof signature"}

        return {"status": "accepted", "vote": vote, "verified_commitment": commitment[:10]}

if __name__ == "__main__":
    engine = ZKTallyEngine()
    secret_id = "sovereign_citizen_alpha_777"
    commitment = hashlib.sha256(secret_id.encode('utf-8')).hexdigest()
    
    engine.register_voter(commitment)
    proof = engine.generate_proof(secret_id, vote_choice="VETO_STATE_BUDGET")
    result = engine.verify_and_tally(proof)
    print("ZK Tally Result:", json.dumps(result, indent=2))
