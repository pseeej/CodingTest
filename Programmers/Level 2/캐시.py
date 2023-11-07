from collections import deque
def solution(cacheSize, cities):
    answer = 0
    
    cache = deque()
    
    if cacheSize == 0:
        return 5*len(cities)
    
    for city in cities:
        city = city.lower()
        inCache = city in cache
        
        if len(cache) < cacheSize and not inCache:
            cache.append(city)
            answer += 5
            
        elif inCache:
            left = []
            
            mid = cache.index(city)
            newcache = deque()
            for i in range(len(cache)):
                if i != mid:
                    newcache.append(cache[i])
            
            cache = newcache
            cache.append(city)
            answer += 1
            
        elif len(cache) >= cacheSize and not inCache:
            cache.popleft()
            cache.append(city)
            answer += 5
            
        # print(city, ":", ' '.join(cache))
            
    
    return answer
