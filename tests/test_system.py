import unittest
import hashlib
from node.node_daemon import E_ManceDaemon
from consensus.zero_knowledge_tally import ZKTallyEngine

class TestE_ManceSystem(unittest.TestCase):
    def test_daemon_and_zk_governance(self):
        daemon = E_ManceDaemon()
        self.assertIsNotNone(daemon.scraper)
        self.assertIsNotNone(daemon.arbiter)
        self.assertIsNotNone(daemon.runtime)
        zk_engine = ZKTallyEngine()
        secret_id = "integration_test_voter"
        commitment = hashlib.sha256(secret_id.encode("utf-8")).hexdigest()
        zk_engine.register_voter(commitment)
        proof = zk_engine.generate_proof(secret_id, vote_choice="APPROVE_INTELLIGENCE_FEED")
        result = zk_engine.verify_and_tally(proof)
        self.assertEqual(result["status"], "accepted")
        self.assertEqual(result["vote"], "APPROVE_INTELLIGENCE_FEED")
        print("System integration test passed successfully.")

if __name__ == "__main__":
    unittest.main()
