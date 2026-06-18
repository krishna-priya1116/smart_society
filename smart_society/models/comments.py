   # related = 'flat_id.society_id',

    # @api.constrains('flat_id')
    # def check_flat(self):
    #     for record in self:
    #         pass



    # @api.model
    # def create(self, vals_list):
    #     guest_house=super().create(vals_list)
    #     print('\n\n\n.........guest_house........',guest_house)
    #     for house in guest_house:
    #         print('\n........house.........',house)
    #         search_house=self.env['society.flat'].search([
    #             ('flat_status','=','guest_house')
    #         ],limit=1)
    #         print('..................search_house...............',search_house)




# class Committee(models.Model):
#     _name='society.committee'
#     _description='Committees in society'
#
#     name=fields.Char(string='Committee name')
#     committee_name=fields.Many2many('res.partner',string='Committee members',required=True)
#     chairman_name=fields.Many2one('res.partner',string='Chairman')
#     secretary_name=fields.Many2one('res.partner',string='Secretary')
#     society_id=fields.Many2one('society.setup',string='Society')
#



# @api.depends('price_per_person','person_count','days')
# def calculate_person_price(self):
#     for record in self:
#         record.total_price = (record.person_count * record.price_per_person)*record.days
#

# @api.constrains('tower_count')
    # def generate_tower(self):
    #     for record in self:
    #         for tower in range(record.tower_count):
    #             tower=self.env['society.tower'].search([
    #                 ('society_id','=',record.id),
    #                 ('name', '=', f'{record.id}-tower-{tower + 1}')
    #             ])
    #             if not tower:
    #                 self.env['society.tower'].create({
    #                 'name':f'{record.id}-tower-{tower+1}',
    #                 'society_id':record.id,
    #                 })

    # @api.constrains('gym_capacity')
    # def create_gym_slot(self):
    #     for record in self:
    #         print('..............record........',record)
    #         list1=['morning','afternoon','evening','night']
    #         for shift in range(len(list1)):
    #             print('.........shift....',shift)
    #             first_letter=(list1[shift][0]).upper()
    #             print('\n\n\n\n........first_letter.....',first_letter)
    #             print('\n\n\n....record.gym_capacity....',record.gym_capacity)
    #             for slot in range(record.gym_capacity):
    #                 # print('\n\n...slot.....',slot)
    #                 exist_slot=self.env['gym.slots'].search([
    #                     ('name','=',f'{first_letter}-slot{slot + 1}'),
    #                     ('society_id', '=', record.id),
    #
    #                 ])
    #                 # ('name','=',f'res-{park.parking_place}-t{park.tower_id.id}-{i + 1}'),
    #                 if not exist_slot:
    #                     print('\n\n\n......not.exist_slot..', exist_slot)
    #                     g_slots=self.env['gym.slots'].create({
    #                         'name':f'{first_letter}-slot{slot + 1}',
    #                         'society_id':record.id,
    #                         'shift':list1[shift],
    #                     })
    #                     print('.....g_slots......',g_slots)


# class GymSlots(models.Model):
#     _name='gym.slots'
#     _description='Gym Slots Model'
#
#     society_id=fields.Many2one('society.setup',string='Society')
#     name=fields.Char(string='Gym Slots Name')
#     shift=fields.Selection(selection=[('morning','Morning'),('afternoon','Afternoon'),('evening','Evening'),('night','Night')])
#     gym_booking_charge=fields.Float(related='society_id.gym_booking_charge',string='Gym Booking Charge')
#     is_occupied=fields.Boolean(string='Is Occupied')
#     resident_id=fields.Many2one('resident.registrations',string='Resident ID')
#
#     @api.onchange('resident_id')
#     def is_occupied_resident(self):
#         for record in self:
#             if record.resident_id:
#                 record.is_occupied=True
#             elif not record.resident_id:
#                 record.is_occupied=False
# self.save_to_model()


# def save_to_model(self):
#     self.ensure_one()
#
#     save_record=self.env['emergency.broadcast'].create({
#         'name':self.name,
#         'description':self.description,
#         'flat_id':self.flat_ids,
#         'tower_ids':self.tower_ids,
#         'datetime':self.datetime,
#         # 'resident_emails':self.resident_emails,
#     })
#     return {
#         'type': 'ir.actions.act_window',
#         'res_model': 'emergency.broadcast.save',
#         'res_id': save_record.id,
#         'view_mode': 'form,list',
#         'target': 'current',
#     }


