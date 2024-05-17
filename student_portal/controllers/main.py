from odoo import http
from odoo.http import request

class StudentPortal(http.Controller):

    @http.route('/student_portal', auth='public', website=True)
    def index(self, **kwargs):
        students = request.env['student.student'].sudo().search([])
        return request.render('student_portal.portal_template', {'students': students})
