import java.util.Scanner;

// Implements Quick Sort Algorithm in Reverse

public class QuickSortReverseSherri 
{

	public static void quickSort(int[] arry) 
	{
		quickSort(arry, 0, arry.length - 1);
	}
	
	private static void quickSort(int[] arry, int first, int last) 
	{
		// if arry has more than one element
		if (last > first) 
		{
			int pIndex = partition(arry, first, last);
			
			quickSort(arry, first, pIndex - 1);
			quickSort(arry, pIndex + 1, last);
		}
	}

	// swap values arr[i] and arr[j]
	public static void swap(int[] arr, int i, int j) 
	{
		int temp = arr[i];
		arr[i] = arr[j];
		arr[j] = temp;
	}
	
	// partition array. return next pivot.
	private static int partition(int[] arry, int first, int last) 
	{
		// set pivot to first element
		int pivot = arry[first];
		// set low index
		int low = first + 1;
		// set high index
		int high = last;
		
		// iterate through subarray
		while (high > low) 
		{
						
			// move low pointer while low >= pivot and low and high don't cross - low <= high
			while (low <= high && arry[low] >= pivot) 
			{
				low++;
			}
			
			// move high pointer while high < pivot and low and high don't cross - low <= high
			while (low <= high && arry[high] < pivot) 
			{
				high--;
			}
			
			// if high > low, swap arry[low] and arry[high] values
			if (high > low) 
			{
				swap(arry, low, high);
			}
		}
			
		// if low and high pointers cross, then arry[low] > arry[high]. move high pointer.
		while (high > first && arry[high] <= pivot) 
		{
			high--;			
		}
		
		// if pivot < arry[high], swap arry[first] and arry[high], return high. else return first as next pivot
		if (pivot < arry[high]) 
		{
			arry[first] = arry[high];
			arry[high] = pivot;
			return high;
		}
		else 
		{
			return first;
		}
	}
	
	public static void main(String[] args) 
	{
		// create a scanner
		Scanner input = new Scanner(System.in);
		// prompt user to enter number of integers
		System.out.print("How many integer numbers do you have?: ");
		
		// get number of integers
		int n = input.nextInt();
		
		// get integer inputs
		int[] inputs = new int[n];
		
		// prompt user to enter numbers
		System.out.print("Enter " + n + " integer numbers: ");
		
		// get n number of integers
		for (int i = 0; i < n; i++)
	    {	
			inputs[i] = input.nextInt();
	    }
		
		System.out.println("---------------------------------------------------");
		// display integer array
		System.out.println("Inputs array before sorting (quick):");
		for (int i = 0; i < inputs.length; i++) 
			{
				System.out.print(inputs[i] + " ");
			}
		
		System.out.println();
		quickSort(inputs);
		
		// sort numbers and display
		System.out.println("Inputs array after sorting (quick):");
		for (int i = 0; i < inputs.length; i++) 
		{
			System.out.print(inputs[i] + " ");
		}
		
	}

}
