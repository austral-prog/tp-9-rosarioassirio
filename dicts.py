def create_inventory(items):
    inventory = dict()
    for i in items:
        counter = 0
        for k in items:
            if i == k:
                counter += 1
                inventory[i] = counter  
    return inventory
    
def add_items(inventory, items):
    for i in set(items):
        if i in inventory:
            counter = items.count(i)
            inventory[i] += counter
        else:
            inventory[i] = items.count(i)
    return inventory

def decrement_items(inventory, items):
    for i in set(items):
        if inventory[i] != 0:
            inventory[i] -= items.count(i)
        if inventory[i] < 0:
            inventory[i] = 0
    return inventory


def remove_item(inventory, item):
    if item in inventory.keys():
         del inventory[item]
    return inventory


def list_inventory(inventory):
    new_list = []
    for k,v in inventory.items():
        if v > 0:
            new_list.append((k,v))
    return new_list
