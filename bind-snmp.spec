%include	/usr/lib/rpm/macros.perl
Summary:	Bind SNMP script
Summary(pl):	Skrypt Bind SNMP
Name:		bind-snmp
Version:	1.1
Release:	0.1
License:	GPL
Group:		Networking/Daemons
Source0:	http://www.bayour.com/bind9-snmp/bind9-snmp_%{version}.tgz
# Source0-md5:	834c7e296e9d5ba28d870629a618715f
URL:		http://www.bayour.com/bind9-snmp/
BuildRequires:	rpm-perlprov
Requires:	bind >= 9.0.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		webadminroot /usr/share/cacti

%description
This is a pass-through script for SNMP that gives all the Bind9
statistics that can be (is) retrieved with 'rndc status'.

%description -l pl
To jest skrypt dla SNMP dostarczaj±cy wszystkie statystyki Binda 9,
jakie mo¿na pobraæ za pomoc± polecenia 'rndc status'.

%package -n net-snmp-mibs-bind
Summary:        MIBs for BIND9
Summary(pl):	MIB-y dla BIND-a 9
Group:          Applications/System
Requires:	net-snmp-mibs

%description -n net-snmp-mibs-bind
MIBs for BIND9.

%description -n net-snmp-mibs-bind -l pl
MIB-y dla BIND-a 9.

%package -n cacti-bind
Summary:        BIND9 plugin for Cacti
Summary(pl):	Wtyczka BIND9 dla Cacti
Group:          Applications/System
Requires:	net-snmp-mibs-bind = %{version}-%{release}
Requires:	cacti

%description -n cacti-bind
BIND9 plugin for Cacti.

%description -n cacti-bind -l pl
Wtyczka BIND9 dla Cacti.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{webadminroot}/resource/snmp_queries
install -d $RPM_BUILD_ROOT%{_datadir}/snmp/mibs
install -d $RPM_BUILD_ROOT%{_sysconfdir}/{snmp,cron.d}

install etc/snmp/* $RPM_BUILD_ROOT%{_sysconfdir}/snmp
install usr/share/cacti/resource/snmp_queries/* $RPM_BUILD_ROOT%{webadminroot}/resource/snmp_queries
install usr/share/snmp/mibs/* $RPM_BUILD_ROOT%{_datadir}/snmp/mibs

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/snmp/*.pl

%files -n net-snmp-mibs-bind
%defattr(644,root,root,755)
%{_datadir}/snmp/mibs/*

%files -n cacti-bind
%defattr(644,root,root,755)
%doc tmp/*.xml
%{webadminroot}/resource/snmp_queries/*.xml
