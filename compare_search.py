import timeit
from typing import Callable

from bm import boyer_moore_search
from kmp import kmp_search
from rabina import rabin_karp_search


def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()


def benchmark(func: Callable, text_: str, pattern_: str):
    setup_code = f"from __main__ import {func.__name__}"
    stmt = f"{func.__name__}(text, pattern)"
    return timeit.timeit(stmt=stmt, setup=setup_code, globals={'text': text_, 'pattern': pattern_}, number=10)


if __name__ == '__main__':
    article_1 = read_file('article_1.txt')
    article_2 = read_file('article_2.txt')
    real_patterns = ["корисний для", "ациклічного графу"]

    fake_pattern = "розваги вихідного дня"

    for i, article in enumerate([article_1, article_2]):
        results = []
        for pattern in (real_patterns[i], fake_pattern):
            time = benchmark(boyer_moore_search, article, pattern)
            results.append((boyer_moore_search.__name__, pattern, time))
            time = benchmark(kmp_search, article, pattern)
            results.append((kmp_search.__name__, pattern, time))
            time = benchmark(rabin_karp_search, article, pattern)
            results.append((rabin_karp_search.__name__, pattern, time))
        title = f"{'Алгоритм':<30} | {'Підрядок':<30} | {'Час виконання, сек'}"

        print(f'Стаття #{i + 1}')
        print(" " * len(title))
        print(" " * len(title))
        print(title)
        print("-" * len(title))
        for result in results:
            print(f"{result[0]:<30} | {result[1]:<30} | {result[2]}")
        print(" " * len(title))
