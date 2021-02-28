import java.util.ArrayList;
import java.util.List;

/*
 * @lc app=leetcode id=389 lang=java
 *
 * [389] Find the Difference
 */

// @lc code=start
class Solution {
    public char findTheDifference(String s, String t) {
        List<Character> letters = new ArrayList<>();
        for (char c: s.toCharArray()) letters.add(c);

        for (char c: t.toCharArray())  
            if (letters.contains(c)) letters.remove((Character) c);
            else    return c;

        return ' ';
    }
    public static void main(String[] args) {
        System.out.println(new Solution().findTheDifference("abcd", "abcde"));
    }
}
// @lc code=end

