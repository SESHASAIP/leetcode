class Solution:
    result = 0
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:

        # creating a graph 
        graph = defaultdict(list)
        for a,b in edges:
            graph[a].append(b)

        # making a count map to store max count
        count_map  = defaultdict(int) 

        # running a dfs for each path to find count 
        def dfs(node,current_path):
            current_path.add(node)
            count_map[colors[node]] +=1
            self.result = max(self.result,count_map[colors[node]])
            for c in graph[node]:
                print(c)
                print(current_path)
                if c in current_path:
                    return -1
                else:
                    if dfs(c, current_path) == -1:
                        return -1
            current_path.remove(node)
            count_map[colors[node]] -=1






        # looping to over the each node
        for i in range(len(colors)):
            if dfs(i, set()) == -1:
                return -1 
            # for v in count_map.values():
            # count_map = defaultdict(int)  
        return self.result         
