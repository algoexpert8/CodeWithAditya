//This time, we'll use a switch-case condition instead of an if-else statement as it is more efficient than a block of nested-ifs
import java.util.Scanner;

public class Calculator {
    public static void main(String args[]){
        System.out.println("CALCULATOR");
        double num1;
        double num2;
        String operation;
        Scanner input = new Scanner(System.in);
        System.out.println("Enter 1st Number:");
        num1 = input.nextDouble();
        System.out.println("Enter 2nd Number:");
        num2 = input.nextDouble();
        System.out.println("Enter An Operation From Addition (+), Subtraction (-), Multiplication (*) or Division (/):");
        operation = input.next();
        switch (operation){
            case "+":
                double sum = num1+num2;
                System.out.println("The sum is: "+sum);
                break;
            case "-":
                double difference = num1-num2;
                System.out.println("The difference is: "+difference);
                break;
            case "*":
                double product = num1*num2;
                System.out.println("The product is: "+product);
                break;
            case "/":
                double quotient = num1/num2;
                System.out.println("The quotient is: "+quotient);
                break;
            default:
                System.out.println("That's an invalid input!");
        }
    }
}