'''Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, 
there are exactly 6 routes to the bottom right corner.
1)  (0,0) → (1,0) → (2,0)  
                      ↓  
                      (2,1)  
                      ↓  
                      (2,2)  
    
2)  (0,0) → (1,0)  
              ↓  
              (1,1) → (2,1)  
                      ↓  
                      (2,2)  
    
3)  (0,0) → (1,0)  
              ↓  
              (1,1)  
              ↓  
              (1,2) → (2,2)  
    
4)  (0,0)  
    ↓  
    (0,1) → (1,1) → (2,1)  
                      ↓  
                      (2,2)  

5)  (0,0)  
    ↓  
    (0,1) → (1,1)  
              ↓  
              (1,2) → (2,2)  
    
6)  (0,0)  
    ↓  
    (0,1)  
    ↓  
    (0,2) → (1,2) → (2,2)  


How many such routes are there through a 20x20 grid?'''

import math
# def find_paths(start, end, memo):
#     if start == end:
#         return 1
#     elif start[0] > end[0] or start[1] > end[1]:
#         return 0

#     r_point, b_point = (start[0] + 1, start[1]), (start[0], start[1] + 1)
#     if r_point not in memo:
#         memo[r_point] = find_paths(r_point, end, memo)

#     if b_point not in memo:
#         memo[b_point] = find_paths(b_point, end, memo)

#     return memo[r_point] + memo[b_point]


# print(find_paths((0, 0), (20, 20), {}))

print(math.factorial(40) / (math.factorial(20) * math.factorial(20)))
