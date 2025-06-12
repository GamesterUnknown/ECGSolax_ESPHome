import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import pipsolar, uart, time as time_component
from esphome.const import CONF_ID
from esphome.components.pipsolar import PipsolarComponent
from esphome.components.pipsolar import CONFIG_SCHEMA
#DEPENDENCIES = ["uart"]
CODEOWNERS = ["@GamesterUnknown"]
#AUTO_LOAD = ["binary_sensor", "text_sensor", "sensor", "switch", "output", "select"]
#MULTI_CONF = True
AUTO_LOAD = ["pipsolar"]

#CONF_MY_PIPSOLAR_ID = "my_pipsolar_id"
CONF_TIME_ID = "time_id"

mypipsolar_ns = cg.esphome_ns.namespace("mypipsolar")
MyPipsolarComponent = mypipsolar_ns.class_("MyPipSolar", pipsolar.PipsolarComponent)
#PipsolarComponent = pipsolar_ns.class_("Pipsolar", cg.Component)

CONFIG_SCHEMA = cv.All(
    cv.Schema({
        cv.GenerateID(): cv.declare_id(MyPipsolarComponent),
        cv.Optional("time_id"): cv.use_id(time_component.RealTimeClock),
    })
    .extend(cv.polling_component_schema("1s"))
    .extend(uart.UART_DEVICE_SCHEMA)
)

#CONFIG_SCHEMA = cv.Schema(
#    {
#        cv.GenerateID(): cv.declare_id(MyPipsolarComponent),
#        cv.Optional("time_id"): cv.use_id(time_component.RealTimeClock),
#    }
#).extend(cv.polling_component_schema("1s")).extend(uart.UART_DEVICE_SCHEMA)

#CONFIG_SCHEMA = cv.All(
#    pipsolar.CONFIG_SCHEMA,
#    cv.Schema({
#        cv.GenerateID(): cv.declare_id(MyPipsolarComponent),
#        cv.Optional("time_id"): cv.use_id(time_component.RealTimeClock),
#    })
#)


def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    yield cg.register_component(var, config)
    yield uart.register_uart_device(var, config)

    if CONF_TIME_ID in config:
        time_ = yield cg.get_variable(config["time_id"])
        cg.add(var.set_time_component(time_))

