class TreeNode:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
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

    def print_tree(self, type):
        if type=='name':
            value = f'{self.name}'
        elif type=='designation':
            value = f'{self.designation}'
        elif type=='both':
            value = f'{self.name} ({self.designation})'

        spaces = ' '*self.get_level()*3
        prefix = spaces + '|__' if self.parent else ""
        print(prefix + value)
        if len(self.children) > 0:
            for child in self.children:
                child.print_tree(type)

def build_management_tree():
    infra_head = TreeNode('Vishwa','Infrastructure Head')
    infra_head.add_child(TreeNode('Dhaval', 'Colud Manager'))
    infra_head.add_child(TreeNode('Abhijit', 'App Manager'))

    hr_head = TreeNode('Gels', 'HR Head')
    hr_head.add_child(TreeNode('Peter', 'Recruitment Manager'))
    hr_head.add_child(TreeNode('Waqas', 'Policy Manager'))

    cto_head = TreeNode('Chinmay', 'CTO')
    cto_head.add_child(TreeNode('Vishwa', 'Infrastructure Head'))
    cto_head.add_child(TreeNode('Amir','Application Head'))

    ceo_head = TreeNode('Nilupul', 'CEO')
    ceo_head.add_child(cto_head)
    ceo_head.add_child(hr_head)

    return ceo_head


if __name__ == '__main__':
    root_node = build_management_tree()
    root_node.print_tree("name") # prints only name hierarchy
    root_node.print_tree("designation") # prints only designation hierarchy
    root_node.print_tree("both") # prints both (name and designation) hierarchy