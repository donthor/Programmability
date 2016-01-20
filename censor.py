def median(numbers):
    numsort = sorted(numbers)
    print len(numsort)
    if len(numsort) % 2 != 0:
        mid = (len(numsort) - 1) / 2
        mediannum = numsort[mid]
    else:
        mid = len(numsort) / 2
        mediannum = (numsort[mid] + numsort[mid-1]) / 2

median([1,2,3,4])
