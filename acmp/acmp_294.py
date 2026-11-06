# k1, l1, m1 = map(int, input().split())
# k2, l2, m2 = map(int, input().split())

# cena_boltov = k1 * l1 // 100 * m1
# cena_gaek = k2 * l2 // 100 * m2

# ostalos_boltov = k1 - k1 * l1 // 100
# ostalos_gaek = k2 - k2 * l2 // 100

# cena_dop = 0

# if ostalos_boltov > ostalos_gaek:
#     cena_dop = (ostalos_boltov - ostalos_gaek) * m1
# elif ostalos_gaek > ostalos_boltov:
#     cena_dop = (ostalos_gaek - ostalos_boltov) * m2

# result = cena_boltov + cena_gaek + cena_dop

# print(result)


# k1, n1, m1 = map(int, input().split())
# k2, n2, m2 = map(int, input().split())

# bolt = k1 - k1 * n1 // 100
# gaika = k2 - k2 * n2 // 100

# if bolt < gaika:
#     bo = gaika - bolt
#     print(bo * m2 + k1 * n1 // 100 * m1 + k2 * n2 // 100 * m2)
# elif bolt > gaika:
#     ga = bolt - gaika
#     print(ga * m1 + k1 * n1 // 100 * m1 + k2 * n2 // 100 * m2)

k1, l1, m1 = map(int, input().split())
k2, l2, m2 = map(int, input().split())


lost_bolts = k1 * l1 // 100
lost_nuts = k2 * l2 // 100
remaining_bolts = k1 - lost_bolts
remaining_nuts = k2 - lost_nuts
unusable_bolts = lost_bolts * m1
unusable_nuts = lost_nuts * m2

if remaining_bolts > remaining_nuts:
    damage = (remaining_bolts - remaining_nuts) * m1
else:
    damage = (remaining_nuts - remaining_bolts) * m2

total_damage = unusable_bolts + unusable_nuts + damage
print(total_damage)
