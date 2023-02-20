def producer():
    for item in range(0, 3):
        yield item


def processing(sequence):
    for item in sequence:  # sequence - producer()
        print(f'processing {item}')
        yield item * 2


def consumer(sequence):
    for item in sequence:  # sequence - processing(pr)
        yield f'prepared item {item}'


pr = producer()
# for item in pr: print(item * 2)
process1 = processing(sequence=pr)
# for item in process1: print(f'prepared item {item}')
results = consumer(process1)
for final_elem in results:
    print(final_elem)

# producer -> processing() -> consumer() ->
# 0 ->         0 * 2 = 0   -> prepared item 0 ->
