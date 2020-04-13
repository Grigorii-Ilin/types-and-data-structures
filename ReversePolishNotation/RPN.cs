using System;
using System.Collections.Generic;
using System.Text;

namespace ReversePolishNotation {
    class RPN {

        //Преобразовывание
        static public string ToNotation(string input) {
            string notation = ""; //Результат
            Stack<char> operators = new Stack<char>(); //Операторы

            int i = 0;
            //bool wasDigit = false;
            do {
                char c = input[i];

                if (c==' ') {
                    i++;
                    continue;
                }
                else if (char.IsDigit(c) || c=='.') {
                    //wasDigit = true;
                    notation += c;
                    i++;
                }


            } while (i< input.Length);


            for (int i = 0; i < input.Length; i++) {
                if (IsDelimeter(input[i]))
                    continue;

                //Получаем число
                if (Char.IsDigit(input[i])) {
                    while (!IsDelimeter(input[i]) && !IsOperator(input[i])) {
                        notation += input[i];
                        i++;

                        if (i == input.Length) break;
                    }

                    notation += " ";
                    i--;
                }

                //Получаем операторы
                if (IsOperator(input[i])) {
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
                            if (GetPriority(input[i]) <= GetPriority(operators.Peek())) //приоритет меньше или равен
                                notation += operators.Pop().ToString() + " ";

                        operators.Push(char.Parse(input[i].ToString())); //стек пуст или приоритет выше
                    }
                }
            }

            while (operators.Count > 0)
                notation += operators.Pop() + " ";

            return notation;
        }

        //Вычисление
        static public double Calculate(string notation, double x) {
            double result = 0; //Результат
            Stack<double> temp = new Stack<double>();

            for (int i = 0; i < notation.Length; i++) {
                if (Char.IsDigit(notation[i])) {
                    string a = string.Empty;

                    while (!IsDelimeter(notation[i]) && !IsOperator(notation[i])) {
                        a += notation[i];
                        i++;
                        if (i == notation.Length) break;
                    }
                    temp.Push(double.Parse(a));
                    i--;
                }
                else if (IsOperator(notation[i])) {
                    //Два последних числа
                    double a = temp.Pop();
                    double b = temp.Pop();

                    switch (notation[i]) {
                        case '+': result = b + a; break;
                        case '-': result = b - a; break;
                        case '*': result = b * a; break;
                        case '/': result = b / a; break;
                    }
                    temp.Push(result); //Результат в стек
                }
            }
            return temp.Peek();
        }


        //Проверка на пробел и равно
        static private bool IsDelimeter(char c) {
            if ((" =".IndexOf(c) != -1))
                return true;
            return false;
        }

        //Проверка на оператор
        static private bool IsOperator(char с) {
            if (("+-/*^()".IndexOf(с) != -1))
                return true;
            return false;
        }

        //Приоритет
        static private byte GetPriority(char s) {
            switch (s) {
                case '(': return 0;
                case ')': return 1;
                case '+': return 2;
                case '-': return 3;
                case '*': return 4;
                case '/': return 4;
                case '^': return 5;
                default: return 6;
            }

        }
    }
}
