
def second_largest_number(sample_list):
    largest = 0
    second_largest = 0
    for num in sample_list:
        if largest < num:
            second_largest = largest
            largest = num
        elif (second_largest < num) and (num != largest):
            second_largest = num
    return second_largest

number = second_largest_number([1111,11,21,501,101,111])
print(number)
