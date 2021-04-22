%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/rolling/.*$
%global __requires_exclude_from ^/opt/ros/rolling/.*$

Name:           ros-rolling-system-modes
Version:        0.7.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS system_modes package

License:        Apache License 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-rolling-builtin-interfaces
Requires:       ros-rolling-launch-ros
Requires:       ros-rolling-rclcpp
Requires:       ros-rolling-rclcpp-lifecycle
Requires:       ros-rolling-system-modes-msgs
Requires:       ros-rolling-ros-workspace
BuildRequires:  ros-rolling-ament-cmake
BuildRequires:  ros-rolling-ament-cmake-cppcheck
BuildRequires:  ros-rolling-ament-cmake-cpplint
BuildRequires:  ros-rolling-ament-cmake-flake8
BuildRequires:  ros-rolling-ament-cmake-gmock
BuildRequires:  ros-rolling-ament-cmake-gtest
BuildRequires:  ros-rolling-ament-cmake-pep257
BuildRequires:  ros-rolling-ament-cmake-uncrustify
BuildRequires:  ros-rolling-ament-index-python
BuildRequires:  ros-rolling-ament-lint-auto
BuildRequires:  ros-rolling-builtin-interfaces
BuildRequires:  ros-rolling-launch-testing-ament-cmake
BuildRequires:  ros-rolling-launch-testing-ros
BuildRequires:  ros-rolling-rclcpp
BuildRequires:  ros-rolling-rclcpp-lifecycle
BuildRequires:  ros-rolling-ros2run
BuildRequires:  ros-rolling-system-modes-msgs
BuildRequires:  ros-rolling-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
The system modes concept assumes that a robotics system is built from components
with a lifecycle. It adds a notion of (sub-)systems, hiararchically grouping
these nodes, as well as a notion of modes that determine the configuration of
these nodes and (sub-)systems in terms of their parameter values.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/rolling" \
    -DAMENT_PREFIX_PATH="/opt/ros/rolling" \
    -DCMAKE_PREFIX_PATH="/opt/ros/rolling" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/rolling

%changelog
* Thu Apr 22 2021 Arne Nordmann <arne.nordmann@bosch.com> - 0.7.0-1
- Autogenerated by Bloom

* Fri Apr 09 2021 Arne Nordmann <arne.nordmann@bosch.com> - 0.6.0-1
- Autogenerated by Bloom

* Tue Apr 06 2021 Arne Nordmann <arne.nordmann@bosch.com> - 0.5.0-2
- Autogenerated by Bloom

* Thu Mar 18 2021 Arne Nordmann <arne.nordmann@bosch.com> - 0.5.0-1
- Autogenerated by Bloom

* Fri Mar 12 2021 Arne Nordmann <arne.nordmann@bosch.com> - 0.4.2-2
- Autogenerated by Bloom

* Mon Mar 08 2021 Arne Nordmann <arne.nordmann@bosch.com> - 0.4.2-1
- Autogenerated by Bloom

