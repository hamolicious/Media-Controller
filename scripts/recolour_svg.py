
import os

SVG_PATH = r'static\svg'
SVG_LINE_COLOR = '#eff9d6'

for file in os.listdir(SVG_PATH):
	if not file.endswith('.svg') : continue

	file_path = os.path.join(SVG_PATH, file)
	with open(file_path, 'r') as file:
		data = file.readlines()

	stroke_tag = 'stroke'
	index = data[0].index(stroke_tag + '="') + len(stroke_tag) + 2
	end_anchor = data[0][index + len(stroke_tag)+2::].index('"') + 1
	current_color = data[0][index:index + end_anchor]
	data[0] = data[0][:index:] + SVG_LINE_COLOR + data[0][index + end_anchor::]

	with open(file_path, 'w') as file:
		file.writelines(data)
