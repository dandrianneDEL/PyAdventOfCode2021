from mmap import ALLOCATIONGRANULARITY
import filehelper
paths = filehelper.readfile()

class Path:
    start: 'Node' # https://stackoverflow.com/questions/33837918/type-hints-solve-circular-dependency
    target: 'Node'

    def __init__(self, start:'Node', target:'Node') -> None:
        self.start = start
        self.target = target

    def has_visited(self, node1: 'Node', node2: 'Node') -> bool:
        return (node1 == self.start or node1 == self.target) and (node2 == self.start or node2 == self.target)

class Node:
    name: str
    isSmall: bool
    paths = list[Path]

    def __init__(self, name, isSmall) -> None:
        self.name = name
        self.isSmall = isSmall
        self.paths = []

    def is_linked_with(self, node:'Node') -> bool:
        return any(path.start.name == node.name or path.target.name == node.name for path in self.paths)
    
    def link(self, target:'Node') -> None:
        p = Path(self, target)
        self.paths.append(p)
        target.paths.append(p)

    def to_string(self) -> str:
        txt=f"{self.name}(small={self.isSmall}):["
        for path in self.paths:
            if path.start.name == self.name:
                txt += f",{path.target.name}"
            else:
                txt += f",{path.start.name}"
        return f"{txt}]"

# https://www.geeksforgeeks.org/python-test-if-string-contains-any-uppercase-character/
def contains_uppercase(input:str) -> bool:
    return any(ele.isupper() for ele in input)

def init_nodes(paths:dict) -> dict:
    allNodes = {}
    for key in paths.keys():
        isSmall = not contains_uppercase(key)
        allNodes[key] = Node(key, isSmall)
        for path in paths[key]:
            if not path in allNodes.keys():
                isSmall = not contains_uppercase(path)
                allNodes[path] = Node(path, isSmall)
    return allNodes

def link_nodes(paths:dict, nodes:dict) -> dict:
    for key in paths.keys():
        for path in paths[key]:
            start:Node = nodes[key]
            target:Node = nodes[path]
            if not start.is_linked_with(target):
                start.link(target)
    return nodes

def navigate_to_end(start:Node, visited:list[Node], end: Node) -> list[list[Path]]:
    uniquePaths = []
    for path in start.paths:
        if path.start.name == start.name:
            targetNode = path.target
        else:
            targetNode = path.start
        hasVisitedSmallTwice = has_visited_small_cave_twice(visited) 
        if targetNode not in visited or not targetNode.isSmall or (not hasVisitedSmallTwice and targetNode.name not in ['start', 'end']):
            deepcopyVisited = [] + visited
            deepcopyVisited.append(targetNode)
            if targetNode == end:
                uniquePaths.append(deepcopyVisited)
            else:
                subUniquePaths = navigate_to_end(targetNode, deepcopyVisited, end)
                for subPath in subUniquePaths:
                    uniquePaths.append(subPath)
    
    for voyage in uniquePaths:
        pathStr = list(map(lambda p: p.name, voyage))
        print(f"{pathStr}")

    return uniquePaths

def has_visited_small_cave_twice(visited:list[Node])->bool:
    smallNodes = list(filter(lambda n: n.isSmall, visited))
    totalCountDict = {}
    for n in smallNodes:
        if n.name in totalCountDict.keys():
            return True
        else: 
            totalCountDict[n.name] = 1
    return False

# ******************************************
# PART 2 - Navigate all paths
# visit a single small cave twice. 
# Specifically, big caves can be visited any number of times, a single small cave can be visited at most twice, and the remaining small caves can be visited at most once
# how many paths through this cave system are there?
# ******************************************
allNodes = init_nodes(paths)
allNodes = link_nodes(paths, allNodes)
print(f"{list(map(lambda n : allNodes[n].to_string(), allNodes))}")

start = allNodes['start']
end = allNodes['end']
allPaths = navigate_to_end(start, [start], end)

print(f"All possible paths: {len(allPaths)}")