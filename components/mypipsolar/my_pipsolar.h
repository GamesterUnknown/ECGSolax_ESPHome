#pragma once

#include "pipsolar.h"
#include "esphome/core/component.h"
#include "esphome/components/time/real_time_clock.h"

namespace esphome {
namespace mypipsolar {

class MyPipSolar : public pipsolar::PipSolar {
 public:
  void setup() override;
  void send_set_datetime();
};

}  // namespace mypipsolar
}  // namespace esphome

