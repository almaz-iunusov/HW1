time = int(input("Введите какое-нибудь количество времени в секундах:"))
# hours = time // 3600
hours = (time // 3600) % 24
# minutes = (time // 60) - hours * 60
minutes = (time // 60) % 60
# sec = time - ((hours * 3600) + (minutes * 60))
sec = time % 60
# print(hours, ":", minutes, ":", sec)
# print(f"{time //3600}:{(time // 60) - (time //3600) * 60}:{time - ((((time // 3600) * 3600) + ((time // 60) - (time // 3600) * 60) * 60))}")
# print(f"{hours}:{minutes}:{sec}")
# print("%dh:%dm:%ds" % (hours, minutes, sec))
print("%02d:%02d:%02d" % (hours, minutes, sec))

