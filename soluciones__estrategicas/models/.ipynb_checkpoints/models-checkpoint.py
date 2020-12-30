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

    diasdegraciacredito = fields.Integer('Días de gracias (Crédito)', default=0)

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
    
    nombrereferenciafamiliar1 = fields.Char('Nombre Referencia Familiar 1')
    telefonodereferenciafamiliar1 = fields.Char('Teléfono Referencia Familiar 1')
    direcciondereferenciafamiliar1 = fields.Char('Domicilio Referencia Familiar 1')
    relacionreferenciafamiliar1 = fields.Selection( [('1','Padre'), ('2','Madre'), ('3','Hermano(a)'), ('4','Primo(a)'), ('5','Amigo(a)'), ('6','Cuñado(a)'), ('7','Abuelo(a)'), ('8','Compañero(a) Trabajo'), ('9','Esposo(a)'), ('10','Compañero(a) de vida'), ('11','Tio(a)'),('12','Hijo(a)'),('13','Yerno'),('14','Sobrino(a)'),('15','Nuera'),('16','Suegro(a)'),('17','Nieto(a)'),('18','Jefe(a)'),('19','Hijastro(a)'),('20','Comadre'),('21','Compadre')]
, 'Relación Referencia Familiar 1')
    
    nombrereferenciafamiliar2 = fields.Char('Nombre Referencia Familiar 2')
    telefonodereferenciafamiliar2 = fields.Char('Teléfono Referencia Familiar 2')
    direcciondereferenciafamiliar2 = fields.Char('Domicilio Referencia Familiar 2')
    relacionreferenciafamiliar2 = fields.Selection([('1','Padre'), ('2','Madre'), ('3','Hermano(a)'), ('4','Primo(a)'), ('5','Amigo(a)'), ('6','Cuñado(a)'), ('7','Abuelo(a)'), ('8','Compañero(a) Trabajo'), ('9','Esposo(a)'), ('10','Compañero(a) de vida'), ('11','Tio(a)'),('12','Hijo(a)'),('13','Yerno'),('14','Sobrino(a)'),('15','Nuera'),('16','Suegro(a)'),('17','Nieto(a)'),('18','Jefe(a)'),('19','Hijastro(a)'),('20','Comadre'),('21','Compadre')], 'Relación Referencia Familiar 2')
    
    nombrereferenciapersonal1 = fields.Char('Nombre Referencia Personal 1')
    telefonodereferenciapersonal1 = fields.Char('Teléfono Referencia Personal 1')
    direcciondereferenciapersonal1 = fields.Char('Domicilio Referencia Personal 1')
    relacionreferenciapersonal1 = fields.Selection([('1','Padre'), ('2','Madre'), ('3','Hermano(a)'), ('4','Primo(a)'), ('5','Amigo(a)'), ('6','Cuñado(a)'), ('7','Abuelo(a)'), ('8','Compañero(a) Trabajo'), ('9','Esposo(a)'), ('10','Compañero(a) de vida'), ('11','Tio(a)'),('12','Hijo(a)'),('13','Yerno'),('14','Sobrino(a)'),('15','Nuera'),('16','Suegro(a)'),('17','Nieto(a)'),('18','Jefe(a)'),('19','Hijastro(a)'),('20','Comadre'),('21','Compadre')], 'Relación Referencia Personal 1')
    
    nombrereferenciapersonal2 = fields.Char('Nombre Referencia Personal 2')
    telefonodereferenciapersonal2 = fields.Char('Teléfono Referencia Personal 2')
    direcciondereferenciapersonal2 = fields.Char('Domicilio Referencia Personal 2')
    relacionreferenciapersonal2 = fields.Selection([('1','Padre'), ('2','Madre'), ('3','Hermano(a)'), ('4','Primo(a)'), ('5','Amigo(a)'), ('6','Cuñado(a)'), ('7','Abuelo(a)'), ('8','Compañero(a) Trabajo'), ('9','Esposo(a)'), ('10','Compañero(a) de vida'), ('11','Tio(a)'),('12','Hijo(a)'),('13','Yerno'),('14','Sobrino(a)'),('15','Nuera'),('16','Suegro(a)'),('17','Nieto(a)'),('18','Jefe(a)'),('19','Hijastro(a)'),('20','Comadre'),('21','Compadre')], 'Relación Referencia Personal 2')
    
    
    #codeudor
    nombrecodeudor = fields.Char('Nombre Codeudor')
    
    
    fechadenacimientocodeudor = fields.Date('Fecha de Nacimiento Codeudor')
    edadcodeudor = fields.Integer('Edad Codeudor')
    domiciliocodeudor = fields.Char('Domicilio Codeudor')
    duicodeudor = fields.Char('DUI Codeudor')
    nitcodeudor = fields.Char('NIT Codeudor')
    tipodeviviendacodeudor = fields.Selection([('Propia', 'Propia'), ('Alquilada', 'Alquilada')],'Tipo de Vivienda Codeudor')
    fechadeexpedicionduicodeudor = fields.Date('Fecha Expedicion DUI ')
    fechadeexpiracionduicodeudor = fields.Date('Fecha Expiración DUI ')
    
    
    lugardetrabajocodeudor = fields.Char('Lugar de Trabajo Codeudor')
    direcciondetrabajocodeudor = fields.Char('Dirección Codeudor')
    telefonofijocodeudor = fields.Char('Teléfono Fijo Codeudor')
    telefonocelularcodeudor = fields.Char('Teléfono Celular Codeudor')
    jefeinmediatocodeudor = fields.Char('Jefe Inmediato Codeudor')
    telefonotrabajocodeudor = fields.Char('Telefono Trabajo Codeudor')
    telefonojefeinmediatocodeudor = fields.Char('Teléfono Jefe Inmediato Codeudor')
    ocupacioncodeudor = fields.Char('Ocupación Codeudor')
    salariocodeudor = fields.Float('Salario Codeudor')
    ingresosextrascodeudor = fields.Char('Detalle Ingresos Extras Codeudor')

    nombredelamadrecodeudor = fields.Char('Nombre de la Madre Codeudor')
    telefonodelamadrecodeudor = fields.Char('Teléfono de la Madre Codeudor')
    direcciondelamadrecodeudor = fields.Char('Dirección de la Madre Codeudor')
    lugardetrabajodelamadrecodeudor = fields.Char('Lugar de Trabajo de la Madre Codeudor')
    direccionlugardetrabajodelamadrecodeudor = fields.Char('Dirección lugar de trabajo de la madre Codeudor')
    jefeinmediatodelamadrecodeudor = fields.Char('Jefe Inmediato de la Madre Codeudor')
    telefonodeljefeinmediatodelamadrecodeudor = fields.Char('Telefono del Jefe Inmediato de la Madre Codeudor')
    
    nombredelpadrecodeudor = fields.Char('Nombre del Padre Codeudor')
    telefonodelpadrecodeudor = fields.Char('Teléfono del Padre Codeudor')
    direcciondelpadrecodeudor = fields.Char('Dirección del Padre Codeudor')
    lugardetrabajodelpadrecodeudor = fields.Char('Lugar de Trabajo del Padre Codeudor')
    direccionlugardetrabajodelpadrecodeudor = fields.Char('Dirección lugar de trabajo del Padre Codeudor')
    jefeinmediatodelpadrecodeudor = fields.Char('Jefe Inmediato del Padre Codeudor')
    telefonodeljefeinmediatodelpadrecodeudor = fields.Char('Telefono del Jefe Inmediato del Padre Codeudor')
    
    nombredeconyuguecodeudor = fields.Char('Nombre de Conyugue Codeudor')
    telefonodeconyuguecodeudor = fields.Char('Teléfono de Conyugue Codeudor')
    direcciondeconyuguecodeudor = fields.Char('Dirección de Conyugue Codeudor')
    lugardetrabajodeconyuguecodeudor = fields.Char('Lugar de Trabajo de Conyugue Codeudor')
    direccionlugardetrabajodeconyuguecodeudor = fields.Char('Dirección lugar de trabajo de Conyugue Codeudor')
    jefeinmediatodeconyuguecodeudor = fields.Char('Jefe Inmediato de Conyugue Codeudor')
    telefonodeljefeinmediatodeconyuguecodeudor = fields.Char('Telefono del Jefe Inmediato de Conyugue Codeudor')
    
    nombrereferenciafamiliar1codeudor = fields.Char('Nombre Referencia Familiar 1 Codeudor')
    telefonodereferenciafamiliar1codeudor = fields.Char('Teléfono Referencia Familiar 1 Codeudor')
    direcciondereferenciafamiliar1codeudor = fields.Char('Domicilio Referencia Familiar 1 Codeudor')
    relacionreferenciafamiliar1codeudor = fields.Selection([('1','Padre'), ('2','Madre'), ('3','Hermano(a)'), ('4','Primo(a)'), ('5','Amigo(a)'), ('6','Cuñado(a)'), ('7','Abuelo(a)'), ('8','Compañero(a) Trabajo'), ('9','Esposo(a)'), ('10','Compañero(a) de vida'), ('11','Tio(a)'),('12','Hijo(a)'),('13','Yerno'),('14','Sobrino(a)'),('15','Nuera'),('16','Suegro(a)'),('17','Nieto(a)'),('18','Jefe(a)'),('19','Hijastro(a)'),('20','Comadre'),('21','Compadre')], 'Relación Referencia Familiar 1 Codeudor')
    
    nombrereferenciafamiliar2codeudor = fields.Char('Nombre Referencia Familiar 2 Codeudor')
    telefonodereferenciafamiliar2codeudor = fields.Char('Teléfono Referencia Familiar 2 Codeudor')
    direcciondereferenciafamiliar2codeudor = fields.Char('Domicilio Referencia Familiar 2 Codeudor')
    relacionreferenciafamiliar2codeudor = fields.Selection([('1','Padre'), ('2','Madre'), ('3','Hermano(a)'), ('4','Primo(a)'), ('5','Amigo(a)'), ('6','Cuñado(a)'), ('7','Abuelo(a)'), ('8','Compañero(a) Trabajo'), ('9','Esposo(a)'), ('10','Compañero(a) de vida'), ('11','Tio(a)'),('12','Hijo(a)'),('13','Yerno'),('14','Sobrino(a)'),('15','Nuera'),('16','Suegro(a)'),('17','Nieto(a)'),('18','Jefe(a)'),('19','Hijastro(a)'),('20','Comadre'),('21','Compadre')], 'Relación Referencia Familiar 2 Codeudor')
    
    nombrereferenciapersonal1codeudor = fields.Char('Nombre Referencia Personal 1 Codeudor')
    telefonodereferenciapersonal1codeudor = fields.Char('Teléfono Referencia Personal 1 Codeudor')
    direcciondereferenciapersonal1codeudor = fields.Char('Domicilio Referencia Personal 1 Codeudor')
    relacionreferenciapersonal1codeudor = fields.Selection([('1','Padre'), ('2','Madre'), ('3','Hermano(a)'), ('4','Primo(a)'), ('5','Amigo(a)'), ('6','Cuñado(a)'), ('7','Abuelo(a)'), ('8','Compañero(a) Trabajo'), ('9','Esposo(a)'), ('10','Compañero(a) de vida'), ('11','Tio(a)'),('12','Hijo(a)'),('13','Yerno'),('14','Sobrino(a)'),('15','Nuera'),('16','Suegro(a)'),('17','Nieto(a)'),('18','Jefe(a)'),('19','Hijastro(a)'),('20','Comadre'),('21','Compadre')], 'Relación Referencia Personal 1 Codeudor')
    
    nombrereferenciapersonal2codeudor = fields.Char('Nombre Referencia Personal 2 Codeudor')
    telefonodereferenciapersonal2codeudor = fields.Char('Teléfono Referencia Personal 2 Codeudor')
    direcciondereferenciapersonal2codeudor = fields.Char('Domicilio Referencia Personal 2 Codeudor')
    relacionreferenciapersonal2codeudor = fields.Selection([('1','Padre'), ('2','Madre'), ('3','Hermano(a)'), ('4','Primo(a)'), ('5','Amigo(a)'), ('6','Cuñado(a)'), ('7','Abuelo(a)'), ('8','Compañero(a) Trabajo'), ('9','Esposo(a)'), ('10','Compañero(a) de vida'), ('11','Tio(a)'),('12','Hijo(a)'),('13','Yerno'),('14','Sobrino(a)'),('15','Nuera'),('16','Suegro(a)'),('17','Nieto(a)'),('18','Jefe(a)'),('19','Hijastro(a)'),('20','Comadre'),('21','Compadre')], 'Relación Referencia Personal 2 Codeudor')
    
    solicitudes_lineas = fields.One2many('solicitudes.credito.lineas','cliente_id')
    


    
    @api.onchange('fechadenacimiento')
    def actualizaredad(self):
        hoy = date.today()
        
        anionac= 1900
        dia=1
        mes=1
        
        if not self.fechadenacimiento:
            anionac = 1900
            dia = 1
            mes = 1
        else:
            anionac = self.fechadenacimiento.year
            mes = self.fechadenacimiento.month
            dia = self.fechadenacimiento.day
        
        edad = hoy.year - anionac
        full_year_passed = (hoy.month, hoy.day) < (mes, dia)
        if not full_year_passed:
            edad -= 1
        edad+=1   
        self.edad = edad
    

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
    pago_solicitud_id = fields.One2many('account.payment','solicitud_id')
    
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
        noombre=''
        self.cuota = cuota
        self.montoprestado = self.montoaprobado - self.montoanticipo
        self.saldodespuesanticipo = self.cuota * self.numerodecuotas
        cuotasaldoinicial = self.saldodespuesanticipo
        for nc in range(self.numerodecuotas):
            cuotasaldofinal = cuotasaldoinicial - cuota
            nuevafecha = fecha + timedelta(days=dias)
            fechalimite = nuevafecha + timedelta(days=self.cliente_id.diasdegraciacredito)

            nombre = '(' + str(nc+1) + ') - ' + fechalimite.strftime('%d/%m/%Y') + ' - ' + '${:,.2f}'.format(cuota)
            self.env['solicitudes.credito.lineas.cuotas'].create({'solicitud_id': self.id,'cuotanumero': nc+1, 'cuotafecha':nuevafecha,'cuotafechapagada':nuevafecha,'cuotasaldoinicial':cuotasaldoinicial, 'cuotamonto':cuota,'cuotasaldofinal':cuotasaldofinal, 'cuotamontorecibido':0,'cuotaestatus':'E','cuotafechalimite':fechalimite,'name':nombre}) 

            

            fecha = nuevafecha
            cuotasaldoinicial = cuotasaldofinal
    
