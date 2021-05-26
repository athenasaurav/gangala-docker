# -*- coding: utf-8 -*-
###############################################################################
#
#   consult_booking_mcq_rasa for Odoo
#   Copyright (C) 2004-today OpenERP SA (<http://www.openerp.com>)
#   Copyright (C) 2016-today Geminate Consultancy Services (<http://geminatecs.com>).
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as
#   published by the Free Software Foundation, either version 3 of the
#   License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
from odoo.http import request
from datetime import datetime, timedelta
from odoo import http, api, fields, models, modules, tools, _
from odoo.addons.im_livechat.controllers.main import LivechatController

class LivechatControllerTestData(http.Controller):

    @http.route('/Testdata', type='http',website=True, auth='public')
    def sample_sales_order(self,**kwargs):
        email = kwargs.get('0')
        name = kwargs.get('1')
        product_name = kwargs.get('2')
        product_uom_qty = kwargs.get('3')
        price_unit = kwargs.get('4')
        booking_date = kwargs.get('5')
        booking_slot = kwargs.get('6')
        state = request.env.ref('base.state_in_gj')
        
        booking_slot_val = request.env['booking.slot'].sudo().search([]).name_get()
        for ids in booking_slot_val:
            if ids[1] == str(booking_slot):
                booking_slot_ab = ids

        partner_name = request.env['res.partner'].sudo().search([('email','=',email)])
        if not partner_name:
            partner_name = request.env['res.partner'].sudo().create({
                'name': name,
                'email': email,
                'state_id': state.id
                })

        company_id = request.env.company.sudo().id
        sample_sale_order = request.env['sale.order'].sudo().create({
            'partner_id': partner_name.id,
            'is_booking_type': True,
            'payment_start_date':fields.Datetime.now(),
        })
        product = request.env['product.product'].sudo().search([('name', '=', product_name)], limit=1)
        request.env['sale.order.line'].sudo().create({
            'name': _('Sample Order Line'),
            'product_id': product.id,
            'product_uom_qty': product_uom_qty,
            'price_unit': price_unit,
            'order_id': sample_sale_order.id,
            'booking_date': booking_date,
            'booking_slot_id': booking_slot_ab[0],
            'company_id': sample_sale_order.company_id.id,
        })
        return sample_sale_order.name


