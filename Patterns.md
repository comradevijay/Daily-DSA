# 8 Core DSA Patterns — Python Reference Guide

A practical breakdown of the 8 most common interview patterns, with the core idea, a reusable Python template, complexity, and practice problems for each.

---

## 1. Sliding Window

**Idea:** Instead of recomputing a result for every possible sub-array/substring from scratch (which is usually O(n²) or worse), maintain a "window" (a range defined by two pointers, `left` and `right`) over the data. Expand the window by moving `right`, and shrink it by moving `left` when a condition is violated. This way each element is processed a constant number of times, giving O(n).

**When to use:** Problems involving contiguous subarrays/substrings with a constraint — "longest", "shortest", "contains exactly K", "at most K", "sum equals target".

**Two flavors:**
- **Fixed-size window** — window size is given (e.g., size K).
- **Variable-size window** — window grows/shrinks based on a condition.

**Python template (variable-size):**
```python
def sliding_window_template(s: str, k: int) -> int:
    left = 0
    max_len = 0
    freq = {}

    for right in range(len(s)):
        c = s[right]
        freq[c] = freq.get(c, 0) + 1

        # Shrink window while condition is violated
        while len(freq) > k:
            left_char = s[left]
            freq[left_char] -= 1
            if freq[left_char] == 0:
                del freq[left_char]
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len
```

