from odoo import http
from odoo.http import request

class StudentPortal(http.Controller):

    @http.route(['/student/profile'], type='http', auth='user', website=True)
    def student_profile(self, **kw):
        # Get the logged-in user
        user = request.env.user

        # Find the student record associated with the logged-in user
        student = request.env['op.student'].sudo().search([('user_id', '=', user.id)], limit=1)

        if student:
            print("Student Name:", student.name)
            print("Student Email:", student.email)

            return request.render('student_port_ajmeer.custom_portal_ajmeer', {
                "students": [student]  # Render as a list for consistency with previous logic
            })
        else:
            # Handle case where student record is not found for the logged-in user
            return "No student record found for the logged-in user."

