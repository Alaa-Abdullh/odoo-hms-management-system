from odoo import models,fields

class  doctors(models.Model):
     _name="hms.doctor"

     # firstname = fields.Char()
     # lastname = fields.Char()
     name = fields.Char(string="Doctor Name", required=True)
     image =fields.Binary()

     patient_ids = fields.Many2many('hms.patient')