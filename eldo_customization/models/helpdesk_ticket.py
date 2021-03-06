# -*- coding: utf-8 -*-
from odoo import models, fields, api


class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'
   
    stage_name = fields.Char(string="Stage", related="stage_id.name")

    @api.model
    def message_new(self, msg, custom_values=None):
        res = super(HelpdeskTicket, self).message_new(msg=msg, custom_values=custom_values)
        res.update({'stage_id': self.env.ref('eldo_customization.stage_new_email').id})
        return res

    @api.multi
    def message_update(self, msg, update_vals=None):
        res = super(HelpdeskTicket, self).message_update(msg=msg, update_vals=update_vals)
        self.write({'stage_id': self.env.ref('eldo_customization.stage_new_email').id})
        return res
