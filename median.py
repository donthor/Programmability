def median(numbers):
    numsort = sorted(numbers)
    if len(numsort) % 2 != 0:
        mid = (len(numsort) - 1) / 2
        mediannum = numsort[mid]
    else:
        mid = len(numsort) / 2
        mediannum = (float(numsort[mid]) + float(numsort[mid-1])) / 2

    print mediannum

median([4,5,5,4])
