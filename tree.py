import sys

class tree:
    def __init__(self, i):
	self.left  = None
	self.right = None
	self.value = i

    def getLeft(self):
	return self.left

    def getRight(self):
	return self.right

    def insert(self, value):
	if self.value == value:
	    return value
	elif value > self.value:
	    return (self.right or tree(value)).insert(value)
	else:
	    return (self.left or tree(value)).insert(value)

    @staticmethod
    def insert2(root, value):
	if root == None:
	    return
	if value > root.value:
	    if root.getRight() == None:
	        root.right = tree(value)
	    else:
	        tree.insert(root.getRight(), value)
	else:
	    if root.getLeft() == None:
	        root.left = tree(value)
            else:
	        tree.insert(root.getLeft(), value)

    @staticmethod
    def inorder(root):
	if root != None:
	    tree.inorder(root.getLeft())
	    print root.value
	    tree.inorder(root.getRight())


def main(argv):
    root = tree(19)
    root.insert(5)
    root.insert(15)
    root.insert(13)
    root.insert(16)
    tree.inorder(root)

#root = tree(19)
#tree.insert2(root, 5)
#tree.insert2(root, 15)
#tree.insert2(root, 13)
#tree.insert2(root, 16)
#tree.inorder(root)

if __name__ == "__main__":
    try:
    	sys.exit(main(sys.argv))
    except Exception as e:
        print "exception: %s" % (str(e))
        sys.exit(1)
