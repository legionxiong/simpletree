class SIMPLETREE(object):
    def __init__(self):
        self.tree = {}
        self.root = None
        self._depth = {}
        self.curr_depth = 0
        self.curr_node = []
  
    def add(self, node, parent=None):
        if parent:
            self.set_curr_node(parent)
        if not self.tree:
            self.root = node
        elif node not in self.curr_node:
            self.curr_node.append(node)
        self.curr_depth += 1
        self.tree[node] = self.curr_node = []
        self._depth[node] = self.curr_depth
  
    def set_curr_node(self, node):
        self.curr_node = self.tree[node]
        self.curr_depth = self._depth[node]
  
    def delete(self, node):
        if node not in self.tree:
            print('No such node in this tree!')
            return
        self.tree.pop(node)
        for k, v in self.tree.iteritems():
            if node in v:
                v.remove(node)
                self.curr_node = self.tree[k]
        self.clean_up(self.depth())
  
    def clean_up(self, r=0):
        keys = self.tree.keys()
        vals = self.tree.values()
        nodes = [n for node in vals for n in node]
        nodes.append(self.root)
        for k in keys:
            if k not in nodes:
                self.tree.pop(k)
        depth_keys = self._depth.keys()
        for dk in depth_keys:
            if dk not in nodes:
                self._depth.pop(dk)
        r -= 1
        if r > 0:
            self.clean_up(r)
  
    def parent(self, node):
        for k, v in self.tree.iteritems():
            if node in v:
                return k
    
    def children(self, node):
        return self.tree[node]
  
    def depth(self):
        return max(self._depth.values())