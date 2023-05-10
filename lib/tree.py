class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    # return self.breadth_first_tree_traversal(id)
    return self.depth_first_tree_traversal(id)
  
  def breadth_first_tree_traversal(self, id):
    node = self.root
    nodes_to_visit = [node]

    while len(nodes_to_visit) > 0:
      node = nodes_to_visit.pop(0)
      if id == node['id']:
        return node
      nodes_to_visit = nodes_to_visit + node['children']
      
    return None
  
  def depth_first_tree_traversal(self, id):
    node = self.root
    nodes_to_visit = [node]
    
    while len(nodes_to_visit) > 0:
      node = nodes_to_visit.pop(0)
      
      if id == node['id']:
        return node
      nodes_to_visit = node["children"] + nodes_to_visit
      
    return None


# General Breadth first and Depth first methods ======

def breadth_first_traversal(node):
  result = []
  nodes_to_visit = [node]
  
  while len(nodes_to_visit) > 0:
    node = nodes_to_visit.pop(0)
    result.append(node['value'])
    nodes_to_visit = nodes_to_visit + node['children']
    
  return result

def depth_first_traversal(node):
  result = []
  nodes_to_visit = [node]
  
  while len(nodes_to_visit) > 0:
    node = nodes_to_visit.pop(0)
    
    result.append(node['value'])
    nodes_to_visit = node["children"] + nodes_to_visit
    
  return result

def depth_first_traversal_recursive(node, result = []):
  result.append(node['value'])
  
  for child in node['children']:
    depth_first_traversal_recursive(child, result)
    
  return result

# Debugging functions =================

child4 = {'value': 5, 'children':[]}
child5 = {'value': 6, 'children':[]}
child6 = {'value': 7, 'children': []}
child1 = {'value': 2, 'children':[child4]}
child2 = {'value': 3, 'children':[]}
child3 = {'value': 4, 'children':[child5, child6]}

root = {'value': 1, 'children':[child1, child2, child3]}

print("Breadth", breadth_first_traversal(root))
print("Depth", depth_first_traversal(root))
print("Depth Rec", depth_first_traversal_recursive(root))