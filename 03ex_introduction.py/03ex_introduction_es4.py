var = 2
add = 1e-1
for i in range(20):
    var = var + add
    add = add * 1e-1
    print(f'Step {i}')
    print(var)

print("After 14 steps there is no difference in numbers.")
