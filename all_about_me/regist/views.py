from django.shortcuts import render
from datetime import datetime, date, time, timezone


def registration(request):
    weekdays = {
        1: "Понедельник",
        2: "Вторник",
        3: "Среда",
        4: "Четверг",
        5: "Пятница",
        6: "Суббота",
        7: "Воскресенье"
    }
    now_time = datetime.now()
    format_time = f"{weekdays.get(datetime.weekday(now_time))}, {now_time.hour}:{now_time.minute}"
    return render(request, "regist/reg.html", context={'nowtime': format_time})