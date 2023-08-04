import pandas as pd

def binary_without_first_last(binary_num):
    if len(binary_num) > 2:
        return binary_num[1:-1]
    else:
        return '0'

def binary_to_decimal(binary_num):
    return int(binary_num, 2)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def convert_to_binary(input_file, output_file):
    df = pd.read_csv(input_file)
    df['binary'] = df['number'].apply(lambda x: bin(x)[2:])
    df['binary_nucleus'] = df['binary'].apply(binary_without_first_last)
    df['decimal_nucleus'] = df['binary_nucleus'].apply(binary_to_decimal)
    df.to_csv(output_file, index=False)

if __name__ == "__main__":
    input_file = "./dataset/primes_smaller.csv"
    output_file = "output.csv"
    convert_to_binary(input_file, output_file)