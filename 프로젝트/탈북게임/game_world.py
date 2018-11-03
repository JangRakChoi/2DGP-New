# layer 0: Background Objects
# layer 1: Foreground Objects

objects = [[],[],[]]

def add_object(o, layer):
    objects[layer].append(o)

def remove_object(o):
    for i in range(len(objects)-1,0,-1):
        if o in objects[i]:
            objects[i].remove(o)
            del o

def clear():
    for o in all_objects():
        del o
    objects.clear()

def all_objects():
    for i in range(len(objects)):
        for o in objects[i]:
            yield o