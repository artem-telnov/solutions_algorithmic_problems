class Solution:

    def roman_to_int(self, s: str) -> int:
        # создаем мапу, которая позволит нам сопоставить
        # римское число, арабскому
        hash_t = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        # создаем стэк и закидываем первое число,
        # сразу преобразив его в арабское
        res = [hash_t[s[0]]]

        for c in s[1::]:
            if res[-1] > hash_t[c]:
                # если текущее больше нового, значит расчет "разряда" закончен.
                #   Мы можем начинать расчет следующего.
                res.append(hash_t[c])
            elif res[-1] == hash_t[c]:
                # если равны, то складываем
                res[-1] += res[-1]
            else:
                res[-1] = hash_t[c] - res[-1]

        return sum(res)