# def save_to_model(self):
#     self.ensure_one()
#
#     save_record=self.env['society.alert'].create({
#         'name':self.name,
#         'description':self.description,
#         'flat_id':self.flat_id,
#         # 'tower_id':self.tower_id,
#         'user_id':self.user_id,
#         'location':self.location,
#         'datetime':self.datetime,
#         'to_committee':self.to_committee,
#         # 'committee_emails':self.committee_emails,
#     })
#     return {
#         'type': 'ir.actions.act_window',
#         'res_model': 'society.alert.save',
#         'res_id': save_record.id,
#         'view_mode': 'form,list',
#         'target': 'current',
#     }

# @api.onchange('tower_id')
    # def _check_tower_id(self):
    #     for record in self:
    #
    #         list_tower=[]
    #         if record.tower_id:
    #             print('\n\n\n......record.tower_id.....',record.tower_id)
    #             if len(record.tower_id)>1:
    #                 list_tower.append(record.tower_id)
    #         print('\n\n\n......record.tower_id.....',list_tower)
    # #




    # @api.constrains('tower_id')
    # def _check_tower_id(self):
    #     for record in self:
    #         list1=[]
    #         if record.tower_id:
    #             print('\n\n\nrecord.tower_id.....................',record.tower_id)
    #         help_desk_id=self.env['help.desk'].search([
    #             ('tower_id','=',record.tower_id.id),
    #         ])
    #         print('.........help_desk_id.....................',help_desk_id)
    #
    #         list1.append(help_desk_id)
    #         print('\n\n\n.........list1............',list1)
    #         for i in list1:
    #             record.write({
    #                 'help_desk_id':i,
    #             })
    #         print('\n\n\n.......record.help_desk_id.....',record.help_desk_id)




            # , limit = 1
            # record.help_desk_id=record.help_desk_id.mapped(list1)
            # if not help_desk_id:
            #     print('')
            # record.help_desk_id.mapped('help_desk_id')




# class Complaint(models.Model):
#     _name = 'complaint.desk'
#     _description = 'Complaint desk'
#     _inherit = ['mail.thread', 'mail.activity.mixin']
#
#     name = fields.Char(string='Complaint', required=True)
#     tower_id = fields.Many2one(related='flat_id.tower_id', string='Tower', required=True)
#     # tower_id = fields.Many2one('society.tower', string='Tower', required=True)
#     # flat_id = fields.Many2one('society.flat', string='Flat', required=True)
#     flat_id = fields.Many2one(related='resident_id.flat_id', string='Flat', required=True)
#     resident_id = fields.Many2one('resident.registrations', string='Resident')
#     description = fields.Char(string='Description', required=True)
#     create_date=fields.Datetime(string='Create Date',default=fields.Date.today())
#     to_committee = fields.Many2one('society.committee')
#     help_desk_id = fields.Many2one('help.desk', string='Helpdesk')
#     user_id = fields.Many2one('res.users',string='Resident',default=lambda self: self.env.user)
#     committee_emails = fields.Char( string='Committee Emails',compute='_compute_committee_emails')
#     stage = fields.Selection([
#         ('draft', 'Draft'),
#         ('send', 'Sent'),
#         ('on_process', 'On Process'),
#         ('hold', 'Hold'),
#         ('resolve', 'Resolved'),
#         ('reject', 'Rejected'),
#     ], string='Stage', default='draft', tracking=True)
#     proof = fields.Binary(string='Proof Photo/video')
#
#     def draft_complaint(self):
#         for record in self:
#             if record.stage=='send' or record.stage=='cancel':
#                 record.stage = 'draft'
#
#     def cancel_complaint(self):
#         for record in self:
#             if record.stage == 'send':
#                 raise ValidationError("The complaint is already send, can't cancel")
#             record.stage = 'cancel'
#
#     @api.onchange('resident_id')
#     def help_desk_id_check(self):
#         for record in self:
#             help_desk_id=self.env['help.desk'].search([
#                 ('tower_id','=',record.tower_id.id),
#             ],limit=1)
#             print('\n\n\n\n.............................help_desk_id.......',help_desk_id)
#             if not record.help_desk_id:
#                 record.help_desk_id = help_desk_id
#
#     @api.depends('to_committee')
#     def _compute_committee_emails(self):
#         for record in self:
#             emails = []
#             for partner in record.to_committee.committee_name_id:
#                 if partner.email:
#                     emails.append(partner.email)
#
#             if record.to_committee.chairman_id.email:
#                 emails.append(record.to_committee.chairman_id.email)
#
#             if record.to_committee.secretary_id.email:
#                 emails.append(record.to_committee.secretary_id.email)
#
#             emails = list(set(emails))
#             record.committee_emails = ",".join(emails)
#
#     def send_complaint(self):
#         template = self.env.ref(
#             'smart_society.complaint_email_template_smart_society',
#             raise_if_not_found=False
#         )
#         if not template:
#             raise UserError("Mail Template not found. Please check the template.")
#         for record in self:
#             record.stage = 'send'
#             # This sends the email AND logs it in the chatter
#             record.message_post_with_source(
#                 template,
#                 email_layout_xmlid='mail.mail_notification_layout_with_responsible_signature',
#                 subtype_xmlid='mail.mt_comment',
#             )

