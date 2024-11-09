# Solution for the task
with open("1_24.txt", "r") as F:
    s = F.read().strip()

maxLen, curLen = 1, 1  # Initialize the maximum and current sequence lengths

for i in range(1, len(s)):
    # Check if the current character is of a different type than the previous one
    if (s[i].isdigit() and s[i-1].isalpha()) or (s[i].isalpha() and s[i-1].isdigit()):
        curLen += 1  # Increase current sequence length
        if curLen > maxLen:
            maxLen = curLen  # Update maximum length if the current sequence is longer
    else:
        curLen = 1  # Reset current sequence length if characters are of the same type

print(maxLen)
