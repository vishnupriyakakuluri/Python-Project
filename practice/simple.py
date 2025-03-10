#1
#def minion_game(string):
#     vowels = "AEIOU"
#     kevin_score = 0
#     stuart_score = 0
#
#     for i in range(len(string)):
#         if string[i] in vowels:
#             kevin_score += len(string) - i
#         else:
#             stuart_score += len(string) - i
#
#     if kevin_score > stuart_score:
#         print(f"Kevin {kevin_score}")
#     elif stuart_score > kevin_score:
#         print(f"Stuart {stuart_score}")
#     else:
#         print("Draw")
#
#
# # Example usage
# minion_game("BANANA")

#2=======================================================
# def merge_the_tools(s, k):
#     for i in range(0, len(s), k):  # Iterate in steps of k
#         substring = s[i:i+k]  # Get the substring of length k
#         unique_chars = ""  # Initialize empty string to store unique characters
#         for char in substring:
#             if char not in unique_chars:
#                 unique_chars += char  # Append unique characters
#         print(unique_chars)  # Print the result
#
# # Example usage
# merge_the_tools("AABCAAADA", 3)


#3=====================================================


# def happiness_calculator():
#     # Read input values
#     n, m = map(int, input().split())  # Read n and m (not used directly)
#     arr = list(map(int, input().split()))  # Read the array
#     A = set(map(int, input().split()))  # Read set A (liked elements)
#     B = set(map(int, input().split()))  # Read set B (disliked elements)
#
#     # Compute happiness
#     happiness = sum((1 if num in A else -1 if num in B else 0) for num in arr)
#
#     # Output the result
#     print(happiness)
#
# # Example usage
# # happiness_calculator()  # Uncomment this line to use with standard input

#========================================================

# def happiness_calculator():
#     # Read input values
#     n, m = input().split()  # Read n and m (not used directly)
#     arr = input().split()  # Read the array
#     A = set(input().split())  # Read set A (liked elements)
#     B = set(input().split())  # Read set B (disliked elements)
#
#     # Initialize happiness
#     happiness = 0
#
#     # Iterate through the array and update happiness
#     for num in arr:
#         if num in A:
#             happiness += 1
#         elif num in B:
#             happiness -= 1
#
#     # Output the result
#     print(happiness)
#
# # Example usage
# # happiness_calculator()  # Uncomment this line to use with standard input

#=4=====================================================

# from collections import OrderedDict
#
#
# def word_occurrences():
#     n = int(input().strip())  # Read the number of words
#     word_count = OrderedDict()  # Maintain order of first appearance
#
#     for _ in range(n):
#         word = input().strip()
#         word_count[word] = word_count.get(word, 0) + 1
#
#     print(len(word_count))  # Number of distinct words
#     print(" ".join(map(str, word_count.values())))  # Occurrences in order of appearance
#
# # Example usage
# # word_occurrences()  # Uncomment this line to use with standard input

#5=======================================================


# from itertools import groupby
#
# def compress_string(s):
#     compressed = [(len(list(group)), int(key)) for key, group in groupby(s)]
#     print(" ".join(map(str, compressed)))
#
# # Example usage
# # compress_string("1222311")  # Uncomment this line to test

#=6================================================

# class EvenStream:
#     def __init__(self):
#         self.current = 0
#
#     def get_next(self):
#         num = self.current
#         self.current += 2
#         return num
#
# class OddStream:
#     def __init__(self):
#         self.current = 1
#
#     def get_next(self):
#         num = self.current
#         self.current += 2
#         return num
#
# def print_from_stream(n, stream=None):
#     if stream is None:
#         stream = EvenStream()
#     for _ in range(n):
#         print(stream.get_next())
#
# # Example usage
# if __name__ == "__main__":
#     queries = int(input().strip())
#     for _ in range(queries):
#         stream_name, n = input().split()
#         n = int(n)
#         if stream_name == "even":
#             print_from_stream(n)
#         else:
#             print_from_stream(n, OddStream())

#=========================================================
# class Stream:
#     def __init__(self, start):
#         self.current = start
#         self.step = 2
#
#     def get_next(self):
#         num = self.current
#         self.current += self.step
#         return num
#
# def print_from_stream(n, stream=None):
#     stream = stream or Stream(0)
#     for _ in range(n):
#         print(stream.get_next())
#
# if __name__ == "__main__":
#     for _ in range(int(input().strip())):
#         stream_name, n = input().split()
#         print_from_stream(int(n), Stream(1) if stream_name == "odd" else None)

