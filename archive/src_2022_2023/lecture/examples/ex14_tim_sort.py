"""
Source code from https://gist.github.com/vladris/13bf84513e76b75a60b0eb761207541e

Python Timsort implementation based on the OpenJDK Java implementation
"""

MIN_MERGE = 32
MIN_GALLOP = 7

minGallop = MIN_GALLOP


def minRunLength(n):
    r = 0
    while n >= MIN_MERGE:
        r |= n & 1
        n >>= 1
    return n + r


def binarySort(arr, lo, hi, start):
    if start == lo:
        start += 1

    while start < hi:
        pivot = arr[start]
        left, right = lo, start

        while left < right:
            mid = (left + right) // 2
            if pivot < arr[mid]:
                right = mid
            else:
                left = mid + 1

        arr.pop(start)
        arr.insert(left, pivot)

        start += 1


def reverseRange(arr, lo, hi):
    hi -= 1
    while lo < hi:
        arr[lo], arr[hi] = arr[hi], arr[lo]
        lo += 1
        hi -= 1


def countRunAndMakeAscending(arr, lo, hi):
    runHi = lo + 1
    if runHi == hi:
        return 1

    if arr[lo] > arr[runHi]:  # Descending run
        while runHi < hi and arr[runHi] < arr[runHi - 1]:
            runHi += 1
        reverseRange(arr, lo, runHi)
    else:  # Ascending run
        while runHi < hi and arr[runHi] >= arr[runHi - 1]:
            runHi += 1

    return runHi - lo


def gallopLeft(key, arr, base, len, hint):
    lastOfs, ofs = 0, 1
    if key > arr[base + hint]:
        maxOfs = len - hint
        while ofs < maxOfs and key > arr[base + hint + ofs]:
            lastOfs = ofs
            ofs = (ofs << 1) + 1

        if ofs > maxOfs:
            ofs = maxOfs

        lastOfs += hint
        ofs += hint
    else:
        maxOfs = hint + 1
        while ofs < maxOfs and key <= arr[base + hint - ofs]:
            lastOfs = ofs
            ofs = (ofs << 1) + 1

        if ofs > maxOfs:
            ofs = maxOfs

        lastOfs, ofs = hint - ofs, hint - lastOfs

    lastOfs += 1
    while lastOfs < ofs:
        mid = lastOfs + (ofs - lastOfs) // 2

        if key > arr[base + mid]:
            lastOfs = mid + 1
        else:
            ofs = mid

    return ofs


