# from odoo import http


# class Ramadhaniperpuslib(http.Controller):
#     @http.route('/ramadhaniperpuslib/ramadhaniperpuslib', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ramadhaniperpuslib/ramadhaniperpuslib/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ramadhaniperpuslib.listing', {
#             'root': '/ramadhaniperpuslib/ramadhaniperpuslib',
#             'objects': http.request.env['ramadhaniperpuslib.ramadhaniperpuslib'].search([]),
#         })

#     @http.route('/ramadhaniperpuslib/ramadhaniperpuslib/objects/<model("ramadhaniperpuslib.ramadhaniperpuslib"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ramadhaniperpuslib.object', {
#             'object': obj
#         })

