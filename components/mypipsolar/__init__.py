import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import uart, pipsolar
from esphome.const import CONF_ID

mypipsolar_ns = cg.esphome_ns.namespace("mypipsolar")
MyPipSolar = mypipsolar_ns.class_("MyPipSolar", pipsolar.PipsolarComponent)

# Візьмемо схему зсередини cv.All батьківського CONFIG_SCHEMA:
PARENT_SCHEMA = cv.Schema({cv.GenerateID(): cv.declare_id(pipsolar.PipsolarComponent)})\
    .extend(cv.polling_component_schema("1s"))\
    .extend(uart.UART_DEVICE_SCHEMA)

# Тепер розширимо її додатковими параметрами для mypipsolar
CONFIG_SCHEMA = cv.All(
    PARENT_SCHEMA.extend({
        # тут додаємо свої додаткові параметри, наприклад:
        # cv.Optional("custom_param"): cv.string,
    })
)

def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    yield cg.register_component(var, config)
    yield uart.register_uart_device(var, config)
    # Тут додай свій додатковий код ініціалізації, якщо треба
