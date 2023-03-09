"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node', nodeList: list = None) -> List[int]:
        if not root: return nodeList
        if nodeList == None: nodeList = []
        nodeList.append(root.val)
        for child in root.children:
            self.preorder(child, nodeList)
        return nodeList