#==7========================================================

# import re
#
# def replace_logical_operators(n, lines):
#     pattern = r"(?<= )&&(?= )|(?<= )\|\|(?= )"
#     for line in lines:
#         print(re.sub(pattern, lambda x: 'and' if x.group() == '&&' else 'or', line))
#
# # Example usage
# if __name__ == "__main__":
#     n = int(input().strip())
#     lines = [input() for _ in range(n)]
#     replace_logical_operators(n, lines)

#=========================================================
# def replace_logical_operators(n, lines):
#     for line in lines:
#         line = line.replace(" && ", " and ").replace(" || ", " or ")
#         print(line)
#
# # Example usage
# if __name__ == "__main__":
#     n = int(input().strip())
#     lines = [input() for _ in range(n)]
#     replace_logical_operators(n, lines)


#===8===============================================

# from collections import Counter
#
# def most_common_chars(s):
#     counter = Counter(s)
#     sorted_chars = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
#     for char, freq in sorted_chars[:3]:
#         print(char, freq)
#
# # Example usage
# if __name__ == "__main__":
#     s = input().strip()
#     most_common_chars(s)

#===9=================================================

# from collections import deque
#
#
# def can_stack_cubes(cubes):
#     dq = deque(cubes)
#     last = float('inf')  # Initialize last stacked cube size to a large value
#
#     while dq:
#         if dq[0] >= dq[-1]:
#             pick = dq.popleft()
#         else:
#             pick = dq.pop()
#
#         if pick > last:
#             return "No"
#         last = pick
#
#     return "Yes"
#
#
# # Read input
# def main():
#     t = int(input().strip())
#     for _ in range(t):
#         n = int(input().strip())
#         cubes = list(map(int, input().split()))
#         print(can_stack_cubes(cubes))
#
#
# # Example usage
# if __name__ == "__main__":
#     main()
#==10==========================================

# from itertools import combinations
#
#
# def probability_of_a(n, letters, k):
#     indices = list(range(n))
#     a_indices = {i for i, letter in enumerate(letters) if letter == 'a'}
#     total_combinations = list(combinations(indices, k))
#     a_combinations = [comb for comb in total_combinations if any(i in a_indices for i in comb)]
#
#     probability = len(a_combinations) / len(total_combinations)
#     print(f"{probability:.4f}")
#
#
# # Example usage
# if __name__ == "__main__":
#     n = int(input().strip())
#     letters = input().split()
#     k = int(input().strip())
#     probability_of_a(n, letters, k)
#====11====================================================

import math
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return Complex(real, imag)

    def __truediv__(self, other):
        denominator = other.real ** 2 + other.imag ** 2
        real = (self.real * other.real + self.imag * other.imag) / denominator
        imag = (self.imag * other.real - self.real * other.imag) / denominator
        return Complex(real, imag)

    def mod(self):
        return Complex(math.sqrt(self.real ** 2 + self.imag ** 2), 0)

    def __str__(self):
        return "{:.2f}{}{:.2f}i".format(self.real, '+' if self.imag >= 0 else '-', abs(self.imag))
if __name__ == "__main__":
    a_real, a_imag = map(float, input().split())
    b_real, b_imag = map(float, input().split())

    a = Complex(a_real, a_imag)
    b = Complex(b_real, b_imag)

    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    print(a.mod())
    print(b.mod())

#==12=======================================================

# def sort_spreadsheet():
#     # Read n (rows) and m (columns)
#     n, m = map(int, input().split())
#
#     # Read the spreadsheet data
#     data = [list(map(int, input().split())) for _ in range(n)]
#
#     # Read the column index to sort by
#     k = int(input().strip())
#
#     # Sort based on the k-th column (0-indexed)
#     data.sort(key=lambda row: row[k])
#
#     # Print the sorted data
#     for row in data:
#         print(" ".join(map(str, row)))
#
#
# # Example usage
# if __name__ == "__main__":
#     sort_spreadsheet()

#==============================================

