"""
This was also assked in turing code challenge
"""
from typing import List
from collections import defaultdict


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:

        ingress = defaultdict(set)
        egress =defaultdict(set)
        for p, q in trust:
            egress[p].add(q)
            ingress[q].add(p)
        for i in range(1, N+1):
            if len(egress[i]) == 0 and len(ingress[i]) == N - 1:
                return i
        return -1 