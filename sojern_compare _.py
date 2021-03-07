def compareVersion(version1: str, version2: str) -> int:
    v1 = [int(num) for num in version1.split(".")]
    v2 = [int(num) for num in version2.split(".")]
    
    n = max(len(v1), len(v2))
    for i in range(n):
        n1 = v1[i] if i < len(v1) else 0
        n2 = v2[i] if i < len(v2) else 0
        if n1 > n2:
            return 1
        elif n1 < n2:
            return -1
    return 0

print(compareVersion("0.1", "1.1"))
print(compareVersion("1.2.9.9.9.9", "1.3"))
print(compareVersion("1.10", "1.3.4"))