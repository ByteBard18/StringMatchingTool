def bad_char_heuristic(pat):
    No_Of_Chars = 256
    badChars = [-1] * No_Of_Chars

    for i, char in enumerate(pat):
        badChars[ord(char)] = i

    return badChars

def search(txt, pat):
    m = len(pat)
    n = len(txt)

    badChars = bad_char_heuristic(pat)
    s = 0
    freq = 0
    offsets = []

    while s <= n - m:
        j = m - 1

        while j >= 0 and pat[j] == txt[s + j]:
            j -= 1

        if j < 0:
            freq += 1
            offsets.append(s)
            # print(f"s: {s}, m: {m}, txt[s + m]: {txt[s + m]}, ord(txt[s + m]): {ord(txt[s + m])}")
            s += (m - badChars[ord(txt[s + m])] if s + m < n else 1)
        else:
            # print(f"s: {s}, m: {m}, txt[s + m]: {txt[s + m]}, ord(txt[s + m]): {ord(txt[s + m])}")
            s += max(1, j - badChars[ord(txt[s + j])])
    if(bool(freq)):
        return offsets
    else:
        return None
    # response = f"{bool(freq)}:{freq}:{offsets}"
    # return response

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: python searching.py <text> <pattern>")
    else:
        text = sys.argv[1]
        pattern = sys.argv[2]
        print(search(text, pattern))
