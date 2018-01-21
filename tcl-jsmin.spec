%{!?directory:%define directory /usr}

%define buildroot %{_tmppath}/%{name}
%define packagename jsmin

Name:          tcl-jsmin
Summary:       A Tcl JavaScript minifier
Version:       1.0
Release:       0
License:       BSD 3-clause
Group:         Development/Libraries/Tcl
Source:        %{name}-%{version}.tar.gz
URL:           https://github.com/flightaware/jsmin-tcl
BuildArch:     noarch
BuildRequires: tcl
Requires:      tcl
BuildRoot:     %{buildroot}

%description
JSMin-Tcl is a JavaScript minifier written in Tcl. Although inspired by
Douglas Crockford's C-based JSMin, it has its own implementation and
is not simply port. The behavior should be identical to Crockford's JSMin.

%prep
%setup -q -n %{name}-%{version}

%build

%install
dir=%buildroot%tcl_noarchdir/%packagename%version
mkdir -p $dir
cp *.tcl $dir
chmod -x $dir/*.tcl

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README.md LICENSE
%tcl_noarchdir/%packagename%version

