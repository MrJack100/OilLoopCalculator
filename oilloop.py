def maxPotential(oil, ratio=False) -> tuple:
	if ratio != False:
		fuel, plastic, rubber = ratio
		if (fuel + plastic + rubber) % 3 == 0:
			maxFuel = (oil * 3) / (fuel + plastic + rubber) * fuel
			maxPlastic = (oil * 3) / (fuel + plastic + rubber) * plastic
			maxRubber = (oil * 3) / (fuel + plastic + rubber) * rubber
	else:
		maxFuel = oil * 3
		maxPlastic = oil * 3
		maxRubber = oil * 3
	byproductResin = maxFuel / 2
	return(oil, maxFuel, maxPlastic, maxRubber, byproductResin)

def requiredOil(fuel, plastic, rubber):
	return((fuel + plastic + rubber) / 3)

def oilLoop(fuel, plastic, rubber):
	totalOil = requiredOil(fuel, plastic, rubber)
	byproductResin = fuel / 4
	plasticRubberOil = totalOil - (fuel / 8 * 3)
	totalResin = (plasticRubberOil / 3 * 2) + byproductResin
	plasticRubberFuel = plasticRubberOil / 3 * 8
	percentage = (totalResin / 2) / (plasticRubberFuel * 3)
	recycledRubberTotal = plasticRubberFuel * (1 - percentage)
	recycledPlasticTotal = plasticRubberFuel * (1 + percentage)
	inputRubber = recycledRubberTotal - rubber
	inputPlastic = recycledPlasticTotal - plastic
	print(inputRubber, inputPlastic)
	recycledPlasticRefineries = recycledPlasticTotal / 60
	recycledRubberRefineries = recycledRubberTotal / 60
	return(totalOil, recycledPlasticRefineries, recycledRubberRefineries)