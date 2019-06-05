def optimalUtilization(maximumOperatingTravelDistance, forwardShippingRouteList, returnShippingRouteList):
    forwardShippingRouteList = sorted(forwardShippingRouteList, key = lambda x: x[1])
    returnShippingRouteList = sorted(returnShippingRouteList, key = lambda x: x[1], reverse = True)

    idxf = 0
    idxr = 0
    best = 0
    result = []

    while (idxf  < len(forwardShippingRouteList) and idxr < len(returnShippingRouteList)):
        elSum = forwardShippingRouteList[idxf][1] + returnShippingRouteList[idxr][1]
        if elSum > maximumOperatingTravelDistance:
            idxr += 1
        else:
            if elSum > best:
                best = elSum
                result = []
            if elSum == best:
                result.append([forwardShippingRouteList[idxf][0], returnShippingRouteList[idxr][0]])
            idxf += 1
    return result  