import sys

def read_numbers_from_file(filename):
    """从文件中读取数字，假设每行一个数字。"""
    try:
        with open(filename, 'r') as file:
            numbers = [float(line.strip()) for line in file]
        return numbers
    except FileNotFoundError:
        print(f"文件 {filename} 未找到")
        sys.exit(1)
    except ValueError:
        print(f"文件 {filename} 中包含无效的数字")
        sys.exit(1)

def perform_operation(numbers, operation):
    """根据操作符执行相应的计算。"""
    if operation == 'add':
        result = sum(numbers)
    elif operation == 'minus':
        result = numbers[0]
        for num in numbers[1:]:
            result -= num
    elif operation == 'multiply':
        result = 1
        for num in numbers:
            result *= num
    elif operation == 'divide':
        result = numbers[0]
        for num in numbers[1:]:
            if num == 0:
                print("错误：除数不能为零")
                sys.exit(1)
            result /= num
    else:
        print(f"不支持的操作: {operation}")
        sys.exit(1)
    return result

def main():
    if len(sys.argv) != 3:
        print("用法: python calculator.py <操作> <文件名>")
        sys.exit(1)

    operation = sys.argv[1]
    filename = sys.argv[2]

    numbers = read_numbers_from_file(filename)
    result = perform_operation(numbers, operation)
    
    print(f"结果: {result}")

if __name__ == "__main__":
    main()
