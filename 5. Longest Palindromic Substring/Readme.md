相关题目 409. Longest Palindrome/ 
1. `5.py` 遍历每个字符作为中心位置，然后再在该位置上用扩展法，记录并更新得到的最长的回文长度。时间复杂度是 $O(n^2)​$。

2. 马拉车（Manacher）算法，解决重复访问的问题。
   参考文章[https://segmentfault.com/a/1190000003914228](https://segmentfault.com/a/1190000003914228)

   1. 记录回文串的最右侧边界 max_right，以及取得最右侧边界时的中心位置 center
   2. searched 记录已经遍历过的字符串的回文半径
   3. 遍历字符串，判断当前字符串位置 i 在最右侧边界 max_right 的左侧还是右侧
      1. 如果在左侧
         1. 通过 2*center - i 找到 i 关于 center 左对称的位置 j。
         2. 取左对称位置 j 的回文半径与 max_right - i 的最小值作为当前位置的回文半径起始值，解决重复从 1 开始遍历的问题
         3. 判断从当前回文半径开始是否是回文。
      2. 如果在右侧
         1. 对当前位置 i 左右遍历，直至遇到不相同的字符为止，更新 max_right 和 center。
   4. 时间和空间复杂度均是 $O(n)$。
   5. 通过添加 `#` 避免奇偶数判断。
   6. 通过添加特殊字符 `^ $` 避免边界判断。

3. 动态规划代码

   参考 [https://www.youtube.com/watch?v=hTuHzZk0LyI](https://www.youtube.com/watch?v=hTuHzZk0LyI)

   [https://leetcode.com/problems/longest-palindromic-substring/discuss/157861/Python3-DP-Solution-with-Lots-of-Comments](https://leetcode.com/problems/longest-palindromic-substring/discuss/157861/Python3-DP-Solution-with-Lots-of-Comments)

   1. 每个动态规划代码都涉及网格

   2. 建立 $n\times n$ 的网格 dp，`dp[i][j]` 代表字符串从 i 到 j 是否是回文串

   3. 初始化

      1. 如果是一个字符，也就是 `dp[i][i]` 都等于 True
      2. 如果两个字符，判断 `dp[i][i+1]`，如果相等，则是回文串；如果不相等，不是回文串。

   4. 超过两个字符时，填表的规则：

      判断字符串的 i 和 j 位是否相等，

      如果相等，判断 `dp[i+1][j-1]` 是否是回文串。比如字符串 `s = abcba`，i=0 和 j = 4 时，s[i] == s[j]，则利用已有结果，判断 `dp[1][3]` 是否是回文串。

      **这也是 DP 先解决小问题，后解决大问题的思路所在。**

   5. 输出最长回文字串，判断条件为 True 时，判断 j-i+1 是否大于最长 length。
      如果是，记录最大长度以及起始坐标，输出 string[start, start+max_length]。

   6. 时间复杂度 $O(n^2)$，空间复杂度 $O(n^2)$。

