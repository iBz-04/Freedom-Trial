class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        R = len(ring)
        A = 26
        K = len(key)
        INF = 10**20
        indices = collections.defaultdict(list)
        for index, c in enumerate(ring):
            indices[c].append(index)

        has_cache = [[False] * R for _ in range(K)]
        cache = [[None] * R for _ in range (K)]

        def find_min(index, location):
            if index == K:
                return 0
            if has_cache[index][location]:
                return cache[index][location]

            best = INF
            for next_index in indices[key[index]]:
                best = min(
                    best,
                    find_min(index + 1, next_index)
                    + min(
                        abs(location - next_index),
                        abs(location + R - next_index),
                        abs(next_index + R - location),
                    )
                    + 1
                )
            has_cache[index][location] = True
            cache[index][location] = best
            return best
            
        return find_min(0,0)
