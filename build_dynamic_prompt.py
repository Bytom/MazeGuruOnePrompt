import os
import sys
import random

csv_dir = os.path.join("", "csvs")
subject_dict = {
	"human":{
		"gender":"gender.csv",
		"age":"age.csv",
		"skin":"skin.csv",
		"outfits":"outfits.csv",
		"accessories":"accessories.csv",
		"pose":"poses.csv",
		"body type":"body-types.csv",
		"hair":"hair.csv",
		"expression": "expression.csv",
		"jobs": "jobs.csv",
		"culture": "cultures.csv"
	},
	"fictional character":{
		"fictional":"fictional-characters.csv",
		"outfits":"outfits.csv",
		"accessories":"accessories.csv",
		"pose":"pose.csv",
		"body type":"body-types.csv",
		"hair":"hair.csv",
		"expression": "expression.csv"
	},
	"humanoid":{
		"humanoid":"humanoids.csv",
		"age":"age.csv",
		"skin":"skin.csv",
		"outfits":"outfits.csv",
		"accessories":"accessories.csv",
		"pose":"pose.csv",
		"body type":"body-types.csv",
		"hair":"hair.csv",
		"expression": "expression.csv"
	},
	"animal":{
		"animals": "animals.csv"
	},
	"building":{
		"building type": "buildings.csv",
		"materials": "materials.csv",
		"colors":"colors.csv"
	},
	"vehicles":{
		"vehicle type": "vehicles.csv",
		"materials": "materials.csv",
		"colors": "colors.csv"
	},
	"object":{
		"object type": "objects.csv",
		"materials": "materials.csv",
		"colors": "colors.csv"
	},
	"plant":{
		"plant type": "plants.csv"
	},
	"landscape":{
		"scenery": "scenery.csv",
		"time": "time.csv",
		"season": "season.csv",
		"weather": "weather.csv"
	},
	"location":{
		"location": "locations.csv",
		"time": "time.csv",
		"season": "season.csv",
		"weather": "weather.csv"
	},
	"scene":{
		"scene": "scene.csv"
	},
	"event":{
		"events": "events.csv"
	}
}

type_of_image_dic = {
	"photography":{
		"photography-technology": "photography-technology.csv",
		"photographic-equipment": "photographic-equipment.csv",
		"photography-parameters": "photography-parameters.csv",
		"film": "film.csv",
		"photographer": "photographer.csv"
	},
	"painting":{
		"painting type": "painting-type.csv",
		"brush type": "brush-type.csv",
		"pigment type": "pigment-type.csv",
		"painting style": "painting-style.csv",
		"painter": "painter.csv"
	},
	"illustration":{
		"illustration type": "illustration-type.csv",
		"movieorgame": "movieorgame.csv",
		"illustrator": "illustrator.csv"
	},
	"architectural design":{
		"national culture": "national-culture.csv",
		"architectural style": "architectural-style.csv",
		"architectural age": "architectural-age.csv",
		"architect": "architect.csv"
	},
	"graphic design":{
		"design style": "design-style.csv",
		"design purpose": "design-purpose.csv",
		"color schema": "colorscheme.csv",
		"graphic designer": "graphic-designer.csv"
	},
	"fashion design":{
		"fashion style": "fashion-style.csv",
		"fashion age": "fashion-age.csv",
		"fashion brand": "fashion-brand.csv",
		"fashion designer": "fashion-designer.csv"
	},
	"anime":{
		"anime style": "anime-style.csv",
		"animation": "animation.csv",
		"animation studio": "animation-studio.csv",
		"animator": "animator.csv"
	}	
}

magic_dic = {
	"magic_words": "magic-words.csv"
}

others_dic = {
	"angle": "angle.csv",
	"background": "background.csv",
	"colorscheme": "colorscheme.csv",
	"light": "lighting.csv"
}


def get_csvs(filepath):
	ret = []
	if os.path.exists(filepath):
		f = open(filepath, "r")
		for line in f:
			ret.append(line.strip())
		f.close()
	return ret

def random_choice_num_from_arr(arr, num):
	if len(arr) < num:
		return []
	else:
		random_arr = random.shuffle(arr)
		return random_arr[:num]


class OneButton(object):
	def __init__(self):
		self.magic_words = get_csvs(magic_dic["magic_words"])

	def get_other_prompt(self):
		other_file = others_dic[random.choice(list(others_dic.keys()))]
		csv_path = os.path.join(csv_dir, other_file)
		lines = get_csvs(csv_path)
		return random.choice(lines)

	def get_prompt(self, type_of_image, subject, special_words):
		prompt_arr = [f"({type_of_image})"]
		type_of_image = type_of_image.lower()
		subject = subject.lower()
		
		s_dic = subject_dict[subject]
		
		for key, csv_file in s_dic.items():
			csv_path = os.path.join(csv_dir, csv_file)
			lines = get_csvs(csv_path)
			if lines:
				#prompt_arr.append(f"[{key}]:" + random.choice(lines))
				prompt_arr.append(random.choice(lines))
			else:
				print(f"empty:{csv_path}")

		type_dic = type_of_image_dic[type_of_image]
		for key, csv_file in type_dic.items():
			csv_path = os.path.join(csv_dir, csv_file)
			lines = get_csvs(csv_path)
			if lines:
				# prompt_arr.append(f"[{key}]:" + random.choice(lines))
				prompt_arr.append(random.choice(lines))
			else:
				print(f"empty:{csv_path}")

		prompt_arr.append(self.get_other_prompt())
		return ','.join(prompt_arr)		


def test():
	type_of_image = "photography"
	subject = "Human"
	special_words = "special"

	button = OneButton()
	prompt = button.get_prompt(type_of_image, subject, special_words)
	print(prompt)


if __name__ == "__main__":
	test()
