import recipe
from subprocess import call

def generateParamsString(recipe):
	param_string = " "

	for key in recipe:
		if type(recipe[key]) is dict:
			params = recipe[key]
			for value in params:
				param_string += " " + key + " " + value + "=" + str(params[value])
				pass

		if type(recipe[key]) is bool and recipe[key] == True:
			print key
			param_string += key
			pass

		if type(recipe[key]) is str or type(recipe[key]) is int:
			if recipe[key] != "":
				param_string += key + "=" + str(recipe[key])
				pass
			pass

		if type(recipe[key]) is list:
			param_string += key + "="
			array = recipe[key]

			for index in range(len(array)):
				if index != len(array)-1:
					param_string += array[index] + "+"
				else:
					param_string += array[index]
				pass
			pass
		pass
		param_string += " "
	pass
	return param_string

# generateParamsString(recipe.example)

call(['pandoc', 'document.md' + generateParamsString(recipe.example)])

# call(["pandoc", "document.md" + generateParamsString(recipe.example)])
