
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