class SolicitudesCreditoCuotas(models.Model):
    _name = 'solicitudes.credito.lineas.cuotas'
    _description = 'Cuotas de Credito'
    solicitud_id = fields.Many2one('solicitudes.credito.lineas','ID Solicitud')
    name = fields.Char('Descripción')
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
    pago_id = fields.One2many('account.payment','cuota_id')
    
    
        

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
        
        sol = 0
        if self.solicitud_id.id == False:
            sol=0
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
        
        if solicitud == False:
            solicitud=0
        
        
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
        domain =[('partner_id', '=', -1)]
        solicitudes_list=[]
        _logger.info('_get_solicitudes domain 4.0 = ')
        solicitudes_model = self.env['solicitudes.credito.lineas'].search([('id','=',-2),('estatus','=','A')])
     
        
        solicitudes_model = self.env['solicitudes.credito.lineas'].search([('cliente_id.id','=',self.partner_id.id),])
        #,('estatus','=','A')

        for each in solicitudes_model:
            solicitudes_list.append(each[0])
   
        if solicitudes_list:
            domain =[('id', 'in', solicitudes_list)]


        if solicitudes_list:
            domain =[('solicitud_id', 'in', solicitudes_list), ('estatus', '=', 'F')]

        return domain
    
    
    tipodocumento = fields.Selection([('FAC', 'Factura Consumidor Final'), ('CCF', 'Comprobante de crédito Fiscal')],'Tipo de Documento', default="FAC")
    solicitud_id = fields.Many2one('solicitudes.credito.lineas','Solicitud de Crédito',domain=_get_solicitudes, help='Seleccione una solicitud del cliente o deje en blanco en caso que sea compra sin crédito')
    
    def name_get(self):
        
        _logger.info('************************************************ NAMEGET FACTURA ***************************************')
        
        
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
    
    
#################################
#Campos Pago
#################################       
    
