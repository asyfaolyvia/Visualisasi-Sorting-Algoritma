# Tugas Besar Analisis Kompleksitas Algoritma
# Nama : Asyfa Dwi Olyvia (1303194025)
#        Eliza Fatrisia (1303190039)

import random
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def swap(A, i, j):
    """Fungsi pembantu untuk menukar elemen i dan j didalam list A"""

    if i != j:
        A[i], A[j] = A[j], A[i]


def mergesort(A, start, end):
    """Merge sort"""

    if end <= start:
        return

    mid = start + ((end - start + 1) // 2) - 1
    yield from mergesort(A, start, mid)
    yield from mergesort(A, mid + 1, end)
    yield from merge(A, start, mid, end)
    yield A


def merge(A, start, mid, end):
    """Fungsi pembantu untuk merge sort"""

    merged = []
    leftIdx = start
    rightIdx = mid + 1

    while leftIdx <= mid and rightIdx <= end:
        if A[leftIdx] < A[rightIdx]:
            merged.append(A[leftIdx])
            leftIdx += 1
        else:
            merged.append(A[rightIdx])
            rightIdx += 1

    while leftIdx <= mid:
        merged.append(A[leftIdx])
        leftIdx += 1

    while rightIdx <= end:
        merged.append(A[rightIdx])
        rightIdx += 1

    for i, sorted_val in enumerate(merged):
        A[start + i] = sorted_val
        yield A


def selectionsort(A):
    """selection sort"""
    if len(A) == 1:
        return

    for i in range(len(A)):
        minVal = A[i]
        minIdx = i
        for j in range(i, len(A)):
            if A[j] < minVal:
                minVal = A[j]
                minIdx = j
            yield A
        swap(A, i, minIdx)
        yield A


if __name__ == "__main__":
    # Meminta inputan angka dan metode sorting yang dipilih
    N = int(input("Masukkan banyaknya angka : "))
    method_msg = "Pilihan metode sortring : \n[m]erge Sort \n[s]election Sort\nMasukkan huruf pertama metode sorting yang dipilih : "
    method = input(method_msg)

    # Generate angka random
    A = [x + 1 for x in range(N)]
    random.seed(time.time())
    random.shuffle(A)

    if  method == "m":
        title = "Merge sort"
        generator = mergesort(A, 0, N - 1)
    else:
        title = "Selection sort"
        generator = selectionsort(A)

    fig, ax = plt.subplots()
    ax.set_title(title)

    bar_rects = ax.bar(range(len(A)), A, align="edge")

    ax.set_xlim(0, N)
    ax.set_ylim(0, int(1.07 * N))

    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

    iteration = [0]


    def update_fig(A, rects, iteration):
        for rect, val in zip(rects, A):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text("# of operations: {}".format(iteration[0]))


    anim = animation.FuncAnimation(fig, func=update_fig,
                                   fargs=(bar_rects, iteration), frames=generator, interval=1,
                                   repeat=False)
    plt.show()