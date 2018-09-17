果然自己的解决方法复杂度$O(n^2)$太高，没有通过，Time Limit Exceeded。

better 中利用 collection.Counter() 得到关于出现次数的字典，
分成两种情况考虑：
1. k>1，同时 c+k 在字典中
2. k==0，同时有数字同时出现两次

**主要在于计数的字典上**，这个字典如果不知道 collection.Counter()，也可以自己生成。