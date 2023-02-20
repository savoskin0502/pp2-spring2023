class Good:
    amount = 0

    def __init__(self, name, price, **kwargs):
        self.name = name
        self.price = price
        self.attributes = kwargs
        self.amount += 1

    def __str__(self):
        return f"{self.name}(price={self.price}, attributes={self.attributes})"


class Accountant:
    def __init__(self):
        self.money = 0


class Shop:
    def __init__(self, name, goods: list[Good] = None):
        self.name = name
        self.goods = self.setup_goods(goods=goods)
        self.accountant = Accountant()

    @staticmethod
    def setup_goods(goods):
        if goods is None:
            return []
        return goods

    def display_goods(self):
        for idx, good in enumerate(self.goods):
            print(idx + 1, good, sep=' - ')

    def append(self, good):
        self.goods.append(good)

    def buy(self, index):
        if 1 <= index <= len(self.goods):
            good = self.goods[index - 1]
            del self.goods[index - 1]
            return f'продано {good}'
        return "такого товара нет"


if __name__ == '__main__':
    acc = Accountant()
    macbook = Good(name='MacBook Pro M1', price=1_200_000, ram=32)
    laptop = Good(name='Asus', price=2_200_000, ram=64, cpu=3_600, cpu_count=12)
    kbtu_store = Shop(name='лавка КБТУ', goods=[macbook])
    kbtu_store.append(laptop)

    running = True
    print('`display` - display goods.')
    print('`end` - end.')
    print('`buy n` - buy good.')

    while running:
        command, *args = input().split()
        if command == 'display':
            kbtu_store.display_goods()
        elif command == 'end':
            running = False
            print('пока')
        elif command == 'buy' and len(args):
            print(
                kbtu_store.buy(int(args[0]))
            )
            # print('окей, продано')
