

def divider(big_number):
    factor_list = []
    counter = 2
    while counter < big_number:
        if big_number % counter == 0:
            factor_list.append(counter)
            big_number = big_number/counter
        else:
            counter = counter + 1
    factor_list.append(big_number)
    return factor_list



def main():
    print max(divider(600851475143))
    return 0

if __name__ == '__main__':
    main()