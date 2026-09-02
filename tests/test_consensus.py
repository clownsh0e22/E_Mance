import unittest
import hashlib
from consensus.zero_knowledge_tally import ZKTallyEngine

class TestZKTallyEngine(unittest.TestCase):
    def setUp(self):
        self.engine = ZKTallyEngine()
        self.voter_id = "test_operator"
        self.commitment = hashlib.sha256(self.voter_id.encode()).hexdigest()
        self.engine.register_voter(self.commitment)

    def test_valid_proof_tally(self):
        proof = self.engine.generate_proof(self.voter_id, "RATIFY")
        result = self.engine.verify_and_tally(proof)
        self.assertEqual(result["status"], "accepted")
        self.assertEqual(result["device_verified"], "Blockstream Jade Plus")

    def test_invalid_voter_proof(self):
        proof = self.engine.generate_proof("imposter_voter", "RATIFY")
        result = self.engine.verify_and_tally(proof)
        self.assertEqual(result["status"], "rejected")

if __name__ == "__main__":
    unittest.main()
