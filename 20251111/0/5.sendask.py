class Sender:
    _first_call = True

    @classmethod
    def report(cls):
        if cls._first_call:
            print("Greetings!")
            cls._first_call = False
        else:
            print("Get away!")


class Asker:
    @staticmethod
    def askall(lst):
        for item in lst:
            item.report()


# Тестирование
senders = [Sender() for _ in range(3)]
asker = Asker()
asker.askall(senders)
# Вывод:
# Greetings!
# Get away!
# Get away!