#pragma once

#include "esphome.h"
#include "esphome/components/time/real_time_clock.h"


namespace esphome {
namespace mypipsolar {

class MyPipSolar : public pipsolar::PipsolarComponent {
 public:
  void set_time_component(time::RealTimeClock *time) { this->time_ = time; }

  void setup() override;
  void loop() override;

 protected:
  time::RealTimeClock *time_{nullptr};
  bool time_synchronized_{false};

  void sync_time_if_needed();
};

}  // namespace mypipsolar
}  // namespace esphome
