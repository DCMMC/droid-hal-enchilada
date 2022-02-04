# These and other macros are documented in dhd/droid-hal-device.inc
# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define device enchilada
%define device_pretty OnePlus 6
%define vendor oneplus
%define vendor_pretty Oneplus

%define installable_zip 1

%include rpm/droid-hal-oneplus-sdm845.inc

%include rpm/dhd/droid-hal-device.inc
