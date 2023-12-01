import re
values = []
with open("d1.txt") as file:
    for line in file:
        values.append(line.rstrip())
sum = 0
replacements_dictionary = {'one' : 'on1e', 'two' : 'tw2o', 'three' : 'thr3e','four': 'fo4ur', 'five':'fi5ve','six': 'si6x','seven': 'sev7en','eight' :
'ei8ght','nine':'ni9ne'}
for line in values:
    for key,value in replacements_dictionary.items():
        line = line.replace(key, value)
    digits = re.sub('\D','',line)
    sum += int(digits[0] + digits[-1])
print(sum)
