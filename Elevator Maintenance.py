def solution(l):
    # Your code here
      
    result = sorted(l, key=lambda l:[int(i) for i in l.split('.')])
    return(result)       


print(solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]))