#pragma once

#include "esphome.h"
#include "esphome/components/time/real_time_clock.h"
#include "esphome/components/pipsolar/pipsolar.h"


namespace esphome {
namespace mypipsolar {

class MyPipSolar : public pipsolar::Pipsolar {
 public:
  void set_time_component(time::RealTimeClock *time) { this->time_ = time; }
  void sync_time();

  void setup() override;
  void loop() override;

 protected:
  time::RealTimeClock *time_{nullptr};
  bool time_synchronized_{false};

  
};

}  // namespace mypipsolar
}  // namespace esphome
