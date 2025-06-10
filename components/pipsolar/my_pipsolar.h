#pragma once

#include "pipsolar.h"
#include "esphome/core/component.h"
#include "esphome/components/time/real_time_clock.h"

namespace esphome {
namespace pipsolar {

class MyPipSolar : public PipSolar {
 public:
  void setup() override {
    PipSolar::setup();  // зберігаємо базову поведінку

    // Затримка для надійності
    this->set_timeout("set_time", 5000, [this]() { this->send_set_datetime(); });
  }

  void send_set_datetime() {
    auto *time = esphome::rtc::global_time;
    if (time == nullptr || !time->now().is_valid()) {
      ESP_LOGW("pipsolar", "Немає дійсного часу для встановлення.");
      return;
    }

    auto now = time->now();
    char buffer[32];
    snprintf(buffer, sizeof(buffer), "DAT<%02d%02d%02d%02d%02d%02d\r",
             now.year % 100, now.month, now.day,
             now.hour, now.minute, now.second);

    std::string command(buffer);
    ESP_LOGI("pipsolar", "Встановлення часу: %s", command.c_str());

    this->write_bytes(std::vector<uint8_t>(command.begin(), command.end()));
  }
};

}  // namespace pipsolar
}  // namespace esphome

// 🔁 Реєструємо наш клас під назвою "pipsolar"
REGISTER_COMPONENT(esphome::pipsolar::MyPipSolar, pipsolar);
