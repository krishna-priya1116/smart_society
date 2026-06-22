# #
#         <!--<odoo>-->
# <!--    <record id="view_dashboard_home_forms" model="ir.ui.view">-->
# <!--        <field name="name">society.dashboard.form</field>-->
# <!--        <field name="model">society.dashboard</field>-->
# <!--        <field name="arch" type="xml">-->
# <!--            <form string="Smart Society Dashboard">-->
# <!--                <sheet>-->
# <!--                    <style>-->
# <!--                        .dashboard-header {-->
# <!--                            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);-->
# <!--                            color: white;-->
# <!--                            padding: 30px;-->
# <!--                            border-radius: 12px;-->
# <!--                            margin-bottom: 20px;-->
# <!--                            box-shadow: 0 4px 15px rgba(0,0,0,0.1);-->
# <!--                        }-->
# <!--                        .dashboard-header h1 {-->
# <!--                            margin: 0;-->
# <!--                            font-size: 32px;-->
# <!--                            font-weight: 700;-->
# <!--                            letter-spacing: -0.5px;-->
# <!--                        }-->
# <!--                        .dashboard-header p {-->
# <!--                            margin: 8px 0 0 0;-->
# <!--                            opacity: 0.95;-->
# <!--                            font-size: 14px;-->
# <!--                        }-->
# <!--                        .o_notebook .nav-link {-->
# <!--                            border: none;-->
# <!--                            border-bottom: 3px solid transparent;-->
# <!--                            color: #6c757d;-->
# <!--                            font-weight: 600;-->
# <!--                            transition: all 0.3s ease;-->
# <!--                            padding: 12px 20px;-->
# <!--                            margin-right: 8px;-->
# <!--                            border-radius: 8px 8px 0 0;-->
# <!--                        }-->
# <!--                        .o_notebook .nav-link:hover {-->
# <!--                            background-color: #f0f0f0;-->
# <!--                            color: #495057;-->
# <!--                            border-bottom-color: #667eea;-->
# <!--                        }-->
# <!--                        .o_notebook .nav-link.active {-->
# <!--                            color: #667eea;-->
# <!--                            background-color: #f8f9ff;-->
# <!--                            border-bottom-color: #667eea;-->
# <!--                            box-shadow: 0 2px 8px rgba(102, 126, 234, 0.15);-->
# <!--                        }-->
# <!--                        .oe_kanban_card {-->
# <!--                            background: #ffffff;-->
# <!--                            border: 1px solid #e9ecef;-->
# <!--                            border-radius: 12px;-->
# <!--                            box-shadow: 0 2px 8px rgba(0,0,0,0.08);-->
# <!--                            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);-->
# <!--                            overflow: hidden;-->
# <!--                        }-->
# <!--                        .oe_kanban_card:hover {-->
# <!--                            box-shadow: 0 8px 24px rgba(0,0,0,0.15);-->
# <!--                            transform: translateY(-4px);-->
# <!--                            border-color: #667eea;-->
# <!--                        }-->
# <!--                        .oe_kanban_content {-->
# <!--                            padding: 16px;-->
# <!--                        }-->
# <!--                        .oe_kanban_title {-->
# <!--                            font-size: 15px;-->
# <!--                            font-weight: 700;-->
# <!--                            color: #2d3436;-->
# <!--                            margin: 0 0 12px 0;-->
# <!--                            display: flex;-->
# <!--                            align-items: center;-->
# <!--                            gap: 8px;-->
# <!--                        }-->
# <!--                        .oe_kanban_title b {-->
# <!--                            display: block;-->
# <!--                            overflow: hidden;-->
# <!--                            text-overflow: ellipsis;-->
# <!--                            white-space: nowrap;-->
# <!--                            flex: 1;-->
# <!--                        }-->
# <!--                        .oe_kanban_text {-->
# <!--                            font-size: 13px;-->
# <!--                            color: #636e72;-->
# <!--                            line-height: 1.5;-->
# <!--                            margin-bottom: 12px;-->
# <!--                        }-->
# <!--                        .oe_kanban_text p {-->
# <!--                            margin: 0 0 8px 0;-->
# <!--                        }-->
# <!--                        .oe_kanban_text strong {-->
# <!--                            color: #2d3436;-->
# <!--                            font-weight: 600;-->
# <!--                        }-->
# <!--                        .oe_kanban_footer {-->
# <!--                            border-top: 1px solid #f1f3f5;-->
# <!--                            padding-top: 10px;-->
# <!--                            display: flex;-->
# <!--                            justify-content: space-between;-->
# <!--                            align-items: center;-->
# <!--                        }-->
# <!--                        .status-badge {-->
# <!--                            display: inline-block;-->
# <!--                            padding: 4px 10px;-->
# <!--                            border-radius: 20px;-->
# <!--                            font-size: 12px;-->
# <!--                            font-weight: 600;-->
# <!--                            text-transform: uppercase;-->
# <!--                            letter-spacing: 0.5px;-->
# <!--                        }-->
# <!--                        .badge-draft { background-color: #e3f2fd; color: #1976d2; }-->
# <!--                        .badge-published { background-color: #e8f5e9; color: #388e3c; }-->
# <!--                        .badge-closed { background-color: #fce4ec; color: #c2185b; }-->
# <!--                        .badge-in-progress { background-color: #fff3e0; color: #f57c00; }-->
# <!--                        .kanban-group-header {-->
# <!--                            font-size: 14px;-->
# <!--                            font-weight: 700;-->
# <!--                            color: #667eea;-->
# <!--                            text-transform: uppercase;-->
# <!--                            letter-spacing: 1px;-->
# <!--                            padding: 12px 0;-->
# <!--                            border-bottom: 2px solid #667eea;-->
# <!--                            margin-bottom: 16px;-->
# <!--                        }-->
# <!--                        .empty-state {-->
# <!--                            text-align: center;-->
# <!--                            padding: 40px 20px;-->
# <!--                            color: #95a5a6;-->
# <!--                        }-->
# <!--                        .empty-state-icon {-->
# <!--                            font-size: 48px;-->
# <!--                            margin-bottom: 12px;-->
# <!--                        }-->
# <!--                    </style>-->
# <!--                    <group>-->
# <!--                        <div class="dashboard-header">-->
# <!--                            <h1> Smart Society Dashboard</h1>-->
# <!--                            <p>Real-time overview of society operations and resident management</p>-->
# <!--                        </div>-->
# <!--                        <group>-->
# <!--                            <div class="row g-2">-->
# <!--                                <div class="col-3">-->
# <!--                                    <button type="object" name="sos_alerts"-->
# <!--                                            class="btn bg-danger-subtle border border-danger border-2 rounded-3 shadow-sm text-danger fw-bold"-->
# <!--                                            style="width:100%; height:70px; transition: all 0.3s ease;"-->
# <!--                                            onmouseover="this.style.backgroundColor='#f8d7da'; this.style.boxShadow='0 6px 20px rgba(220, 53, 69, 0.4)';"-->
# <!--                                            onmouseout="this.style.backgroundColor=''; this.style.boxShadow='0 2px 8px rgba(0,0,0,0.1)';">-->
# <!--                                         Emergency SOS Alert-->
# <!--                                    </button>-->
# <!--                                </div>-->
# <!--                                <div class="col-3">-->
# <!--                                    <button type="object" name="fire_alerts"-->
# <!--                                            class="btn bg-danger-subtle border border-danger border-2 rounded-3 shadow-sm text-danger fw-bold"-->
# <!--                                            style="width:100%; height:70px; transition: all 0.3s ease;"-->
# <!--                                            onmouseover="this.style.backgroundColor='#f8d7da'; this.style.boxShadow='0 6px 20px rgba(220, 53, 69, 0.4)';"-->
# <!--                                            onmouseout="this.style.backgroundColor=''; this.style.boxShadow='0 2px 8px rgba(0,0,0,0.1)';">-->
# <!--                                         Emergency FIRE Alert-->
# <!--                                    </button>-->
# <!--                                </div>-->
# <!--                                <div class="col-3">-->
# <!--                                    <button type="object" name="medical_panic_buttons"-->
# <!--                                            class="btn bg-danger-subtle border border-danger border-2 rounded-3 shadow-sm text-danger fw-bold"-->
# <!--                                            style="width:100%; height:70px; transition: all 0.3s ease;"-->
# <!--                                            onmouseover="this.style.backgroundColor='#f8d7da'; this.style.boxShadow='0 6px 20px rgba(220, 53, 69, 0.4)';"-->
# <!--                                            onmouseout="this.style.backgroundColor=''; this.style.boxShadow='0 2px 8px rgba(0,0,0,0.1)';">-->
# <!--                                         Medical/Panic Button-->
# <!--                                    </button>-->
# <!--                                </div>-->
# <!--                                <div class="col-3">-->
# <!--                                    <button type="object" name="emergency_broadcast"-->
# <!--                                            class="btn bg-danger-subtle border border-danger border-2 rounded-3 shadow-sm text-danger fw-bold"-->
# <!--                                            style="width:100%; height:70px; transition: all 0.3s ease;"-->
# <!--                                            groups="smart_society.group_registration_committee,smart_society.group_registration_administration"-->
# <!--                                            onmouseover="this.style.backgroundColor='#f8d7da'; this.style.boxShadow='0 6px 20px rgba(220, 53, 69, 0.4)';"-->
# <!--                                            onmouseout="this.style.backgroundColor=''; this.style.boxShadow='0 2px 8px rgba(0,0,0,0.1)';">-->
# <!--                                         Emergency Broadcast-->
# <!--                                    </button>-->
# <!--                                </div>-->
# <!--                            </div>-->
# <!--                        </group>-->
# <!--                        <group col="4" class="mt-3">-->
# <!--                            <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 20px; border-radius: 10px; text-align: center;">-->
# <!--                                <strong style="font-size: 24px; display: block;">-->
# <!--                                    <field name="total_notices" readonly="1"/>-->
# <!--                                </strong>-->
# <!--                                <span style="font-size: 12px; opacity: 0.9;">Total Notices</span>-->
# <!--                            </div>-->
# <!--                            <div style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); color: white; padding: 20px; border-radius: 10px; text-align: center;">-->
# <!--                                <strong style="font-size: 24px; display: block;">-->
# <!--                                    <field name="total_events" readonly="1"/>-->
# <!--                                </strong>-->
# <!--                                <span style="font-size: 12px; opacity: 0.9;">Total Events</span>-->
# <!--                            </div>-->
# <!--                            <div style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); color: white; padding: 20px; border-radius: 10px; text-align: center;">-->
# <!--                                <strong style="font-size: 24px; display: block;">-->
# <!--                                    <field name="total_complaints" readonly="1"/>-->
# <!--                                </strong>-->
# <!--                                <span style="font-size: 12px; opacity: 0.9;">Total Complaints</span>-->
# <!--                            </div>-->
# <!--                        </group>-->
# <!--                    </group>-->
# <!--                    <notebook>-->
#
# <!--                        &lt;!&ndash; Notices Kanban View &ndash;&gt;-->
# <!--                        <page string=" Notices">-->
# <!--                            <field name="notice_ids" readonly="1">-->
# <!--                                <kanban default_group_by="stage">-->
# <!--                                    <field name="name"/>-->
# <!--                                    <field name="description"/>-->
# <!--                                    <field name="create_date"/>-->
# <!--                                    <field name="stage"/>-->
# <!--                                    <templates>-->
# <!--                                        <t t-name="card">-->
# <!--                                            <div class="oe_kanban_card">-->
# <!--                                                <div class="oe_kanban_content">-->
# <!--                                                    <div class="oe_kanban_title">-->
# <!--&lt;!&ndash;                                                        <span style="font-size: 16px;"></span>&ndash;&gt;-->
# <!--                                                        <b><field name="name"/></b>-->
# <!--                                                    </div>-->
# <!--                                                    <div class="oe_kanban_text">-->
# <!--                                                        <field name="description"/>-->
# <!--                                                    </div>-->
# <!--                                                    <div class="oe_kanban_footer">-->
# <!--                                                        <small class="text-muted">-->
# <!--&lt;!&ndash;                                                            <i class="fa fa-calendar"></i> &ndash;&gt;-->
# <!--                                                            <field name="create_date"/>-->
# <!--                                                        </small>-->
# <!--                                                        <span class="status-badge badge-published">-->
# <!--                                                            <field name="stage"/>-->
# <!--                                                        </span>-->
# <!--                                                    </div>-->
# <!--                                                </div>-->
# <!--                                            </div>-->
# <!--                                        </t>-->
# <!--                                    </templates>-->
# <!--                                </kanban>-->
# <!--                            </field>-->
# <!--                        </page>-->
#
# <!--                        &lt;!&ndash; Events Kanban View &ndash;&gt;-->
# <!--                        <page string=" Events">-->
# <!--                            <field name="event_ids" readonly="1">-->
# <!--                                <kanban default_group_by="stage">-->
# <!--                                    <field name="name"/>-->
# <!--                                    <field name="event_time_start"/>-->
# <!--                                    <field name="event_time_end"/>-->
# <!--                                    <field name="event_place"/>-->
# <!--                                    <field name="stage"/>-->
# <!--                                    <templates>-->
# <!--                                        <t t-name="card">-->
# <!--                                            <div class="oe_kanban_card">-->
# <!--                                                <div class="oe_kanban_content">-->
# <!--                                                    <div class="oe_kanban_title">-->
# <!--&lt;!&ndash;                                                        <span style="font-size: 16px;"></span>&ndash;&gt;-->
# <!--                                                        <b><field name="name"/></b>-->
# <!--                                                    </div>-->
# <!--                                                    <div class="oe_kanban_text">-->
# <!--                                                        <p>-->
# <!--                                                            <span style="display: inline-block; width: 90px;"> Location:</span>-->
# <!--                                                            <strong><field name="event_place"/></strong>-->
# <!--                                                        </p>-->
# <!--                                                        <p>-->
# <!--                                                            <span style="display: inline-block; width: 90px;"> Start:</span>-->
# <!--                                                            <strong><field name="event_time_start"/></strong>-->
# <!--                                                        </p>-->
# <!--                                                        <p>-->
# <!--                                                            <span style="display: inline-block; width: 90px;"> End:</span>-->
# <!--                                                            <strong><field name="event_time_end"/></strong>-->
# <!--                                                        </p>-->
# <!--                                                    </div>-->
# <!--                                                    <div class="oe_kanban_footer">-->
# <!--                                                        <span class="status-badge badge-in-progress">-->
# <!--                                                            <field name="stage"/>-->
# <!--                                                        </span>-->
# <!--                                                    </div>-->
# <!--                                                </div>-->
# <!--                                            </div>-->
# <!--                                        </t>-->
# <!--                                    </templates>-->
# <!--                                </kanban>-->
# <!--                            </field>-->
# <!--                        </page>-->
#
# <!--                        &lt;!&ndash; Complaints Kanban View &ndash;&gt;-->
# <!--                        <page string="Complaints">-->
# <!--                            <field name="complaint_ids" readonly="1">-->
# <!--                                <kanban default_group_by="stage">-->
# <!--                                    <field name="name"/>-->
# <!--                                    <field name="resident_id"/>-->
# <!--                                    <field name="tower_id"/>-->
# <!--                                    <field name="flat_id"/>-->
# <!--                                    <field name="stage"/>-->
# <!--                                    <field name="create_date"/>-->
# <!--                                    <templates>-->
# <!--                                        <t t-name="card">-->
# <!--                                            <div class="oe_kanban_card">-->
# <!--                                                <div class="oe_kanban_content">-->
# <!--                                                    <div class="oe_kanban_title">-->
# <!--&lt;!&ndash;                                                        <span style="font-size: 16px;"></span>&ndash;&gt;-->
# <!--                                                        <b><field name="name"/></b>-->
# <!--                                                    </div>-->
# <!--                                                    <div class="oe_kanban_text">-->
# <!--                                                        <p>-->
# <!--                                                            <span style="display: inline-block; width: 90px; color: #667eea; font-weight: 600;"> Resident:</span>-->
# <!--                                                            <field name="resident_id"/>-->
# <!--                                                        </p>-->
# <!--                                                        <p>-->
# <!--                                                            <span style="display: inline-block; width: 90px; color: #667eea; font-weight: 600;"> Tower:</span>-->
# <!--                                                            <field name="tower_id"/>-->
# <!--                                                        </p>-->
# <!--                                                        <p>-->
# <!--                                                            <span style="display: inline-block; width: 90px; color: #667eea; font-weight: 600;"> Flat:</span>-->
# <!--                                                            <field name="flat_id"/>-->
# <!--                                                        </p>-->
# <!--                                                    </div>-->
# <!--                                                    <div class="oe_kanban_footer">-->
# <!--                                                        <small class="text-muted">-->
# <!--&lt;!&ndash;                                                            <i class="fa fa-clock-o"></i>&ndash;&gt;-->
# <!--                                                            <field name="create_date"/>-->
# <!--                                                        </small>-->
# <!--                                                        <span class="status-badge badge-draft">-->
# <!--                                                            <field name="stage"/>-->
# <!--                                                        </span>-->
# <!--                                                    </div>-->
# <!--                                                </div>-->
# <!--                                            </div>-->
# <!--                                        </t>-->
# <!--                                    </templates>-->
# <!--                                </kanban>-->
# <!--                            </field>-->
# <!--                        </page>-->
#
# <!--                    </notebook>-->
# <!--                </sheet>-->
# <!--            </form>-->
# <!--        </field>-->
# <!--    </record>-->
#
# <!--</odoo>-->
#
#
#
# <!--<odoo>-->
# <!--    <record id="view_dashboard_home_forms" model="ir.ui.view">-->
# <!--        <field name="name">society.dashboard.form</field>-->
# <!--        <field name="model">society.dashboard</field>-->
# <!--        <field name="arch" type="xml">-->
# <!--            <form string="Smart Society Dashboard">-->
# <!--                <sheet>-->
# <!--                    <group>-->
# <!--                        <div class="oe_title">-->
# <!--                            <h1>Society Dashboard</h1>-->
# <!--                        </div>-->
# <!--                        <group>-->
# <!--                            <div class="row g-2">-->
# <!--                                <div class="col-3">-->
# <!--                                    <button type="object" name="sos_alerts"-->
# <!--                                            class="btn bg-danger-subtle border border-danger border-2 rounded-3 shadow-sm text-danger fw-bold"-->
# <!--                                            style="width:100%; height:70px;">Emergency SOS Alert-->
# <!--                                    </button>-->
# <!--                                </div>-->
# <!--                                <div class="col-3">-->
# <!--                                    <button type="object" name="fire_alerts"-->
# <!--                                            class="btn bg-danger-subtle border border-danger border-2 rounded-3 shadow-sm text-danger fw-bold"-->
# <!--                                            style="width:100%; height:70px;">Emergency FIRE Alert-->
# <!--                                    </button>-->
# <!--                                </div>-->
# <!--                                <div class="col-3">-->
# <!--                                    <button type="object" name="medical_panic_buttons"-->
# <!--                                            class="btn bg-danger-subtle border border-danger border-2 rounded-3 shadow-sm text-danger fw-bold"-->
# <!--                                            style="width:100%; height:70px;">-->
# <!--                                        Medical/Panic Button-->
# <!--                                    </button>-->
# <!--                                </div>-->
# <!--                                <div class="col-3">-->
# <!--                                    <button type="object" name="emergency_broadcast"-->
# <!--                                            class="btn bg-danger-subtle border border-danger border-2 rounded-3 shadow-sm text-danger fw-bold"-->
# <!--                                            style="width:100%; height:70px;"-->
# <!--                                            groups="smart_society.group_registration_committee,smart_society.group_registration_administration">-->
# <!--                                        Emergency Broadcast Button-->
# <!--                                    </button>-->
# <!--                                </div>-->
# <!--                            </div>-->
# <!--                        </group>-->
# <!--                        <group col="4">-->
# <!--                            <field name="total_notices" readonly="1"/>-->
# <!--                            <field name="total_events" readonly="1"/>-->
# <!--                            <field name="total_complaints" readonly="1"/>-->
# <!--&lt;!&ndash;                            <field name="total_visitors" readonly="1"/>&ndash;&gt;-->
# <!--                        </group>-->
# <!--                    </group>-->
# <!--                    <notebook>-->
#
# <!--                        &lt;!&ndash; Notices Kanban View &ndash;&gt;-->
# <!--                        <page string="Notices">-->
# <!--                            <field name="notice_ids" readonly="1">-->
# <!--                                <kanban default_group_by="stage">-->
# <!--                                    <field name="name"/>-->
# <!--                                    <field name="description"/>-->
# <!--                                    <field name="create_date"/>-->
# <!--                                    <field name="stage"/>-->
# <!--                                    <templates>-->
# <!--                                        <t t-name="card">-->
# <!--                                            <div class="oe_kanban_card">-->
# <!--                                                <div class="oe_kanban_content">-->
# <!--                                                    <div class="oe_kanban_title">-->
# <!--                                                        <b><field name="name"/></b>-->
# <!--                                                    </div>-->
# <!--                                                    <div class="oe_kanban_text">-->
# <!--                                                        <field name="description"/>-->
# <!--                                                    </div>-->
# <!--                                                    <div class="oe_kanban_footer">-->
# <!--                                                        <small class="text-muted">-->
# <!--                                                            <field name="create_date"/>-->
# <!--                                                        </small>-->
# <!--                                                    </div>-->
# <!--                                                </div>-->
# <!--                                            </div>-->
# <!--                                        </t>-->
# <!--                                    </templates>-->
# <!--                                </kanban>-->
# <!--                            </field>-->
# <!--                        </page>-->
#
# <!--                        &lt;!&ndash; Events Kanban View &ndash;&gt;-->
# <!--                        <page string="Events">-->
# <!--                            <field name="event_ids" readonly="1">-->
# <!--                                <kanban default_group_by="stage">-->
# <!--                                    <field name="name"/>-->
# <!--                                    <field name="event_time_start"/>-->
# <!--                                    <field name="event_time_end"/>-->
# <!--                                    <field name="event_place"/>-->
# <!--                                    <field name="stage"/>-->
# <!--                                    <templates>-->
# <!--                                        <t t-name="card">-->
# <!--                                            <div class="oe_kanban_card">-->
# <!--                                                <div class="oe_kanban_content">-->
# <!--                                                    <div class="oe_kanban_title">-->
# <!--                                                        <b><field name="name"/></b>-->
# <!--                                                    </div>-->
# <!--                                                    <div class="oe_kanban_text">-->
# <!--                                                        <p>-->
# <!--                                                            <strong>Location:</strong> <field name="event_place"/>-->
# <!--                                                        </p>-->
# <!--                                                        <p>-->
# <!--                                                            <strong>Start:</strong> <field name="event_time_start"/><br/>-->
# <!--                                                            <strong>End:</strong> <field name="event_time_end"/>-->
# <!--                                                        </p>-->
# <!--                                                    </div>-->
# <!--                                                </div>-->
# <!--                                            </div>-->
# <!--                                        </t>-->
# <!--                                    </templates>-->
# <!--                                </kanban>-->
# <!--                            </field>-->
# <!--                        </page>-->
#
# <!--                        &lt;!&ndash; Complaints Kanban View &ndash;&gt;-->
# <!--                        <page string="Complaints">-->
# <!--                            <field name="complaint_ids" readonly="1">-->
# <!--                                <kanban default_group_by="stage">-->
# <!--                                    <field name="name"/>-->
# <!--                                    <field name="resident_id"/>-->
# <!--                                    <field name="tower_id"/>-->
# <!--                                    <field name="flat_id"/>-->
# <!--                                    <field name="stage"/>-->
# <!--                                    <field name="create_date"/>-->
# <!--                                    <templates>-->
# <!--                                        <t t-name="card">-->
# <!--                                            <div class="oe_kanban_card">-->
# <!--                                                <div class="oe_kanban_content">-->
# <!--                                                    <div class="oe_kanban_title">-->
# <!--                                                        <b><field name="name"/></b>-->
# <!--                                                    </div>-->
# <!--                                                    <div class="oe_kanban_text">-->
# <!--                                                        <p>-->
# <!--                                                            <strong>Resident:</strong> <field name="resident_id"/><br/>-->
# <!--                                                            <strong>Tower:</strong> <field name="tower_id"/><br/>-->
# <!--                                                            <strong>Flat:</strong> <field name="flat_id"/>-->
# <!--                                                        </p>-->
# <!--                                                    </div>-->
# <!--                                                    <div class="oe_kanban_footer">-->
# <!--                                                        <small class="text-muted">-->
# <!--                                                            <field name="create_date"/>-->
# <!--                                                        </small>-->
# <!--                                                    </div>-->
# <!--                                                </div>-->
# <!--                                            </div>-->
# <!--                                        </t>-->
# <!--                                    </templates>-->
# <!--                                </kanban>-->
# <!--                            </field>-->
# <!--                        </page>-->
#
# <!--                    </notebook>-->
# <!--                </sheet>-->
# <!--            </form>-->
# <!--        </field>-->
# <!--    </record>-->
#
# <!--</odoo>-->
#
#
#
#
#
#
#
#
#
# <!--<odoo>-->
# <!--    <record id="view_dashboard_home_forms" model="ir.ui.view">-->
# <!--        <field name="name">society.dashboard.form</field>-->
# <!--        <field name="model">society.dashboard</field>-->
# <!--        <field name="arch" type="xml">-->
# <!--            <form string="Smart Society Dashboard">-->
# <!--                <sheet>-->
# <!--                    <group>-->
# <!--                        <div class="oe_title">-->
# <!--                            <h1>Society Dashboard</h1>-->
# <!--                        </div>-->
# <!--                        <group>-->
# <!--                            <div class="row g-2">-->
# <!--                                <div class="col-3">-->
# <!--                                    <button type="object" name="sos_alerts"-->
# <!--                                            class="btn bg-danger-subtle border border-danger border-2 rounded-3 shadow-sm text-danger fw-bold"-->
# <!--                                            style="width:100%; height:70px;">Emergency SOS Alert-->
# <!--                                    </button>-->
# <!--                                </div>-->
# <!--                                <div class="col-3">-->
# <!--                                    <button type="object" name="fire_alerts"-->
# <!--                                            class="btn bg-danger-subtle border border-danger border-2 rounded-3 shadow-sm text-danger fw-bold"-->
# <!--                                            style="width:100%; height:70px;">Emergency FIRE Alert-->
# <!--                                    </button>-->
# <!--                                </div>-->
# <!--                                <div class="col-3">-->
# <!--                                    <button type="object" name="medical_panic_buttons"-->
# <!--                                            class="btn bg-danger-subtle border border-danger border-2 rounded-3 shadow-sm text-danger fw-bold"-->
# <!--                                            style="width:100%; height:70px;">-->
# <!--                                        Medical/Panic Button-->
# <!--                                    </button>-->
# <!--                                </div>-->
# <!--                                <div class="col-3">-->
# <!--                                    <button type="object" name="emergency_broadcast"-->
# <!--                                            class="btn bg-danger-subtle border border-danger border-2 rounded-3 shadow-sm text-danger fw-bold"-->
# <!--                                            style="width:100%; height:70px;"-->
# <!--                                            groups="smart_society.group_registration_committee,smart_society.group_registration_administration">-->
# <!--                                        Emergency Broadcast Button-->
# <!--                                    </button>-->
# <!--                                </div>-->
# <!--                            </div>-->
# <!--                        </group>-->
# <!--                        <group col="4">-->
# <!--                            <field name="total_notices" readonly="1"/>-->
# <!--                            <field name="total_events" readonly="1"/>-->
# <!--                            <field name="total_complaints" readonly="1"/>-->
# <!--&lt;!&ndash;                            <field name="total_visitors" readonly="1"/>&ndash;&gt;-->
# <!--                        </group>-->
# <!--                    </group>-->
# <!--                    <notebook>-->
#
# <!--                        &lt;!&ndash; Notices &ndash;&gt;-->
# <!--                        <page string="Notices">-->
# <!--                            <field name="notice_ids" readonly="1">-->
# <!--                                <list>-->
# <!--                                    <field name="name"/>-->
# <!--                                    <field name="description"/>-->
# <!--                                    <field name="create_date"/>-->
# <!--                                    <field name="stage"/>-->
# <!--                                </list>-->
# <!--                            </field>-->
# <!--                        </page>-->
# <!--                        &lt;!&ndash; Events &ndash;&gt;-->
# <!--                        <page string="Events">-->
# <!--                            <field name="event_ids" readonly="1">-->
# <!--                                <list>-->
# <!--                                    <field name="name"/>-->
# <!--                                    <field name="event_time_start"/>-->
# <!--                                    <field name="event_time_end"/>-->
# <!--                                    <field name="event_place"/>-->
# <!--                                    <field name="stage"/>-->
# <!--                                </list>-->
# <!--                            </field>-->
# <!--                        </page>-->
# <!--                        &lt;!&ndash; Complaints &ndash;&gt;-->
# <!--                        <page string="Complaints">-->
# <!--                            <field name="complaint_ids" readonly="1">-->
# <!--                                <list>-->
# <!--                                    <field name="name"/>-->
# <!--                                    <field name="resident_id"/>-->
# <!--                                    <field name="tower_id"/>-->
# <!--                                    <field name="flat_id"/>-->
# <!--                                    <field name="stage"/>-->
# <!--                                    <field name="create_date"/>-->
# <!--                                </list>-->
# <!--                            </field>-->
# <!--                        </page>-->
# <!--                    </notebook>-->
# <!--                </sheet>-->
# <!--            </form>-->
# <!--        </field>-->
# <!--    </record>-->
#
# <!--</odoo>-->

