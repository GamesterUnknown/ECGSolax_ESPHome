#pragma once

#include "pipsolar.h"
#include "esphome/core/component.h"
#include "esphome/components/time/real_time_clock.h"
#include "esphome/core/yaml.h"  // Для esphome::yaml::Schema

namespace esphome {
namespace mypipsolar {

class MyPipSolar : public PipSolar {
 public:
  void setup() override;
  void send_set_datetime();
  
  static const esphome::yaml::Schema &get_config_schema();
};

extern const esphome::yaml::Schema CONFIG_SCHEMA;

}  // namespace pipsolar
}  // namespace esphome
