class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        is_collide = lambda x, y: x > 0 and y < 0
        for item in asteroids:
            stack.append(item)
            while len(stack) > 1 and is_collide(stack[-2], stack[-1]):

                nv = stack.pop()
                v = stack.pop()

                if abs(nv) > abs(v):
                    stack.append(nv)
                elif abs(nv) < abs(v):
                    stack.append(v)

        return stack
