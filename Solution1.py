def infinity_gen(input_list):
    len_list = len(input_list)
    if len_list == 0:
        raise ValueError(
            'В функцию infinity_gen не может быть передан пустой список!'
        )
    left = 0
    right = len_list - 1
    while True:
        yield input_list[left]
        if right > left:
            yield input_list[right]
        left += 1
        right -= 1
        if left > right:
            left, right = 0, len_list - 1


if __name__ == '__main__':
    st = input('Введите последовательность символов содержащую цифры: ')
    num_list = [num for num in st if num.isdecimal()]
    if len(num_list) == 0:
        run = False
        print('Вы не ввели ни одной цифры.')
    else:
        run = True
        gen = infinity_gen(num_list)
    while run:
        answer = input('Продолжить выполнение программы?(y/n) ')
        if answer.lower() in ('yes', 'y'):
            print(next(gen))
        elif answer.lower() in ('n', 'no'):
            run = False
        else:
            print(
                '\nНеверный ввод. Введите "y" или "n".'
            )
    print('Заверщение работы!')

