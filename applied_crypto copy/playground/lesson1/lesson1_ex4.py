import math

# def num_permutations_no_repeats(n, k):
#     nmk = n - k
#     quotient = 1
#     for i in range(n, nmk, -1):
#         quotient *= i
#     return quotient


words_in_dict = 187632
sec_per_hour = 60 * 60 
words_per_sec = words_in_dict / 0.1
sec_per_year = 60 * 60 * 24 * 365.25
words_per_hour = words_per_sec * sec_per_hour
words_per_year = words_per_sec * sec_per_year
core_hour_cost = 0.005

for k in range(1,6):
    n = words_in_dict ** k
    # n = num_permutations_no_repeats(words_in_dict, k)
    time_to_crack_hours = n / words_per_hour
    time_to_crack_years = n / words_per_year
    print(f"Message space for {k} word phrases and dict size of {words_in_dict}: {n}")
    print(f"This size is 2^{math.log(n,2)}")
    print(f"Time to brute force crack: {time_to_crack_hours} hours; {time_to_crack_years} years")
    print(f"Cost to crack: ${time_to_crack_hours * core_hour_cost}")
    print("-----------------------------------------------------------------------------")