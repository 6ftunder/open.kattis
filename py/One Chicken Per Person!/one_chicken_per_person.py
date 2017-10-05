needed_chicken, chickens_in_stock = map(int, input().split())

# how many chickens are left/needed
leftover = chickens_in_stock - needed_chicken

print('Dr. Chaz will have {} piece{} of chicken left over!'.format(leftover, '' if leftover == 1 else 's')
      if needed_chicken < chickens_in_stock else 'Dr. Chaz needs {} more piece{} of chicken!'.format(abs(leftover), '' if leftover == -1 else 's'))
