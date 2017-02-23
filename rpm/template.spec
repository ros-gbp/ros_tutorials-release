Name:           ros-lunar-turtlesim
Version:        0.7.1
Release:        0%{?dist}
Summary:        ROS turtlesim package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/turtlesim
Source0:        %{name}-%{version}.tar.gz

Requires:       qt5-qtbase
Requires:       qt5-qtbase-gui
Requires:       ros-lunar-geometry-msgs
Requires:       ros-lunar-message-runtime
Requires:       ros-lunar-rosconsole
Requires:       ros-lunar-roscpp
Requires:       ros-lunar-roscpp-serialization
Requires:       ros-lunar-roslib
Requires:       ros-lunar-rostime
Requires:       ros-lunar-std-msgs
Requires:       ros-lunar-std-srvs
BuildRequires:  qt5-qtbase-devel
BuildRequires:  ros-lunar-catkin
BuildRequires:  ros-lunar-geometry-msgs
BuildRequires:  ros-lunar-message-generation
BuildRequires:  ros-lunar-rosconsole
BuildRequires:  ros-lunar-roscpp
BuildRequires:  ros-lunar-roscpp-serialization
BuildRequires:  ros-lunar-roslib
BuildRequires:  ros-lunar-rostime
BuildRequires:  ros-lunar-std-msgs
BuildRequires:  ros-lunar-std-srvs

%description
turtlesim is a tool made for teaching ROS and ROS packages.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Wed Feb 22 2017 Dirk Thomas <dthomas@osrfoundation.org> - 0.7.1-0
- Autogenerated by Bloom

