# Linear Search

### Slide 1:
Hi Everyone!  
Welcome back to Algorismo!

Today, we’re going to explore Linear Search—quite literally the search we use every day.  
Whether it’s finding your keys, looking for a name in a list, or searching through files, this fundamental algorithm is at the heart of our daily routines.

Let’s dive in and see why it’s so indispensable.

---

### Slide 2:
In our first video, we laid the foundation by discussing what algorithms are—step-by-step procedures for solving problems.  
We introduced a simple problem to find the student with the maximum grade from a list of given grades.  
We then discussed how to express the algorithms, beginning with simple pseudocode, and then writing the same using Python.  
Then, we organized our code as the `find_max` function.

In the exercise, we used the same `find_max` function to explore the concept of complexity analysis, where we saw how the number of steps or operations grow with the size of the input.

---

### Slide 3:
Let’s quickly revisit the complexity analysis of the `find_max` function. Here’s the code.

The key part to note is the loop that checks each element in the list to determine if it’s the maximum.  
This operation’s complexity is directly influenced by the input size because, for every additional element in the list, the algorithm performs one more comparison.  
Therefore, the loop at line 3 will execute `n` times for a list of length `n`.  
Whereas, lines 1, 2, and 6 will execute only once no matter the input size.

Summing all these steps results in `3n + 3` as the total number of steps this algorithm will take to find the maximum number from a list of size `n`.  
To simplify further, we can say that as the size of the input grows, `3n + 3` is dominated by `n`, and the effects of constants do not change. This is what we call a linear relationship—if the list size doubles, the number of operations also doubles.

Formally, we can say that the complexity of the `find_max` algorithm is O(n). Understanding this notion of step count or complexity helps us evaluate the efficiency of algorithms, which is crucial when working with large amounts of data.

---

### Slide 4:
Let’s write our `linear_search` algorithm.  
The algorithm to find the maximum number was named the `FindMax` algorithm. Similarly, we name our search algorithm `LinearSearch`, an apt name that clearly reflects its function.

For `LinearSearch`, the input is a list of numbers, and we add an additional input—the target value we’re searching for within that list.  
The output of `LinearSearch` is the position of the target value within the list or `-1` if the target is not found. This indicates whether and where the target exists in the list.

In `FindMax`, we initialized a variable `max` to the first element in the list. In `LinearSearch`, there’s no need for such an initialization. Our focus is solely on finding a match for the target value, so we skip this step.

In both algorithms, we loop through each number in the list. In `FindMax`, we compared the current number to `max`. In `LinearSearch`, we check if it equals the target value.

If a match is found, we return the index of the current element immediately. After the loop completes, if the target is not found, we return `-1`. That’s it!

---

### Slide 5:
Let’s move on to the implementation. On the left, we have the `find_max` function, and on the right, we begin writing the `linear_search` function.  
Both functions use a loop to iterate through the list.

In `linear_search`, if a match is found, the function returns the result immediately.  
If the loop completes without finding a match, `linear_search` returns `-1`, indicating the target isn’t in the list.

---

### Slide 6:
Now, let’s refine our `linear_search` function to make it easier to return the position of the target.  
Instead of using a simple `for` loop, we switch to a `range`-based loop. This loop allows us to work with the index directly, which is crucial for returning the position of the target in the list.

For each index `i`, we check whether the element at that index equals the target. If a match is found, the function immediately returns the index `i`.

---

### Slide 7:
Let’s further refine our `linear_search` function to make the output more informative.  
We’ll store the result of `linear_search` in a variable called `index`.

If `index` equals `-1`, it means the target wasn’t found, so we print a message saying, "The target is not found!"  
Otherwise, we print, "The target is found at location: `index`."

To improve flexibility, we replace the hardcoded target value with an input statement, allowing the user to search for any number without modifying the code.

---

### Slide 8:
Now, let’s demonstrate how you can visualize and step through this code using **PythonTutor**, a great tool for understanding how each line of code is executed.  

We’ll walk through the entire process of running our `linear_search` function with a sample input list and target value. This will help you see how the function progresses, how the loop iterates through the list, and when the function returns the result.

Visit the PythonTutor website, paste the code, and step through it to watch the function in action! You can modify the input list and target to test different scenarios.

---

### Slide 9:
Let’s analyze the complexity of the `linear_search` function by counting the steps involved.

The loop iterates over the list, checking each element. In the **worst case**, the loop checks every element, taking `n` steps. In the **best case**, the target is found at the first position, taking just 1 step.

Inside the loop, the condition is checked every time. If a match is found, the function returns immediately.  
After the loop, if the target wasn’t found, the function returns `-1`.

In the worst case, the total number of steps can be represented as `2n + 3`, which simplifies to `O(n)` in Big-O notation.  
In the best case, the time complexity is `O(1)` because the search completes after a single comparison.

---

### Slide 10:
Let’s recap what we covered today:
1. We analyzed the step count or complexity of our `find_max` algorithm.
2. We briefly defined Big-O notation.
3. We took a deep dive into the `LinearSearch` algorithm, comparing it to `find_max` and refining the code.
4. We conducted a complexity analysis of `LinearSearch` in both best and worst case scenarios.

Check out the exercise on GitHub to explore the step counts of Linear Search in different scenarios!

Coming up next, we’ll explore **Binary Search**, which takes search efficiency to a whole new level.

---

### Slide 11:
That's all for now.  
Thank you for watching and joining me on this journey through algorithms.

Don’t forget to check out the code examples and exercises on our GitHub page.  
See you next time for our lesson on Binary Search. Happy coding!
