# lc-642: Design a search autocomplete system [Dictionary solution]

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



class AutocompleteSystem:
	def __init__(self, sentences: List[str], times: List[int]):
		self.history = defaultdict(int)
		for s, t in zip(sentences, times):
			self.history[s] = t
		self.curr_input = ""


	def input(self, c:str)->List[str]:
		# Check for end sentence
		if c == "#":
		# if reached end of sentence keep it in history
			self.history[self.curr_input] += 1			
			self.curr_input = ""
			return []
		# update the current running string keeping track of 
		# curernt search
		self.curr_input += c
		
		# response array
		suggestions = []
		# since the history array is limited size, iterate through each
		for sentence in self.history:
			# if start of sentences match some sentence in history	
			if sentence.startswith(self.curr_input):
			# maintain a tuple of (hotness, sentence)			
				suggestions.append((self.history[sentence], sentence))
		# sort sentences in decreasing order of hotness
		suggestions.sort(reverse=True)
		# return top 3 suggestion
		return [suggestion[1] for suggestion in suggestions[:3]]