# class NoticeBoardPortal(CustomerPortal):
#
#     def _prepare_home_portal_values(self,counters):
#         values=super()._prepare_home_portal_values(counters)
#         if 'notice_count' in counters:
#             resident=request.env['resident.registrations'].sudo().search([
#                 ('user_id','=',request.env.user.id)
#             ],limit=1)
#             print('\n\n\n....NoticeBoardPortal.....resident....',resident)
#             domain=[('stage', '=', 'send')]
#             if resident and resident.tower_id:
#                 print('\n\n\n....NoticeBoardPortal.....if....')
#                 domain=[('tower_id','in',resident.tower_id.ids),('stage','=','send')]
#             values['notice_count']=request.env['notice.board'].sudo().search_count(domain)
#             print('\n\n\n.....NoticeBoardPortal.....values',values)
#         return values
#
#
#
#     @http.route('/my/notices',type='http',auth='user',website=True)
#     def notice_board(self,**kw):
#         resident = request.env['resident.registrations'].sudo().search([
#             ('user_id', '=', request.env.user.id)
#         ], limit=1)
#         print('\n\n\nnotice_board........resident.....',resident)
#         domain=[('stage','=','send')]
#         if resident and resident.tower_id:
#             print('\n\n\n....notice_board.....if....')
#             domain=[('tower_id','in',resident.tower_id.ids),
#                     ('stage','=','send')]
#         notices=request.env['notice.board'].sudo().search(domain,order='create_date desc')
#         return request.render('smart_society.portal_notice_board',
#                               {'notices':notices,
#                                'resident':resident}
#         )
#     @http.route('/my/notice/<int:notice_id>/',type='http',auth='user',website=True)
#     def notice_detail(self,notice_id,**kw):
#         notice=request.env['notice.board'].sudo().browse(notice_id)
#         if not notice.exists():
#             return request.redirect('/my/notices')
#         return request.render('smart_society.portal_notice_detail',
#                               {'notice':notice,})


