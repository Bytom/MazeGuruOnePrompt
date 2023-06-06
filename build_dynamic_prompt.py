import os
import sys
import random

ori_outputs_dir = "ori_outputs"
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
		"pose":"poses.csv",
		"body type":"body-types.csv",
		"expression": "expression.csv"
	},
	"humanoid":{
		"humanoid":"humanoids.csv",
		"outfits":"outfits.csv",
		"accessories":"accessories.csv",
		"pose":"poses.csv",
		"body type":"body-types.csv",
		"expression": "expression.csv"
	},
	"animal":{
		"animals": "animals.csv"
	},
	"building":{
		"building type": "buildings.csv",
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
	"background": "background.csv",
	"colorscheme": "colorscheme.csv",
	"light": "lighting.csv"
}

support_dic = {
	"photography": ["human", "fictional character", "humanoid", "animal", "building", "vehicles", "object", "plant", "landscape", "location", "scene", "event"],
	"painting": ["human", "fictional character", "humanoid", "animal", "building", "vehicles", "object", "plant", "landscape", "location", "scene", "event"],
	"illustration": ["human", "fictional character", "humanoid", "animal", "building", "vehicles", "object", "plant", "landscape", "location", "scene", "event"],
	"architectural design": ["building", "location"],
	"graphic design": ["human", "animal", "building", "vehicles", "landscape", "location", "scene"],
	"fashion design": ["human", "fictional character", "plant"],
	"anime": ["human", "fictional character", "humanoid", "animal", "landscape", "scene", "event"]
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
		random.shuffle(arr)
		return arr[:num]


class OneButton(object):
	def __init__(self):
		self.magic_words = get_csvs(os.path.join(csv_dir, magic_dic["magic_words"]))

	def judge_not_support(self, type_of_image, subject):
		if type_of_image not in support_dic.keys():
			return False
		if subject in support_dic[type_of_image]:
			return True
		return False

	def get_other_prompt(self):
		other_file = others_dic[random.choice(list(others_dic.keys()))]
		csv_path = os.path.join(csv_dir, other_file)
		lines = get_csvs(csv_path)
		return random.choice(lines)

	def get_prompt(self, type_of_image, subject, special_words):
		type_of_image = type_of_image.lower()
		subject = subject.lower()

		if not self.judge_not_support(type_of_image, subject):
			msg = "not support"
			return msg

		if special_words:
			prompt_arr = [f"({special_words})", f"({type_of_image})"]
		else:
			prompt_arr = [f"({type_of_image})"]
		
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

		magic_words = random_choice_num_from_arr(self.magic_words, 2)
		prompt_arr.extend(magic_words)
		prompt_arr.append(self.get_other_prompt())
		return ','.join(prompt_arr)		


def run_file(in_txt, out_txt, nums=10):
	button = OneButton()
	ret = []
	f = open(f"./ori_inputs/{in_txt}", "r")
	for line in f:
		type_of_image, subject = line.strip().split(',')
		special_words = ""
		for i in range(nums):
			prompt = button.get_prompt(type_of_image, subject, special_words)
			ret.append(prompt)
	f.close()

	if not os.path.exists(ori_outputs_dir):
		os.mkdir(ori_outputs_dir)

	f = open(f"{ori_outputs_dir}/{out_txt}", "w")
	for prompt in ret:
		f.write(prompt + "\n")
	f.close()
	return ret


def test(special_words, type_of_image, subject):
	button = OneButton()
	#print(type_of_image, subject, special_words)
	prompt = button.get_prompt(type_of_image, subject, special_words)
	print(prompt)
	return prompt



if __name__ == "__main__":
	run_file("in.txt", "out.txt", 4)
	exit(0)

	type_of_image = "photography"
	subject = "Human"
	special_words = "special"


	if len(sys.argv) > 3:
		type_of_image = sys.argv[1]
		subject = sys.argv[2]
		special_words = sys.argv[3:]
		special_words = ','.join([str(x) for x in special_words])
	elif len(sys.argv) == 3:
		type_of_image = sys.argv[1]
		subject = sys.argv[2]
		special_words = ""
	# print(sys.argv)
	test(special_words, type_of_image, subject)

