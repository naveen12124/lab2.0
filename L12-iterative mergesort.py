def mergesort(list):
    if len(list) < 2: return list
    mi = int(len(list)/2)
    le = mergesort(list[:mi])
    ri = mergesort(list[mi:])
    return merge(le, ri)

def merge(le, ri):
    if not len(le) or not len(ri): return le or ri
    result = []
    i, j = 0, 0
    while (len(result) < len(le) + len(ri)):
        if le[i] < ri[j]:
            result.append(le[i])
            i+= 1
        else:
            result.append(ri[j])
            j+= 1
        if i == len(le) or j == len(ri):
            result.extend(le[i:] or ri[j:])
            break
    return result


l = list(map(int,input("Enter elements to sort: ").split()))
print("Merge sort : ", mergesort(l))
