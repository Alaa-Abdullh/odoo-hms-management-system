from odoo import models, fields, api

class PatientLog(models.Model):
    _name = "hms.patient.log"
    _description = "Patient Log"

    patient_id = fields.Many2one('hms.patient')
    created_by = fields.Many2one('res.users')
    date = fields.Datetime()
    description = fields.Text()

    @api.model
    def create(self, vals):
        vals['created_by'] = self.env.user.id
        return super(PatientLog, self).create(vals)