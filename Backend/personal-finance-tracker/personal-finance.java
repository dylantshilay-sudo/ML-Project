import java.text.NumberFormat;
import java.util.Scanner;


public class Main {
    public static void main(String[] args){
        Scanner scanner  =  new Scanner(System.in);
        System.out.print("What is your name? ");
        String name = scanner .nextLine();
        System.out.println("Hello "+ name + "!!");
        System.out.println();

        System.out.println("Let me ask you some questions");
        System.out.println();

        // Revenue
        System.out.print("Monthly income: ");
        double monthlyIncome = scanner.nextDouble();
        // Expenses
        System.out.print("Rent: ");
        double rent = scanner.nextDouble();
        System.out.print("Food: ");
        double food = scanner.nextDouble();
        System.out.print("Transport:  ");
        double transport = scanner.nextDouble();
        System.out.print("Entertainment: ");
        double entertainment = scanner.nextDouble();
        scanner.close();
        double totalExpenses = rent + food + transport + entertainment;
        double remainingMoney = monthlyIncome - totalExpenses;

        double savingRate = remainingMoney/monthlyIncome;

        NumberFormat percent = NumberFormat.getPercentInstance();
        NumberFormat currency = NumberFormat.getCurrencyInstance();

        final String STYLE = "===============================";
        final String LINE = "--------------------------------";

        // Header
        System.out.println(STYLE);
        System.out.println();
        System.out.println("FINANCIAL REPORT");
        System.out.println();
        System.out.println(STYLE);
        System.out.println();


        // Body

        System.out.println("Name: "+ name);
        System.out.println();
        System.out.println("Monthly Income \t: "+currency.format(monthlyIncome));
        System.out.println();
        System.out.println("Rent \t:"+ currency.format(rent));
        System.out.println("Food \t:"+ currency.format(food));
        System.out.println("Transport \t:"+ currency.format(transport));
        System.out.println("Entertainment \t:"+ currency.format(entertainment));
        System.out.println();
        System.out.println(LINE);
        System.out.println();

        // Footer
        System.out.println("Total Expenses \t:"+ currency.format(totalExpenses));
        System.out.println();
        System.out.println("Remaining \t:"+ currency.format(remainingMoney));
        System.out.println();
        System.out.println("Saving Rate \t:" + percent.format(savingRate));
        System.out.println();
        System.out.println(STYLE);




    }
}
