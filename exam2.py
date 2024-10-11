def chewie(word):
	if len(word) < 2:
		return []
	word = word.casefold()
	new_list = []
	for count in range(len(word) - 1):
		pair = str(word[count]) + str(word[count + 1])
		new_list.insert(count, pair)
	return new_list


def pair_frequencies(words):
	pairs = []
	amount_pairs = []
	for count in range(len(words)):
		new_list = chewie(words[count])
		for new_count in range(len(new_list)):
			phrase = str(new_list[new_count])
			pairs.insert(new_count, phrase)
			pairs.insert(new_count + 1, 0)
			value = pairs(new_count + 1) + 1
			amount_pairs.insert(new_count, value)
			print(phrase + ": " + str(amount_pairs[new_count]))
