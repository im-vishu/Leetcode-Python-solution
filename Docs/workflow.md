# Problem Solving Workflow

This document outlines a structured approach to solving LeetCode problems efficiently and learning systematically.

---

## 1️⃣ Understand the Problem

* Read the problem carefully, including constraints and examples.
* Identify **inputs**, **outputs**, and **edge cases**.
* Highlight important details such as array size limits or special cases.
* Example: If array length <= 10^5, O(n^2) solutions might be too slow.

**Resources:**

* [LeetCode Problem Guide](https://leetcode.com/explore/)
* [GeeksforGeeks Problem Understanding](https://www.geeksforgeeks.org/fundamentals-of-algorithms/)

---

## 2️⃣ Plan Your Approach

* Start with a **brute-force solution** to understand the problem.
* Identify possible optimizations (hash maps, two pointers, sliding window, recursion, DP).
* Consider multiple approaches and select the one with optimal **time & space complexity**.
* Draw diagrams or examples to visualize algorithms.

**Tips:**

* Think about corner cases.
* Write pseudocode before coding.
* Use whiteboard or paper if needed.

**Resources:**

* [NeetCode Roadmaps](https://neetcode.io/)
* [Striver’s SDE Sheet](https://takeuforward.org/interviews/strivers-sde-sheet/)

---

## 3️⃣ Write Clean Code

* Use meaningful variable names.
* Add **docstrings** with problem ID, title, link, difficulty, topics, and description.
* Modularize code into functions for readability.
* Include comments for non-obvious logic.

**Example Docstring:**

```python
"""
LeetCode 1. Two Sum
https://leetcode.com/problems/two-sum/
Difficulty: Easy
Topics: Array, Hash Map
"""
```

**Resources:**

* [Python PEP 8 Guidelines](https://pep8.org/)
* [Clean Code Practices](https://github.com/ryanmcdermott/clean-code-python)

---

## 4️⃣ Test Your Solution

* Run provided sample test cases.
* Create additional tests for **edge cases** and **large inputs**.
* Use `pytest` for automated testing.

**Example:**

```python
def test_two_sum():
    assert two_sum([2,7,11,15], 9) == [0,1]
```

**Resources:**

* [Pytest Documentation](https://docs.pytest.org/)
* [Effective Python Testing](https://realpython.com/pytest-python-testing/)

---

## 5️⃣ Analyze Complexity

* Determine **time complexity** (Big O notation) and **space complexity**.
* Evaluate if solution can be optimized further.
* Compare multiple approaches in terms of efficiency.

**Resources:**

* [Big O Cheat Sheet](https://www.bigocheatsheet.com/)
* [GeeksforGeeks Complexity Analysis](https://www.geeksforgeeks.org/analysis-of-algorithms-set-1-asymptotic-analysis/)

---

## 6️⃣ Document & Submit

* Save the solution in the correct folder based on difficulty or topic.
* Add a corresponding **tutorial markdown file** explaining your approach.
* Update **progress tracker** and README table.

**Resources:**

* [GitHub Docs for Contribution](https://docs.github.com/en/get-started/quickstart/contributing-to-projects)

---

## 7️⃣ Optional Tips & Best Practices

* Use **visual aids** (flowcharts, diagrams) for complex problems.
* Participate in **LeetCode contests** for time-bound practice.
* Review others’ solutions to learn alternative approaches.
* Maintain a **daily or weekly practice log** to track improvement.

**Free Tools:**

* [Excalidraw](https://excalidraw.com/) — Diagram visualization
* [Draw.io](https://app.diagrams.net/) — Algorithm visualization
* [LeetCode Discuss](https://leetcode.com/discuss/) — Community insights
