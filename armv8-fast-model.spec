%define	cname	FM000-KT-00035-r0p8-52rel06
%define debug_package	%nil

Summary:        Interactive text-mode process viewer for Linux
Name:           armv8-fast-model
Version:	0.8.5206
Release:        2
License:        GPLv2+
Group:          Emulators
Url:		https://silver.arm.com/browse/FM00A
Source0:        https://silver.arm.com/download/Development_Tools/ESL:_Fast_Models/Fast_Models/%{cname}.tgz
Source1:	armv8-fast-model.rpmlintrc
ExclusiveArch:	x86_64

%description
The ARMv8 architecture introduces 64-bit support to the
ARM architecture with a focus on power-efficient implementation
while maintaining compatibility with existing 32-bit software.
By adopting a clean approach ARMv8-A processors, such as the
ARM Cortex-A57 and ARM Cortex-A53, extend the performance range
available while maintaining the low power consumption
characteristics of the ARM processors that will
power tomorrow's most innovative and efficient devices.

%prep
%setup -q -n Foundation_v8pkg

%build
echo "empty"

%install
mkdir -p %{buildroot}/%{_bindir}
install -m755 models/Linux64_GCC-4.1/Foundation_v8 %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_libdir}
install -m0644 models/Linux64_GCC-4.1/*.so* %{buildroot}/%{_libdir}

%files
%{_bindir}/Foundation_v8
%{_libdir}/libMAXCOREInitSimulationEngine.so.2
%{_libdir}/libarmctmodel.so
