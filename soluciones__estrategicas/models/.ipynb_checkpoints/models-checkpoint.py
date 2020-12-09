# -*- coding: utf-8 -*-


from functools import partial
from itertools import groupby

from odoo import models, fields, api, SUPERUSER_ID, _
from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError, Warning
from odoo.tools.misc import formatLang, get_lang
from odoo.osv import expression
from odoo.tools import float_is_zero, float_compare

from datetime import date
from datetime import datetime
from datetime import timedelta
import numpy as np
import logging
import time


_logger = logging.getLogger(__name__)
#################################
#Campos Compañia
#################################

class AgregarCamposCompany(models.Model):
    _inherit = 'res.company'
    
    nit = fields.Char('NIT')
    nrc = fields.Char('NRC' )
    giro = fields.Char('Giro')
    companysize = fields.Selection([('Pequeña', 'Pequeña'), ('Mediana', 'Mediana'), ('Grande', 'Grande')],'Tamaño Empresa')
    


#################################
#Campos Cliente y Proveedor
#################################    

class AgregarCamposPartner(models.Model):
    _inherit = 'res.partner'
    
    dui = fields.Char('DUI')
    nit = fields.Char('NIT')
    nrc = fields.Char('NRC' )
    giro = fields.Char('Giro')
    nombrecomercial = fields.Char('Nombre Comercial')
    
    companysize = fields.Selection([('Pequeña', 'Pequeña'), ('Mediana', 'Mediana'), ('Grande', 'Grande')],'Tamaño Empresa')
    fechadenacimiento = fields.Date('Fecha de Nacimiento')
    edad = fields.Integer('Edad')
    tipodevivienda = fields.Selection([('Propia', 'Propia'), ('Alquilada', 'Alquilada')],'Tipo de Vivienda')
    fechadeexpediciondui = fields.Date('Fecha Expedicion DUI')
    fechadeexpiraciondui = fields.Date('Fecha Expiración DUI')
    interes = fields.Float('% Interes','digits(5,2)')
    diasdegraciacredito = fields.Integer('Días de gracia (Crédito)', default=0)
    codigo_anterior = fields.Char('Código Anterior')
    
    lugardetrabajo = fields.Char('Lugar de Trabajo')
    direcciondetrabajo = fields.Char('Dirección')
    jefeinmediato = fields.Char('Jefe Inmediato')
    telefonotrabajo = fields.Char('Telefono Trabajo')
    telefonojefeinmediato = fields.Char('Teléfono Jefe Inmediato')
    ocupacion = fields.Char('Ocupación')
    #currency_id = fields.Many2one('res.currency','Moneda')
    salario = fields.Float('Salario')
    ingresosextras = fields.Char('Detalle Ingresos Extras')

    nombredelamadre = fields.Char('Nombre de la Madre')
    telefonodelamadre = fields.Char('Teléfono de la Madre')
    direcciondelamadre = fields.Char('Dirección de la Madre')
    lugardetrabajodelamadre = fields.Char('Lugar de Trabajo de la Madre')
    direccionlugardetrabajodelamadre = fields.Char('Dirección lugar de trabajo de la madre')
    jefeinmediatodelamadre = fields.Char('Jefe Inmediato de la Madre')
    telefonodeljefeinmediatodelamadre = fields.Char('Telefono del Jefe Inmediato de la Madre')
    
    nombredelpadre = fields.Char('Nombre del Padre')
    telefonodelpadre = fields.Char('Teléfono del Padre')
    direcciondelpadre = fields.Char('Dirección del Padre')
    lugardetrabajodelpadre = fields.Char('Lugar de Trabajo del Padre')
    direccionlugardetrabajodelpadre = fields.Char('Dirección lugar de trabajo del Padre')
    jefeinmediatodelpadre = fields.Char('Jefe Inmediato del Padre')
    telefonodeljefeinmediatodelpadre = fields.Char('Telefono del Jefe Inmediato del Padre')
    
    nombredeconyugue = fields.Char('Nombre de Conyugue')
    telefonodeconyugue = fields.Char('Teléfono de Conyugue')
    direcciondeconyugue = fields.Char('Dirección de Conyugue')
    lugardetrabajodeconyugue = fields.Char('Lugar de Trabajo de Conyugue')
    direccionlugardetrabajodeconyugue = fields.Char('Dirección lugar de trabajo de Conyugue')
    jefeinmediatodeconyugue = fields.Char('Jefe Inmediato de Conyugue')
    telefonodeljefeinmediatodeconyugue = fields.Char('Telefono del Jefe Inmediato de Conyugue')
    
    nombrereferenciafamiliar1 = fields.Char('Nombre ')
    telefonodereferenciafamiliar1 = fields.Char('Teléfono ')
    direcciondereferenciafamiliar1 = fields.Char('Domicilio ')
    relacionreferenciafamiliar1 = fields.Selection( [('1','Padre'), ('2','Madre'), ('3','Hermano(a)'), ('4','Primo(a)'), ('5','Amigo(a)'), ('6','Cuñado(a)'), ('7','Abuelo(a)'), ('8','Compañero(a) Trabajo'), ('9','Esposo(a)'), ('10','Compañero(a) de vida'), ('11','Tio(a)')]
, 'Relación ')
    
    nombrereferenciafamiliar2 = fields.Char('Nombre  ')
    telefonodereferenciafamiliar2 = fields.Char('Teléfono  ')
    direcciondereferenciafamiliar2 = fields.Char('Domicilio  ')
    relacionreferenciafamiliar2 = fields.Selection([('1','Padre'), ('2','Madre'), ('3','Hermano(a)'), ('4','Primo(a)'), ('5','Amigo(a)'), ('6','Cuñado(a)'), ('7','Abuelo(a)'), ('8','Compañero(a) Trabajo'), ('9','Esposo(a)'), ('10','Compañero(a) de vida'), ('11','Tio(a)')], 'Relación  ')
    
    nombrereferenciapersonal1 = fields.Char('Nombre    ')
    telefonodereferenciapersonal1 = fields.Char('Teléfono    ')
    direcciondereferenciapersonal1 = fields.Char('Domicilio    ')
    relacionreferenciapersonal1 = fields.Selection([('1','Padre'), ('2','Madre'), ('3','Hermano(a)'), ('4','Primo(a)'), ('5','Amigo(a)'), ('6','Cuñado(a)'), ('7','Abuelo(a)'), ('8','Compañero(a) Trabajo'), ('9','Esposo(a)'), ('10','Compañero(a) de vida'), ('11','Tio(a)')], 'Relación    ')
    
    nombrereferenciapersonal2 = fields.Char('Nombre     ')
    telefonodereferenciapersonal2 = fields.Char('Teléfono     ')
    direcciondereferenciapersonal2 = fields.Char('Domicilio     ')
    relacionreferenciapersonal2 = fields.Selection([('1','Padre'), ('2','Madre'), ('3','Hermano(a)'), ('4','Primo(a)'), ('5','Amigo(a)'), ('6','Cuñado(a)'), ('7','Abuelo(a)'), ('8','Compañero(a) Trabajo'), ('9','Esposo(a)'), ('10','Compañero(a) de vida'), ('11','Tio(a)')], 'Relación     ')
    
    
    #codeudor
    nombrecodeudor = fields.Char('Nombre       ')
    
    
    fechadenacimientocodeudor = fields.Date('Fecha de Nacimiento      ')
    edadcodeudor = fields.Integer('Edad  ')
    domiciliocodeudor = fields.Char('Domicilio      ')
    duicodeudor = fields.Char('DUI ')
    nitcodeudor = fields.Char('NIT ')
    tipodeviviendacodeudor = fields.Selection([('Propia', 'Propia'), ('Alquilada', 'Alquilada')],'Tipo de Vivienda  ')
    fechadeexpedicionduicodeudor = fields.Date('Fecha Expedicion DUI ')
    fechadeexpiracionduicodeudor = fields.Date('Fecha Expiración DUI ')
    
    
    lugardetrabajocodeudor = fields.Char('Lugar de Trabajo      ')
    direcciondetrabajocodeudor = fields.Char('Dirección      ')
    telefonofijocodeudor = fields.Char('Teléfono Fijo ')
    telefonocelularcodeudor = fields.Char('Teléfono Celular   ')
    jefeinmediatocodeudor = fields.Char('Jefe Inmediato      ')
    telefonotrabajocodeudor = fields.Char('Telefono Trabajo      ')
    telefonojefeinmediatocodeudor = fields.Char('Teléfono Jefe Inmediato      ')
    ocupacioncodeudor = fields.Char('Ocupación      ')
    salariocodeudor = fields.Float('Salario      ')
    ingresosextrascodeudor = fields.Char('Detalle Ingresos Extras ')

    nombredelamadrecodeudor = fields.Char('Nombre de la Madre ')
    telefonodelamadrecodeudor = fields.Char('Teléfono de la Madre ')
    direcciondelamadrecodeudor = fields.Char('Dirección de la Madre ')
    lugardetrabajodelamadrecodeudor = fields.Char('Lugar de Trabajo de la Madre ')
    direccionlugardetrabajodelamadrecodeudor = fields.Char('Dirección lugar de trabajo de la madre ')
    jefeinmediatodelamadrecodeudor = fields.Char('Jefe Inmediato de la Madre ')
    telefonodeljefeinmediatodelamadrecodeudor = fields.Char('Telefono del Jefe Inmediato de la Madre ')
    
    nombredelpadrecodeudor = fields.Char('Nombre del Padre ')
    telefonodelpadrecodeudor = fields.Char('Teléfono del Padre ')
    direcciondelpadrecodeudor = fields.Char('Dirección del Padre ')
    lugardetrabajodelpadrecodeudor = fields.Char('Lugar de Trabajo del Padre ')
    direccionlugardetrabajodelpadrecodeudor = fields.Char('Dirección lugar de trabajo del Padre ')
    jefeinmediatodelpadrecodeudor = fields.Char('Jefe Inmediato del Padre ')
    telefonodeljefeinmediatodelpadrecodeudor = fields.Char('Telefono del Jefe Inmediato del Padre ')
    
    nombredeconyuguecodeudor = fields.Char('Nombre de Conyugue       ')
    telefonodeconyuguecodeudor = fields.Char('Teléfono de Conyugue       ')
    direcciondeconyuguecodeudor = fields.Char('Dirección de Conyugue       ')
    lugardetrabajodeconyuguecodeudor = fields.Char('Lugar de Trabajo de Conyugue       ')
    direccionlugardetrabajodeconyuguecodeudor = fields.Char('Dirección lugar de trabajo de Conyugue       ')
    jefeinmediatodeconyuguecodeudor = fields.Char('Jefe Inmediato de Conyugue       ')
    telefonodeljefeinmediatodeconyuguecodeudor = fields.Char('Telefono del Jefe Inmediato de Conyugue       ')
    
    nombrereferenciafamiliar1codeudor = fields.Char('Nombre        ')
    telefonodereferenciafamiliar1codeudor = fields.Char('Teléfono        ')
    direcciondereferenciafamiliar1codeudor = fields.Char('Domicilio        ')
    relacionreferenciafamiliar1codeudor = fields.Selection([('1','Padre'), ('2','Madre'), ('3','Hermano(a)'), ('4','Primo(a)'), ('5','Amigo(a)'), ('6','Cuñado(a)'), ('7','Abuelo(a)'), ('8','Compañero(a) Trabajo'), ('9','Esposo(a)'), ('10','Compañero(a) de vida'), ('11','Tio(a)')], 'Relación        ')
    
    nombrereferenciafamiliar2codeudor = fields.Char('Nombre         ')
    telefonodereferenciafamiliar2codeudor = fields.Char('Teléfono         ')
    direcciondereferenciafamiliar2codeudor = fields.Char('Domicilio         ')
    relacionreferenciafamiliar2codeudor = fields.Selection([('1','Padre'), ('2','Madre'), ('3','Hermano(a)'), ('4','Primo(a)'), ('5','Amigo(a)'), ('6','Cuñado(a)'), ('7','Abuelo(a)'), ('8','Compañero(a) Trabajo'), ('9','Esposo(a)'), ('10','Compañero(a) de vida'), ('11','Tio(a)')], 'Relación         ')
    
    nombrereferenciapersonal1codeudor = fields.Char('Nombre           ')
    telefonodereferenciapersonal1codeudor = fields.Char('Teléfono           ')
    direcciondereferenciapersonal1codeudor = fields.Char('Domicilio           ')
    relacionreferenciapersonal1codeudor = fields.Selection([('1','Padre'), ('2','Madre'), ('3','Hermano(a)'), ('4','Primo(a)'), ('5','Amigo(a)'), ('6','Cuñado(a)'), ('7','Abuelo(a)'), ('8','Compañero(a) Trabajo'), ('9','Esposo(a)'), ('10','Compañero(a) de vida'), ('11','Tio(a)')], 'Relación           ')
    
    nombrereferenciapersonal2codeudor = fields.Char('Nombre            ')
    telefonodereferenciapersonal2codeudor = fields.Char('Teléfono            ')
    direcciondereferenciapersonal2codeudor = fields.Char('Domicilio            ')
    relacionreferenciapersonal2codeudor = fields.Selection([('1','Padre'), ('2','Madre'), ('3','Hermano(a)'), ('4','Primo(a)'), ('5','Amigo(a)'), ('6','Cuñado(a)'), ('7','Abuelo(a)'), ('8','Compañero(a) Trabajo'), ('9','Esposo(a)'), ('10','Compañero(a) de vida'), ('11','Tio(a)')], 'Relación            ')
    
    solicitudes_lineas = fields.One2many('solicitudes.credito.lineas','cliente_id')
    
    def imprimir_formulario(self):
        _logger.info("imprimir_formulario_clientes")

        return self.env.ref('soluciones__estrategicas.solicitud_credito').report_action(self)

