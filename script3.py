import heapq
import os


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


class HuffmanCoding:
    def encode(self, text):
        frequency = self.make_frequency_dict(text)
        heap = self.make_heap(frequency)
        tree = self.merge_nodes(heap)
        codes = self.make_codes(tree)

        encoded_text = self.get_encoded_text(text, codes)
        return encoded_text

    def make_frequency_dict(self, text):
        frequency = {}
        for character in text:
            if not character in frequency:
                frequency[character] = 0
            frequency[character] += 1
        return frequency

    def make_heap(self, frequency):
        heap = []
        for key in frequency:
            node = Node(key, frequency[key])
            heapq.heappush(heap, node)
        return heap

    def merge_nodes(self, heap):
        while (len(heap) > 1):
            node1 = heapq.heappop(heap)
            node2 = heapq.heappop(heap)

            merged = Node(None, node1.freq + node2.freq)
            merged.left = node1
            merged.right = node2

            heapq.heappush(heap, merged)

        return heap[0]

    def make_codes(self, root, current_code="", codes={}):
        if (root == None):
            return
        if (root.char != None):
            codes[root.char] = current_code
        self.make_codes(root.left, current_code + "0", codes)
        self.make_codes(root.right, current_code + "1", codes)
        return codes

    def get_encoded_text(self, text, codes):
        encoded_text = ""
        for character in text:
            encoded_text += codes[character]
        return encoded_text


# Sample Scenario
text = "this is an example of huffman encoding"
huffman = HuffmanCoding()
encoded_text = huffman.encode(text)
print("Encoded Text:", encoded_text)
