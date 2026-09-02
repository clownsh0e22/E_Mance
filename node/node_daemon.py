# Master Node Daemon for E_Mance
import time
import threading
import json
from aggregator.osint_scraper import OSINTScraper
from aggregator.truth_arbiter import TruthArbiter
from inference.edge_runtime import EdgeRuntime
from node.p2p_mesh import MeshNode

class E_ManceDaemon:
    def __init__(self):
        self.scraper = OSINTScraper()
        self.arbiter = TruthArbiter()
        self.runtime = EdgeRuntime()
        self.mesh = MeshNode(host='127.0.0.1', port=8888)

    def run_cycle(self):
        # Start background server thread for mesh communication
        server_thread = threading.Thread(target=self.mesh.start_server, daemon=True)
        server_thread.start()
        time.sleep(0.5)

        print("--- Starting E_Mance Intelligence Cycle ---")
        feeds = self.scraper.fetch_global_feeds()
        if not feeds:
            print("No feeds collected.")
            self.mesh.stop()
            return

        consensus = self.arbiter.evaluate_consensus(feeds)
        analysis = self.runtime.analyze_intelligence(consensus)
        
        for item in analysis:
            message = {
                "action": "intelligence_broadcast",
                "payload": item
            }
            print(f"Broadcasting verified intelligence to mesh network...")
            self.mesh.send_message('127.0.0.1', 8888, message)

        time.sleep(1)
        self.mesh.stop()

if __name__ == "__main__":
    daemon = E_ManceDaemon()
    daemon.run_cycle()
