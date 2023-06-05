import os
import sys

csv_dir = os.path.join("", "csvs")
subject_dict = {
	"human":{
		"gender":"gender.csv",
		"age":"age.csv",
		"skin":"skin.csv",
		"outfits":"outfits.csv",
		"accessories":"accessories.csv",
		"pose":"pose.csv",
		"body type":"body-types.csv",
		"hair":"hair.csv",
		"expression": "expression.csv",
		"jobs": "jobs.csv",
		"culture": "culture.csv"
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

type_of_image = {
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
		"illustration type": "illustration-type.csv"
		"movieorgame": "movieorgame.csv"
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

class OneButton(object):
	def __init__(self):
		pass

	def get_prompt():
		pass


def test():
	type_of_image = "photography"
	subject = "Human"
	special_words = "special"

	button = OneButton()
	prompt = button.get_prompt(type_of_image, subject, special_words)
	print(prompt)


if __name__ == "__main__":
	test()
