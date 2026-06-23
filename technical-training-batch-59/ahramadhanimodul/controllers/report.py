    
from odoo import http
from odoo.http import content_disposition, request
import io
import xlsxwriter

class AttendeesReport(http.Controller):

    @http.route([
        '/attendees/excel_report/<model("ahramadhanimodul.session"):session>',
    ], type='http', auth="user", csrf=False)
    def get_attendees_excel_report(self, session=None,**args):
        response = request.make_response(
            None,
            headers=[
                ('Content-Type', 'application/vnd.ms-excel'),
                ('Content-Disposition', content_disposition('Attendees {}'.format(session.name) + '.xlsx'))
            ]
        )
 
        # buat object workbook dari library xlsxwriter
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        
        report_name = 'Attendees of {} in {}'.format(session.name, session.course_id.name)
        sheet = workbook.add_worksheet(report_name[:31])

        headers =["No","Name","Phone","Email"]
        bold = workbook.add_format({'bold': True})

        for col_num, header in enumerate(headers):
            sheet.write(0, col_num, header, bold)
        
        # NO | Name | Phone | Email
        
        row_num = 1
        for attendee in session.partner_ids:
            
            # ISIAN COLUMN NO
            sheet.write(row_num, 0, '{}'.format(row_num or ''))
            
            # ISIAN COLUMN NAME
            sheet.write(row_num, 1, attendee.name or '')
            
            # ISIAN COLUMN PHONE
            sheet.write(row_num, 2, attendee.phone or '')
            
            # ISIAN COLUMN EMAIL
            sheet.write(row_num, 3, attendee.email or '')
            
            # MENAMBAH DATA ROW NUM
            row_num += 1

        # masukkan file excel yang sudah digenerate ke response dan return 
        # sehingga browser bisa menerima response dan mendownload file yang sudah digenerate
        workbook.close()
        output.seek(0)
        response.stream.write(output.read())
        output.close()
 
        return response