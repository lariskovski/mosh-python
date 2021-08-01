
# recursive, not very optimized
def bad_fibonacci(sequence_index):
    if sequence_index == 0:
        return 0
    elif sequence_index == 1:
        return 1
    else:
        return fibonacci(sequence_index-1) + fibonacci(sequence_index-2)

def fibonacci(sequence_index):
    current = 0
    after = 1

    for _ in range(0, sequence_index + 1):
        current, after = after, current + after
    
    return current

sequence_index = 33

for i in range(sequence_index):
    print(fibonacci(i))

print('##################################')

for i in range(sequence_index):
    print(bad_fibonacci(i))
