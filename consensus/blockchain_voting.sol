// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract DirectDemocracyVeto {
    mapping(bytes32 => uint256) public votes;
    function castVeto(bytes32 proposalId) public {
        votes[proposalId]++;
    }
}
