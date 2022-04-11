# 优先广度搜索
# 优先广度搜索解决的两类问题：有没有和最短

from collections import deque

# 定义图

graph = {}
graph["you"] = {'alice', 'bob', 'claire'}
graph['bob'] = ["anuj", "peggy"]
graph['alice'] = ["peggy"]
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = ['']
graph['peggy'] = ['']
graph['thom'] = ['']
graph['jonny'] = ['']


def person_is_seller(name):
    return name[-1] == 'm'

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person + ' is a mango seller')
                return True
            else:
                search_queue += graph[person] # 添加除了'you'认识的人
                searched.append(person)
    return False

search("you")