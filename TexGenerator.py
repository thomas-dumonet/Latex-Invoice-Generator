# -*- coding: utf-8 -*-
import jinja2
import os
from jinja2 import Template


class LatexTemplateGenerator:
	def __init__(self, templatePath):
		self.latex_jinja_env = jinja2.Environment(
			block_start_string = '\BLOCK{',
			block_end_string = '}',
			variable_start_string = '\VAR{',
			variable_end_string = '}',
			comment_start_string = '\#{',
			comment_end_string = '}',
			line_statement_prefix = '%-',
			line_comment_prefix = '%#',
			trim_blocks = True,
			autoescape = False,
			loader = jinja2.FileSystemLoader(templatePath)
		)

	def render(self, data, filename):
		template = self.latex_jinja_env.get_template('template.tex')
		document = template.render(data)
		with open(filename, 'wb+') as output:
			output.write(document.encode('utf-8'))
