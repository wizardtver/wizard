"""Game - guess the number / Игра угадай число
PC to guess and guesses the number itself /
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """To guess the number by random / Рандомно угадываем число

    Args:
        number (int, optional): Guesses number / 
        Загаданное число. Defaults to 1.

    Returns:
        int: The number of trying / Число попыток
    """
    count = 0
    predict_number = np.random.randint(1, 101)  # random number
    mn = 1
    mx = 100
    while True: 
        count += 1
        number = (mn + mx)//2
        if number == predict_number:
            print(f'число {number} найден за {count} попыток!')
            break  # exit from the loop if guessed right number
        elif number > predict_number:
            mx = number
        else:
            mn = number
        
                
    return (count)


def score_game(random_predict) -> int:
    """How many attempts on average for 1000 approaches our 
    algorithm guesses
    За какое количство попыток в среднем за 1000 подходов
    угадывает наш алгоритм

    Args:
        random_predict ([type]): to guess function
                                 функция угадывания

    Returns:
        int: average number of tries / среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # to fix seed for reproducibility / 
    # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  
    # to made the list of numbers / загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)