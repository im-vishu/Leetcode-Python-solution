# LeetCode Python Solutions 🧠💻

A curated collection of **LeetCode problems solved in Python** — clean, tested, and easy to navigate.

Each solution follows a consistent format with explanations, time and space complexity, and a test case. The goal is to make this repo a go‑to reference for Pythonic LeetCode solutions.

---

## 📁 Repository Structure

```
LeetCode-Python-Solutions/
├── README.md                # Problem table and overview
├── solutions/               # Python solution files
│   ├── lc_1_two_sum.py
│   ├── lc_2_add_two_numbers.py
│   └── ...
├── tests/                   # pytest test files
│   ├── test_lc_1_two_sum.py
│   └── ...
├── tools/                   # helper scripts (auto-generate table)
│   └── generate_readme_table.py
└── requirements.txt
```

---

## 📊 Problem Table

| ID | Title           | Difficulty | Topics            | Solution                                                     | Status   |
| -: | --------------- | ---------- | ----------------- | ------------------------------------------------------------ | -------- |
|  1 | Two Sum         | Easy       | Array, Hash Table | [lc_1_two_sum.py](solutions/lc_1_two_sum.py)                 | ✅ Tested |
|  2 | Add Two Numbers | Medium     | Linked List, Math | [lc_2_add_two_numbers.py](solutions/lc_2_add_two_numbers.py) | ✅ Tested |

*(Table auto‑updates using `tools/generate_readme_table.py`)*

---

## 🧩 Example Solution Template

Each file should include the following structure:

```python
"""
LeetCode 1. Two Sum
https://leetcode.com/problems/two-sum/
Difficulty: Easy
Topics: Array, Hash Table

Approach: Use a hash map to store complements for O(n) lookup.
Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in seen:
                return [seen[comp], i]
            seen[num] = i

if __name__ == "__main__":
    print(Solution().twoSum([2,7,11,15], 9))  # [0, 1]
```

---

## 🧪 Tests

Write simple, clean tests in `tests/` using **pytest**:

```python
from solutions.lc_1_two_sum import Solution

def test_two_sum():
    assert Solution().twoSum([2,7,11,15], 9) == [0,1]
```

Run all tests:

```bash
pytest -v
```

---

## ⚙️ Tools

The script `tools/generate_readme_table.py` scans all solution files and rebuilds the problem table automatically. It extracts metadata (problem ID, title, difficulty, topics) from the file header.

```bash
python tools/generate_readme_table.py
```

---

## 🧠 Contributing

1. Follow file naming convention: `lc_<id>_<title>.py`
2. Add a clear docstring with metadata.
3. Add a test file in `tests/`.
4. Run `pytest` before committing.
5. Run the README table generator.

---

## 🪪 License

MIT License — feel free to use, share, and improve.

---

## 🚀 Goals

* 100+ LeetCode Python solutions.
* Automated README table generation.
* Tested, readable, and consistent solutions.
* Beginner-friendly structure for contributions.

---

**Maintainer:** [@im-vishu](https://github.com/im-vishu)

**Connect:** [LinkedIn](https://www.linkedin.com/in/vishant--chaudhary)
