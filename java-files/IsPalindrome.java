
public class IsPalindrome {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
//		return isPalindrome(s, 0, s.length() - 1);
		System.out.println(isPalindrome("Sass", 0, 3));
	}

	public static boolean isPalindrome(String s, int low, int high) {
		if (high <= low) // Base case
			return true;
		else if (s.charAt(low) != s.charAt(high)) // Base case
			return false;
		else
			return isPalindrome(s, low + 1, high - 1);

	}

}
