from tank import Tank

tanks = { "a":Tank("Alice"), "b":Tank("Bob"), "c":Tank("Carol") }
alive_tanks = len(tanks)

while alive_tanks > 1:

	print
	for tank_name in sorted( tanks.keys() ):
		print tank_name, str(tanks[tank_name])

	first = raw_input("Who fires? ").lower()
	second = raw_input("Who at? " ).lower()

	try:
		first_tank = tanks[first]
		second_tank = tanks[second]
	except KeyError, name:
		print "No such tank!",name
		continue

	if first == second:
		print "You cannot attack yourself"
		continue

	if not first_tank.alive or not second_tank.alive:
		print "One of those tanks is dead"
		continue

	print
	print "*" * 30

	first_tank.fire_at(second_tank)
	if not second_tank.alive:
		alive_tanks -= 1

	print "*" * 30

for tank in tanks.values():
	if tank.alive:
		print str(tank), "is the WINNER!!!"
		break