class SolicitudesCredito(models.Model):
    _name = 'solicitudes.credito.lineas'
    _description = 'Solicitudes de crédito'
    name = fields.Char('Descripción')
    cliente_id = fields.Many2one('res.partner','ID Solicitud')
    fechasolicitud = fields.Date('Fecha de Solicitud          ', default=datetime.now())
    fechaestatus = fields.Date('Fecha Estatus', default=datetime.now())
    montodesolicitud = fields.Float('Monto Solicitado')
    montoaprobado = fields.Float('Monto Aprobado')
    montoanticipo = fields.Float('Anticipo')
    montoprestado = fields.Float('Monto Prestado')
    fechaInicio = fields.Date('Fecha Inicio del Crédito', default=datetime.now())
    periodicidaddepago = fields.Selection([('S', 'Semanal'), ('Q', 'Quincenal'), ('M', 'Mensual')],'Periodicidad de Pago')

    numerodecuotas = fields.Integer('Número de Cuotas', default=1)
    porcentajedeinteresdelcredito = fields.Float('Interés del crédito %')
    porcentajedeinteresmoratorio = fields.Float('Interés Moratorio %')
    cuota = fields.Float('Cuota Fija')
    saldodespuesanticipo = fields.Float('Saldo Después de Anticipo')
    estatus = fields.Selection([('E', 'Evaluación'), ('A', 'Aprobado'), ('D','Denegado'), ('C','Cancelado'), ('F','Facturado'),('P','Pagado')],'Estatus', default="E")
    solicitudes_lineas_cuotas = fields.One2many('solicitudes.credito.lineas.cuotas','solicitud_id')
    factura_solicitud = fields.One2many('sale.advance.payment.inv','solicitud_id')
    
    def imprimir_corrida_financiera(self):
        _logger.info("imprimir_corrida_financiera: TEST")
        _logger.info(self.id)
        _logger.info(self.solicitudes_lineas_cuotas)
        return self.env.ref('soluciones__estrategicas.reporte_corrida_financiera').report_action(self)
        #return {'type': 'ir.actions.report','report_name': 'client_contracts.contract_template','report_type':"qweb-pdf",'data': context,}
    
    #@api.model_create_multi
    def generar_cuotas_credito(self):
    
        dias = 30
        fecha = self.fechaInicio
        fechalimite = self.fechaInicio 
        cuota = -1 * np.pmt((self.porcentajedeinteresdelcredito/100), self.numerodecuotas, self.montoaprobado - self.montoanticipo)
        self.cuota = cuota
        self.montoprestado = self.montoaprobado - self.montoanticipo
        self.saldodespuesanticipo = self.cuota * self.numerodecuotas
        cuotasaldoinicial = self.saldodespuesanticipo
        for nc in range(self.numerodecuotas):
            cuotasaldofinal = cuotasaldoinicial - cuota
            nuevafecha = fecha + timedelta(days=dias)
            fechalimite = nuevafecha + timedelta(days=self.cliente_id.diasdegraciacredito)
            self.env['solicitudes.credito.lineas.cuotas'].create({'solicitud_id': self.id,'cuotanumero': nc+1, 'cuotafecha':nuevafecha,'cuotafechapagada':nuevafecha,'cuotasaldoinicial':cuotasaldoinicial, 'cuotamonto':cuota,'cuotasaldofinal':cuotasaldofinal, 'cuotamontorecibido':0,'cuotaestatus':'E','cuotafechalimite':fechalimite}) 
            fecha = nuevafecha
            cuotasaldoinicial = cuotasaldofinal
    
