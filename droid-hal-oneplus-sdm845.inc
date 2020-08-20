# These and other macros are documented in dhd/droid-hal-device.inc
# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define vendor oneplus

%define vendor_pretty OnePlus

%define droid_target_aarch64 1

%define installable_zip 0

# We use our own solution for mounting, in this case it's slotmount
%define use_own_mounts 1

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

%define android_config \
#define WANT_ADRENO_QUIRKS 1 \
%{nil}
