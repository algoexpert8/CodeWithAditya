import java.util.Scanner;
public class examPercentage {
    public static void main(String args[]){
        Scanner input = new Scanner(System.in);
        System.out.println("Enter The name of your exam:");
        String examname  = input.nextLine();
        System.out.println("OK, now enter the total marks that can be scored in the exam:");
        double total = input.nextDouble();
        System.out.println("Now enter your marks:");
        double yourmarks = input.nextDouble();
        double percentage = yourmarks/total*100;
        System.out.println("You scored "+ percentage + "% " + "in your " + examname + " exam");
    }
}