class AccountPayment(models.Model):
    _inherit = 'account.payment'
    
    
    def name_get(self):
        
        _logger.info('************************************************ NAMEGET FACTURA PAGOS ***************************************')
        
        
        result = []
        partner = -2
        if not self.partner_id.id:
            partner=-2
        else:
            partner = self.partner_id.id
            
        qry = "SELECT a.id, a.name, a.cuotanumero from solicitudes_credito_lineas_cuotas a inner join solicitudes_credito_lineas b on b.id = a.solicitud_id where b.cliente_id=" + str(partner) + " and a.cuotaestatus='E' and b.estatus='F' order by solicitud_id,cuotanumero"
        
        _logger.info(qry)
        self.env.cr.execute(qry)
        #self.deadline = env.cr.fetchone()[0]
        registros= self.env.cr.fetchall()
        
        _logger.info("******** registros *********")
        _logger.info(len(registros))
        
        for record in registros:
            if self.env.context.get('mostrar', False):
            # Only goes off when the custom_search is in the context values.
                result.append((record.id, "{} - ${}".format(record.name, record.montocuota)))
                _logger.info("******** THEN *********")
            else:
                result.append((record[0], record[1]))
                _logger.info("******** ELSE *********")
        return result
    
    def get_cuotas_domain(self):
        domain =[('solicitud_id', '=', -1)]
        solicitudes_list=[]
        _logger.info('>>>>>>>>>>>>>>>>>>>>>>>_get_solicitudes domain 5.0 = <<<<<<<<<<<<<<<<<')
        solicitudes_model = self.env['solicitudes.credito.lineas'].search([('id','=',-2),('estatus','=','F')])
        #_logger.info(self.order.partner_id)
        #if self._context.get('active_model') == 'sale.order' and self._context.get('active_id', False):
        _logger.info('<<<<<<<<<<<<<<<<< active >>>>>>>>>>><')
        _logger.info(self._context.get('active_model'))
        _logger.info(self._context.get('active_id', False))
        
        if self._context.get('active_model') == 'account.move' and self._context.get('active_id', False):
            pago = self.env['account.move'].browse(self._context.get('active_id'))
            _logger.info('******************PARTNER DE PAGOS******************************')
            _logger.info(pago.partner_id.id)
            _logger.info('****************************************************************')

            solicitudes_model = self.env['solicitudes.credito.lineas'].search([('id','=',pago.solicitud_id.id),('estatus','=','F')])
            #,('estatus','=','A')
        for each in solicitudes_model:
            solicitudes_list.append(each.id)
        if solicitudes_list:
            domain =[('solicitud_id', 'in', solicitudes_list),('cuotaestatus','=','E')]
            #_logger.info('_get_solicitudes domain = ' + domain[0] + domain[1])
            #    return domain
        _logger.info('_get_solicitudes_PAGO domain CONTEO = ')
        _logger.info(domain)
        return domain
    
    solicitud_id = fields.Many2one('solicitudes.credito.lineas','Solicitud de Crédito', help='Seleccione una solicitud del cliente o deje en blanco en caso que sea compra sin crédito')
    cuota_id = fields.Many2one('solicitudes.credito.lineas.cuotas','Cuota',domain=get_cuotas_domain, help='Seleccione una cuota del cliente o deje en blanco en caso que sea compra sin crédito')
    
    
    
    
    def _get_payment_chatter_link(self):
        self.ensure_one()
        return '<a href=# data-oe-model=account.payment data-oe-id=%d>%s</a>' % (self.id, self.name)

    @api.onchange('partner_id', 'payment_method_id', 'journal_id')
    def _onchange_set_payment_token_id(self):
        res = {}

        if not self.payment_method_code == 'electronic' or not self.partner_id or not self.journal_id:
            self.payment_token_id = False
            return res

        partners = self.partner_id | self.partner_id.commercial_partner_id | self.partner_id.commercial_partner_id.child_ids
        domain = [('partner_id', 'in', partners.ids), ('acquirer_id.journal_id', '=', self.journal_id.id)]
        self.payment_token_id = self.env['payment.token'].search(domain, limit=1)

        res['domain'] = {'payment_token_id': domain}
        return res

    def _prepare_payment_transaction_vals(self):
        self.ensure_one()
        
        
        
        
        return {
            'amount': self.amount,
            'currency_id': self.currency_id.id,
            'partner_id': self.partner_id.id,
            'partner_country_id': self.partner_id.country_id.id,
            'invoice_ids': [(6, 0, self.invoice_ids.ids)],
            'payment_token_id': self.payment_token_id.id,
            'acquirer_id': self.payment_token_id.acquirer_id.id,
            'payment_id': self.id,
            'type': 'server2server',
        }

    def _create_payment_transaction(self, vals=None):
        for pay in self:
            if pay.payment_transaction_id:
                raise ValidationError(_('A payment transaction already exists.'))
            elif not pay.payment_token_id:
                raise ValidationError(_('A token is required to create a new payment transaction.'))

        transactions = self.env['payment.transaction']
        for pay in self:
            transaction_vals = pay._prepare_payment_transaction_vals()

            if vals:
                transaction_vals.update(vals)

            transaction = self.env['payment.transaction'].create(transaction_vals)
            transactions += transaction

            # Link the transaction to the payment.
            pay.payment_transaction_id = transaction
            
        

        return transactions

    def action_validate_invoice_payment(self):
        res = super(AccountPayment, self).action_validate_invoice_payment()
        self.mapped('payment_transaction_id').filtered(lambda x: x.state == 'done' and not x.is_processed)._post_process_after_done()
        return res

    def post(self):
        # Post the payments "normally" if no transactions are needed.
        # If not, let the acquirer updates the state.
        #                                __________            ______________
        #                               | Payments |          | Transactions |
        #                               |__________|          |______________|
        #                                  ||                      |    |
        #                                  ||                      |    |
        #                                  ||                      |    |
        #  __________  no s2s required   __\/______   s2s required |    | s2s_do_transaction()
        # |  Posted  |<-----------------|  post()  |----------------    |
        # |__________|                  |__________|<-----              |
        #                                                |              |
        #                                               OR---------------
        #  __________                    __________      |
        # | Cancelled|<-----------------| cancel() |<-----
        # |__________|                  |__________|

        payments_need_trans = self.filtered(lambda pay: pay.payment_token_id and not pay.payment_transaction_id)
        transactions = payments_need_trans._create_payment_transaction()

        res = super(AccountPayment, self - payments_need_trans).post()

        transactions.s2s_do_transaction()
        
        cuota_id=-2
        cuota_id = self.cuota_id.id
            
        cuotafechapagada = self.payment_date
        cuotamontorecibido = self.amount
        qry=""
            
        if cuota_id:
            qry="update solicitudes_credito_lineas_cuotas set cuotaestatus='P', cuotafechapagada='" + str(cuotafechapagada) + "', cuotamontorecibido=" + str(cuotamontorecibido)+" where id=" + str(cuota_id)
            self.env.cr.execute(qry)
            
        _logger.info("******** QRY *********")
        _logger.info("CUOTA: " + str(cuota_id))
        _logger.info("Fecha Pagada: " + str(cuotafechapagada))
        _logger.info("Cuota Monto Recibido: " + str(cuotamontorecibido))
        _logger.info(qry)
        _logger.info("**********************************************")
        

        return res
    
    
    
    
    
    
    

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
