import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import uart
from esphome.const import CONF_ID
import esphome.components.pipsolar as parent

DEPENDENCIES = ["uart"]
AUTO_LOAD = ["sensor", "switch", "binary_sensor"]  # Якщо потрібно
CODEOWNERS = ["@твійGitHub"]

mypipsolar_ns = cg.esphome_ns.namespace("pipsolar")
MyPipSolar = mypipsolar_ns.class_("MyPipSolar", parent.PipsolarComponent)

CONFIG_SCHEMA = parent.CONFIG_SCHEMA.extend(
    {
        # Тут можна додати свої параметри, або просто використати батьківський
    }
)

def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    yield cg.register_component(var, config)
    yield uart.register_uart_device(var, config)
