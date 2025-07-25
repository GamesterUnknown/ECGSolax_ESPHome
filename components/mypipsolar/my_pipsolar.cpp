#include "my_pipsolar.h"
#include "esphome/core/log.h"
#include "esphome/core/helpers.h"
#include "esphome/components/pipsolar/pipsolar.h"

namespace esphome {
namespace pipsolar {

static const char *const TAG = "mypipsolar";

void MyPipSolar::setup() {
  ESP_LOGI(TAG, "MyPipSolar setup");
  Pipsolar::setup();  
}

void MyPipSolar::loop() {
  Pipsolar::loop();  
}

void MyPipSolar::update() {
  Pipsolar::update();  
  
}

void MyPipSolar::sync_time() {
  if (!this->time_) {
    ESP_LOGW(TAG, "RTC (time component) not available");
    return;
  }

  auto now = this->time_->now();

  if (!now.is_valid()) {
    ESP_LOGW(TAG, "Time not valid");
    return;
  }

  // Формуємо рядок DAT<YYMMDDHHMMSS>
  char buffer[32];
  snprintf(buffer, sizeof(buffer), "DAT<%02d%02d%02d%02d%02d%02d>\r",
           now.year % 100, now.month, now.day_of_month,
           now.hour, now.minute, now.second);

  ESP_LOGI(TAG, "Sending time sync command: %s", buffer);

  // Надсилаємо через UART
  //this->write_str(buffer);  // do not sent exact command to uart yeat

  // Опційно: якщо потрібно дочекатися відповіді — можна реалізувати тут
  // наприклад: this->expect_response("ACK", timeout);
}

}  // namespace pipsolar
}  // namespace esphome
