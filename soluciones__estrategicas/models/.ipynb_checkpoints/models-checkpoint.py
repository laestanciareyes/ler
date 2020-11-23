# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError, Warning
from datetime import date
from datetime import datetime
from datetime import timedelta
import numpy as np
import logging

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
    domiciliocodeudor = fields.Char('Domicilio      ')
    duicodeudor = fields.Char('DUI ')
    nitcodeudor = fields.Char('NIT ')
    tipodeviviendacodeudor = fields.Selection([('Propia', 'Propia'), ('Alquilada', 'Alquilada')],'Tipo de Vivienda  ')
    fechadeexpedicionduicodeudor = fields.Date('Fecha Expedicion DUI ')
    fechadeexpiracionduicodeudor = fields.Date('Fecha Expiración DUI ')
    
    
    lugardetrabajocodeudor = fields.Char('Lugar de Trabajo      ')
    direcciondetrabajocodeudor = fields.Char('Dirección      ')
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
    estatus = fields.Selection([('E', 'Evaluación'), ('A', 'Aprobado'), ('D','Denegado'), ('C','Cancelado')],'Estatus', default="E")
    solicitudes_lineas_cuotas = fields.One2many('solicitudes.credito.lineas.cuotas','solicitud_id')
    
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
        cuota = -1 * np.pmt((self.porcentajedeinteresdelcredito/100), self.numerodecuotas, self.montoaprobado - self.montoanticipo)
        self.cuota = cuota
        self.montoprestado = self.montoaprobado - self.montoanticipo
        self.saldodespuesanticipo = self.cuota * self.numerodecuotas
        cuotasaldoinicial = self.saldodespuesanticipo
        for nc in range(self.numerodecuotas):
            cuotasaldofinal = cuotasaldoinicial - cuota
            nuevafecha = fecha + timedelta(days=dias)
            self.env['solicitudes.credito.lineas.cuotas'].create({'solicitud_id': self.id,'cuotanumero': nc+1, 'cuotafecha':nuevafecha,'cuotafechapagada':nuevafecha,'cuotasaldoinicial':cuotasaldoinicial, 'cuotamonto':cuota,'cuotasaldofinal':cuotasaldofinal, 'cuotamontorecibido':0,'cuotaestatus':'E'}) 
            fecha = nuevafecha
            cuotasaldoinicial = cuotasaldofinal
    
class SolicitudesCreditoCuotas(models.Model):
    _name = 'solicitudes.credito.lineas.cuotas'
    _description = 'Cuotas de Credito'
    solicitud_id = fields.Many2one('solicitudes.credito.lineas','ID Cuota')
    cuotanumero = fields.Integer('Cuota')
    cuotafecha = fields.Date('Fecha de pago')
    cuotafechapagada = fields.Date('Fecha pagada')
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
