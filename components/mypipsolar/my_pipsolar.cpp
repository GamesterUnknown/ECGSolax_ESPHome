#include "my_pipsolar.h"
#include "esphome/core/log.h"

namespace esphome {
namespace pipsolar {

static const char *const TAG = "my_pipsolar";

void MyPipSolar::setup() {
  PipSolar::setup();

  this->set_timeout("set_time", 5000, [this]() { this->send_set_datetime(); });
}

void MyPipSolar::send_set_datetime() {
  auto *time = esphome::rtc::global_time;
  if (time == nullptr || !time->now().is_valid()) {
    ESP_LOGW(TAG, "Немає дійсного часу для встановлення.");
    return;
  }

  auto now = time->now();
  char buffer[32];
  snprintf(buffer, sizeof(buffer), "DAT<%02d%02d%02d%02d%02d%02d\r",
           now.year % 100, now.month, now.day,
           now.hour, now.minute, now.second);

  std::string command(buffer);
  ESP_LOGI(TAG, "Встановлення часу: %s", command.c_str());

  this->write_bytes(std::vector<uint8_t>(command.begin(), command.end()));
}
const esphome::yaml::Schema CONFIG_SCHEMA = pipsolar::CONFIG_SCHEMA;

const esphome::yaml::Schema &MyPipSolar::get_config_schema() {
  return CONFIG_SCHEMA;
}

}  // namespace mypipsolar
}  // namespace esphome

ESP_REGISTER_COMPONENT(esphome::mypipsolar::MyPipSolar, mypipsolar);
