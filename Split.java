import java.util.Scanner;

public class Split {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scanner = new Scanner(System.in);
		System.out.println("Please enter a STRING: ");
		String input = scanner.next();
		System.out.println("Please enter a Number: ");
		int number = scanner.nextInt();
		
		Split(input, number);

	}
	
	public static void Split(String str, int size){
		int stringSize = str.length();
		//int numberOfSubstring = stringSize/size;
		int subStringSize = stringSize/size;
		int remainder = stringSize%size;
		for(int i = 0; i < size; i++){
			if(remainder > 0){
			System.out.print(str.substring(0, subStringSize+1) + " " + ", ");
			str = str.substring(subStringSize+1);
			remainder--;
			}
			else{
				System.out.print(str.substring(0, subStringSize) + " ");
				str = str.substring(subStringSize);
			}
		}
	}

}
