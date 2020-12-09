input_ = input()
split_ = input_.split()
output_ = []
for i in split_:
    if i.endswith('s'):
        output_.append(i)
print('_'.join(output_))
