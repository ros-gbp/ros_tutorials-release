Name:           ros-jade-turtlesim
Version:        0.5.2
Release:        0%{?dist}
Summary:        ROS turtlesim package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/turtlesim
Source0:        %{name}-%{version}.tar.gz

Requires:       qt
Requires:       ros-jade-geometry-msgs
Requires:       ros-jade-message-runtime
Requires:       ros-jade-rosconsole
Requires:       ros-jade-roscpp
Requires:       ros-jade-roscpp-serialization
Requires:       ros-jade-roslib
Requires:       ros-jade-rostime
Requires:       ros-jade-std-msgs
Requires:       ros-jade-std-srvs
BuildRequires:  qt-devel
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-geometry-msgs
BuildRequires:  ros-jade-message-generation
BuildRequires:  ros-jade-rosconsole
BuildRequires:  ros-jade-roscpp
BuildRequires:  ros-jade-roscpp-serialization
BuildRequires:  ros-jade-roslib
BuildRequires:  ros-jade-rostime
BuildRequires:  ros-jade-std-msgs
BuildRequires:  ros-jade-std-srvs

%description
turtlesim is a tool made for teaching ROS and ROS packages.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Wed Dec 31 2014 Dirk Thomas <dthomas@osrfoundation.org> - 0.5.2-0
- Autogenerated by Bloom

