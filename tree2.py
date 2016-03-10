import sys

class tree:
    def __init__(self, value = 0):
	self.left = None
	self.right = None
	self.value = value

    def getLeft(self):
	return self.left

    def getRight(self):
	return self.right

    def inorder(self):
	if self != None:
	    if self.left != None: self.left.inorder()
	    print self.value
	    if self.right != None: self.right.inorder()

    def insert(self, value):
	if self == None:
	    return
	if value > self.value:
	    if self.right == None: self.right = tree(value)
	    else: self.right.insert(value)
	else:
	    if self.left == None: self.left = tree(value)
	    else: self.left.insert(value)


def main(argv):
    root = tree(10)
    root.insert(25)
    root.insert(13)
    root.insert(20)
    root.insert(9)
    root.inorder()


if __name__ == "__main__":
    try:
	sys.exit(main(sys.argv))
    except Exception as e:
        print str(e)
