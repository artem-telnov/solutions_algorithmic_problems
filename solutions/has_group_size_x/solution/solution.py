import collections
import math


class Solution:
    def hasGroupsSizeX(self, deck: list[int]) -> bool:
        # Получаем словарь из списка - [1,2,3,1] -> {1: 2, 2: 1, 3: 1}
        # Ключ словаря - это элемент списка, а значение - количество элементов в списке
        d = collections.Counter(deck)

        # Начинаем итерироваться по значениям
        values = iter(d.values())
        # Берем первое значение
        # Мы можем не проверять на то что первого значения нет,
        # deck имеет длину >= 1
        gcd = next(values)

        # Итерируемся по всем значениям
        for value in values:
            # Находим НОК двух чисел
            gcd = math.gcd(gcd, value)

            # Если НОК равен 1, то значит минимальная группа - это 1 и на группы,
            # в которых больше 1го элемента мы разбить не можем
            if gcd == 1:
                return False
        # Если НОК всех чисел больше 1
        # То разбить на группы можно
        return gcd > 1