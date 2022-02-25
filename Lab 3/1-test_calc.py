import lab02

if __name__ == "__main__":

	#Test 1 - Testing add function
	lab02.initialize()

	lab02.add(42)


	if lab02.get_current_value() == 42:
		print("Test 1 passed")
	else:
		print("Test 1 failed")

	#Test 2 -- Testing one undo
	lab02.initialize()

	lab02.add(100)
	lab02.subtract(100)
	lab02.undo()
	if lab02.get_current_value() == 100:
		print("Test 2 passed")
	else:
		print("Test 2 failed")


	#Test 3 -- Producing Error
	lab02.initialize()

	lab02.subtract(100)
	lab02.divide(0)

	if lab02.get_current_value() == "ERROR":
		print("Test 3 passed")
	else:
		print("Test 3 failed")