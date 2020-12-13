tup1_location = (1, 2, 3 );
tup2_location = (4, 5, 6 );
tup3_location = (7, 8, 9 );

list1=['1','2','3']
list2=['4','5','6']
list3=['7','8','9']

selected_value=2
location_ticked=''

for xloc in tup1_location:
    if selected_value==xloc:
        list1[xloc-1]='X'
        location_ticked='1'
        print (list1)
        print (list2)
        print (list3)
        break
