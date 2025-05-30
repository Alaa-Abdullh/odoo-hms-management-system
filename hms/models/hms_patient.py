import re
from odoo import models, fields, api
from datetime import date
from odoo.exceptions import ValidationError

class Patient(models.Model):
    _name = "hms.patient"
    _description = "Patient"

    firstname = fields.Char()
    lastname = fields.Char()
    birth_date = fields.Date()
    history = fields.Html()
    cr_Ratio = fields.Float()
    blood = fields.Selection([('a+', 'A+'), ('o+', 'O+'), ('b+', 'B+')])
    pcr = fields.Boolean()
    image = fields.Binary()
    address = fields.Text()
    age = fields.Integer(compute="compute_age", store=True)
    email = fields.Char()

    department_id = fields.Many2one('hms.department')
    doctor_ids = fields.Many2many('hms.doctor', string="Doctors")
    state = fields.Selection([
        ('undetermined', 'Undetermined'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('serious', 'Serious')
    ], default='undetermined')
    level = fields.Selection([('level1', 'Level 1'), ('level2', 'Level 2'), ('level3', 'Level 3')])
    log_ids = fields.One2many('hms.patient.log', 'patient_id')

    def unlink(self):
        for rec in self:
            if rec.log_ids or rec.doctor_ids or rec.department_id:
                raise ValidationError("You can't delete a customer linked to a patient.")
        return super().unlink()

    @api.constrains('email')
    def check_email(self):
        for rec in self:
            if rec.email:
                if not re.match(r"[^@]+@[^@]+\.[^@]+", rec.email):
                    raise ValidationError("Invalid email")
                if self.env['res.partner'].search_count([('email', '=', rec.email), ('id', '!=', rec.id)]) > 0:
                    raise ValidationError("Email must be unique among customers.")

    def approve_action(self):
        for rec in self:
            if rec.level == 'level1':
                rec.level = 'level2'
            elif rec.level == 'level2':
                rec.level = 'level3'

    def create_level_log(self):
        for record in self:
            vals = {
                'description': "Level changed to %s" % (record.level),
                'patient_id': self.id
            }
            self.env['hms.patient.log'].create(vals)

    @api.constrains('age')
    def check_age(self):
        for record in self:
            if record.age < 0:
                raise ValidationError("Age can't be negative number")
            elif record.age == 0:
                raise ValidationError("Age can't be zero")

    @api.depends('birth_date')
    def compute_age(self):
        for record in self:
            if record.birth_date:
                today = date.today()
                record.age = today.year - record.birth_date.year - (
                    (today.month, today.day) < (record.birth_date.month, record.birth_date.day)
                )
            else:
                record.age = 0