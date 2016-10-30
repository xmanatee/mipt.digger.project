import collections
import numpy as np

class RectangleBuilder:
  def __init__(self):
    self.q = collections.deque()
    pass

  def __call__(self, edges):
    i = -1
    sh = []
    for line in edges:
      i += 1
      j = 0
      cnt_1 = 0
      chosen = []
      for px in line:
        j += 1
        if px == 0:
          if cnt_1 > 15:
            if len(chosen) > 0 and chosen[-1][1] > j - cnt_1 - 3:
              chosen[-1] = (chosen[-1][0], j)
            else:
              chosen.append((j - cnt_1, j))
          cnt_1 = 0
        else:
          cnt_1 += 1
      if len(chosen) > 0:
        sh.append((i, np.array(chosen)))
    self.q.append(sh)
    if len(self.q) > 25:
      self.q.popleft()

    px_on_height = {}
    for fr in self.q:
      for ch in fr:
        if ch[0] not in px_on_height:
          px_on_height[ch[0]] = 0
        ln = 0
        for c in ch[1]:
          ln += c[1] - c[0]
        px_on_height[ch[0]] += ln

    it = px_on_height.items()
    it = sorted(it, key=lambda x: -x[1] if 10 < x[0] < 220 else 100500)
    min_y = 1337
    max_y = -1
    for k, v in it:
      if max(max_y, k) - min(min_y, k) < 20:
        max_y = max(max_y, k)
        min_y = min(min_y, k)

    min_x = 1337
    max_x = -1
    for fr in self.q:
      for ch in fr:
        if min_y <= ch[0] <= max_y:
          min_x = min(min_x, ch[1][0][0])
          max_x = max(max_x, ch[1][-1][1])
    return (min_x, min_y), (max_x, max_y)
