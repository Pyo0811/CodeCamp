import inventory

def add_to_inventory(inventory, added_items) :
    # ここにコードを書きます。
    for s in added_items :
        inventory.setdefault(s,0)        
        print(inventory)
        inventory[s] = inventory[s] + 1
    return inventory

inv = {'金賃' : 42, 'ロープ': 1}
dragon_loot = ['金賃', '手裏剣', '金賃', '金賃', 'ルビー']
inv = add_to_inventory(inv, dragon_loot)
inventory.display_inventory(inv)