# import re
#
# def is_valid_email(s):
#     pattern = r'^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$'
#     return re.match(pattern, s) is not None
#
# def filter_and_sort_emails(n, emails):
#     valid_emails = sorted(filter(is_valid_email, emails))
#     print(valid_emails)
#
# # Example usage
# if __name__ == "__main__":
#     n = int(input().strip())
#     emails = [input().strip() for _ in range(n)]
#     filter_and_sort_emails(n, emails)


#=======================================================

# import re
# def is_valid_credit_card(card):
#     pattern = r'^[4-6]\d{3}(-?\d{4}){3}$'
#     consecutive_repeats = r'(\d)(\1{3,})'
#     if re.match(pattern, card) and not re.search(consecutive_repeats, card.replace('-', '')):
#         return "Valid"
#     return "Invalid"
# def validate_credit_cards(n, cards):
#     for card in cards:
#         print(is_valid_credit_card(card))
# # Example usage
# if __name__ == "__main__":
#     n = int(input().strip())
#     cards = [input().strip() for _ in range(n)]
#     validate_credit_cards(n, cards)

#==========================================================

# import re
#
#
# def is_valid_credit_card(card):
#     # Ensure valid format: Starts with 4, 5, or 6 and is either 16 digits or grouped in XXXX-XXXX-XXXX-XXXX format
#     if not re.match(r'^[4-6]\d{3}(-?\d{4}){3}$', card):
#         return "Invalid"
#
#     # Remove hyphens and check for 4 or more consecutive repeating digits
#     card_number = card.replace("-", "")
#     if re.search(r'(\d)\1{3,}', card_number):
#         return "Invalid"
#
#     return "Valid"
#
#
# # Read input
# n = int(input().strip())
# print(n)
# for _ in range(n):
#     print(is_valid_credit_card(input().strip()))
#================================================

# s = input().strip()
# result = []
# count = 1
#
# for i in range(1, len(s)):
#     if s[i] == s[i - 1]:
#         count += 1
#     else:
#         result.append((count, int(s[i - 1])))
#         count = 1
#
# # Append the last group
# result.append((count, int(s[-1])))
#
# # Print output
# print(" ".join(str(item) for item in result))

#=========================================================

# s = input().strip()
#
# # Count occurrences manually
# char_count = {}
# for char in s:
#     if char in char_count:
#         char_count[char] += 1
#     else:
#         char_count[char] = 1
#
# # Convert dictionary to list of tuples
# char_list = [(char, count) for char, count in char_count.items()]
#
# # Custom sorting: Sort by count (descending), then by character (ascending)
# for i in range(len(char_list)):
#     for j in range(i + 1, len(char_list)):
#         if char_list[i][1] < char_list[j][1] or (char_list[i][1] == char_list[j][1] and char_list[i][0] > char_list[j][0]):
#             char_list[i], char_list[j] = char_list[j], char_list[i]  # Swap elements
#
# # Print top 3 characters
# for char, count in char_list[:3]:
#     print(char, count)

#============================================================
# class EvenStream:
#     def __init__(self):
#         self.current = 0
#
#     def get_next(self):
#         self.current += 2
#         return self.current - 2
# class OddStream:
#     def __init__(self):
#         self.current = 1
#
#     def get_next(self):
#         self.current += 2
#         return self.current - 2
# # Fixing the function
# def print_from_stream(n, stream=None):
#     if stream is None:
#         stream = EvenStream()  # Ensure a new instance each time
#     for _ in range(n):
#         print(stream.get_next())
# # Reading input
# q = int(input().strip())  # Number of queries
#
# for _ in range(q):
#     stream_name, n = input().split()
#     n = int(n)
#     if stream_name == "even":
#         print_from_stream(n)  # Use default EvenStream
#     else:
#         print_from_stream(n, OddStream())  # Use a new OddStream
#==============================================================

# def score_words(words):
#     vowels = {'a', 'e', 'i', 'o', 'u', 'y'}  # Use a set for faster lookup
#     score = 0
#     for word in words:
#         num_vowels = sum(1 for letter in word if letter in vowels)  # Count vowels in the word
#         score += 2 if num_vowels % 2 == 0 else 1  # Apply scoring rule
#
#     return score
# # Read input
# n = int(input().strip())  # Number of words
# words = input().strip().split()  # Read words as a list
#
# # Compute and print the score
# print(score_words(words))

#==============================================================


