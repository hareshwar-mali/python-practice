# Reverse a string
# input: str = “i.like.this.program.very.much”
# output: str = “much.very.program.this.like.i”

input_str = 'i.like.this.program.very.much'
input_str = input_str.split('.')
# type 1 to solve problem
output_str = list(reversed(input_str))
output_str = '.'.join(output_str)
# type 2 to solve problem
print('.'.join(input_str[::-1]))
# print(output_str)