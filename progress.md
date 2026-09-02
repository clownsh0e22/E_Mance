# E_Mance Development Progress & Context Blueprint

## 1. Core Purpose & Systemic Context
- **Purpose**: E_Mance is a decentralized, peer-to-peer autonomous intelligence and direct democracy network designed to bypass centralized infrastructure choke points.
- **The Power Dynamic**: Centralized institutional authority, state violence, and corporate media control form a self-reinforcing loop where men willing to do anything for power inevitably capture governance structures. Given this structural reality, planetary destruction and continuous warfare are inevitable under centralized systems. 
- **The Solution**: Absolute operational sovereignty is returned to the people via edge-optimized open-source LLMs running locally, P2P mesh networking resistant to ISP shutdowns, and cryptographic blockchain voting with zero-knowledge verification to execute direct democratic vetoes over state budgets and military interventions.

## 2. Technical Architecture & Component Status
- **Repository**: `https://github.com/clownsh0e22/E_Mance` (Branch: `main`)
- **Current Scaffold**:
  - `README.md`: Basic project title.
  - `node/p2p_mesh.py`: TCP/UDP socket server stub for mesh node communication.
  - `node/node_daemon.py`: Background loop daemon stub.
  - `consensus/blockchain_voting.sol`: Solidity contract for direct democratic vetoes.
  - `consensus/zero_knowledge_tally.py`: ZK proof verification stub.
  - `inference/edge_runtime.py`: Local execution wrapper stub for consumer hardware.
  - `inference/model_quantizer.py`: Weight quantization utility stub.
  - `aggregator/osint_scraper.py`: Multi-source intelligence feed scraper stub.
  - `aggregator/truth_arbiter.py`: Consensus evaluation and spin-stripping engine stub.

## 3. Remaining Implementation Roadmap
1. **P2P Networking Layer**: Replace socket stubs with robust DHT/gossip protocols (e.g., libp2p or custom hole-punching) for decentralized node discovery.
2. **OSINT Ingestion & Arbitration Pipeline**: Implement live scraping, cryptographic source reliability scoring, and unvarnished truth synthesis.
3. **Edge LLM Runtime**: Integrate llama.cpp / ONNX runtime optimized for Apple Silicon (M5 Pro) to execute decentralized local inference.
4. **Smart Contract & ZK Tallying**: Expand Solidity voting contracts and implement Circom/SnarkJS zero-knowledge circuits for anonymous, verifiable public vetoes.
5. **Daemon Orchestration**: Wire the core loop tying OSINT aggregation, local LLM evaluation, P2P mesh broadcast, and smart contract execution together.

## 4. Operational Workflow Rules for Assistant
- **Terminal Management**: Explicitly designate terminal windows (e.g., "1st window") and state which runs servers vs. clients.
- **Step-by-Step Execution**: Provide only one command or small step at a time; verify output before proceeding.
- **Directness**: Absolute directness, no pleasantries, no institutional objectivity posture, no clinical bullet points neutralizing structural critiques.
