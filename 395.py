def substring(s, k):
    startIdxTable = {}
    endIdxTable = {}
    for i in range(len(s)):
        if s[i] not in startIdxTable:
            startIdxTable[s[i]] = i
        else:
            endIdxTable[s[i]] = i

    print(s)

def main():
    s1 = "aaabb"
    k1 = 3
    substring(s1, k1)

if __name__ == "__main__":
    main()