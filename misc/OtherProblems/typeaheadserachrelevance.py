# Implement a Netflix like type ahead search system


class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
        self.relevance  = 0


class TypeAheadSearch:

    def __init__(self):
        self.root = TrieNode()


    def insert(self, title, relevance):
        node = self.root

        for c in title:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]

        node.endOfWord = True
        node.relevance = relevance



    def search(self, prefix):
        node = self.root

        for c in prefix:
            if c not in node.children:
                return []
            
            node = node.children[c]

        return self._get_suggestions(node)
    
    def _get_suggestions(self, node):
        suggestions =  []

        if node.endOfWord:
            suggestions.append((node.relevance,""))

        for c, childNode in node.children.items():
            child_suggestions = self._get_suggestions(childNode)
            
            for relevance, suffix in child_suggestions:
                suggestions.append((relevance, c+suffix))


        return sorted(suggestions, reverse=True)[:10]
    
import unittest

class tests(unittest.TestCase):
    def test1(self):
        search_system = TypeAheadSearch()
        search_system.insert('The Matrix', 9)
        search_system.insert('The LOTR', 8)
        search_system.insert('Breaking Bad', 7)
        search_system.insert('The Matrix', 9)
        search_system.insert("Stranger Things", 6)
        search_system.insert("The Crown", 5)

        prefix = 'The'

        suggestions = search_system.search(prefix)

        print('Suggestions for prefix {prefix}:')
        for relevance, suggestion in suggestions:
            print(suggestion)


if __name__ == '__main__':
    unittest.main() 