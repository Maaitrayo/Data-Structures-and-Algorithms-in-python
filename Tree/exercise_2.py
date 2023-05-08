class TreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.parent = None
    
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
    
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        
        return level

    def print_tree(self, level):
        if self.get_level > level:
            return
        spaces = ' '*self.get_level()*3
        prefix = spaces + '|__' if self.parent else ""
        print(prefix + self.name)
        if len(self.children) > 0:
            for child in self.children:
                child.print_tree(level)

def build_management_tree():
    gujarat_head = TreeNode('Gujarat')
    gujarat_head.add_child(TreeNode('Ahmedabad'))
    gujarat_head.add_child(TreeNode('Baroda'))

    karnataka_head = TreeNode('Karnataka')
    karnataka_head.add_child(TreeNode('Banguluru'))
    karnataka_head.add_child(TreeNode('Mysore'))

    india = TreeNode('India')
    india.add_child(gujarat_head)
    india.add_child(karnataka_head)
 
    new_jr_head = TreeNode('New Jersey')
    new_jr_head.add_child(TreeNode('Princeton'))
    new_jr_head.add_child(TreeNode('Trenton'))

    california_head = TreeNode('California')
    california_head.add_child(TreeNode('San Francisco'))
    california_head.add_child(TreeNode('Mountain Vaie'))
    california_head.add_child(TreeNode('Palo Alto'))

    usa = TreeNode('USA')
    usa.add_child(new_jr_head)
    usa.add_child(california_head)

    root = TreeNode("Global")
    root.add_child(india)
    root.add_child(usa)

    return root


if __name__ == '__main__':
    root_node = build_management_tree()
    root_node.print_tree(level = 1) # prints only name hierarchy
    root_node.print_tree(level = 2) # prints only designation hierarchy
    root_node.print_tree(level = 3) # prints both (name and designation) hierarchy