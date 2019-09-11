fname = input("Enter file name: ")
fh = open(fname)
count = 0
tot = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : 
    	continue
    count = count + 1
    number = float(line[21:])
    tot = number + tot
avarage = tot/count
print("Average spam confidence:", avarage)