# class NoticeBoardPortal(CustomerPortal):

    # def _get_portal_home_counters(self):
    #     # This tells the portal WHICH counter keys to compute
    #     counters1 = super()._get_portal_home_counters()
    #     counters1 += ['notice_count']  # ← Without this, notice_count never gets requested
    #     print('\n\n\n....NoticeBoardPortal.....counters1.',counters1)
    #     return counters1


    # def _prepare_home_portal_values(self, counters1):
    #     values = super()._prepare_home_portal_values(counters1)

        # if 'notice_count' in counters1:
        #     print('\n\n\n.......notice_count.')
        #     resident = request.env['resident.registrations'].sudo().search([
        #         ('user_id', '=', request.env.user.id)
        #     ], limit=1)
        #     print('resident tower_id:', resident.tower_id.ids)  # ← Check tower IDs
        #     all_notices = request.env['notice.board'].sudo().search([])
        #     print('all notices:', all_notices)
        #     for n in all_notices:
        #         print('notice:', n.name, '| stage:', n.stage, '| towers:', n.tower_id.ids)
        #
        #     domain = [('stage', '=', 'send')]
        #     if resident and resident.tower_id:
        #         domain = [
        #             ('tower_id', 'in', resident.tower_id.ids),
        #             ('stage', '=', 'send')
        #         ]
        #
        #     print('final domain:', domain)
        #     count=values['notice_count'] = request.env['notice.board'].sudo().search_count(domain)
        #     # values['complaint_count'] = count if count > 0 else None
        #
        #     print('final count:', values['notice_count'])
        #     print('final count:', count)
        #     print('\n\n\n.....NoticeBoardPortal.....resident',resident)
        #     domain = [('stage', '=', 'send')]
        #     if resident and resident.tower_id:
        #         domain = [
        #             ('tower_id', 'in', resident.tower_id.ids),
        #             ('stage', '=', 'send')
        #         ]
        #
        #     count=values['notice_count'] = request.env['notice.board'].sudo().search_count(domain)
        #     values['notice_count'] = count if count > 0 else None
        #
        #     print('\n\n\n....NoticeBoardPortal...values.',values)
        # return values
# class EventAnnouncementPortal(CustomerPortal):

    # def _get_portal_home_counters(self):
    #     # This tells the portal WHICH counter keys to compute
    #     counters2 = super()._get_portal_home_counters()
    #     counters2 += ['event_count']  # ← Without this, notice_count never gets requested
    #     print('\n\n\n....EventAnnouncementPortal.....counters2.',counters2)
    #     return counters2


    # def _prepare_home_portal_values(self, counters2):
    #     values = super()._prepare_home_portal_values(counters2)
    #
    #     if 'event_count' in counters2:
    #         print('\n\n\n.......event_count.')
    #         resident = request.env['resident.registrations'].sudo().search([
    #             ('user_id', '=', request.env.user.id)
    #         ], limit=1)
    #         print('resident tower_id:', resident.tower_id.ids)  # ← Check tower IDs
    #         all_events = request.env['event.announcement'].sudo().search([])
    #         print('all_events:', all_events)
    #         for e in all_events:
    #             print('event:', e.name, '| stage:', e.stage, '| towers:', e.tower_id.ids)
    #
    #         domain = [('stage', '=', 'send')]
    #         if resident and resident.tower_id:
    #             domain = [
    #                 ('tower_id', 'in', resident.tower_id.ids),
    #                 ('stage', '=', 'send')
    #             ]
    #
    #         print('final domain:', domain)
    #         count=values['event_count'] = request.env['event.announcement'].sudo().search_count(domain)
    #         # values['complaint_count'] = count if count > 0 else None
    #
    #         print('final event_count count:', values['event_count'])
    #         print('final count:', count)
    #         print('\n\n\n.....EventAnnouncementPortal.....resident',resident)
    #         domain = [('stage', '=', 'send')]
    #         if resident and resident.tower_id:
    #             domain = [
    #                 ('tower_id', 'in', resident.tower_id.ids),
    #                 ('stage', '=', 'send')
    #             ]
    #
    #         count=values['event_count'] = request.env['event.announcement'].sudo().search_count(domain)
    #         values['event_count'] = count if count > 0 else None
    #
    #         print('\n\n\n....EventAnnouncementPortal...values.',values)
    #     return values


   # def _get_portal_home_counters(self):
    #     # This tells the portal WHICH counter keys to compute
    #     counters = super()._get_portal_home_counters()
    #     counters += ['complaint_count']  # ← Without this, notice_count never gets requested
    #     return counters
    #
    # def _prepare_home_portal_values(self, counters):
    #     values = super()._prepare_home_portal_values(counters)
    #     if 'complaint_count' in counters:
    #         count=values['complaint_count'] = request.env['complaint.desk'].sudo().search_count([
    #             ('user_id', '=', request.env.user.id)
    #         ])
    #         values['complaint_count'] = count
    #             # if count > 0 else None
    #     return values



