class TreeNode:
    def __init__(self, x):
        self.left = None
        self.right = None
        self.val = x

    # A function to do inorder tree traversal


class YourSolution:
    def __init__(self):
        pass

    def printInorder(self, A, root):
        if root:
            # First recur on left child
            self.printInorder(A, root.left)

            # then print the data of node
            if root.val != None:
                A.append(root.val)

            # now recur on right child
            self.printInorder(A, root.right)

        return A
    # A function to do preorder tree traversal


    def printPreorder(self, A, root):
        if root:
            # First print the data of node
            if root.val != None:
                A.append(root.val)
            # Then recur on left child
            self.printPreorder(A, root.left)

            # Finally recur on right child
            self.printPreorder(A, root.right)

        return A

    def insertTree(self, A, root, i, n):
        if i < n:
            temp = TreeNode(A[i])
            root = temp

            # insert left child
            root.left = self.insertTree(A, root.left,
                                         2 * i + 1, n)

            # insert right child
            root.right = self.insertTree(A, root.right,
                                          2 * i + 2, n)
        return root

if __name__ == '__main__':
    Y = YourSolution()
    tree = [1, None, 2, None, None, 3]
    n = len(tree)
    root = None
    root = Y.insertTree(tree, root, 0, n)
    A = []
    B = []
    print("Preorder traversal of binary tree is")
    Y.printPreorder(A, root)
    for i in A:
        print(i)
    print("\nInorder traversal of binary tree is")
    Y.printInorder(B, root)
    for i in B:
        print(i)


