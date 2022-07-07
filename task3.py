from typing import Tuple, List, Dict


def intersect(x1: int, x2: int, x3: int, x4: int) -> Tuple[int, int]:
    if x1 <= x4 and x2 >= x3:
        sx = sorted([x1, x2, x3, x4])
        return sx[1], sx[2]


def normalize(lst: list) -> List[int]:
    j = 0
    while j < len(lst):
        lst = list(filter(lambda x: x != 0, lst))
        for i in range(j + 2, len(lst), 2):
            if lst[j] <= lst[i + 1] and lst[j + 1] >= lst[i]:  # intervals intersecting
                # join intersecting intervals:
                lst[j] = min(lst[j], lst[i])
                lst[j + 1] = max(lst[j + 1], lst[i + 1])
                lst[i], lst[i + 1] = 0, 0
        j += 2
    return lst


def appearance(intervals: Dict[str, List[int]]) -> int:
    ppl = normalize(intervals['pupil'])
    ttr = normalize(intervals['tutor'])
    res = 0
    for i in range(0, len(ppl), 2):
        for j in range(0, len(ttr), 2):
            ppl_ttr = intersect(ppl[i], ppl[i + 1], ttr[j], ttr[j + 1])
            if ppl_ttr:
                all_in = intersect(*ppl_ttr, *intervals['lesson'])
                res += all_in[1] - all_in[0]
    return res


tests = [
    {'data': {'lesson': [1594663200, 1594666800],
              'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
              'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
     },
    {'data': {'lesson': [1594702800, 1594706400],
              'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150,
                        1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480,
                        1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503,
                        1594706524, 1594706524, 1594706579, 1594706641],
              'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
     'answer': 3577
     },
    {'data': {'lesson': [1594692000, 1594695600],
              'pupil': [1594692033, 1594696347],
              'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
     'answer': 3565
     },
]

if __name__ == '__main__':
    for i, test in enumerate(tests):
        test_answer = appearance(test['data'])
        assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
