#!/usr/bin/env python3
"""简单的命令行计算器 - 支持加减乘除"""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "错误：除数不能为零！"
    return a / b

def main():
    print("=" * 40)
    print("欢迎使用简单计算器")
    print("支持运算：+  -  *  /")
    print("输入 'q' 退出程序")
    print("=" * 40)
    
    while True:
        print("\n请输入表达式 (格式：数字 运算符 数字):")
        user_input = input("> ").strip()
        
        if user_input.lower() == 'q':
            print("感谢使用，再见！")
            break
        
        try:
            parts = user_input.split()
            if len(parts) != 3:
                print("错误：请输入正确的格式，例如：5 + 3")
                continue
            
            num1, operator, num2 = parts
            num1 = float(num1)
            num2 = float(num2)
            
            if operator == '+':
                result = add(num1, num2)
            elif operator == '-':
                result = subtract(num1, num2)
            elif operator == '*':
                result = multiply(num1, num2)
            elif operator == '/':
                result = divide(num1, num2)
            else:
                print(f"错误：不支持的运算符 '{operator}'")
                continue
            
            print(f"结果：{num1} {operator} {num2} = {result}")
            
        except ValueError:
            print("错误：请输入有效的数字！")
        except Exception as e:
            print(f"发生错误：{e}")

if __name__ == "__main__":
    main()
