def greatest_nextnumber(number_list):
    # Handle edge cases
    if len(number_list) < 2:
        return "Need at least 2 numbers in the list"
    
    # Initialize with negative infinity so any number will be greater
    greatest_number = float("-inf")
    next_greatest_number = float("-inf")
    
    for number in number_list:
        if number > greatest_number:
            # Current number is greater than greatest
            next_greatest_number,greatest_number = greatest_number,number  # Old greatest becomes second
            #greatest_number = number  # New greatest
        elif number > next_greatest_number and number < greatest_number:
            # Current number is between second greatest and greatest
            next_greatest_number = number
    
    return f"greatest_number is {greatest_number} and next_greatest_number is {next_greatest_number}"

number_list = [111,20,53,24,15,67,9,23,11,84,56]

print(greatest_nextnumber(number_list))

'''  
Absolutely! Let me walk you through the thinking process an interviewer wants to see when solving "find the two largest numbers."
Step 1: Understand the Problem
Your thought process: "Okay, I need to find the largest and second largest numbers. Let me clarify a few things..."
Questions to ask:

"What if there are duplicates? Like [5, 5, 3] - is the second largest 5 or 3?"
"What if the array has less than 2 elements?"
"Do I need to preserve the original array?"

Step 2: Think of Different Approaches
Your internal monologue:
"I can think of a few ways to do this:

Sort the array → pick last two → O(n log n) time
Use built-in max twice → remove max, find max again → O(n) but modifies array
Single pass tracking → keep track of largest and second largest → O(n) time, O(1) space"

Say out loud: "I can think of a sorting approach, but that would be O(n log n). Let me try to do this in one pass for O(n) time."
Step 3: Plan the Algorithm Logic
Your thinking:
"If I go through the array once, I need to keep track of two things:

The largest number I've seen so far
The second largest number I've seen so far

When I see a new number, there are three possibilities:

It's bigger than both → new largest (old largest becomes second)
It's between the two → new second largest
It's smaller than both → ignore it"

Step 4: Handle Edge Cases First
Your approach:
"Let me think about edge cases before I start coding:

Empty array or one element → can't find two largest
All same numbers → largest and second largest are the same
Two elements → just compare them"

Step 5: Code with CommentaryStep-by-step Thinking Process CodeCode def find_two_largest(numbers):
    """
    Step-by-step thinking process for interview
    """
    # STEP 1: Handle edge case
    # "First, let me check if I have enough numbers to work with"
    if len(numbers) < 2:
        return "Need at least 2 nStep 6: Walk Through Your Example
Your verbal explanation:
"Let me trace through [3, 7, 2, 9, 1, 5, 8]:

Start: largest=7, second_largest=3 (comparing first two)
See 2: 2 < 3, so no change
See 9: 9 > 7, so largest=9, second_largest=7
See 1: 1 < 7, so no change
See 5: 5 < 7, so no change
See 8: 8 > 7 but < 9, so second_largest=8
Final: largest=9, second_largest=8"

Step 7: Analyze Complexity
Your conclusion:
"This solution is:

Time complexity: O(n) - I visit each element exactly once
Space complexity: O(1) - I only use two variables regardless of input size
This is optimal because I must look at every number at least once"

Step 8: Consider Edge Cases Again
Your final check:
"Let me make sure this handles edge cases:

Duplicates: ✓ (the current != largest check prevents same number being both)
Small arrays: ✓ (handled upfront)
All same numbers: ✓ (would work correctly)"

Key Interview Points:

Think out loud - show your reasoning process
Start simple - handle basic case first, then edge cases
Trace through examples - prove your logic works
State complexity - show you understand efficiency
Test edge cases - demonstrate thorough thinking

This step-by-step approach shows the interviewer you can break down problems systematically!

'''


# Alternative approach using sorting
def greatest_nextnumber_alt(number_list):
    if len(number_list) < 2:
        return "Need at least 2 numbers in the list"
    
    # Remove duplicates and sort in descending order
    unique_numbers = sorted(set(number_list), reverse=True)
    
    if len(unique_numbers) < 2:
        return "Need at least 2 different numbers in the list"
    
    greatest = unique_numbers[0]
    next_greatest = unique_numbers[1]
    
    return f"greatest_number is {greatest} and next_greatest_number is {next_greatest}"

# Test the functions
test_list = [3, 7, 2, 9, 1, 5, 8]
print(greatest_nextnumber(test_list))
# Output: greatest_number is 9 and next_greatest_number is 8

test_list2 = [10, 10, 8, 8, 6]
print(greatest_nextnumber_alt(test_list2))
# Output: greatest_number is 10 and next_greatest_number is 8
