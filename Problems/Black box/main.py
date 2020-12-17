# use the function blackbox(lst) that is already defined
my_own_list = list('dfdjsad')

smt_ = blackbox(my_own_list)

if id(my_own_list) == id(smt_):
    print('modifies')
else:
    print('new')
