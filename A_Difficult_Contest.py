# Bismillahir Rahmanir Rahim
# Jahidul Islam, Green University Of Bangladesh
# @JahidulZaid


t = int(input())
for _ in range(t):
    s = input()
    sorted_s = ''.join(sorted(s))

    if "FFT" in sorted_s or "NTT" in sorted_s:
        print(''.join(reversed(sorted_s)))
    else:
        print(sorted_s)