# <!--    <record id="society_alert_wizard_list_save" model="ir.ui.view">-->
# <!--        <field name="name">society.alert.save.list</field>-->
# <!--        <field name="model">society.alert.save</field>-->
# <!--        <field name="arch" type="xml">-->
# <!--            <list default_order="datetime desc">-->
# <!--                <field name="name"/>-->
# <!--                <field name="description" optional="hide"/>-->
# <!--                <field name="flat_id"/>-->
# <!--                <field name="tower_id"/>-->
# <!--                <field name="user_id"/>-->
# <!--                <field name="location"/>-->
# <!--                <field name="alert_type" optional="hide"/>-->
# <!--                <field name="datetime"/>-->
# <!--            </list>-->
# <!--        </field>-->
# <!--    </record>-->
#
# <!--    <record id="society_alert_wizard_form_save" model="ir.ui.view">-->
# <!--        <field name="name">society.alert.save.form</field>-->
# <!--        <field name="model">society.alert.save</field>-->
# <!--        <field name="arch" type="xml">-->
# <!--            <form string="Alert">-->
# <!--                <sheet>-->
# <!--                    <group>-->
# <!--                        <field name="name"/>-->
# <!--                        <field name="description"/>-->
# <!--                        <field name="to_committee"/>-->
# <!--                        <field name="flat_id"/>-->
# <!--                        <field name="tower_id"/>-->
# <!--                        <field name="user_id"/>-->
# <!--                        <field name="location"/>-->
# <!--                        <field name="alert_type"/>-->
# <!--                        <field name="datetime"/>-->
# <!--                    </group>-->
# <!--                </sheet>-->
# <!--                <chatter/>-->
# <!--            </form>-->
# <!--        </field>-->
# <!--    </record>-->
#
#
# <!--    <record id="society_emergency_broadcast_wizard_list_save" model="ir.ui.view">-->
# <!--        <field name="name">emergency.broadcast.save.list</field>-->
# <!--        <field name="model">emergency.broadcast.save</field>-->
# <!--        <field name="arch" type="xml">-->
# <!--            <list default_order="datetime desc">-->
# <!--                <field name="name"/>-->
# <!--                <field name="description"/>-->
# <!--                <field name="tower_ids"/>-->
# <!--                <field name="flat_ids"/>-->
# <!--                <field name="datetime"/>-->
# <!--            </list>-->
# <!--        </field>-->
# <!--    </record>-->
#
# <!--    <record id="society_emergency_broadcast_wizard_save" model="ir.ui.view">-->
# <!--        <field name="name">emergency.broadcast.save.form</field>-->
# <!--        <field name="model">emergency.broadcast.save</field>-->
# <!--        <field name="arch" type="xml">-->
# <!--            <form string="Emergency">-->
# <!--                <sheet>-->
# <!--                    <group>-->
# <!--                        <field name="name"/>-->
# <!--                        <field name="description"/>-->
# <!--                        <field name="tower_ids" widget="many2many_tags"/>-->
# <!--                        <field name="flat_ids" widget="many2many_tags" invisible="tower_ids"/>-->
# <!--                        <field name="datetime"/>-->
# <!--                    </group>-->
# <!--                </sheet>-->
# <!--                <chatter/>-->
# <!--            </form>-->
# <!--        </field>-->
# <!--    </record>-->
#
#
#
#         <!--                                <div class="col-3" style="cursor:pointer;" name="fire_alert">-->
#         <!--                                    <div class="card bg-danger-subtle border-danger border-2 rounded-3 text-center shadow-sm py-2 px-2"-->
#         <!--                                         style="height:70px;">-->
#         <!--                                        <div class="text-danger fw-bold small">Fire Alert</div>-->
#         <!--                                    </div>-->
#         <!--                                </div>-->
#
#         <!--                                <div class="col-3" style="cursor:pointer;" action="medical_panic_button">-->
#         <!--                                    <div class="card bg-danger-subtle border-danger border-2 rounded-3 text-center shadow-sm py-2 px-2"-->
#         <!--                                         style="height:70px;">-->
#         <!--                                        <div class="text-danger fw-bold small">Medical / Panic</div>-->
#         <!--                                    </div>-->
#         <!--                                </div>-->
#
#         <!--                                <div class="col-3" style="cursor:pointer;" action="emergency_broadcast">-->
#         <!--                                    <div class="card bg-danger-subtle border-danger border-2 rounded-3 text-center shadow-sm py-2 px-2"-->
#         <!--                                         style="height:70px;">-->
#         <!--                                        <div class="text-danger fw-bold small">Emergency Broadcast</div>-->
#         <!--                                    </div>-->
#         <!--                                </div>-->
# John Smith  Shilp Aron Society Committee
#
# john_smith@example.com
#
# Ron Gibson Shilp Aron Society Committee
# ron_gibson12@example.com
# 
# San Joaquin  Shilp Aron Society Committee
# san_joaquin22@example.com
#
# Robert Wilson  SA t1 Committee
# robert_wilson13@example.com
#
# William Davis  SA t2 Committee
# william_davis@example.com
#
#
# Richard Moore   SA t1 Block A committee
# richard_moore11@example.com
#
# Jennifer White     SA t1 Block B Committee
# jennifier_white2@example.com
#
#
# Jessica Thompson  SA t1 Block C committee
# jessica78@example.com
#
#
# Michael Johnson SA t2 Block A committee
# michael_johnson12@example.com
#
# Christopher Anderson   SA t2 Block B committee
# chirst78@example.com
#
# Daniel Thomas  SA t2 Block C committee
# daniel_thomas88@example.com
#
#
# Sarah Martin  SA t2 Block D committee
# sarah89@example.com
#
#





