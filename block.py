import datetime
import hashlib

#defining block
class Block:
	blockNo = 0
	data = None
	next = None
	hash = None
	nonce = 0
	previous_hash = 0x0
	timestamp = datetime.datetime.now()

	def __init__(self,data):
		self.data = data

	def hash(self):
		h =  hashlib.sha256()
		h.update(
		str(self.nonce).encode('utf-8') +
		str(self.data).encode('utf-8') +
		str(self.previous_hash).encode('utf-8') +
		str(self.timestamp).encode('utf-8') +
		str(self.blockNo).encode('utf-8') 
		)
		return h.hexdigest()

	def __str(self):
		#print the value of block
		return "Block Hash: " + str(self.hash()) + "\nBlockNo: " + str(self.blockNo) + "\nBlock Data: " + str(self.data) + "\nHashes: " + str(self.nonce) + "\n--------------"


#define the vlockchain datastructure
class Blockchain:

	maxNonce = 2**32
	diff = 10
	target = 2**(256-diff)
	#generates the first block  in the blockchain
	block = Block("Genesis")
	#set it as the head of the our blockchain
	head = block
	#adds a given block to the chain of blocks
	def add(self, block):
		block.previous_hash = self.block.hash()
		block.blockNo = self.block.blockNo + 1

		self.block.next = block
		self.block = self.block.next

	#determines whether or not we can add a given block to the blockchain
	def mine(self,block):
		for n in range(self.maxNonce):
			if int(block.hash(),16) <= self.target:
				self.add(block)
				print(block)
				break
			else:
				block.nonce +=1


#Print the blockchain
#initialize blockchain
blockchain = Blockchain()

#mine 10 blocks
for n in range(10):
	blockchain.mine(Block("Block " + str(n+1)))

#print out each block in the blockchain
while blockchain.head != None:
	print(blockchain.head)
	blockchain.head = blockchain.head.next	






