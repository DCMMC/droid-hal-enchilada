# These and other macros are documented in dhd/droid-hal-device.inc
# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define device fajita
%define device_pretty OnePlus 6T

%include rpm/droid-hal-oneplus-sdm845.inc

Version: 0.0.1
Release: 1
License: BSD-3-Clause
Source: %{name}-%{version}.tar.gz
%description
%files
