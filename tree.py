import json


with open('input.json') as f:
    data = json.load(f)


def has_branch(node):
    try:
        node['branches']
        return True;
    except:
        return False;


def get_leaves(node):
    leaves = []
    if(has_branch(node)):
        for branch in node['branches']:
            leaves.extend(get_leaves(branch))
    else:
        leaves.extend(node['leaves'])
    return leaves;


def get_pair(data):
    req = []
    if(type(data) == dict):
        # current data is a node
        id = data['id']
        req.append((id, get_leaves(data)))
        if(has_branch(data)):
            req.extend(get_pair(data['branches']))
    else:
        # current data is a list
        for branch in data:
            req.extend(get_pair(branch))

    return req    

print(get_leaves({
    "branches": data,
}))

print(get_pair(data))
