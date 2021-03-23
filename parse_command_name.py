import json


def kakadu():
    d = dict()
    l = []
    l0 = []
    l1 = []
    with open('/home/alex/Desktop/J.json', 'r') as fil:
        pl = json.load(fil)
    for data in pl:
        Alias = data['teamAlias']
        Name = data['teamName']
        if Alias not in l:
            l.append(Alias)
        if Name not in l1:
            l1.append(Name)





    with open('/home/alex/Desktop/teamName.json', 'r') as f:
        pass

kakadu()
