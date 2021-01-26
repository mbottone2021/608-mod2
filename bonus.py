import statistics
print('Page length of books in home library')
Pages = [23, 444, 556, 761, 34, 21, 59, 255, 345, 234, 451, 234, 278, 452, 332, 56, 88, 103, 122, 145, 166, 156, 190, 29, 298, 766, 989, 76, 45, 38, 246, 90, 72, 54, 26, 438, 332, 290, 443, 630, 53, 234, 254, 198, 101, 76, 1231, 442, 203, 132, 344, 43, 233, 219, 45, 486, 864, 345, 567, 324, 56, 76, 11, 34, 345, 67, 86, 34, 222, 456, 867, 34, 456, 781, 45, 567, 87, 99, 341, 23, 345, 34, 64, 77, 645, 234, 198, 232, 123, 168, 245, 456, 13, 242, 187, 1289, 23, 235, 23, 345]
a = len(Pages)
print('Count of book pages', a)
b = sum(Pages)
print('Sum of book pages', b)
c = statistics.mean(Pages)
print('Mean of book pages', c)
d = statistics.median(Pages)
print('Median of book pages', d)
e = statistics.mode(Pages)
print('Mode of book pages', e)
