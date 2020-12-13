tup1_location = (1, 2, 3 );
tup2_location = (4, 5, 6 );
tup3_location = (7, 8, 9 );
list1=['1','2','3']
list2=['4','5','6']
list3=['7','8','9']
# provide selected_value with values 1 to 9 only
selected_value=5
location_ticked=''

for xloc in tup1_location:
    if selected_value==xloc:
        list1[xloc-1]='X'
        location_ticked='1'
        print (list1)
        break
    
if location_ticked=='':
    print (tup1_location)
    
location_ticked=''

for xloc in tup2_location:
    if selected_value==xloc:
        list2[xloc-4]='X'
        location_ticked='1'
        print (list2)
        break

if location_ticked=='':
    print (tup2_location)
    
location_ticked=''


for xloc in tup3_location:
    if selected_value==xloc:
        list3[xloc-7]='X'
        location_ticked='1'
        print (list3)
        break

if location_ticked=='':
    print (tup3_location)
