#!/usr/bin/env python3
# This file is automatically generated!
# Source File:        0x11-system_info.json
# Device ID:          0x11
# Device Name:        system_info
# Timestamp:          09/09/2019 @ 17:37:24.169029 (UTC)

from enum import IntEnum


__all__ = ['ConfigBlockWriteCodesEnum',
           'DeviceModesEnum',
           'ApplicationIndexesEnum',
           'SosMessagesEnum',
           'BootReasonsEnum']


class CommandsEnum(IntEnum): 
    get_main_application_version = 0x00
    get_bootloader_version = 0x01
    get_board_revision = 0x03
    get_mac_address = 0x06
    get_stats_id = 0x13
    get_processor_name = 0x1F
    get_boot_reason = 0x20
    get_last_error_info = 0x21
    get_sku = 0x38
    get_core_up_time_in_milliseconds = 0x39
    get_event_log_status = 0x3A
    get_event_log_data = 0x3B
    enable_sos_message_notify = 0x3D
    sos_message_notify = 0x3E
    get_sos_message = 0x3F
    clear_sos_message = 0x44


class ConfigBlockWriteCodesEnum(IntEnum):
    ''' '''
    CB_SUCCESS = 0  #: 
    CB_BUSY = 1  #: 
    CB_FS_ERROR = 2  #: 


class DeviceModesEnum(IntEnum):
    ''' '''
    factory_mode = 0  #: 
    user_play_test_mode = 1  #: 
    user_out_of_box_mode = 2  #: 
    user_full_mode = 3  #: 


class ApplicationIndexesEnum(IntEnum):
    ''' '''
    bootloader = 0  #: 
    main_application = 1  #: 


class SosMessagesEnum(IntEnum):
    ''' '''
    unknown = 0  #: 
    subprocessor_crashed = 1  #: 


class BootReasonsEnum(IntEnum):
    ''' '''
    cold_boot = 0  #: 
    unexpected_reset = 1  #: 
    application_reset_due_to_error = 2  #: 
    application_reset_for_a_firmware_update = 3  #: 
    processor_is_booting_from_sleep = 4  #: 
    processor_is_resetting_for_some_non_error_reason = 5  #: 
