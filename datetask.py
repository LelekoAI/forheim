def day_number(date: list[int], month_dict: dict[int, list[int, str]]) -> int:
    day = 0
    if leap_year(date[2]):
        month_dict[date[2]][1] = 29
        for i in range(1, date[1] + 1):
            day += month_dict[i][0]
        day -= month_dict[date[1]][0] - date[0]
    else:
        for i in range(1, date[1] + 1):
            day += month_dict[i][0]
        day -= month_dict[date[1]][0] - date[0]
    return day


def leap_year(year: int) -> bool:
    if year % 4 == 0:
        return True
    else:
        return False


def new_date(number: int, gap: int, leap: bool, months_dict: dict[int, list[int, str]], date_list: list[int]) -> str:
    count = 1
    if leap:

        if number + gap > 366:
            date_list[2] += 1
            with_gap = number + gap - 366
            while True:
                if with_gap < months_dict[count+1][0]:
                    break
                with_gap -= months_dict[count][0]
                count += 1
            date_list[0] = with_gap
            date_list[1] = count
        else:
            with_gap = number + gap
            while True:
                if with_gap < months_dict[count + 1][0]:
                    break
                with_gap -= months_dict[count][0]
                count += 1
            date_list[0] = with_gap
            date_list[1] = count
    else:
        if number + gap > 365:
            date_list[2] += 1
            with_gap = number + gap - 365
            while True:
                if with_gap < months_dict[count + 1][0]:
                    break
                with_gap -= months_dict[count][0]
                count += 1
            date_list[0] = with_gap
            date_list[1] = count
        else:
            with_gap = number + gap
            while True:
                if with_gap < months_dict[count + 1][0]:
                    break
                with_gap -= months_dict[count][0]
                count += 1
            date_list[0] = with_gap
            date_list[1] = count
    return f"день - {date_list[0]}, месяц - {date_list[1]}, год - {date_list[2]}"


def main():
    months_dict: dict[int, list[int, str]] = {1: [31, 'Январь'], 2: [28, 'Февраль'], 3: [31, 'Март'],
                                              4: [30, 'Апрель'], 5: [31, 'Май'], 6: [30, 'Июнь'],
                                              7: [31, 'Июль'], 8: [31, 'Август'], 9: [30, 'Сентябрь'],
                                              10: [31, 'Октябрь'], 11: [30, 'Ноябрь'], 12: [31, 'Декабрь']}
    gap: int = int(input('введите интервал(дни): '))
    print('введите дату')
    count = 1
    date_list: list[int] = []
    while count <= 3:
        if count == 1:
            date_day = int(input('введите день: '))
            date_list.append(date_day)
        elif count == 2:
            date_month = int(input('введите месяц: '))
            date_list.append(date_month)
        else:
            date_year = int(input('введите год: '))
            date_list.append(date_year)
        count += 1
    print(day_number(date_list, months_dict))
    print(new_date(day_number(date_list, months_dict), gap, leap_year(date_list[2]), months_dict, date_list))


if __name__ == '__main__':
    main()
