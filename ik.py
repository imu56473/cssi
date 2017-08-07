S = raw_input ("please enter  a word:")
collect = []
n = ""

for x in range (0,len(S)):
    if x % 2 == 0:
        n = n + S[x].upper()
    else:
        n = n + S[x].lower()

print (n)
