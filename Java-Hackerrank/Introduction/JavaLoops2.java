// https://www.hackerrank.com/challenges/java-loops/problem?isFullScreen=true
import java.util.*;

public class JavaLoops2 {
	public static void main(String []argh){
		Scanner in = new Scanner(System.in);
		int t=in.nextInt();
		for(int i=0;i<t;i++){
			int a = in.nextInt();
			int b = in.nextInt();
			int n = in.nextInt();
			for (int j=1;j<=n;j++) {
				int m = 1;
				int result = a;
				for (int k=1;k<=j;k++){
					result += m * b;
					m *= 2;
				}
				System.out.print(result + " ");
			}
			System.out.println();
		}
		in.close();
	}
}