# Copyright (c) 2022, cosmos and contributors
# For license information, please see license.txt

from cgitb import text
import frappe
from frappe import _
from frappe.model.document import Document

class TranslateText(Document):
	def validate(self):
		self.before_insert()
	
	def before_insert(self):
		translationList = frappe.get_doc('TranslationDoc', 'TranslationList')

		for row in translationList.get("translation_table"):
			if self.translate == row.fromtext:
				frappe.msgprint(_("Program detected that your input is in the list of need to be translated texts. \n \n" + self.translate +" is translated to "+ row.totext))
				self.translate = row.totext
				break
		
				

