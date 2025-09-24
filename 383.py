from collections import Counter


def can_construct(ransomNote, magazine):
    # -------------O(n+m)----------------
    # rn_freq = {i: 0 for i in ransomNote}
    # m_freq = {j:0 for j in magazine}

    # for i in ransomNote:
    #     rn_freq[i] += 1
    # for i in magazine:
    #     m_freq[i] += 1

    # for key, value in rn_freq.items():
    #     if key not in m_freq.keys() or value > m_freq[key]:
    #             return False
    # return True

    # --------------O(n+m) but cleaner------------------
    return not (Counter(ransomNote) - Counter(magazine))


print(can_construct('aa', 'aab'))
