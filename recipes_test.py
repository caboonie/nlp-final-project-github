import json

sum_ = 0
for filename in ['recipes_raw_nosource_ar.json', 'recipes_raw_nosource_epi.json', 'recipes_raw_nosource_fn.json']:

	with open(filename) as f:
	  data = json.load(f)
	sum_ += len(data)
	# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
	print(len(data))

print(sum_)