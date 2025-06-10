import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import uart
from esphome.const import CONF_ID
from esphome.components import pipsolar as parent

DEPENDENCIES = ['uart']
AUTO_LOAD = ['sensor', 'text_sensor', 'binary_sensor', 'switch', 'output', 'select']

mypipsolar_ns = cg.esphome_ns.namespace('pipsolar')  # те саме namespace!
MyPipSolar = mypipsolar_ns.class_('MyPipSolar', parent.PipsolarComponent)

CONFIG_SCHEMA = parent.CONFIG_SCHEMA.extend({
    # сюди можна додати свої параметри, якщо потрібно, поки лишаємо порожнім
})

def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    yield cg.register_component(var, config)
    yield uart.register_uart_device(var, config)
