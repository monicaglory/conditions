# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line
def farm_action(weather, time_of_day, cow_milking_status,location_cows,season,slurry_tank,grass_status):
  if location_cows == 'pasture' and time_of_day == 'night':
    return 'take cows to cowshed'
  elif weather == 'rainy' and location_cows == 'pasture':
    return 'take cows to cowshed'
  elif cow_milking_status == True and location_cows == 'cowshed':
    return 'milk cows'
  elif cow_milking_status == True and location_cows == 'pasture':
    return 'take cows to cowshed\nmilk cows\ntake cows back to pasture'
  elif weather != 'sunny' or 'windy' and location_cows == 'cowshed' and slurry_tank == True:
    return 'fertilize pasture'
  elif weather != 'sunny' or 'windy' and location_cows == 'cowshed' and slurry_tank == False:
    return 'wait'
  elif weather != 'sunny' or 'windy' and location_cows == 'pasture' and slurry_tank == True:
    return 'take cows to cowshed\nfertilize pasture\ntake cows back to pasture'
  elif weather == 'sunny' and location_cows == 'cowshed' and season == 'spring' and grass_status == True:
    return 'mow grass'
  elif weather== 'sunny' and location_cows == 'pasture' and season == 'spring' and grass_status == True:
    return 'take cows to cowshed\nmow grass\ntake cows back to pasture'
  else: 
    return 'wait'
print(farm_action('sunny', 'day', True, 'pasture', 'spring', False, True))
print(farm_action('rainy', 'night', False, 'cowshed', 'winter', False, True))