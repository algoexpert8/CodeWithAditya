import java.util.Scanner;
public class CircArea {
    public static void main(String args[]){
        Scanner input = new Scanner(System.in);
        System.out.println("Enter the radius of the Circle. Do not enter the units. Radius = Diameter/2");
        double radius = input.nextDouble();
        double circum = radius*2*Math.PI;
        double area = radius*radius*Math.PI;
        System.out.println("The circumference (perimeter) of the circle is: "+circum);
        System.out.println("The area of the circle is: "+area);

    }

}