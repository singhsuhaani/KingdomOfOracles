#Kingdom of Oracles Numerical Inventory List - Suhaani Singh
#This program creates 3 inventory lists for 3 different characters in the TBG
#And prints as a numbered list with a label of the inventory it belongs to


common_inv = ['axe', 'wagon', 'cattle', 'coin pouch']          #defines inventory list for common
knight_inv = ['horse', 'sword', 'armour']                      #defines inventory list for knight
royalty_inv = ['crown', 'books', 'gloves']                     #defines inventory list for royalty

print("Available common items:")                               #label
for index in range(len(common_inv)):                           #loops number of indexes in list  
    item = common_inv[index]                                   #stores item at current index in variable            
    print (f"{index + 1}. {item}")                             #adds 1 to index since it starts at 0

print("Available knight items:")                               #label
for index in range(len(knight_inv)):                           #loops number of indexes in list  
    item = knight_inv[index]                                   #stores item at current index in variable   
    print (f"{index + 1}. {item}")                             #adds 1 to index since it starts at 0

print("Available royalty items:")                              #label 
for index in range(len(royalty_inv)):                          #loops number of indexes in list  
    item = royalty_inv[index]                                  #stores item at current index in variable           
    print (f"{index + 1}. {item}")                             #adds 1 to index since it starts at 0