class SolicitudesCreditoCuotas(models.Model):
    _name = 'solicitudes.credito.lineas.cuotas'
    _description = 'Cuotas de Credito'
    solicitud_id = fields.Many2one('solicitudes.credito.lineas','ID Solicitud')
    cuotanumero = fields.Integer('Cuota')
    cuotafecha = fields.Date('Fecha de pago')
    cuotafechapagada = fields.Date('Fecha pagada')
    cuotafechalimite = fields.Date('Fecha Límite de Pago')
    cuotasaldoinicial=fields.Float('Saldo Inicial')
    cuotamonto = fields.Float('Cuota Fija')
    cuotasaldofinal = fields.Float('Saldo Final')
    
    cuotainteres=fields.Float('Interes Cuota','digits(10,5)')
    cuotatotal = fields.Float(compute='total_cuota',string='Total Cuota')
    cuotamontorecibido = fields.Float('Monto Pagado')
    cuotaestatus = fields.Selection([('E', 'Pendiente'), ('P', 'Pagada')],'Estatus')
    
    
        

#################################
#Campos Productos
#################################     
    
class AgregarCamposProductos(models.Model):
    _inherit = 'product.template'
    codigo_anterior = fields.Char('Código Anterior')
    

#################################
#Campos Facturas (Documentos)
################################# 
#@api.depends('order.id','order.partner_id')
class AgregarCamposFactura(models.TransientModel):
    _inherit = 'sale.advance.payment.inv'
    _description = 'Campos Adicionales para factura '
    
    @api.model
    def _count(self):
        return len(self._context.get('active_ids', []))

    @api.model
    def _default_product_id(self):
        product_id = self.env['ir.config_parameter'].sudo().get_param('sale.default_deposit_product_id')
        return self.env['product.product'].browse(int(product_id)).exists()

    @api.model
    def _default_deposit_account_id(self):
        return self._default_product_id().property_account_income_id

    @api.model
    def _default_deposit_taxes_id(self):
        return self._default_product_id().taxes_id

    @api.model
    def _default_has_down_payment(self):
        if self._context.get('active_model') == 'sale.order' and self._context.get('active_id', False):
            sale_order = self.env['sale.order'].browse(self._context.get('active_id'))
            return sale_order.order_line.filtered(
                lambda sale_order_line: sale_order_line.is_downpayment
            )

        return False

    @api.model
    def _default_currency_id(self):
        if self._context.get('active_model') == 'sale.order' and self._context.get('active_id', False):
            sale_order = self.env['sale.order'].browse(self._context.get('active_id'))
            return sale_order.currency_id
        
    def name_get(self):
        result = []
        for record in self:
            if self.env.context.get('mostrar', False):
                # Only goes off when the custom_search is in the context values.
                result.append((record.id, "{} - ${}".format(record.name, record.montoaprobado)))
            else:
                result.append((record.id, record.name))
        return result
    
    def _get_solicitudes(self):
        domain =[('id', '=', -1)]
        solicitudes_list=[]
        _logger.info('_get_solicitudes domain 3.0 = ')
        solicitudes_model = self.env['solicitudes.credito.lineas'].search([('cliente_id.id','=',-2),('estatus','=','A')])
        #_logger.info(self.order.partner_id)
        #if self._context.get('active_model') == 'sale.order' and self._context.get('active_id', False):
        if self._context.get('active_model') == 'sale.order' and self._context.get('active_id', False):
            sale_order = self.env['sale.order'].browse(self._context.get('active_id'))
            _logger.info('************************************************')
            _logger.info(sale_order.partner_id.id)
            _logger.info('************************************************')
            domain
            solicitudes_model = self.env['solicitudes.credito.lineas'].search([('cliente_id.id','=',sale_order.partner_id.id),('estatus','=','A')])
        #,('estatus','=','A')
        for each in solicitudes_model:
            solicitudes_list.append(each.id)
        if solicitudes_list:
            domain =[('id', 'in', solicitudes_list)]
            #_logger.info('_get_solicitudes domain = ' + domain[0] + domain[1])
        #    return domain
        _logger.info('_get_solicitudes domain CONTEO = ')
        _logger.info(len(domain))
        return domain
    
    
    
    
    
    name = fields.Char('Descripcion Solicitud')
    tipodocumento = fields.Selection([('FAC', 'Factura Consumidor Final'), ('CCF', 'Comprobante de crédito Fiscal')],'Tipo de Documento', default="FAC")
    solicitud_id = fields.Many2one('solicitudes.credito.lineas','Solicitud de Crédito',domain=_get_solicitudes,help='Seleccione una solicitud del cliente o deje en blanco en caso que sea compra sin crédito')
    
    @api.onchange('tipodocumento')
    def onchange_tipodocumento(self):
        self.env['ir.config_parameter'].sudo().set_param('var.tipodocumento', self.tipodocumento)
    
    @api.onchange('solicitud_id')
    def onchange_solicitud_id(self):
        self.env['ir.config_parameter'].sudo().set_param('var.solicitud_id', self.solicitud_id.id)
    
    
    #def create(self, context=None):
    #    _logger.info('****************************** INICIANDO sale.advance.payment.inv *************************')
    
    @api.onchange('advance_payment_method')
    def onchange_advance_payment_method(self):
        if self.advance_payment_method == 'percentage':
            amount = self.default_get(['amount']).get('amount')
            return {'value': {'amount': amount}}
        return {}
    
    def _prepare_invoice_values(self, order, name, amount, so_line):
        
        invoice_vals = {
            'ref': order.client_order_ref,
            'type': 'out_invoice',
            'invoice_origin': order.name,
            'invoice_user_id': order.user_id.id,
            'narration': order.note,
            'partner_id': order.partner_invoice_id.id,
            'fiscal_position_id': order.fiscal_position_id.id or order.partner_id.property_account_position_id.id,
            'partner_shipping_id': order.partner_shipping_id.id,
            'currency_id': order.pricelist_id.currency_id.id,
            'invoice_payment_ref': order.reference,
            'invoice_payment_term_id': order.payment_term_id.id,
            'invoice_partner_bank_id': order.company_id.partner_id.bank_ids[:1].id,
            'team_id': order.team_id.id,
            'campaign_id': order.campaign_id.id,
            'medium_id': order.medium_id.id,
            'source_id': order.source_id.id,
            'tipodocumento':self.tipodocumento,
            'solicitud_id':self.solicitud_id,
            'invoice_line_ids': [(0, 0, {
                'name': name,
                'price_unit': amount,
                'quantity': 1.0,
                'product_id': self.product_id.id,
                'product_uom_id': so_line.product_uom.id,
                'tax_ids': [(6, 0, so_line.tax_id.ids)],
                'sale_line_ids': [(6, 0, [so_line.id])],
                'analytic_tag_ids': [(6, 0, so_line.analytic_tag_ids.ids)],
                'analytic_account_id': order.analytic_account_id.id or False,
            })],
        }
        _logger.info('************************Preparando información de orden hacia factura... ************************2')
        _logger.info(self.tipodocumento)
        
        sol = -2
        if not self.solicitud_id.id:
            sol=-2
        else:
            sol=self.solicitud_id.id
        
        qryupdate = "update solicitudes_credito_lineas set estatus='F' where id = " + str(sol) 
        #qryConsulta = "select count(*) as nreg from nominaclientes_detalle where nomina_id='" +nominaId +"' and nomina_emp_id = " + empId
        _logger.info('************************ QUERY UPDATE ************************2')
        _logger.info(qryupdate)
        self.env.cr.execute(qryupdate)
        #raise Warning('test')
        return invoice_vals
    
    def _get_advance_details(self, order):
        context = {'lang': order.partner_id.lang}
        if self.advance_payment_method == 'percentage':
            amount = order.amount_untaxed * self.amount / 100
            name = "Down payment of %s%%" % (self.amount)
        else:
            amount = self.fixed_amount
            name = 'Down Payment'
        del context

        return amount, name
    
    def _create_invoice(self, order, so_line, amount):
        _logger.info('************************Preparando información de orden hacia factura... ************************1')
        if (self.advance_payment_method == 'percentage' and self.amount <= 0.00) or (self.advance_payment_method == 'fixed' and self.fixed_amount <= 0.00):
            raise UserError(_('The value of the down payment amount must be positive.'))

        amount, name = self._get_advance_details(order)

        invoice_vals = self._prepare_invoice_values(order, name, amount, so_line)

        if order.fiscal_position_id:
            invoice_vals['fiscal_position_id'] = order.fiscal_position_id.id
        invoice = self.env['account.move'].sudo().create(invoice_vals).with_user(self.env.uid)
        invoice.message_post_with_view('mail.message_origin_link',
                    values={'self': invoice, 'origin': order},
                    subtype_id=self.env.ref('mail.mt_note').id)
        return invoice
    
    def _prepare_so_line(self, order, analytic_tag_ids, tax_ids, amount):
        context = {'lang': order.partner_id.lang}
        so_values = {
            'name': 'Down Payment: %s' % (time.strftime('%m %Y'),),
            'price_unit': amount,
            'product_uom_qty': 0.0,
            'order_id': order.id,
            'discount': 0.0,
            'product_uom': self.product_id.uom_id.id,
            'product_id': self.product_id.id,
            'analytic_tag_ids': analytic_tag_ids,
            'tax_id': [(6, 0, tax_ids)],
            'is_downpayment': True,
        }
        del context
        return so_values
    
    def create_invoices(self):
        _logger.info('************************Preparando información de orden hacia factura... ************************0')
        sale_orders = self.env['sale.order'].browse(self._context.get('active_ids', []))

        if self.advance_payment_method == 'delivered':
            sale_orders._create_invoices(final=self.deduct_down_payments)
            _logger.info('************************Preparando información de orden hacia factura... ************************01')
        else:
            _logger.info('************************Preparando información de orden hacia factura... ************************02')
            # Create deposit product if necessary
            if not self.product_id:
                _logger.info('************************Preparando información de orden hacia factura... ************************03')
                vals = self._prepare_deposit_product()
                self.product_id = self.env['product.product'].create(vals)
                self.env['ir.config_parameter'].sudo().set_param('sale.default_deposit_product_id', self.product_id.id)

            sale_line_obj = self.env['sale.order.line']
            for order in sale_orders:
                amount, name = self._get_advance_details(order)

                if self.product_id.invoice_policy != 'order':
                    raise UserError(_('The product used to invoice a down payment should have an invoice policy set to "Ordered quantities". Please update your deposit product to be able to create a deposit invoice.'))
                if self.product_id.type != 'service':
                    raise UserError(_("The product used to invoice a down payment should be of type 'Service'. Please use another product or update this product."))
                taxes = self.product_id.taxes_id.filtered(lambda r: not order.company_id or r.company_id == order.company_id)
                if order.fiscal_position_id and taxes:
                    tax_ids = order.fiscal_position_id.map_tax(taxes, self.product_id, order.partner_shipping_id).ids
                else:
                    tax_ids = taxes.ids
                analytic_tag_ids = []
                for line in order.order_line:
                    analytic_tag_ids = [(4, analytic_tag.id, None) for analytic_tag in line.analytic_tag_ids]

                so_line_values = self._prepare_so_line(order, analytic_tag_ids, tax_ids, amount)
                so_line = sale_line_obj.create(so_line_values)
                self._create_invoice(order, so_line, amount)
        if self._context.get('open_invoices', False):
            return sale_orders.action_view_invoice()
        return {'type': 'ir.actions.act_window_close'}
    
    def _prepare_deposit_product(self):
        return {
            'name': 'Down payment',
            'type': 'service',
            'invoice_policy': 'order',
            'property_account_income_id': self.deposit_account_id.id,
            'taxes_id': [(6, 0, self.deposit_taxes_id.ids)],
            'company_id': False,
        }
    
    
