import os
os.system('cls')



def ritm_slogi(stihi):
    razdelno = stihi.split()
    glasnye = []
    for slovo in razdelno:
        glasnye_odinak = len([i for i in slovo if i.lower() in 'ёуеыаоэяию'])
        glasnye.append(glasnye_odinak)
    if len(set(glasnye)) == 1:
        return "Ритм есть. Парам пам-пам"
    else:
        return "Ритма нет. Пам парам"

stih = "пара-ра-рам рам-пам-папам па-ра-па-дам"
print(ritm_slogi(stih))
stih = "ЕХАЛ грека через реку. Видит грека  "
print(ritm_slogi(stih))