**Complexity:** O(n) time, O(k) space (for the window's tracking structure).

**Practice problems:**
- Longest Substring Without Repeating Characters
- Longest Substring with At Most K Distinct Characters
- Maximum Sum Subarray of Size K (fixed window)
- Minimum Window Substring
- Permutation in String

---

## 2. Subsets (Combinations / Permutations)

**Idea:** To generate all subsets, combinations, or permutations of a set, you build a decision tree: at each step, decide whether to include/exclude an element (subsets) or which element to place next (permutations). This is typically done with **backtracking** — recursively building a partial solution, and undoing the last choice ("backtrack") to try the next branch. It explores the tree similarly to BFS/DFS, but is usually implemented with DFS-style recursion.

**When to use:** "Find all possible..." problems — subsets, combinations, permutations, partitions.

**Python template (subsets via backtracking):**
```python
def subsets(nums: list[int]) -> list[list[int]]:
    result = []

    def backtrack(start: int, current: list[int]):
        result.append(current[:])  # every prefix is a valid subset

        for i in range(start, len(nums)):
            current.append(nums[i])         # choose
            backtrack(i + 1, current)        # explore
            current.pop()                    # un-choose (backtrack)

    backtrack(0, [])
    return result
```

**Python template (permutations):**
```python
def permute(nums: list[int]) -> list[list[int]]:
    result = []
    used = [False] * len(nums)

    def backtrack(current: list[int]):
        if len(current) == len(nums):
            result.append(current[:])
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            current.append(nums[i])
            backtrack(current)
            current.pop()
            used[i] = False

    backtrack([])
    return result
```

**Complexity:** O(2ⁿ) for subsets, O(n!) for permutations — exponential, since you're enumerating every combination.

**Practice problems:**
- Subsets / Subsets II (with duplicates)
- Permutations / Permutations II
- Combination Sum
- Letter Combinations of a Phone Number
- Palindrome Partitioning

---

## 3. Modified Binary Search

**Idea:** Standard binary search assumes a sorted array and looks for an exact value. The "modified" version adapts the same divide-and-conquer logic to less obvious situations — arrays that are sorted but rotated, arrays with duplicates, or searching for a boundary/condition rather than an exact match. The key skill is figuring out, at each step, **which half is still "search-worthy"** based on extra checks (e.g., comparing `nums[mid]` to `nums[left]`/`nums[right]`).

**When to use:** Sorted (or partially sorted) array problems where brute force is O(n) but you suspect O(log n) is possible.

**Python template (search in rotated sorted array):**
```python
def search(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid

        if nums[left] <= nums[mid]:  # left half is sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:  # right half is sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1
```

**Complexity:** O(log n) time, O(1) space.

**Practice problems:**
- Search in Rotated Sorted Array (I and II — II has duplicates)
- Find Minimum in Rotated Sorted Array
- Find Peak Element
- Search a 2D Matrix
- Find First and Last Position of Element in Sorted Array

---

## 4. Top K Elements (Heap)

**Idea:** When you need the "K largest/smallest/most frequent" elements, sorting the whole dataset is O(n log n) — wasteful when you only need K of them. A **Heap** (Python's `heapq`, which is a min-heap by default) lets you maintain just the top K candidates at all times, giving O(n log k). For "K largest", use a **min-heap of size K** (the smallest of your top-K sits at the top, ready to be evicted when something bigger shows up). For "K smallest", invert your comparisons (push negatives) or use a max-heap equivalent.

**When to use:** "Kth largest/smallest", "K most frequent", "K closest points", scheduling problems.

**Python template (Kth largest element):**
```python
import heapq

def find_kth_largest(nums: list[int], k: int) -> int:
    min_heap = []  # heapq is a min-heap by default

    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)  # remove smallest, keeping only top K

    return min_heap[0]  # smallest of the top K = Kth largest overall
```

**Python template (Top K frequent elements):**
```python
import heapq
from collections import Counter

def top_k_frequent(nums: list[int], k: int) -> list[int]:
    freq = Counter(nums)
    min_heap = []

    for num, count in freq.items():
        heapq.heappush(min_heap, (count, num))
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    return [num for count, num in min_heap]
```

**Complexity:** O(n log k) time, O(k) space.

**Practice problems:**
- Kth Largest Element in an Array
- Top K Frequent Elements
- K Closest Points to Origin
- Find K Pairs with Smallest Sums
- Task Scheduler

---

## 5. Binary Tree DFS

**Idea:** Depth-First Search explores as far down a branch as possible before backtracking — the natural fit for trees, implemented recursively (or with an explicit stack). There are three traversal orders depending on when you "visit" the current node relative to its children:
- **Preorder:** node → left → right
- **Inorder:** left → node → right (gives sorted order for a BST)
- **Postorder:** left → right → node

**When to use:** Problems about depth, paths, subtree properties, or anything where you need to fully explore one branch before moving to the next.

**Python template (max depth — basic recursive DFS):**
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_depth(root: TreeNode) -> int:
    if root is None:
        return 0
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)
    return max(left_depth, right_depth) + 1
```

**Python template (path sum — DFS with path tracking):**
```python
def has_path_sum(root: TreeNode, target_sum: int) -> bool:
    if root is None:
        return False
    if root.left is None and root.right is None:
        return target_sum == root.val
    return (has_path_sum(root.left, target_sum - root.val) or
            has_path_sum(root.right, target_sum - root.val))
```

**Complexity:** O(n) time (visits every node once), O(h) space for the recursion stack (h = tree height).

**Practice problems:**
- Maximum Depth of Binary Tree
- Path Sum / Path Sum II
- Diameter of Binary Tree
- Validate Binary Search Tree
- Lowest Common Ancestor of a Binary Tree

---

## 6. Topological Sort

**Idea:** When you have tasks with dependencies (a Directed Acyclic Graph, or DAG), topological sort gives you a linear ordering where every task appears after everything it depends on. The most common implementation is **Kahn's Algorithm**: compute the in-degree (number of incoming edges) for every node, start with nodes that have in-degree 0 (no dependencies), and process them via BFS — each time you "complete" a node, decrement the in-degree of its neighbors, and queue up any that hit 0.

**When to use:** Scheduling/ordering problems with prerequisites — course schedules, build dependencies, task ordering.

**Python template (Kahn's Algorithm — Course Schedule II):**
```python
from collections import deque

def find_order(num_courses: int, prerequisites: list[list[int]]) -> list[int]:
    graph = [[] for _ in range(num_courses)]
    in_degree = [0] * num_courses

    for course, prereq in prerequisites:
        graph[prereq].append(course)  # prereq -> course
        in_degree[course] += 1

    queue = deque([i for i in range(num_courses) if in_degree[i] == 0])
    order = []

    while queue:
        course = queue.popleft()
        order.append(course)

        for next_course in graph[course]:
            in_degree[next_course] -= 1
            if in_degree[next_course] == 0:
                queue.append(next_course)

    return order if len(order) == num_courses else []  # empty = cycle detected
```

**Complexity:** O(V + E) time (vertices + edges), O(V + E) space.

**Practice problems:**
- Course Schedule (detect if it's possible)
- Course Schedule II (return the actual order)
- Alien Dictionary
- Sequence Reconstruction
- Minimum Height Trees

---

## 7. Binary Tree BFS

**Idea:** Breadth-First Search explores a tree **level by level**, using a **Queue** to keep track of which nodes to visit next. You process all nodes at the current depth before moving to the next depth — perfect for anything where "level" matters.

**When to use:** Level-order traversal, finding the minimum depth, zigzag traversal, connecting nodes at the same level.

**Python template (level order traversal):**
```python
from collections import deque

def level_order(root: TreeNode) -> list[list[int]]:
    result = []
    if root is None:
        return result

    queue = deque([root])

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(current_level)

    return result
```

**Complexity:** O(n) time, O(w) space where w is the maximum width of the tree.

**Practice problems:**
- Binary Tree Level Order Traversal
- Binary Tree Zigzag Level Order Traversal
- Minimum Depth of Binary Tree
- Populating Next Right Pointers in Each Node
- Average of Levels in Binary Tree

---

## 8. Two-Pointer

**Idea:** On a sorted array (or one you can sort), use two indices that move toward each other (or in tandem) instead of nested loops. Typically `left` starts at the beginning and `right` at the end; based on whether the current sum/comparison is too big or too small, you move one pointer inward. This turns an O(n²) brute-force search into O(n).

**When to use:** Sorted array problems involving pairs/triplets — sum targets, closest values, removing duplicates, comparing from both ends.

**Python template (Two Sum II — sorted array):**
```python
def two_sum(numbers: list[int], target: int) -> list[int]:
    left, right = 0, len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return [left + 1, right + 1]  # 1-indexed
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return [-1, -1]
```

**Python template (3Sum — fix one, two-pointer the rest):**
```python
def three_sum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    result = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # skip duplicates

        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1

    return result
```

**Complexity:** O(n) for Two Sum II, O(n²) for 3Sum (one loop + two-pointer inside).

**Practice problems:**
- Two Sum II (sorted input)
- 3Sum / 3Sum Closest
- Container With Most Water
- Remove Duplicates from Sorted Array
- Trapping Rain Water

---

## Quick Decision Guide

| Clue in the problem | Likely pattern |
|---|---|
| "Longest/shortest substring/subarray with condition" | Sliding Window |
| "All possible subsets/combinations/permutations" | Subsets (Backtracking) |
| "Sorted array" + not a plain lookup | Modified Binary Search |
| "Kth largest/smallest" or "top K" | Top K Elements (Heap) |
| "Depth", "path", tree recursion | Binary Tree DFS |
| "Prerequisites", "build order", dependencies | Topological Sort |
| "Level order", "by level" | Binary Tree BFS |
| "Sorted array" + pair/triplet sum | Two-Pointer |