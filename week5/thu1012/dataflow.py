
# producer - generate data
# processing1 - prepare data ( оставить только клиентов какого-то города )
# processing2 - выдавать пенсию всем клиентам ( из processing 1 )
# consumer - читают результат окончательный нашей обработки ( например из processing 1 )

def producer():
    for item in range(2, 5):
        yield item  # return 2, and pause


def processing_1(sequence_gen):
    for item in sequence_gen:  # item - 2
        yield item * 2  # return - 4, pause


def consumer(sequence_gen):
    print('i"m in consumer')
    for item in sequence_gen:  # StopIteration
        print(f"result item - {item}")


producer1 = producer()
proc1 = processing_1(sequence_gen=producer1)
consumer(sequence_gen=proc1)
consumer(sequence_gen=proc1)

# print(next(proc1))
# for item in producer1:
#     print(item * 2)
