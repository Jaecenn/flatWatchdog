import re


def getSqMetersValue(sqMetersString):
    squareReg = re.compile('\d+(?=\sm²)')

    sqMetersString= sqMetersString.replace(u'\xa0', u' ')
    sqMetersString = squareReg.findall(sqMetersString)

    if len(sqMetersString) == 1:
        sqMetersString = sqMetersString[0] 
    elif len(sqMetersString) == 2:
        sqMetersString = int(sqMetersString[0]) + round(int(sqMetersString[1])/2)
        sqMetersString = str(sqMetersString)
    else:
        sqMetersString = "1"

    return sqMetersString

def getPriceValue(priceString):
    priceReg = re.compile('\d+(?=Kč)')

    price = priceString.replace(u'\xa0', u' ')
    price = price.replace(u'\n', u'') 
    price = price.replace(u' ', u'')
    price = priceReg.findall(price)

    if len(price) == 1:
        price = price[0] 
    else:
        price = "1"

    return price