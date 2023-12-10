num1 = float(input("Digite o primeiro numero:\n"))
num2 = float(input("Digite o segundo numero:\n"))
operation = input("Digite a operacao que deseja realizar(+, -, *, /)\n")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2
else:
    print("Operacao invalida!")
    result = 0
print(f"Resultado e: {result:.2f}")