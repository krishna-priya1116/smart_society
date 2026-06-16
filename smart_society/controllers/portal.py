from odoo.addons.portal.controllers.portal import CustomerPortal
from odoo import http,fields
from odoo.http import request
import base64


class SocietyPortal(CustomerPortal):

    def _get_portal_home_counters(self):
        counters = super()._get_portal_home_counters()
        counters += ['complaint_count', 'notice_count','event_count','alert_count','broadcast_count','bill_count']
        print('\n\n\n...........counters......',counters)
        return counters

    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)

        # Complaint Count
        if 'complaint_count' in counters:
            complaint_count = request.env['complaint.desk'].sudo().search_count([])
                # ('user_id', '=', request.env.user.id)
            values['complaint_count'] = complaint_count

        # Maintenance bill
        if 'bill_count' in counters:
            bill_count = request.env['society.maintenance'].sudo().search_count([])
            values['bill_count']=bill_count

        #Alert Count
        if 'alert_count' in counters:
            print('\n\n\n.......alert_count........ if alert_count in counters:..........................')
            alert_count= request.env['resident.alerts'].sudo().search_count([])
            # ('user_id', '=', request.env.user.id)
            print('\n\n\n.......alert_count..................................',alert_count)
            values['alert_count'] = alert_count

        # Notice Count
        if 'notice_count' in counters:
            resident = request.env['resident.registrations'].sudo().search([
                ('user_id', '=', request.env.user.id)
            ], limit=1)

            domain = [('stage', '=', 'send')]

            if resident and resident.tower_id:
                domain = [
                    ('tower_id', 'in', resident.tower_id.ids),
                    ('stage', '=', 'send')
                ]

            notice_count = request.env['notice.board'].sudo().search_count(domain)
            values['notice_count'] = notice_count

        # Event Count
        if 'event_count' in counters:
            resident = request.env['resident.registrations'].sudo().search([
                ('user_id', '=', request.env.user.id)
            ], limit=1)

            domain = [('stage', '=', 'send')]

            if resident and resident.tower_id:
                domain = [
                    ('tower_id', 'in', resident.tower_id.ids),
                    ('stage', '=', 'send')
                ]

            event_count = request.env['event.announcement'].sudo().search_count(domain)
            values['event_count'] = event_count

        #Broadcast Count
        if 'broadcast_count' in counters:
            resident = request.env['resident.registrations'].sudo().search([
                ('user_id', '=', request.env.user.id)
            ], limit=1)

            domain = []

            if resident and resident.tower_id:
                domain = [
                    ('tower_ids', 'in', resident.tower_id.ids),

                ]

            broadcast_count = request.env['emergency.broadcasts'].sudo().search_count(domain)
            values['broadcast_count'] = broadcast_count

        # if 'gym_count' in counters:
        #     resident = request.env['resident.registrations'].sudo().search([
        #         ('user_id', '=', request.env.user.id)
        #     ], limit=1)
        #     values['gym_count'] = request.env['gym.booking'].search_count([
        #         ('resident_id', '=', resident.id)
        #     ]) if resident else 0
        #
        # if 'cbh_count' in counters:
        #     resident = request.env['resident.registrations'].sudo().search([
        #         ('user_id', '=', request.env.user.id)
        #     ], limit=1)
        #     values['cbh_count'] = request.env['clubhouse.booking'].search_count([
        #         ('resident_id', 'in', [resident.id])
        #     ]) if resident else 0
        # # Alert Count
        # if 'alert_count' in counters:
        #     resident=request.env['resident.registrations'].sudo().search([
        #         ('user_id', '=', request.env.user.id)
        #     ], limit=1)

        # values['gym_count'] = gym_count
        # values['cbh_count'] = cbh_count
        # values['facility_count'] = gym_count + cbh_count
        return values

    # my / invoices

    @http.route('/my/complaints', type='http', auth='user', website=True)
    def my_complaints(self, **kw):

        complaint = request.env['complaint.desk'].search([], limit=1)
        print('.......user_id....',complaint.user_id)
        print('.........resident_id..........',complaint.resident_id)
        resident = request.env['resident.registrations'].sudo().search([
            ('user_id', '=', request.env.user.id)
        ], limit=1)
        # complaints = request.env['complaint.desk'].sudo().search([
        #     ('user_id', '=', request.env.user.id),
        #     ('resident_id', '=', resident.id),
        # ])

        print("Current User:", request.env.user.id)
        print("Current Resident:", resident.id)

        complaints = request.env['complaint.desk'].sudo().search([
            ('resident_id', '=', resident.id)
        ])
        for c in complaints:
            print(
                "Complaint:",
                c.id,
                "User:",
                c.user_id.id if c.user_id else False,
                "Resident:",
                c.resident_id.id if c.resident_id else False
            )
        return request.render('smart_society.portal_my_complaints', {
            'complaints': complaints
        })



    @http.route('/my/complaint/new', type='http', auth='user', website=True)
    def complaint_form(self, **kw):
        committees = request.env['society.committee'].sudo().search([])
        return request.render('smart_society.portal_complaint_form', {
            'committees': committees
        })


    @http.route('/my/complaint/<int:complaint_id>/', type='http', auth='user', website=True)
    def complaint_detail(self, complaint_id, access_token=None, **kw):
        complaint = request.env['complaint.desk'].sudo().browse(complaint_id)
        if complaint.user_id.id != request.env.user.id:
            return request.redirect('/my/complaints')
        return request.render('smart_society.portal_complaint_detail', {
            'complaint': complaint
        })


    @http.route('/my/complaint/submit', type='http', auth='user', methods=['POST'], website=True)
    def submit_complaint(self, **post):
        resident = request.env['resident.registrations'].sudo().search([
            ('user_id', '=', request.env.user.id)
        ], limit=1)

        committee_id = post.get('committee_id')
        try:
            committee_id = int(committee_id) if committee_id else False
        except (ValueError, TypeError):
            committee_id = False

        proof = post.get('proof')
        proof_data = False
        if proof and hasattr(proof, 'read'):
            proof_data = base64.b64encode(proof.read())

        complaint = request.env['complaint.desk'].sudo().create({
            # 'alert_type':post.get('alert_type'),
            'name': post.get('name'),
            'description': post.get('description'),
            'resident_id': resident.id if resident else False,
            'to_committee': committee_id,
            'proof': proof_data,
            'stage': 'send',
        })

        complaint.action_send()
        return request.redirect('/my/complaints')


    @http.route('/my/notices', type='http', auth='user', website=True)
    def notice_board(self, **kw):
        resident = request.env['resident.registrations'].sudo().search([
            ('user_id', '=', request.env.user.id)
        ], limit=1)

        domain = [('stage', '=', 'send')]
        if resident and resident.tower_id:
            domain = [
                ('tower_id', 'in', resident.tower_id.ids),
                ('stage', '=', 'send')
            ]
        notices = request.env['notice.board'].sudo().search(domain, order='create_date desc')
        return request.render('smart_society.portal_notice_board', {
            'notices': notices,
            'resident': resident,
        })

    @http.route('/my/notice/<int:notice_id>/', type='http', auth='user', website=True)
    def notice_detail(self, notice_id, **kw):
        notice = request.env['notice.board'].sudo().browse(notice_id)
        if not notice.exists():
            return request.redirect('/my/notices')
        return request.render('smart_society.portal_notice_detail', {
            'notice': notice,
        })


    @http.route('/my/events', type='http', auth='user', website=True)
    def event_announcement(self, **kw):
        resident = request.env['resident.registrations'].sudo().search([
            ('user_id', '=', request.env.user.id)
        ], limit=1)

        domain = [('stage', '=', 'send')]
        if resident and resident.tower_id:
            domain = [
                ('tower_id', 'in', resident.tower_id.ids),
                ('stage', '=', 'send')
            ]
        events = request.env['event.announcement'].sudo().search(domain, order='create_date desc')
        return request.render('smart_society.portal_event_announcement', {
            'events': events,
            'resident': resident,
        })

    @http.route('/my/broadcasts', type='http', auth='user', website=True)
    def emergency_broadcasts(self, **kw):
        resident = request.env['resident.registrations'].sudo().search([
            ('user_id', '=', request.env.user.id)
        ], limit=1)
        domain = []
        if resident and resident.tower_id:
            domain = [
                ('tower_ids', 'in', resident.tower_id.ids),
            ]
        broadcasts=request.env['emergency.broadcasts'].sudo().search(domain, order='create_date desc')
        return request.render('smart_society.portal_broadcasts', {
            'broadcasts': broadcasts,
            'resident': resident,
        })

    @http.route('/my/event/<int:event_id>/', type='http', auth='user', website=True)
    def event_detail(self, event_id, **kw):
        event = request.env['event.announcement'].sudo().browse(event_id)
        if not event.exists():
            return request.redirect('/my/events')
        return request.render('smart_society.portal_event_detail', {
            'event': event,
        })

    @http.route('/my/broadcast/<int:broadcast_id>/', type='http', auth='user', website=True)
    def broadcast_detail(self, broadcast_id, **kw):
        broadcast = request.env['emergency.broadcasts'].sudo().browse(broadcast_id)
        if not broadcast.exists():
            return request.redirect('/my/broadcasts')
        return request.render('smart_society.portal_broadcast_detail', {
            'broadcast': broadcast,
        })

    @http.route(['/my/invoices','/my/invoices/page/<int:page>'], type='http', auth='user', website=True)
    def portal_my_invoices(self, page=1, date_begin=None,date_end=None, sortby=None,filterby=None, **kw):
        response = super().portal_my_invoices(
            page=page,
            date_begin=date_begin,
            date_end=date_end,
            sortby=sortby,
            filterby=filterby,
            **kw
        )
        # values = self._prepare_my_invoices_values(page, date_begin, date_end, sortby, filterby)
        resident = request.env['resident.registrations'].sudo().search([
            ('user_id', '=', request.env.user.id)
        ], limit=1)
        print('\n\n\n....................resident....',resident)

        maintenance_bills = request.env['society.maintenance'].sudo().search([
            # ('user_id', '=', request.env.user.id)
            # ('resident_id','=',resident.id)
            ('resident_id','in',resident.ids)
        ])
        print('\n\n\n....................maintenance...',maintenance_bills)

        response.qcontext.update({
            'maintenance_bills': maintenance_bills,
            'bill_count': len(maintenance_bills),
        })

        return response


    @http.route('/my/maintenance/pay/<int:bill_id>/', type='http', auth='user', website=True)
    def maintenance_pay(self, bill_id, **kw):
        print('\n\n\n.............maintenance_pay...........')
        bill=request.env['society.maintenance'].sudo().browse(bill_id)

        print('\n\n\n.........maintenance_pay..............bill......',bill)
        resident=request.env['resident.registrations'].sudo().search([
            ('user_id', '=', request.env.user.id)
        ],limit=1)

        print('\n\n\n.........resident...',resident)
        if bill.state != 'paid':
            # partner = bill.resident_id[:1].user_id.partner_id
            # print('bill.resident.user_id.partner_id........................',bill.resident.user_id.partner_id)
            # print('bill.resident[:1].user_id.partner_id................',bill.resident[:1].user_id.partner_id)
            # print('bill.resident_id[:1].user_id.partner_id..................',bill.resident_id[:1].user_id.partner_id)
            # print('\n\n\n.......partner...',partner)
            # payment_term = request.env['account.payment.term'].sudo().search([], limit=1)
            # 'move_type': 'out_invoice',
            # 'partner_id': partner.id,
            income = request.env['account.account'].sudo().search(
                [('account_type', '=', 'income')],
                limit=1
            )
            print("\n\n..........Partner:", resident.partner_id)
            print("\n\n............Receivable Account:", resident.partner_id.property_account_receivable_id)
            print("\n\n.............Payable Account:", resident.partner_id.property_account_payable_id)
            print("Partner:", resident.partner_id.id)
            print("Amount:", bill.total_amount)
            print("Income:", income.id)

            
            invoice=request.env['account.move'].sudo().create({
            'move_type':'out_invoice',
            'partner_id': resident.partner_id.id,
            'invoice_date':fields.Date.today(),
            'invoice_date_due': fields.Date.today(),
            # 'invoice_payment_term_id': payment_term.id,
            'invoice_line_ids':[(0, 0, {
                'name':f'Maintenance Bill{bill.month}/{bill.year}',
                'quantity':1,
                'price_unit':bill.total_amount,
                'account_id': income.id,
            })],
        })
            bill.invoice_id = invoice.id
            invoice.action_post()
            bill.write({
            'state':'paid',
            'is_paid':True,
            'payment_date':fields.Date.today(),
            'invoice_id':invoice.id,
            })
        # bill.action_mark_paid()
        print('...................bill.action_mark_paid().................')
        return request.redirect('/my/maintenance/%s' % bill.id)

    @http.route('/my/maintenance/<int:bill_id>/', type='http', auth='user', website=True)
    def maintenance_bill_detail(self, bill_id, **kw):
        bill = request.env['society.maintenance'].sudo().browse(bill_id)
        print('........maintenance_bill_detail.........bill............',bill)
        # bill.action_mark_paid()
        print('....................bill.action_mark_paid()...............',bill)
        return request.render(
            'smart_society.portal_maintenance_detail',
            {
                'bill': bill,
            }
        )

    @http.route('/my/alerts', type='http',auth='user',website=True)
    def my_alert(self,**kw):

        resident = request.env['resident.registrations'].sudo().search([
            ('user_id', '=', request.env.user.id)
        ], limit=1)
        # events = request.env['event.announcement'].sudo().search(domain, order='create_date desc')
        alerts = request.env['resident.alerts'].sudo().search([
            '|', '|', '|', '|',

            # Alerts created by the logged-in user
            ('alert_from', '=', request.env.user.id),

            # Alerts where resident is directly mentioned
            ('resident_id', 'in', resident.id),

            # Alerts for resident's flat
            ('flat_id', 'in', resident.flat_id.ids),

            # Alerts for resident's tower
            ('tower_id', 'in', resident.tower_id.ids),

            # Society-wide alerts
            '&',
            ('flat_id', '=', False),
            ('tower_id', '=', False),
        ], order='create_date desc')
        if 'alert_type' in kw:
            alerts.write({'alert_type': kw.get('alert_type')})

        return request.render('smart_society.portal_my_alerts', {
            'alerts': alerts
        })

    @http.route('/my/alert/submit', type='http', auth='user', methods=['POST'], website=True)
    def submit_alert(self, **post):
        resident = request.env['resident.registrations'].sudo().search([
            ('user_id', '=', request.env.user.id)
        ], limit=1)

        committee_id = post.get('')
        try:
            committee_id = int(committee_id) if committee_id else False
        except (ValueError, TypeError):
            committee_id = False

        security_id=post.get('')
        try:
            security_id = int(security_id) if security_id else False
        except (ValueError, TypeError):
            security_id = False

        # resident_id=request.httprequest.form.getlist('resident_id')
        # print('\n\n\n...resident_id......',resident_id)
        resident_id=post.get('resident_id')
        try:
            resident_id = int(resident_id) if resident_id else False
        except (ValueError, TypeError):
            resident_id = False

            print('\n\n\n....security id.....',[(6,0,[int(x) for x in request.httprequest.form.getlist('security_id') if x])])
        alert=request.env['resident.alerts'].sudo().create({
            'name':post.get('name'),
            'description':post.get('description'),
            # 'flat_id':post.get('flat_id'),
            'flat_id':[(6,0,[int(x) for x in request.httprequest.form.getlist('flat_id') if x])],
            # [(6, 0, [int(x) for x in request.httprequest.form.getlist('flat_id') if x])],
            # 'tower_id':post.get('tower_id'),
            'tower_id':[(6,0,[int(x) for x in request.httprequest.form.getlist('tower_id') if x])],
            'to_committee':committee_id,
            # 'security_id':security_id,
            'security_id': [(6,0,[int(x) for x in request.httprequest.form.getlist('security_id') if x])],
            'resident_id': resident_id,
            'location':post.get('location'),
            'alert_type':post.get('alert_type'),
            'create_date':post.get('create_date'),
            # 'stage':'draft',
        })

        print('\n\n\n................',[int(x) for x in request.httprequest.form.getlist('flat_id')])
        alert.action_send_email()
        return request.redirect('/my/alerts')

    @http.route('/my/alert/<int:alert_id>',type='http',auth='user',website=True)
    def alert_detail(self, alert_id, access_token=None,**kw):
        alert=request.env['resident.alerts'].sudo().browse(alert_id)
        if alert.user_id.id != request.env.user.id:
            return request.redirect('/my/alerts')
        return request.render('smart_society.portal_alert_detail', {
            'alert': alert
        })

    @http.route('/my/alert/new',type='http',auth='user',website=True)
    def alert_form(self,**kw):
        resident = request.env['resident.registrations'].sudo().search([
            ('user_id', '=', request.env.user.id)
        ], limit=1)

        committees=request.env['society.committee'].sudo().search([
            ('tower_id','=',resident.tower_id.id),
        ])
        security=request.env['security.guard'].sudo().search([
            ('tower_id', '=', resident.tower_id.id),
        ])
        print('\n\n\n....security  ......security[:]....',security[:])
        tower=request.env['society.tower'].sudo().search([])
        flat=request.env['society.flat'].sudo().search([])
        resident_id=request.env['resident.registrations'].sudo().search([])
        alert_types = request.env['resident.alerts']._fields['alert_type'].selection
        # alert_type=request.env['resident.alert'].sudo().search([])

        return request.render('smart_society.portal_alert_form', {
            'committees': committees,
            'security': security,
            'tower':tower,
            'flat':flat,
            # 'resident_id':resident.id,
            'default_committee': committees[:],
            'default_security': security[:],
            'alert_types': alert_types,
            # 'default_name':alert_types,
        })



    @http.route(['/my/facility-bookings'], type='http', auth='user', website=True)
    def portal_facility_bookings(self, tab='gym', **kwargs):
        resident = request.env['resident.registrations'].search([
            ('user_id', '=', request.env.user.id)
        ], limit=1)

        gym_bookings = request.env['gym.booking'].search([
            ('resident_id', '=', resident.id)
        ]) if resident else []

        cbh_bookings = request.env['clubhouse.booking'].search([
            ('resident_id', 'in', [resident.id])
        ]) if resident else []

        # Validate tab value
        if tab not in ('gym', 'clubhouse'):
            tab = 'gym'

        values = {
            'gym_bookings': gym_bookings,
            'cbh_bookings': cbh_bookings,
            'gym_count': len(gym_bookings),
            'cbh_count': len(cbh_bookings),
            'active_tab': tab,
            'resident': resident,
            'page_name': 'facility_bookings',
        }
        return request.render('smart_society.portal_facility_bookings', values)
# emergency sos alert emergency fire alert  medical/panic button  emergency broadcast button
















