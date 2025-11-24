import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from sorting_algorithms.heap_sort import heap_sort


class TestHeapSort:
    def test_empty_list(self):
        assert heap_sort([]) == []

    def test_single_element(self):
        assert heap_sort([20]) == [20]

    def test_sorted_list(self):
        assert heap_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    def test_reverse_sorted(self):
        assert heap_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    def test_duplicates(self):
        assert heap_sort([20, 20, 4, 20, 5]) == [4, 5, 20, 20, 20]

    def test_negative_numbers(self):
        assert heap_sort([-3, -1, -4, -2]) == [-4, -3, -2, -1]

    def test_mixed_numbers(self):
        assert heap_sort([3, -1, 0, -2, 4]) == [-2, -1, 0, 3, 4]

    def test_original_unchanged(self):
        original = [3, 1, 4, 1, 5]
        sorted_arr = heap_sort(original)
        assert original == [3, 1, 4, 1, 5]
        assert sorted_arr == [1, 1, 3, 4, 5]

    def test_none_input(self):
        assert heap_sort(None) == []
