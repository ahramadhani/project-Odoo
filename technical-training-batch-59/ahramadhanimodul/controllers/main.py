from odoo import http

class Academy(http.Controller):

    @http.route('/public/hello', auth='public')
    def hello(self, **kw):
        return "Hello, world"
    
    
    @http.route('/teacher', auth='public')
    def teacher(self, **kw):
        return http.request.render('ahramadhanimodul.teacher_template', {
            'teachers': ["Diana Padilla", "Jody Caroll", "Lester Vaughn", "Andi", "Budi Burhan"],
        })
        
    @http.route('/course', auth='public',  website=True)
    def course(self, **kw):
        Courses = http.request.env['ahramadhanimodul.course'].search([])
        return http.request.render('ahramadhanimodul.course_template', {
            'courses': Courses,
        })
        
    @http.route('/course/<model("ahramadhanimodul.course"):course>/', auth='public', website=True)
    def course_detail(self, course):
        return http.request.render('ahramadhanimodul.template_course_detail', {
            'course': course
        })
        
    # Add Course
    @http.route('/course/add', auth='public', website=True)
    def add_course(self, **kw):
        # get User for responsible
        user_ids = http.request.env['res.users'].sudo().search([])
        return http.request.render('ahramadhanimodul.add_course',{
            'users':user_ids
        })
    
    # Proses do add course
    @http.route('/course/do_add_course', auth='public', methods=['POST'], website=True)
    def do_add_course(self, **post):
        vals = {
            'name':post.get('name'),
            'user_id':int(post.get('user_id')),
            'description':post.get('description'),
        }
        http.request.env['ahramadhanimodul.course'].sudo().create(vals)

        return http.request.redirect('/course')

    # Edit Course
    @http.route('/course/edit/<model("ahramadhanimodul.course"):course>', auth='public', website=True)
    def edit(self, course):
        user_ids = http.request.env['res.users'].sudo().search([])
        return http.request.render('ahramadhanimodul.edit_course',{
            'users':user_ids,
            'course':course,

        })
    
    @http.route('/course/do_edit_course', auth='public', methods=['POST'], website=True)
    def do_edit_course(self, **post):
        course = http.request.env['ahramadhanimodul.course'].sudo().browse(int(post.get('course_id')))
        if course:
            vals = {
                'name':post.get('name'),
                'user_id':int(post.get('user_id')),
                'description':post.get('description'),
            }
            course.sudo().write(vals)

        return http.request.redirect('/course')
    
    # Delete
    @http.route('/course/delete/<model("ahramadhanimodul.course"):course>', auth='public', website=True)
    def delete(self, course):
        if course:
            course.sudo().unlink()
        return http.request.redirect('/course')

#detail session
        # detail session
    @http.route('/course/session/<model("ahramadhanimodul.session"):session>/', auth='public', website=True)
    def session_detail(self, session, **kw):
        return http.request.render(
            'ahramadhanimodul.template_session_detail',
            {'session': session}
        )