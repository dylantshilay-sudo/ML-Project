import java.text.NumberFormat;
import java.util.Scanner;

// Mortgage calculator
public class mortgage {
    public static void main(String[] args){
        Scanner scanner =  new Scanner(System.in);
        NumberFormat currency = NumberFormat.getCurrencyInstance();
        NumberFormat percent = NumberFormat.getPercentInstance();
        // Just a few questions for our user
        System.out.println("Hello !");
        System.out.print("Mortgage amount: ");
        double mortgageAmount = scanner.nextDouble();
        System.out.print("Annual Interest Rate (without %): ");
        double interestRate = scanner.nextDouble();
        System.out.print("Period (Years): ");
        int period = scanner.nextInt();

        // Calculate the mortgage

        // convert the interest rate in decimal
        double monthlyInterestRate = (interestRate/100)/12;

        // total number of monthly payments
        int numberOfPayments = period * 12;

        // Mortgage formula
        // Numerator
        double num = mortgageAmount * monthlyInterestRate * (Math.pow((1+monthlyInterestRate),numberOfPayments));

        // denominator
        double deno = Math.pow((1+monthlyInterestRate), numberOfPayments) - 1;

        // Monthly payment

        double monthlyPayment = num / deno;

        // Output

        final String STYLE="====================";

        // Header
        System.out.println(STYLE);
        System.out.println("MORTGAGE CALCULATOR");
        System.out.println(STYLE);

        // Body
        System.out.println("Mortgage: "+ currency.format(mortgageAmount));
        System.out.println();
        System.out.println("Interest: "+ percent.format(interestRate/100));
        System.out.println();
        System.out.println("Years: "+period);
        System.out.println();
        System.out.println("Monthly Payment: "+ currency.format(monthlyPayment));


        // footer
        System.out.println();

        System.out.println(STYLE);


    }
}