# class EventPortal(CustomerPortal):
#     def _get_portal_home_counters(self):
#         counters = super()._get_portal_home_counters()
#         counters += ['event.announcement']
#         print('\n\n\n....EventPortal.....counters.',counters)
#         return counters
#
#     def _prepare_home_portal_values(self, counters):
#         values = super()._prepare_home_portal_values(counters)
#         if 'event_count' in counters:
#             print('event_count:........')
#         resident = request.env['resident.registrations'].sudo().search([
#             ('user_id', '=', request.env.user.id)
#         ], limit=1)
#         print('resident tower_id:', resident.tower_id.ids)
#         all_events = request.env['event.announcement'].sudo().search([])
#         print('all_events:', all_events)
#         for e in all_events:
#             print('event:', e.name, '| stage:', e.stage, '| towers:', e.tower_id.ids)
#         domain = [('stage', '=', 'send')]
#         if resident and resident.tower_id:
#             domain = [
#                 ('tower_id', 'in', resident.tower_id.ids),
#                 ('stage', '=', 'send')
#             ]
#             print('final domain:', domain)
#             count = values['event_count'] = request.env['event.announcement'].sudo().search(domain)
#             print('final count:', values['event_count'])
#             print('final count:', count)
#             print('\n\n\n.....EventPortal.....resident', resident)
#             count = values['event_count'] = request.env['event.announcement'].sudo().search_count(domain)
#             values['event_count'] = count if count > 0 else None
#
#             print('\n\n\n....EventPortal...values.', values)
#         return values
#
#
#     @http.route('/my/events', type='http', auth='user', website=True)
#     def event_announcement(self, **kw):
#         resident = request.env['resident.registrations'].sudo().search([
#             ('user_id', '=', request.env.user.id)
#         ], limit=1)
#
#         domain = [('stage', '=', 'send')]
#         if resident and resident.tower_id:
#             domain = [
#                 ('tower_id', 'in', resident.tower_id.ids),
#                 ('stage', '=', 'send')
#             ]
#         events = request.env['event.announcement'].sudo().search(domain, order='create_date desc')
#         return request.render('smart_society.portal_event_announcement', {
#             'events': events,
#             'resident': resident,
#         })
#
#
#     @http.route('/my/events/<int:event_id>/', type='http', auth='user', website=True)
#     def event_detail(self, event_id, **kw):
#         event = request.env['event.announcement'].sudo().browse(event_id)
#         if not event.exists():
#             return request.redirect('/my/events')
#         return request.render('smart_society.portal_event_detail', {
#             'event': event,
#         })
# for record in self:
#     print('\n\n\nrecord........................',record)
#     self.message_post_with_source(
#         template,
#         subtype_id=self.env.ref('mail.mt_note').id,
#     )


# @api.model_create_multi
# def create(self, vals_list):
#
#     complaints = super().create(vals_list)
#     template = self.env.ref(
#         'smart_society.email_template_smart_society',
#         raise_if_not_found=False
#     )
#     if template:
#         template.send_mail(self.id, force_send=True)
#
# for complaint in complaints:
#     # Only send if there is an assigned user with an email
#     if complaint.resident_id and complaint.resident_id.email:
#         complaint.message_post_with_source(
#             template,
#             email_layout_xmlid='mail.mail_notification_light',
#             subtype_xmlid='mail.mt_note',
#         )
# return complaints

# subtype_xmlid='mail.mt_note',
#              email_layout_xmlid='mail.mail_notification_light'
# for record in self:                                 this
#     template.send_mail(record.id, force_send=True)   this

# def send_email(self):
#     if not self.env.user.has_group('base.group_system'):
#         raise UserError("You do not have permission to send emails.")
#     template = self.env.ref(
#         'task_management.email_template_manage_tasks',
#         raise_if_not_found=False
#     )
#     if not template:
#         raise UserError("Mail Template not found. Please check the template.")
#     for record in self:
#         # This sends the email AND logs it in the chatter
#         record.message_post_with_source(
#             template,
#             email_layout_xmlid='mail.mail_notification_layout_with_responsible_signature',
#             subtype_xmlid='mail.mt_comment',
#         )

# @api.constrains('to_send')
# def get_committee_name(self):
#     for record in self:
#         if record.to_send:
#             print('........record.to_send.......',record.to_send)

