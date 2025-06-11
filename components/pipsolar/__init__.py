import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import uart, time
from esphome.const import CONF_ID, CONF_TIME_ID

# Оголошуємо namespace і клас-нащадок
mypipsolar_ns = cg.esphome_ns.namespace("mypipsolar")
MyPipSolar = mypipsolar_ns.class_("MyPipSolar", cg.Component)

DEPENDENCIES = ["uart"]
AUTO_LOAD = ["binary_sensor", "sensor", "switch", "output", "text_sensor", "select"]
MULTI_CONF = True

# Схема конфігурації, яка підтримує time
CONFIG_SCHEMA = cv.All(
    cv.Schema({
        cv.GenerateID(): cv.declare_id(MyPipSolar),
        cv.Optional(CONF_TIME_ID): cv.use_id(time.RealTimeClock),
    })
    .extend(cv.polling_component_schema("1s"))
    .extend(uart.UART_DEVICE_SCHEMA)
)

# Зареєструємо платформу під ім’ям "pipsolar"
PLATFORM_SCHEMA = CONFIG_SCHEMA

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await uart.register_uart_device(var, config)

    if CONF_TIME_ID in config:
        time_var = await cg.get_variable(config[CONF_TIME_ID])
        cg.add(var.set_time_component(time_var))
