import java.io.*;
import java.util.Scanner;
import java.util.Stack;


public class Main {

    public static void main(String[] args) throws Exception {
        Scanner in = new Scanner(System.in);
        PrintWriter out = new PrintWriter(System.out, true);
        
        int n = Integer.parseInt(in.nextLine());
        
        for (int k = 0; k < n; k++) {

            Stack<Character> stack = new Stack<>();

            String line = in.nextLine();

            Boolean isCorrect = true;

            for (int i = 0; i < line.length(); i++) {
                char c = line.charAt(i);
                if (c == '(' || c == '[') {
                    stack.push(c);
                } else {
                    if (stack.empty()) {
                        isCorrect = false;
                        break;
                    }
                    char p = stack.pop();
                    if ((c == ')' && p != '(') || (c == ']' && p != '[')) {
                        isCorrect = false;
                        break;
                    }

                }
            }

            if (!stack.empty()) {
                isCorrect = false;
            }

            if (isCorrect) {
                out.println("Yes");
            } else {
                out.println("No");
            }
        }
    }
}
