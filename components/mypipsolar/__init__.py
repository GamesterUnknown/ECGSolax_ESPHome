import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import uart, time as time_component, pipsolar
from esphome.const import CONF_ID

mypipsolar_ns = cg.esphome_ns.namespace("mypipsolar")
MyPipSolar = mypipsolar_ns.class_("MyPipSolar", cg.Component)

CONF_TIME_ID = "time_id"

# Беремо базову схему з pipsolar та розширюємо її додатковим параметром time_id
PARENT_SCHEMA = cv.Schema({cv.GenerateID(): cv.declare_id(pipsolar.PipsolarComponent)})\
    .extend(cv.polling_component_schema("1s"))\
    .extend(uart.UART_DEVICE_SCHEMA)

CONFIG_SCHEMA = cv.All(
    PARENT_SCHEMA.extend({
        cv.Optional(CONF_TIME_ID): cv.use_id(time_component.RealTimeClock),
    })
)

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await uart.register_uart_device(var, config)

    if CONF_TIME_ID in config:
        time_var = await cg.get_variable(config[CONF_TIME_ID])
        cg.add(var.set_time_component(time_var))
