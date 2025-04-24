# ✅ Function to calculate the sum of numbers from n down to 1 (inclusive)
# 🔢 For example: if n = 5 → sum = 5 + 4 + 3 + 2 + 1 = 15
# 📌 Uses formula: sum = n * (n + 1) / 2
def add_from_n_to_1_formula(n: int) -> int:
    return int(n * (n + 1) / 2)  # ✅ Converts to integer, because it gives us float

# 🧪 Test the formula-based function
print(add_from_n_to_1_formula(5))  # Output: 15


# ✅ Function to calculate the sum from n to 1 using a loop 🔁
def add_from_n_to_1_loop(n: int) -> int:
    count = 0
    for num in range(n, 0, -1):  # Starts at n, ends at 1 (inclusive)
        count += num
    return count

# 🧪 Test the loop-based function
print(add_from_n_to_1_loop(5))  # Output: 15


# ✅ Tips and Notes 🧠
# ---------------------
# 🔸 Both methods calculate the same result: sum from n down to 1
# 🔸 Formula method ➤ Time complexity: O(1) ⚡ (best for performance)
# 🔸 Loop method ➤ Time complexity: O(n) 🐢 (easier to understand)
# 🔄 Even though the order is reversed (n to 1), the total sum stays the same
# ❗ You can use either method — just based on preference or need!
