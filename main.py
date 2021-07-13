def CalculateTotalAmount(totalAmount, countMonth, everyMonthAmount, procentByMonth):
    selfInvestAmount = 0
    i = 0
    while (i < countMonth) :
        selfInvestAmount = selfInvestAmount + everyMonthAmount
        totalAmount = totalAmount + everyMonthAmount
        totalAmount = totalAmount + totalAmount * (procentByMonth / 100)
        i = i + 1

    return totalAmount, selfInvestAmount

#Точка входа
if __name__ =="__main__":
    begginingAmount = int(input("Введите сумму начального капитала: "))
    procentStaf = int(input("Введите годовую процентную ставку: "))
    everyMonthAmount = int(input("Введите сумму ежемесячного платежа: "))
    countYear = int(input("Введите кол-во лет инвестирования: "))
    countMonth = countYear * 12
    procentByMonth = procentStaf / 12
    totalAmount, selfInvestAmount = CalculateTotalAmount(begginingAmount, countMonth, everyMonthAmount, procentByMonth)
    print ("Сумма собственных влажений: "+ str(selfInvestAmount))
    print ("Сумма общих финансов: " + str(round(totalAmount, 2)))