class SaleOrder(models.Model):
    _inherit = 'sale.order'
    _description = 'Asignar datos adicionales a la factura'
    
    def _prepare_invoice(self):
        """
        Prepare the dict of values to create the new invoice for a sales order. This method may be
        overridden to implement custom invoice generation (making sure to call super() to establish
        a clean extension chain).
        """
        self.ensure_one()
        # ensure a correct context for the _get_default_journal method and company-dependent fields
        self = self.with_context(default_company_id=self.company_id.id, force_company=self.company_id.id)
        journal = self.env['account.move'].with_context(default_type='out_invoice')._get_default_journal()
        if not journal:
            raise UserError(_('Please define an accounting sales journal for the company %s (%s).') % (self.company_id.name, self.company_id.id))
        
        #adicional = self.env['sale.advance.payment.inv'].browse(self._context.get('tipodocumento'))
        solicitud = -2
        
        tipodoc = self.env['ir.config_parameter'].sudo().get_param('var.tipodocumento')
        solicitud = self.env['ir.config_parameter'].sudo().get_param('var.solicitud_id')
        
        if not self.solicitud_id.id:
            solicitud=-2
        else:
            solicitud=self.solicitud_id.id
        
        _logger.info('************************Preparando información de orden hacia factura SaleOrder... ************************0')
        #_logger.info('longitud de adicional: ' + str(len(adicional)))
        _logger.info(tipodoc)
        _logger.info(solicitud) 
        #_logger.info(solicitud.id)
        _logger.info('**********************************************************************************************************0')
        #_logger.info(adicional)
        #_logger.info(adicional.tipodocumento)
        
        
        invoice_vals = {
            'ref': self.client_order_ref or '',
            'type': 'out_invoice',
            'narration': self.note,
            'currency_id': self.pricelist_id.currency_id.id,
            'campaign_id': self.campaign_id.id,
            'medium_id': self.medium_id.id,
            'source_id': self.source_id.id,
            'invoice_user_id': self.user_id and self.user_id.id,
            'team_id': self.team_id.id,
            'partner_id': self.partner_invoice_id.id,
            'partner_shipping_id': self.partner_shipping_id.id,
            'invoice_partner_bank_id': self.company_id.partner_id.bank_ids[:1].id,
            'fiscal_position_id': self.fiscal_position_id.id or self.partner_invoice_id.property_account_position_id.id,
            'journal_id': journal.id,  # company comes from the journal
            'invoice_origin': self.name,
            'invoice_payment_term_id': self.payment_term_id.id,
            'invoice_payment_ref': self.reference,
            'transaction_ids': [(6, 0, self.transaction_ids.ids)],
            'invoice_line_ids': [],
            'company_id': self.company_id.id,
            'tipodocumento':tipodoc,
            'solicitud_id':solicitud,
        }
        
        qryupdate = "update solicitudes_credito_lineas set estatus='F' where id = " + str(solicitud) 
        #qryConsulta = "select count(*) as nreg from nominaclientes_detalle where nomina_id='" +nominaId +"' and nomina_emp_id = " + empId
        self.env.cr.execute(qryupdate)
        
        return invoice_vals

    def action_quotation_sent(self):
        if self.filtered(lambda so: so.state != 'draft'):
            raise UserError(_('Only draft orders can be marked as sent directly.'))
        for order in self:
            order.message_subscribe(partner_ids=order.partner_id.ids)
        self.write({'state': 'sent'})

    def action_view_invoice(self):
        invoices = self.mapped('invoice_ids')
        action = self.env.ref('account.action_move_out_invoice_type').read()[0]
        if len(invoices) > 1:
            action['domain'] = [('id', 'in', invoices.ids)]
        elif len(invoices) == 1:
            form_view = [(self.env.ref('account.view_move_form').id, 'form')]
            if 'views' in action:
                action['views'] = form_view + [(state,view) for state,view in action['views'] if view != 'form']
            else:
                action['views'] = form_view
            action['res_id'] = invoices.id
        else:
            action = {'type': 'ir.actions.act_window_close'}

        context = {
            'default_type': 'out_invoice',
        }
        if len(self) == 1:
            context.update({
                'default_partner_id': self.partner_id.id,
                'default_partner_shipping_id': self.partner_shipping_id.id,
                'default_invoice_payment_term_id': self.payment_term_id.id or self.partner_id.property_payment_term_id.id or self.env['account.move'].default_get(['invoice_payment_term_id']).get('invoice_payment_term_id'),
                'default_invoice_origin': self.mapped('name'),
                'default_user_id': self.user_id.id,
            })
        action['context'] = context
        return action

    def _get_invoice_grouping_keys(self):
        return ['company_id', 'partner_id', 'currency_id']

    def _create_invoices(self, grouped=False, final=False):
        """
        Create the invoice associated to the SO.
        :param grouped: if True, invoices are grouped by SO id. If False, invoices are grouped by
                        (partner_invoice_id, currency)
        :param final: if True, refunds will be generated if necessary
        :returns: list of created invoices
        """
        if not self.env['account.move'].check_access_rights('create', False):
            try:
                self.check_access_rights('write')
                self.check_access_rule('write')
            except AccessError:
                return self.env['account.move']

        precision = self.env['decimal.precision'].precision_get('Product Unit of Measure')

        # 1) Create invoices.
        invoice_vals_list = []
        for order in self:
            pending_section = None

            # Invoice values.
            invoice_vals = order._prepare_invoice()

            # Invoice line values (keep only necessary sections).
            for line in order.order_line:
                if line.display_type == 'line_section':
                    pending_section = line
                    continue
                if line.display_type != 'line_note' and float_is_zero(line.qty_to_invoice, precision_digits=precision):
                    continue
                if line.qty_to_invoice > 0 or (line.qty_to_invoice < 0 and final) or line.display_type == 'line_note':
                    if pending_section:
                        invoice_vals['invoice_line_ids'].append((0, 0, pending_section._prepare_invoice_line()))
                        pending_section = None
                    invoice_vals['invoice_line_ids'].append((0, 0, line._prepare_invoice_line()))

            if not invoice_vals['invoice_line_ids']:
                raise UserError(_('There is no invoiceable line. If a product has a Delivered quantities invoicing policy, please make sure that a quantity has been delivered.'))

            invoice_vals_list.append(invoice_vals)

        if not invoice_vals_list:
            raise UserError(_(
                'There is no invoiceable line. If a product has a Delivered quantities invoicing policy, please make sure that a quantity has been delivered.'))

        # 2) Manage 'grouped' parameter: group by (partner_id, currency_id).
        if not grouped:
            new_invoice_vals_list = []
            invoice_grouping_keys = self._get_invoice_grouping_keys()
            for grouping_keys, invoices in groupby(invoice_vals_list, key=lambda x: [x.get(grouping_key) for grouping_key in invoice_grouping_keys]):
                origins = set()
                payment_refs = set()
                refs = set()
                ref_invoice_vals = None
                for invoice_vals in invoices:
                    if not ref_invoice_vals:
                        ref_invoice_vals = invoice_vals
                    else:
                        ref_invoice_vals['invoice_line_ids'] += invoice_vals['invoice_line_ids']
                    origins.add(invoice_vals['invoice_origin'])
                    payment_refs.add(invoice_vals['invoice_payment_ref'])
                    refs.add(invoice_vals['ref'])
                ref_invoice_vals.update({
                    'ref': ', '.join(refs)[:2000],
                    'invoice_origin': ', '.join(origins),
                    'invoice_payment_ref': len(payment_refs) == 1 and payment_refs.pop() or False,
                })
                new_invoice_vals_list.append(ref_invoice_vals)
            invoice_vals_list = new_invoice_vals_list

        # 3) Create invoices.

        # As part of the invoice creation, we make sure the sequence of multiple SO do not interfere
        # in a single invoice. Example:
        # SO 1:
        # - Section A (sequence: 10)
        # - Product A (sequence: 11)
        # SO 2:
        # - Section B (sequence: 10)
        # - Product B (sequence: 11)
        #
        # If SO 1 & 2 are grouped in the same invoice, the result will be:
        # - Section A (sequence: 10)
        # - Section B (sequence: 10)
        # - Product A (sequence: 11)
        # - Product B (sequence: 11)
        #
        # Resequencing should be safe, however we resequence only if there are less invoices than
        # orders, meaning a grouping might have been done. This could also mean that only a part
        # of the selected SO are invoiceable, but resequencing in this case shouldn't be an issue.
        if len(invoice_vals_list) < len(self):
            SaleOrderLine = self.env['sale.order.line']
            for invoice in invoice_vals_list:
                sequence = 1
                for line in invoice['invoice_line_ids']:
                    line[2]['sequence'] = SaleOrderLine._get_invoice_line_sequence(new=sequence, old=line[2]['sequence'])
                    sequence += 1

        # Manage the creation of invoices in sudo because a salesperson must be able to generate an invoice from a
        # sale order without "billing" access rights. However, he should not be able to create an invoice from scratch.
        moves = self.env['account.move'].sudo().with_context(default_type='out_invoice').create(invoice_vals_list)

        # 4) Some moves might actually be refunds: convert them if the total amount is negative
        # We do this after the moves have been created since we need taxes, etc. to know if the total
        # is actually negative or not
        if final:
            moves.sudo().filtered(lambda m: m.amount_total < 0).action_switch_invoice_into_refund_credit_note()
        for move in moves:
            move.message_post_with_view('mail.message_origin_link',
                values={'self': move, 'origin': move.line_ids.mapped('sale_line_ids.order_id')},
                subtype_id=self.env.ref('mail.mt_note').id
            )
        return moves
    

