import hashlib
from aggregator.osint_arbiter import OSINTArbiter
from inference.local_runtime import LocalInferenceEngine
from consensus.zero_knowledge_tally import ZKTallyEngine

def main():
    print("=== Starting E_Mance Sovereign Intelligence Pipeline ===")
    
    # 1. OSINT Arbitration
    arbiter = OSINTArbiter()
    feed = arbiter.arbitrate_feed("Decentralized edge networks secure sovereign data", 0.91)
    print(f"[OSINT] Arbitrated Feed: {feed["headline"]}")
    
    # 2. Local Edge Inference
    runtime = LocalInferenceEngine()
    evaluation = runtime.evaluate_intelligence(feed)
    print(f"[Edge Runtime] Verdict: {evaluation["edge_inference_verdict"]}")
    
    # 3. ZK Governance & Hardware Signing
    zk_engine = ZKTallyEngine()
    secret_voter_id = "sovereign_operator_alpha"
    commitment = hashlib.sha256(secret_voter_id.encode("utf-8")).hexdigest()
    
    zk_engine.register_voter(commitment)
    proof = zk_engine.generate_proof(secret_voter_id, vote_choice="RATIFY_INTELLIGENCE")
    result = zk_engine.verify_and_tally(proof)
    
    print(f"[Consensus] Vote Status: {result["status"]}, Device: {result["device_verified"]}")
    print("=== E_Mance Pipeline Completed Successfully ===")

if __name__ == "__main__":
    main()
