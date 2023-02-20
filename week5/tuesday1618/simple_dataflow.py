# producer - generate data
# processing - processing over your data
# consumers - receivers


def consumer(sequence):  # sequence=processing1
    for item in sequence:
        print(f"processed item - {item}")


def producer():
    for item in range(3):
        yield item


def processing(sequence):  # sequence=producer1
    for item in sequence:
        yield item ** 2


producer1 = producer()
processing1 = processing(producer1)
consumer(sequence=processing1)


