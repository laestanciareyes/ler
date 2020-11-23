# -*- coding: utf-8 -*-
# from odoo import http


# class SolucionesEstrategicas(http.Controller):
#     @http.route('/soluciones__estrategicas/soluciones__estrategicas/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/soluciones__estrategicas/soluciones__estrategicas/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('soluciones__estrategicas.listing', {
#             'root': '/soluciones__estrategicas/soluciones__estrategicas',
#             'objects': http.request.env['soluciones__estrategicas.soluciones__estrategicas'].search([]),
#         })

#     @http.route('/soluciones__estrategicas/soluciones__estrategicas/objects/<model("soluciones__estrategicas.soluciones__estrategicas"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('soluciones__estrategicas.object', {
#             'object': obj
#         })
