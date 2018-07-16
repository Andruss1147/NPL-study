import sys
for line in sys.stdin:
    user, discipline = line.strip().split()
    print(user + "\t" + "discipline" + "\t" + discipline)
