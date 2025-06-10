import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import uart
from esphome.const import CONF_ID

# Імпортуємо неймспейс батьківського компонента
parent_ns = cg.esphome_ns.namespace('pipsolar')
PipSolar = parent_ns.class_('PipSolar')  # Так оголошуємо клас

# Створюємо свій неймспейс
mypipsolar_ns = cg.esphome_ns.namespace('mypipsolar')

# Визначаємо клас-нащадок
MyPipSolar = mypipsolar_ns.class_('MyPipSolar', PipSolar)

# Схема конфігурації
CONFIG_SCHEMA = parent_ns.CONFIG_SCHEMA  # або інша схема, якщо є

def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    yield cg.register_component(var, config)
    yield uart.register_uart_device(var, config)
