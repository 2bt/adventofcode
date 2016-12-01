min_total_pw = 9e9

def f(total_pw=0, hp=50, pw=500, boss_hp=55, shield_counter=0, poison_counter=0, recharge_counter=0):


	## part two
	hp -= 1
	if hp <= 0: return



	global min_total_pw
	if total_pw > min_total_pw:	return

	if shield_counter > 0: shield_counter -= 1

	if poison_counter > 0:
		poison_counter -= 1
		boss_hp -= 3
		if boss_hp <= 0:
			if total_pw < min_total_pw:
				min_total_pw = total_pw
				print min_total_pw
			return

	if recharge_counter > 0:
		recharge_counter -= 1
		pw += 101


	for spell in "missile", "drain", "shield", "poison", "recharge":

		next_total_pw			= total_pw
		next_hp					= hp
		next_pw					= pw
		next_boss_hp			= boss_hp
		next_shield_counter		= shield_counter
		next_poison_counter		= poison_counter
		next_recharge_counter	= recharge_counter


		# player's turn
		if spell == "missile" and next_pw >= 53:
			next_pw -= 53
			next_total_pw += 53
			next_boss_hp -= 4
			if next_boss_hp <= 0:
				if next_total_pw < min_total_pw:
					min_total_pw = next_total_pw
					print min_total_pw
				continue
		elif spell == "drain" and next_pw >= 73:
			next_pw -= 73
			next_total_pw += 73
			next_boss_hp -= 2
			next_hp += 2
			if next_boss_hp <= 0:
				if next_total_pw < min_total_pw:
					min_total_pw = next_total_pw
					print min_total_pw
				continue
		elif spell == "shield" and next_pw >= 113 and next_shield_counter == 0:
			next_pw -= 113
			next_total_pw += 113
			next_shield_counter = 6
		elif spell == "poison" and next_pw >= 173 and next_poison_counter == 0:
			next_pw -= 173
			next_total_pw += 173
			next_poison_counter = 6
		elif spell == "recharge" and next_pw >= 229 and next_recharge_counter == 0:
			next_pw -= 229
			next_total_pw += 229
			next_recharge_counter = 5
		else: continue


		armor = 0
		if next_shield_counter > 0:
			next_shield_counter -= 1
			armor = 7

		if next_poison_counter > 0:
			next_poison_counter -= 1
			next_boss_hp -= 3
			if next_boss_hp <= 0:
				if next_total_pw < min_total_pw:
					min_total_pw = next_total_pw
					print min_total_pw
				continue

		if next_recharge_counter > 0:
			next_recharge_counter -= 1
			next_pw += 101


		# boss's turn
		next_hp -= max(8 - armor, 1)
		if next_hp <= 0: continue

		f(next_total_pw, next_hp, next_pw, next_boss_hp, next_shield_counter, next_poison_counter, next_recharge_counter)

f()

print min_total_pw