# def send_email(self):
#     if not self.env.user:
#         # .has_group('base.group_system')
#         raise UserError("You do not have permission to send emails.")
#     template=self.env.ref(
#         'smart_society.email_template_smart_society',
#         raise_if_not_found=False
#     )
#     if not template:
#         raise UserError("Mail Template not found. Please check the template.")
# self.message_post_with_source(
#     template,
#     subtype_xmlid=self.env.ref('mail.mt_note').id
#     # email_layoutxmlid='mail.mail_notification_light',
#     # subtype_xmlid='mail.mt_note',
# )
# active = fields.Boolean(default=True)
# tracking_ids = fields.One2many(
#     'vehicle.tracking',
#     'vehicle_id',
#     string='Tracking'
# )

# @api.constrains('mobile_number','email')
# def check_mobile_number(self):
#     for registration in self:
#         if registration.mobile_number or registration.email:
#             self.env['res.users'].create({
#                 'name':registration.partner_id,
#                 'email': registration.email,
#                 'phone': registration.mobile_number,
#             })
#             self.env['res.partner'].create({
#                 # 'name': registration.name,
#                 'name': registration.partner_id,
#                 'email': registration.email,
#                 'phone': registration.mobile_number,
#             })

# <!--                        <field name="real_owner" domain="[('resident_type','=','tenant'),('resident_type','=','temporary_resident')]"/>-->
# <!--                        <field name="real_owner" invisible ="[('resident_type','not in','tenant or temporary_resident')]"/>-->
# <!--invisible="stage in ['completed','cancelled']"-->
# vehicle_id=fields.Many2one('resident.registrations')

# @api.constrains('parking_slot_id')
# def check_slot_allocation(self):
#     for rec in self:
#         if rec.parking_slot_id:
#             allocated_vehicle = self.search([
#                 ('parking_slot_id', '=', rec.parking_slot_id.id),
#                 ('id', '!=', rec.id)
#             ])
#             if allocated_vehicle:
#                 raise ValidationError('Parking Slot already allocated')
#
# def action_vehicle_entry(self):
#     for rec in self:
#         if rec.is_inside:
#             raise ValidationError('Vehicle already inside')
#
#         if not rec.parking_slot_id:
#             raise ValidationError('No parking slot assigned.')
#
#         if rec.parking_slot_id.is_occupied:
#             raise ValidationError('Parking slot occupied.')
#
#         rec.parking_slot_id.is_occupied = True
#         rec.is_inside = True
#         self.env['vehicle.tracking'].create({
#             'vehicle_id': rec.id,
#             'parking_slot_id': rec.parking_slot_id.id,
#             'entry_time': fields.Datetime.now(),
#             'status': 'inside',
#         })
#
# def action_vehicle_exit(self):
#     for rec in self:
#         tracking = self.env['vehicle.tracking'].search([
#             ('vehicle_id', '=', rec.id),
#             ('status', '=', 'inside')
#         ], limit=1)
#         if tracking:
#             tracking.write({
#                 'exit_time': fields.Datetime.now(),
#                 'status': 'exited'
#             })
#         rec.parking_slot_id.is_occupied = False
#         rec.is_inside = False

# class VehicleTracking(models.Model):
#     _name = 'vehicle.tracking'
#     _description = 'Vehicle Tracking'
#     _order = 'entry_time desc'
#
#     vehicle_id = fields.Many2one(
#         'vehicle.registrations',
#         string='Resident Vehicle'
#     )
#
#     visitor_vehicle_id = fields.Many2one(
#         'visitor.vehicle',
#         string='Visitor Vehicle'
#     )
#
#     parking_slot_id = fields.Many2one(
#         'parking.slot',
#         string='Parking Slot',
#         required=True
#     )
#
#     entry_time = fields.Datetime(
#         string='Entry Time'
#     )
#
#     exit_time = fields.Datetime(
#         string='Exit Time'
#     )
#
#     status = fields.Selection([
#         ('inside', 'Inside'),
#         ('exited', 'Exited')
#     ], default='inside')
#
#     duration = fields.Float(
#         compute='_compute_duration',
#         string='Parking Hours'
#     )

  # def _compute_duration(self):
  #
  #       for rec in self:
  #
  #           rec.duration = 0
  #
  #           if rec.entry_time and rec.exit_time:
  #
  #               diff = rec.exit_time - rec.entry_time
  #
  #               rec.duration = diff.total_seconds() / 3600


