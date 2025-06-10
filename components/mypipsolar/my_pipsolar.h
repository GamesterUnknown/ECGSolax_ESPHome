#pragma once

#include "pipsolar.h"
#include "esphome/core/component.h"
#include "esphome/components/time/real_time_clock.h"

namespace esphome {
namespace pipsolar {

class MyPipSolar : public PipSolar {
 public:
  void setup() override;
  void send_set_datetime();
};

}  // namespace pipsolar
}  // namespace esphome
