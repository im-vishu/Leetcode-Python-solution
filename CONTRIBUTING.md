# Contributing to LeetCode Python Solutions

Thank you for your interest in contributing! Your contributions help make this repository a valuable learning resource for everyone. Please follow the guidelines below.

---

## 📌 Guidelines

1. **Fork the Repository**

   * Click the **Fork** button at the top-right of the repository page.
   * Clone your forked repository:

   ```bash
   ```

git clone [https://github.com/](https://github.com/)<your-username>/LeetCode-Python-Solutions.git
cd LeetCode-Python-Solutions

````

2. **Create a Branch**
   - Always create a new branch for your changes:
   ```bash
git checkout -b feature/<problem-id>-<problem-name>
````

3. **Add a New Problem Solution**

   * Place your Python solution inside the `solutions/` folder.
   * Follow the naming convention: `0001_two_sum.py`.
   * Include a **docstring** at the top of the file with:

     ```python
     """
     LeetCode <Problem ID>. <Problem Title>
     https://leetcode.com/problems/<problem-name>/
     Difficulty: <Easy/Medium/Hard>
     Topics: <Array, Hash Table, etc.>
     Description: <Brief 1-3 line problem description>
     """
     ```

4. **Add Tests (Optional)**

   * Add a test file in the `tests/` folder named `test_<problem-id>_<problem-name>.py`.
   * Use `pytest` to test your solution:

     ```python
     from solutions.<solution-file> import Solution

     def test_example():
         assert Solution().<method>() == <expected>
     ```

5. **Update README Table**

   * Run the auto-generate script to update the problem table:

   ```bash
   python tools/generate_readme_table.py
   ```

6. **Commit and Push Changes**

   ```bash
   ```

git add .
git commit -m "Add solution for <Problem ID> <Problem Name>"
git push origin feature/<problem-id>-<problem-name>

```

7. **Open a Pull Request**
   - Go to your forked repository on GitHub.
   - Click **Compare & Pull Request**.
   - Provide a clear description of the problem added and submit.

---

## 💡 Tips

- Ensure your code is **clean and readable**.
- Include **comments** for clarity where necessary.
- Solve the problem yourself **before looking at existing solutions**.
- Keep your branch focused on **one problem at a time**.

---

Thank you for contributing and helping build a comprehensive LeetCode Python Solutions repository! 🚀

```
