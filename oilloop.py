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

def oilLoopFuelBased(fuel, plastic, rubber):
	if (fuel + plastic + rubber) == 0:
		return("0 (Why did you do this?)", 0, 0)
	else:
		totalOil = (fuel + plastic + rubber) / 3
		byproductResin = fuel / 4
		plasticRubberOil = totalOil - (fuel / 8 * 3)
		totalResin = (plasticRubberOil / 3 * 2) + byproductResin
		plasticRubberFuel = plasticRubberOil / 3 * 8
		percentage = (totalResin / 2) / (plasticRubberFuel * 3)
		recycledRubberTotal = plasticRubberFuel * (1 - percentage)
		recycledPlasticTotal = plasticRubberFuel * (1 + percentage)
		recycledPlasticRefineries = recycledPlasticTotal / 60
		recycledRubberRefineries = recycledRubberTotal / 60
		return(totalOil, recycledPlasticRefineries, recycledRubberRefineries)

def oilLoopHorBased(hor, plastic, rubber):
	totalOil, recycledPlasticRefineries, recycledRubberRefineries = oilLoopFuelBased(hor / 2, plastic, rubber)
	return(totalOil, recycledPlasticRefineries, recycledRubberRefineries)