#################################
#Campos Factura
#################################     
    
class AgregarCamposFactura(models.Model):
    _inherit = 'account.move'
    
    def _get_solicitudes(self):
        #partner=999
        
        domain =[('id', '=', -1)]
        solicitudes_list=[]
        _logger.info('_get_solicitudes domain 4.0 = ')
        solicitudes_model = self.env['solicitudes.credito.lineas'].search([('cliente_id.id','=',-2),('estatus','=','A')])
        #_logger.info(self.order.partner_id)
        #if self._context.get('active_model') == 'sale.order' and self._context.get('active_id', False):
        #if self._context.get('active_model') == 'sale.order' and self._context.get('active_id', False):
        #    sale_order = self.env['sale.order'].browse(self._context.get('active_id'))
        _logger.info('************************************************ partner id **********')
        _logger.info(self.partner_id.id)
        _logger.info('************************************************')
        #domain
        #partner = self.partner_id.id
        #self.env.cr.execute("SELECT id from solicitudes_credito_lineas where cliente_id= {}".format(partner))
        #self.deadline = env.cr.fetchone()[0]
        #solicitudes_model= self.env.cr.fetchall()
        
        solicitudes_model = self.env['solicitudes.credito.lineas'].search([('cliente_id.id','=',self.partner_id.id),])
        #,('estatus','=','A')
        _logger.info('************************************************ each id **********')
        for each in solicitudes_model:
            solicitudes_list.append(each[0])
            _logger.info(each[0])
        _logger.info('************************************************ fin each id **********')    
        if solicitudes_list:
            domain =[('id', 'in', solicitudes_list)]
            #_logger.info('_get_solicitudes domain = ' + domain[0] + domain[1])
        #    return domain
        _logger.info('_get_solicitudes domain CONTEO = ')
        _logger.info(len(domain))
        return domain
    
    
    tipodocumento = fields.Selection([('FAC', 'Factura Consumidor Final'), ('CCF', 'Comprobante de crédito Fiscal')],'Tipo de Documento', default="FAC")
    solicitud_id = fields.Many2one('solicitudes.credito.lineas','Solicitud de Crédito',domain=_get_solicitudes, help='Seleccione una solicitud del cliente o deje en blanco en caso que sea compra sin crédito')
    
    def name_get(self):
        
        _logger.info('************************************************ NAMEGET ***************************************')
        result = []
        partner = -2
        if not self.partner_id.id:
            partner=-2
        else:
            partner = self.partner_id.id
            
        qry = "SELECT id, name from solicitudes_credito_lineas where cliente_id=" + str(partner) + " order by id"
        
        self.env.cr.execute(qry)
        #self.deadline = env.cr.fetchone()[0]
        registros= self.env.cr.fetchall()
        
        _logger.info("******** registros *********")
        _logger.info(len(registros))
        
        for record in registros:
            if self.env.context.get('mostrar', False):
            # Only goes off when the custom_search is in the context values.
                result.append((record.id, "{} - ${}".format(record.name, record.montoaprobado)))
            else:
                result.append((record[0], record[1]))
        return result
    
    
    
    
    
    
    
    
    

    #employee_id = fields.Many2one('hr.employee','Employee',required=True,domain=_get_employee)
    
    #def default_get(self,fields):
        #wt = self.env['solicitudes.credito.lineas']
        #solicitudes = wt.search([('cliente_id', '=', self.solicitud_id.cliente_id)]).id
        
        #self.solicitud_id.search([('cliente_id', '=', self.solicitud_id.cliente_id)])
        #new = wt.browse(solicitudes)
        
        
    #def name_get(self):
        #result = []
        #for record in self:
            #if self.env.context.get('mostrar_solicitudes', False):
                # Only goes off when the custom_search is in the context values.
            #result.append((record.id, "{} {}".format(record.id, record.montoaprobado)))
            #else:
            #    result.append((record.id, record.name))
    
# class soluciones__estrategicas(models.Model):
#     _name = 'soluciones__estrategicas.soluciones__estrategicas'
#     _description = 'soluciones__estrategicas.soluciones__estrategicas'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
