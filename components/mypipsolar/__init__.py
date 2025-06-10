import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import uart
from esphome.const import CONF_ID
from esphome.components import pipsolar as parent

DEPENDENCIES = ['uart']
AUTO_LOAD = ['sensor', 'text_sensor', 'binary_sensor', 'switch', 'output', 'select']

mypipsolar_ns = cg.esphome_ns.namespace('mypipsolar')
MyPipSolar = mypipsolar_ns.class_('MyPipSolar', parent.PipsolarComponent)

# Відокремлюємо базову схему від оригіналу, щоб зробити extend
BASE_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(parent.PipsolarComponent),
}).extend(uart.UART_DEVICE_SCHEMA)

# Створюємо фінальну схему, де викликаємо cv.All без extend на parent.CONFIG_SCHEMA
CONFIG_SCHEMA = cv.All(
    BASE_SCHEMA,
    cv.polling_component_schema('1s'),
)

def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    yield cg.register_component(var, config)
    yield uart.register_uart_device(var, config)
