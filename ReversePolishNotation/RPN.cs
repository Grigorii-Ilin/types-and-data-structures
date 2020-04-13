using System;
using System.Collections.Generic;
using System.Text;


namespace ReversePolishNotation {
    class RPN {
        static public string ToNotation(string input, double x) {
            string notation = "";
            bool unaryMinus = false;
            Stack<char> operators = new Stack<char>(); 

            for (int i = 0; i < input.Length; i++) { //TODO change to do-while

                //spaces
                if (IsSpace(input[i])) {
                    unaryMinus = false;
                    continue;
                }

                //x
                if (input[i]=='x') { 
                    if ((unaryMinus && x>=0)||x<0) {
                        notation += "m";
                    }
                    notation += Math.Abs(x).ToString() + " ";
                    continue;
                }

                //digits
                if (Char.IsDigit(input[i])) {
                    if (unaryMinus) {
                        notation += "m";
                    }

                    while (!IsSpace(input[i]) && !IsOperator(input[i])) {
                        notation += input[i];
                        i++; //TODO it is not good practice, change

                        if (i == input.Length) break;
                    }
                    notation += " ";
                    i--;
                }

                // + - * / () sin
                if (IsOperator(input[i])) {
                    if (input[i] == '-' && Char.IsDigit(input[i+1])) {
                        unaryMinus = true;
                        continue;
                    }
                    unaryMinus = false;

                    if (input[i] == '(')
                        operators.Push(input[i]);
                    else if (input[i] == ')') {
                        char s = operators.Pop();
                        while (s != '(') {
                            notation += s.ToString() + ' ';
                            s = operators.Pop();
                        }
                    }
                    else {
                        if (operators.Count > 0)
                            if (GetPriority(input[i]) <= GetPriority(operators.Peek())) 
                                notation += operators.Pop().ToString() + " ";

                        operators.Push(char.Parse(input[i].ToString())); 

                        if (input[i] == 's')
                            i += 2;
                    }
                }
            }

            while (operators.Count > 0)
                notation += operators.Pop() + " ";

            return notation;
        }

        static public double Calculate(string notation) {
            double result = 0.0; 
            Stack<double> numbers = new Stack<double>();
            bool unaryMinus = false;

            for (int i = 0; i < notation.Length; i++) {
                if (notation[i]=='m') {
                    unaryMinus=true;
                }
                else if (Char.IsDigit(notation[i])) {
                    string numberStr = (unaryMinus)?"-":"";

                    while (!IsSpace(notation[i]) && !IsOperator(notation[i])) {
                        numberStr += notation[i];
                        i++;
                        if (i == notation.Length) break;
                    }
                    numbers.Push(double.Parse(numberStr));
                    i--;

                    unaryMinus = false;
                }
                else if (IsOperator(notation[i])) {
                    double a = numbers.Pop();
                    double b = notation[i] != 's' ? numbers.Pop() : 0.0;

                    switch (notation[i]) {
                        case '+': result = b + a; break;
                        case '-': result = b - a; break;
                        case '*': result = b * a; break;
                        case '/': {
                                try {
                                    result = b / a; 
                                    break;
                                }
                                catch (DivideByZeroException) {
                                    Console.WriteLine("Division of by zero.");
                                    break;
                                }

                            }
                        case 's': result = Math.Sin(a); break; 
                    }
                    numbers.Push(result); 
                }

            }
            return numbers.Peek();
        }


        static private bool IsSpace(char c) {
            return (" ".IndexOf(c) == 0);
        }

        //Проверка на оператор
        static private bool IsOperator(char с) {
            return ("+-/*s()".IndexOf(с) != -1);
        }

        //Приоритет
        static private byte GetPriority(char s) {
            switch (s) {
                case '(': return 0;
                case ')': return 0;
                case 's': return 1;
                case '+': return 2;
                case '-': return 2;
                case '*': return 3;
                case '/': return 3;

            }
            return 10;
        }
    }
}
