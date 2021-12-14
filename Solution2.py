from itertools import cycle


def change_list(input_list: list) -> None:
    copy_list = input_list[:]
    input_list.clear()
    while True:
        try:
            input_list.append(copy_list.pop(0))
            input_list.append(copy_list.pop(-1))
        except IndexError:
            return None


if __name__ == '__main__':
    st = input('Введите последовательность символов содержащую цифры: ')
    num_list = [num for num in st if num.isdecimal()]
    if len(num_list) == 0:
        run = False
        print('Вы не ввели ни одной цифры.')
    else:
        run = True
        change_list(num_list)
        gen = cycle(num_list)
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