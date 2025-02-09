# Input: str = “i.like.this.program.very.much”
# Output: str = “much.very.program.this.like.i”
from audioop import reverse

i_str = "..geeks..for.geeks."
new_str = i_str.split('.')
o_str = '.'.join(new_str[::-1])
print(o_str)