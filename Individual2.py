#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Дано время забега на 100 метров студентами в виде ключ-значение,
найти минимальное время забега
стометровки и минимальный результат забега
"""


def shop(**keywords):
    sum = 0
    n = len(keywords)
    min = keywords["Вася"]
    for kw in keywords:
        sum = sum + keywords[kw]
        if keywords[kw] < min:
            min = keywords[kw]
    print("Наименьшее время стометровки", ":", min)
    print("Среднее время стометровки - ", sum / n)


if __name__ == "__main__":
    shop(Вася = 10.2,
         Петя = 12,
         Денис = 11.2,
         Женя= 9.98,
         Катя= 12.3,
         )
