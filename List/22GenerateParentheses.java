class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> ans = new LinkedList<>();
        helper(ans, "", n, n);
        return ans;
    }
    
    public void helper(List<String> ans, String str, int left, int right) {
        if (left == 0 && right == 0) {
            ans.add(str);
            return;
        }

        if (left > 0) {
            helper(ans, str + "(", left - 1, right);
        }

        if (left < right) {
            helper(ans, str + ")", left, right - 1);
        }
    }
}
