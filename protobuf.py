syntax = "proto2"

package tutorial;

message sensor_data {
	required string sens_type = 1;
	required string unit = 1;
	required int32 timestamp = 1;
}