# select_committee = self.env['society.committee'].search([
#     ('tower_id', '=', search_user.tower_id.id)
# ])
# print('\n\n\n.............select_committee....', select_committee)
# record.to_committee = select_committee
# print('\n\n\n............to_committee..........', record.to_committee)

# @api.depends('to_committee')
# def _compute_committee_emails(self):
#     for record in self:
#         emails = []
#         for partner in record.to_committee.committee_name_id:
#             if partner.email:
#                 emails.append(partner.email)
#         if record.to_committee.chairman_id.email:
#             emails.append(record.to_committee.chairman_id.email)
#         if record.to_committee.secretary_id.email:
#             emails.append(record.to_committee.secretary_id.email)
#         record.committee_emails = ",".join(set(emails))

# @api.depends('to_committee')
# def _compute_committee_emails(self):
#     for record in self:
#         emails = []
#         for security in record.security_id:
#             print('\n\n\n..........security',security)
#             if security.email:
#                 emails.append(security.email)
#         for resident in record.resident_id:
#             print('\n\n\n..........resident',resident)
#             if resident.email:
#                 emails.append(resident.email)
#         for flat in record.flat_id:
#             print('\n\n\n..........flat',flat)
#             resident=self.env['resident.registrations'].search([
#                 ('flat_id','=',flat.id),
#             ])
#             for res in resident:
#                 if res.email:
#                     emails.append(resident.email)
#         for tower in record.tower_id:
#             resident=self.env['resident.registrations'].search([
#                 ('tower_id','=',tower.id),
#             ])
#             for res in resident:
#                 if res.email:
#                     emails.append(resident.email)
#
#         for partner in record.to_committee.committee_name_id:
#             if partner.email:
#                 emails.append(partner.email)
#
#         if record.to_committee.chairman_id.email:
#             emails.append(record.to_committee.chairman_id.email)
#
#         if record.to_committee.secretary_id.email:
#             emails.append(record.to_committee.secretary_id.email)
#
#         emails = list(set(emails))
#         record.committee_emails = ",".join(emails)
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
