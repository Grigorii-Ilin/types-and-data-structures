using System;

namespace ReversePolishNotation {
    class Program {
        static void Main(string[] args) {
            Console.WriteLine("Reverse Polish notation calculator.");

            while (true) {
                Console.WriteLine("\nExample to enter: -2*x + sin(0.5*x)");
                string input = Console.ReadLine(); //TODO check input

                Console.WriteLine("Input left border:");
                double leftBorder = double.Parse(Console.ReadLine());

                Console.WriteLine("Input right border:");
                double rightBorder = double.Parse(Console.ReadLine());

                Console.WriteLine("Input step:");
                double step = double.Parse(Console.ReadLine());

                double x = leftBorder;
                do {
                    string notation = RPN.ToNotation(input, x);
                    Console.WriteLine("RPN: " + notation);

                    double result = RPN.Calculate(notation);
                    Console.WriteLine($"x= {x:N3} Result= {result:N3}");

                    x += step;
                } while (x < rightBorder);



            }
        }
    }
}