def gallopRight(key, arr, base, len, hint):
    ofs, lastOfs = 1, 0

    if key < arr[base + hint]:
        maxOfs = hint + 1
        while ofs < maxOfs and key < arr[base + hint - ofs]:
            lastOfs = ofs
            ofs = (ofs << 1) + 1

        if ofs > maxOfs:
            ofs = maxOfs

        lastOfs, ofs = hint - ofs, hint - lastOfs
    else:
        maxOfs = len - hint
        while ofs < maxOfs and key >= arr[base + hint + ofs]:
            lastOfs = ofs
            ofs = (ofs << 1) + 1

        if ofs > maxOfs:
            ofs = maxOfs

        lastOfs += hint;
        ofs += hint;

    lastOfs += 1
    while lastOfs < ofs:
        mid = lastOfs + ((ofs - lastOfs) // 2)
        if key < arr[base + mid]:
            ofs = mid
        else:
            lastOfs = mid + 1
    return ofs


def mergeLo(arr, lo, mid, hi):
    t = arr[lo:mid]
    i, j, k = lo, mid, 0
    global minGallop
    done = False

    while not done:
        count1, count2 = 0, 0
        while (count1 | count2) < minGallop:
            if t[k] < arr[j]:
                arr[i] = t[k]
                count1 += 1
                count2 = 0
                k += 1
            else:
                arr[i] = arr[j]
                count1 = 0
                count2 += 1
                j += 1
            i += 1

            if k == mid - lo or j == hi:
                done = True
                break

        if done:
            break

        while count1 >= MIN_GALLOP or count2 >= MIN_GALLOP:
            count1 = gallopRight(arr[j], t, k, mid - lo - k, 0)
            if count1 != 0:
                arr[i:i + count1] = t[k:k + count1]
                i += count1
                k += count1
                if k == mid - lo:
                    done = True
                    break

            arr[i] = arr[j]
            i += 1
            j += 1
            if j == hi:
                done = True
                break

            count2 = gallopLeft(t[k], arr, j, hi - j, 0)
            if count2 != 0:
                arr[i:i + count2] = arr[j:j + count2]
                i += count2
                j += count2
                if j == hi:
                    done = True
                    break

            arr[i] = t[k]
            i += 1
            k += 1
            if k == mid - lo:
                done = True
                break

            minGallop -= 1

        if minGallop < 0:
            minGallop = 0
        minGallop += 2

    if k < mid - lo:
        arr[i:hi] = t[k:mid - lo]


def mergeHi(arr, lo, mid, hi):
    t = arr[mid:hi]
    i, j, k = hi - 1, mid - 1, hi - mid - 1
    global minGallop
    done = False

    while not done:
        count1, count2 = 0, 0
        while (count1 | count2) < minGallop:
            if t[k] > arr[j]:
                arr[i] = t[k]
                count1 += 1
                count2 = 0
                k -= 1
            else:
                arr[i] = arr[j]
                count1 = 0
                count2 += 1
                j -= 1
            i -= 1

            if k == -1 or j == lo - 1:
                done = True
                break

        if done:
            break

        while count1 >= MIN_GALLOP or count2 >= MIN_GALLOP:
            count1 = j - lo + 1 - gallopRight(t[k], arr, lo, j - lo + 1, j - lo)
            if count1 != 0:
                arr[i - count1 + 1:i + 1] = arr[j - count1 + 1:j + 1]
                i -= count1
                j -= count1
                if j == lo - 1:
                    done = True
                    break

            arr[i] = t[k]
            i -= 1
            k -= 1
            if k == -1:
                done = True
                break

            count2 = k + 1 - gallopLeft(arr[j], t, 0, k + 1, k)
            if count2 != 0:
                arr[i - count2 + 1:i + 1] = t[k - count2 + 1:k + 1]
                i -= count2
                k -= count2
                if k == -1:
                    done = True
                    break

            arr[i] = arr[j]
            i -= 1
            j -= 1
            if j == lo - 1:
                done = True
                break

            minGallop -= 1

        if minGallop < 0:
            minGallop = 0
        minGallop += 2

    if k >= 0:
        arr[lo:i + 1] = t[0:k + 1]


def mergeAt(arr, stack, i):
    assert i == len(stack) - 2 or i == len(stack) - 3

    base1, len1 = stack[i]
    base2, len2 = stack[i + 1]

    stack[i] = (base1, len1 + len2)
    if i == len(stack) - 3:
        stack[i + 1] = stack[i + 2]
    stack.pop()

    k = gallopRight(arr[base2], arr, base1, len1, 0)
    base1 += k
    len1 -= k
    if len1 == 0:
        return

    len2 = gallopLeft(arr[base1 + len1 - 1], arr, base2, len2, len2 - 1)
    if len2 == 0:
        return

    if len1 > len2:
        mergeLo(arr, base1, base2, base2 + len2)
    else:
        mergeHi(arr, base1, base2, base2 + len2)


def mergeCollapse(arr, stack):
    while len(stack) > 1:
        n = len(stack) - 2
        if (n > 0 and stack[n - 1][1] <= stack[n][1] + stack[n + 1][1]) or \
                (n > 1 and stack[n - 2][1] <= stack[n - 1][1] + stack[n][1]):
            if stack[n - 1][1] < stack[n + 1][1]:
                n -= 1
        elif n < 0 or stack[n][1] > stack[n + 1][1]:
            break

        mergeAt(arr, stack, n)


def mergeForceCollapse(arr, stack):
    while len(stack) > 1:
        n = len(stack) - 2
        if n > 0 and stack[n - 1][1] < stack[n + 1][1]:
            n -= 1

        mergeAt(arr, stack, n)


def tim_sort_vladris(arr):
    lo, hi = 0, len(arr)
    stack = []
    nRemaining = hi
    global minGallop
    minGallop = MIN_GALLOP

    if nRemaining < MIN_MERGE:
        initRunLen = countRunAndMakeAscending(arr, lo, hi)
        binarySort(arr, lo, hi, lo + initRunLen)
        return

    minRun = minRunLength(len(arr))

    while nRemaining > 0:
        runLen = countRunAndMakeAscending(arr, lo, hi)

        if runLen < minRun:
            force = min(nRemaining, minRun)
            binarySort(arr, lo, lo + force, lo + runLen)
            runLen = force

        stack.append((lo, runLen))
        mergeCollapse(arr, stack)

        lo += runLen
        nRemaining -= runLen

    mergeForceCollapse(arr, stack)
