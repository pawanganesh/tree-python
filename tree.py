import json


with open('input.json') as f:
    data = json.load(f)


def solution(data):
    leaves = []
    req = []

    node = {"branches": data}

    if 'branches' in node:
        for branch in node['branches']:
            leaves.extend(get_leaves(branch))
    else:
        leaves.extend(node['leaves'])
    yield leaves

    if(type(data) == dict):
        # current data is a node
        id = data['id']
        req.append((id, get_leaves(data)))
        if 'branches' in data:
            req.extend(get_pair(data['branches']))
    else:
        # current data is a list
        for branch in data:
            req.extend(get_pair(branch))

    yield req


sol = solution(data)

print(next(sol))
print(next(sol))
