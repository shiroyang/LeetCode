class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False]*(len(rooms))

        stack = [0]

        while stack:
            unlocked = stack.pop()
            visited[unlocked] = True
            for key in rooms[unlocked]:
                if not visited[key]:
                    stack.append(key)
        
        if visited.count(True) == len(visited):
            return True
        else:
            return False