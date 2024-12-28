# implementation of is BST function
def is_BST(t:Tree) -> bool:
    """
    Preconditions: items in the tree must be comparable
    Postconditions: output is true if t is a binary search tree, false otherwise
    """
    if is_empty(t):
        return True
    else:
        the_root = t.root
        
        left_tree = t.left
        left_root = left_tree.root
        
        right_tree = t.right
        right_root = right_tree.root
        
        if left_root == None: 
            left_root_ok = True
        else:
            left_root_ok = (left_root < the_root)
        
        if right_root == None:
            right_root_ok = True
        else:
            right_root_ok = (right_root > the_root)
        
        return (is_BST(left_tree) and is_BST(right_tree) and left_root_ok and right_root_ok)
