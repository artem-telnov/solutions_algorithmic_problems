# SearchInRotatedSortedArray Problem

## Описание:
Имеется некий отсортированный массив размеров N. 

Массив несколько раз сдвинули, те у каждого элемента индекс увеличился на 1, а у последнего стал равен нулю

Пример:
```python
array = [1, 2, 3, 4, 5]
# first rotate
array # => [5, 1, 2, 3, 4]
...
```
Таким образом получили массив у которого есть неизвестный сдвиг, но он все также отсортирован относительно этого сдвига.

На вход в функцию подается:
-  `nums` - массив с сдвигом, как описано выше
- `target` - число, которое необходимо найти

Необходимо найти `target` и сказать какой у него индекс или `-1` если такого нет.

## Пример
```python
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4 # Потому что 0 имеет index == 4
```

```python
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
```

---
<a href="https://leetcode.com/problems/search-in-rotated-sorted-array/">Задача на LeetCode</a>