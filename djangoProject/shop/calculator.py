import tensorflow as tf

class Calculator(object):
    num1 = 0
    num2 = 0

    @property
    def num1(self)-> int: return self._num1

    @property
    def num2(self) -> int: return self._num2

    @num1.setter
    def num1(self, num1): self._num1 = num1

    @num2.setter
    def num2(self, num2): self._num2 = num2

class CalculatorService(object):

    @tf.function
    def add(self, num1: int, num2: int): return tf.add(num1, num2)

    @tf.function
    def subtract(self, num1: int, num2: int): return tf.subtract(num1, num2)

    @tf.function
    def multiply(self, num1: int, num2: int): return tf.multiply(num1, num2)

    @tf.function
    def divide(self, num1: int, num2: int): return tf.divide(num1, num2)

if __name__ == '__main__':
    calculator = Calculator()
    service = CalculatorService()
    while True:
        num1 = input('숫자 1 입력\n')
        a = tf.constant(int(num1))
        opcode = input('0,+,-,*,/ \n')
        num2 = input('숫자 2 입력\n')
        b = tf.constant(int(num2))
        if opcode == '0':
            print("종료")
            break
        elif opcode == '+':
            print(f" {a} + {b} = {service.add(a, b)}")
        elif opcode == '-':
            print(f" {a} + {b} = {service.subtract(a, b)}")
        elif opcode == '*':
            print(f" {a} + {b} = {service.multiply(a, b)}")
        elif opcode == '/':
            print(f" {a} + {b} = {service.divide(a, b)}")
        else:
            print('존재하지 않는 연산자')