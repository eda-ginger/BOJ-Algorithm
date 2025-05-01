w, h = map(int, input().split())
n = int(input())
rows = []
cols = []
for _ in range(n):
    o, p = input().split()
    p = int(p)
    if o == '0':
        rows.append(p)
    else:
        cols.append(p)

def extract_size(box, m_size):
    box = sorted(box)
    if len(box) == 0:
        return [m_size]
    else:
        if len(box) == 1:
            result = [box[0], m_size - box[0]]
        else:
            result = []
            for i, v in enumerate(box):
                if i == 0:
                    result.append(v)
                elif i == len(box) - 1:
                    nv = m_size - v
                    result.append(v - box[i-1])
                    result.append(nv)
                else:
                    result.append(v - box[i-1])
        return result 

print(max(extract_size(rows, h)) * max(extract_size(cols, w)))