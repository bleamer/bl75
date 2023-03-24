# lc-642: Design a search autocomplete system [Trie solution]



# Design a search autocomplete system for a search engine. Users may input a sentence (at least one word and end with a special character '#'). For each character they type except '#', you need to return the top 3historical hot sentences that have prefix the same as the part of sentence already typed. Here are the specific rules:

#     The hot degree for a sentence is defined as the number of times a user typed the exactly same sentence before.
#     The returned top 3 hot sentences should be sorted by hot degree (The first is the hottest one). If several sentences have the same degree of hot, you need to use ASCII-code order (smaller one appears first).
#     If less than 3 hot sentences exist, then just return as many as you can.
#     When the input is a special character, it means the sentence ends, and in this case, you need to return an empty list.


#What is input format ? 
#How will the input be accepted ?
#How to accept the input ?
#Special characters mean end of the sentence, no more suggestions
#End of Word are indicated by “ “

from typing import List
import heapq

class TrieNode:
	def __init__(self):
		self.children = {}
		self.is_end_of_word = False
		self.times = 0


class AutocompleteSystem:
	def __init__(self, sentences: List[str], times: List[int]):
		self.root = TrieNode()
		self.keyword = ""
	
		for i in range(len(sentences)):
			self._insert(sentences[i], times[i])


	def _insert(self, sentence, times):
		node = self.root
		for c in sentence:
			if c not in node.children:
				node.children[c] = TrieNode()
			node = node.children[c]
		node.is_end_of_word = True
		node.times += times

	def _dfs(self, node, prefix, heap):
		if node.is_end_of_word:
			heapq.heappush(heap, (-node.times, prefix))
			if len(heap) > 3:
				heapq.heappop(heap)

		for c in node.children:
			self._dfs(node.children[c], prefix+c, heap)


	def input(self, c:str) -> List[str]:
		if c == "#":
			self._insert(self.keyword, 1)
			self.keyword = ""
			return []
		
		self.keyword += c
		node = self.root
		for ch in self.keyword:
			if ch not in node.children:
				return []
			node = node.children[ch]
		

		heap = []
		self._dfs(node, self.keyword, heap)

		res = []
		while heap:
			res.append(heapq.heappop(heap)[1])
		return res[::-1]


# Time complexity = O(n log k)
# space complexity = O(n)

#In this implementation, we first define a TrieNode class to represent a node in the Trie. Each node has a dictionary of children nodes, a boolean value indicating whether the node represents the end of a word, and a count of how many times the word represented by the node has been typed.

#The AutocompleteSystem class has a constructor that takes two arguments, a list of historical sentences and a list of corresponding times. It initializes an empty root node and inserts each historical sentence and its corresponding count into the Trie using the _insert() method.

#The input() method takes a character as input and returns a list of up to three historical sentences that have the same prefix as the characters input so far. If the input is "#", the method inserts the current sentence into the Trie and returns an empty list. Otherwise, it traverses the Trie to find the node representing the prefix of the current sentence, and performs a depth-first search to find all historical sentences that have that prefix using the _dfs() method. The _dfs() method uses a heap to keep track of the top three historical sentences and their corresponding counts.

#This implementation has a time complexity of O(n log k) for inserting n historical sentences, where k is the maximum number of sentences with the same prefix, and a space complexity of O(n).
