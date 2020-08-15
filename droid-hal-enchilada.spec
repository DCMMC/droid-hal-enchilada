# These and other macros are documented in dhd/droid-hal-device.inc
# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define device enchilada
%define vendor oneplus

%define vendor_pretty OnePlus
%define device_pretty OnePlus 6

%define droid_target_aarch64 1

%define installable_zip 0

# Calls /var/lib/platform-updates/flash-bootimg.sh
%define enable_kernel_update 1

%define straggler_files \
    /vendor \
    /system \
    /firmware \
    /persist \
    /bt_firmware \
    /bugreports \
    /cache \
    /d \
    /dsp \
    /product \
    /sdcard \
%{nil}

%define makefstab_skip_entries /vendor /sys/fs/pstore

%define android_config \
#define WANT_ADRENO_QUIRKS 1 \
%{nil}

%include rpm/dhd/droid-hal-device.inc

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"

Version: 0.0.1
Release: 1
License: BSD-3-Clause
Source: %{name}-%{version}.tar.gz
%description
%files