# vehicle_ids=fields.One2many('vehicle.registrations',string='Vehicle')


# def action_generate_slots(self):
#
#     for rec in self:
#
#         # delete old slots
#         rec.parking_slot_ids.unlink()
#         count = 1
#
#         # RESIDENT
#         for i in range(rec.resident_parking):
#             self.env['parking.slot'].create({
#                 'name': f'R-{count}',
#                 'parking_type': 'resident',
#                 'parking_id': rec.id,
#                 'tower_id': rec.tower_id.id,
#                 'parking_place': rec.parking_place,
#             })
#             count += 1
#
#         # VISITOR
#         for j in range(rec.visitor_parking):
#             self.env['parking.slot'].create({
#                 'name': f'V-{count}',
#                 'parking_type': 'visitor',
#                 'parking_id': rec.id,
#                 'tower_id': rec.tower_id.id,
#                 'parking_place': rec.parking_place,
#             })
#             count += 1
#
#         # EV
#         for k in range(rec.ev_parking):
#             self.env['parking.slot'].create({
#                 'name': f'EV-{count}',
#                 'parking_type': 'ev',
#                 'parking_id': rec.id,
#                 'tower_id': rec.tower_id.id,
#                 'parking_place': rec.parking_place,
#             })
#             count += 1
#
#         # OTHER
#         for l in range(rec.other_parking):
#             self.env['parking.slot'].create({
#                 'name': f'O-{count}',
#                 'parking_type': 'other',
#                 'parking_id': rec.id,
#                 'tower_id': rec.tower_id.id,
#                 'parking_place': rec.parking_place,
#             })
#             count += 1
# @api.constrains('resident_parking','visitor_parking','ev_charging','other_parking','parking_slot_ids')
# def check_parking_count(self):
#     for park in self:
#         # if park.resident_parking or park.visitor_parking or park.ev_charging or park.other_parking:
#             # total_count=park.resident_parking+park.visitor_parking+park.ev_charging+park.other_parking
#             # resident_parking_count=len(park.parking_slot_ids.mapped('parking_type'=='resident_parking'))
#             # ev_charging_count=len(park.parking_slot_ids.mapped('parking_type'=='ev_charging'))
#             # visitor_parking_count=len(park.parking_slot_ids.mapped('parking_type'=='visitor_parking'))
#             # other_parking_count=len(park.parking_slot_ids.mapped('parking_type'=='other_parking'))
#             # print('\n\n\n.............resident_parking_count..........',resident_parking_count)
#             # for i in range(resident_parking_count):
#             #     print('\n\n\n\n......................................\n\n\n\n')
#         if park.resident_parking:
#             for i in range(park.resident_parking):
#                 vehicle=self.env['parking.slot'].create({
#                     'tower_id':park.tower_id.id,
#                     'parking_id':park.id,
#                     'parking_type':park.resident_parking,
#                     'name':str(park.parking_place)+str(park.tower_id.id),
#                 })
#                 print('\n\n\n..........park.resident_parking....................',vehicle)
#         if park.ev_charging:
#             for j in range(park.ev_charging):
#                 vehicle=self.env['parking.slot'].create({
#                     'tower_id':park.tower_id.id,
#                     'parking_id':park.id,
#                     'parking_type':park.ev_charging,
#                     'name':str(park.parking_place)+str(park.tower_id.id),
#                 })
#                 print('\n\n\n..........park.resident_parking....................',vehicle)
#         if park.visitor_parking:
#             for k in range(park.visitor_parking):
#                 vehicle=self.env['parking.slot'].create({
#                     'tower_id':park.tower_id.id,
#                     'parking_id':park.id,
#                     'parking_type':park.visitor_parking,
#                     'name':str(park.parking_place)+str(park.tower_id.id),
#                 })
#                 print('\n\n\n..........park.resident_parking....................',vehicle)
#
#         if park.other_parking:
#             for l in range(park.other_parking):
#                 vehicle=self.env['parking.slot'].create({
#                     'tower_id':park.tower_id.id,
#                     'parking_id':park.id,
#                     'parking_type':park.other_parking,
#                     'name':str(park.parking_place)+str(park.tower_id.id),
#                 })
#                 print('\n\n\n..........park.visitor_parking....................',vehicle)
