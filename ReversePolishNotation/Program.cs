using System;

namespace ReversePolishNotation {
    class Program {
        static void Main(string[] args) {
            Console.WriteLine("Reverse Polish notation calculator.");
            Console.WriteLine("Author: Grigorii Ilin");

            while (true) {
                Console.WriteLine("Example to enter: -2*x + sin(0.5*x)");
                string input = Console.ReadLine(); //TODO check input
                string notation = RPN.ToNotation(input);
                Console.WriteLine("RPN: " + notation);

                Console.WriteLine("Input left border:");
                double leftBorder = double.Parse(Console.ReadLine());

                Console.WriteLine("Input right border:");
                double rightBorder = double.Parse(Console.ReadLine());

                Console.WriteLine("Input step:");
                double step = double.Parse(Console.ReadLine());

                double x = leftBorder;
                do {
                    double result = RPN.Calculate(notation, x);
                    Console.WriteLine($"x= {x} Result= {result:N3}");
                    x += step;
                } while (x < rightBorder);



            }
        }
    }
}
