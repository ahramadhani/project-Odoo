# from odoo import http


# class Ahramadhanimodul(http.Controller):
#     @http.route('/ahramadhanimodul/ahramadhanimodul', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ahramadhanimodul/ahramadhanimodul/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ahramadhanimodul.listing', {
#             'root': '/ahramadhanimodul/ahramadhanimodul',
#             'objects': http.request.env['ahramadhanimodul.ahramadhanimodul'].search([]),
#         })

#     @http.route('/ahramadhanimodul/ahramadhanimodul/objects/<model("ahramadhanimodul.ahramadhanimodul"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ahramadhanimodul.object', {
#             'object': obj
#         })

