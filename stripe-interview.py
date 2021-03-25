class RecordComparator:
    def __init__(self, key, sort_direction):
        self.key = key
        self.lt_value = -1 if sort_direction == "asc" else 1
    def compare(self, record_1, record_2):
        record_1_value = int(record_1[self.key]) if self.key in record_1 else 0
        record_2_value = int(record_2[self.key]) if self.key in record_2 else 0

        if record_1_value < record_2_value:
            return self.lt_value
        elif record_1_value > record_2_value:
            return -1*self.lt_value
        else:
            return 0

class MultileKeyComparator:
    def __init__(self, keys_and_directions):
        self.keys_and_directions = keys_and_directions
    def compare(self, record_1, record_2):
        for key,order in self.keys_and_directions:
            comparator = RecordComparator(key, order)
            compare_result = comparator.compare(record_1, record_2)
            if compare_result != 0:
                return compare_result
        return 0

# def compare(record_1, record_2, key):
#     record_1_value = int(record_1[key]) if key in record_1 else 0
#     record_2_value = int(record_2[key]) if key in record_2 else 0

#     if record_1_value < record_2_value:
#         return -1
#     elif record_1_value > record_2_value:
#         return 1
#     else:
#         return 0

def first_by_sort_order(keys, records):
    if not records:
        return {}

    min_record = records[0]
    comparator = MultileKeyComparator(keys)
    for record in records:
        if comparator.compare(record, min_record) == -1:
            min_record = record

    return min_record

def min_by_key(records, key):
    return first_by_key(records, "asc", key)

def first_by_key(records, sort_direction, key):
    if not records:
        return {}

    min_record = records[0]
    comparator = RecordComparator(key, sort_direction)

    for record in records:
        if comparator.compare(record, min_record) == -1:
            min_record = record

    return min_record

import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(min_by_key([{"a": 1, "b": 2}, {"a": 2}], "a"), {"a": 1, "b": 2})
        self.assertEqual(min_by_key([{"a": 2}, {"a": 1, "b": 2}], "a"), {"a": 1, "b": 2})
        self.assertEqual(min_by_key([{"a": 1, "b": 2}, {"a": 2}], "b"), {"a": 2})
        self.assertEqual(min_by_key([{"a": 1, "b": 2}, {"a": 2}], "b"), {"a": 2})
        self.assertEqual(min_by_key([{}], "b"), {})
        self.assertEqual(min_by_key([{"a": -1}, {"b": -1}], "b"), {"b": -1})

    def test_first_desc(self):
        self.assertEqual(first_by_key([{"a": 1, "b": 2}, {"a": 2}], "desc", "a"), {"a": 2})
        self.assertEqual(first_by_key([{"a": 2}, {"a": 1, "b": 2}], "asc", "a"), {"a": 1, "b": 2})
        self.assertEqual(first_by_key([{"a": 1, "b": 2}, {"a": 2}], "desc" ,"b"), {"a": 1, "b": 2})
        self.assertEqual(first_by_key([{"a": 1, "b": 2}, {"a": 2}], "asc", "b"), {"a": 2})
        self.assertEqual(first_by_key([{}], "asc", "b"), {})
        self.assertEqual(first_by_key([{"a": -1}, {"b": -1}], "asc", "b"), {"b": -1})

    def test_multi_keys(self):
        self.assertEqual(
            first_by_sort_order(
                [("a", "desc")],
                [{"a": 5.0}, {"a": 6.0}]
            ),
            {"a": 6.0}
        )
        self.assertEqual(
            first_by_sort_order(
                [("b", "asc"), ("a", "asc")],
                [{"a": -5, "b": 10}, {"a": -4, "b": 9}]
            ),
            {"a": -4, "b": 9}
        )
        self.assertEqual(
            first_by_sort_order(
                [("b", "asc"), ("a", "asc")],
                [{"a": -5, "b": 10}, {"a": -4, "b": 10}]
            ),
            {"a": -5, "b": 10}
        )

if __name__ == '__main__':
    unittest.main()

