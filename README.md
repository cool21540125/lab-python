
# python 練功


Qid  | Date       | Level  | File
---- | ---------- | ------ | --------------------
260  | 2023.09.14 | M      | [SingleNumberIII](./leetcode/SingleNumberIII.py)
1    | 2023.09.16 | E      | [TwoSum](./leetcode/TwoSum.py)
136  | 2023.09.16 | E      | [SingleNumber](./leetcode/SingleNumber.py)
20   | 2023.09.16 | E      | [Valid Parentheses](./leetcode/ValidParentheses.py)

2    | 2023.09.16 | M      | [Add Two Numbers](./leetcode/AddTwoNumbers.py)


# Note

## 2. Add Two Numbers

自行測試成功, 但 leetcode 出現 runtime Error

```
TypeError: ListNode{val: 7, next: ListNode{val: 0, next: ListNode{val: 8, next: None}}} is not valid value for the expected return type ListNode
    raise TypeError(str(ret) + " is not valid value for the expected return type ListNode");
Line 97 in _driver (Solution.py)
    _driver()
Line 104 in <module> (Solution.py)
During handling of the above exception, another exception occurred:
TypeError: unhashable type: 'ListNode'
Line 48 in has_cycle (./python3/listnode.py)
Line 61 in serialize (./python3/listnode.py)
Line 75 in _serialize (./python3/__serializer__.py)
    out = ser._serialize(ret, 'ListNode')
Line 95 in _driver (Solution.py)
```