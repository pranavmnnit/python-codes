import sys

class tree:
    d = dict()

    def __repr__(self):
	return str(self.value)

    def __init__(self, value = 0):
	self.left = None
	self.right = None
	self.value = value

    def traverse(self, fun, level = 0):
	if self == None: return
	else:
	    if self.left: self.left.traverse(fun, level+1)
	    fun(self, level)
	    if self.right: self.right.traverse(fun, level+1)

    def insert(self, value):
	if self == None: return
	if value > self.value:
	    if self.right == None: self.right = tree(value)
	    else: self.right.insert(value)
        else:
	    if self.left == None: self.left = tree(value)
	    else: self.left.insert(value)

    @staticmethod
    def addNodetoLevel(node, level = 0):
	tree.d.setdefault(level, []).append(node)

    def printLevels(self):
	for (k, v) in self.d.items():
	    print "%s : %r\n" % (k, v)

def main(argv):
    root = tree(1)
    root.insert(10)
    root.insert(12)
    root.insert(8)
    root.insert(16)
    root.insert(11)
    root.traverse(root.addNodetoLevel)
    root.printLevels()

if __name__ == "__main__":
    sys.exit(main(sys.argv))
